"""Exercise independently installable references and safe build failures."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "build_self_contained.py"
SPEC = importlib.util.spec_from_file_location("builder", MODULE)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.skill = self.source / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.output = self.root / "output"

    def write(self, path, body):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    def test_standalone_package_retains_resources_and_local_metadata(self):
        self.write(self.skill / "SKILL.md", "Read ../../assets/references/materials.md\n"
                   "Use ../../assets/templates/state.md\n")
        self.write(self.skill / "agents/openai.yaml", "interface: {}\n")
        self.write(self.source / "assets/references/materials.md", "可选参考\n")
        self.write(self.source / "assets/templates/state.md", "必要现场\n")
        builder.build(self.source, self.output)
        package = self.output / "example"
        self.assertEqual((package / "SKILL.md").read_text(encoding="utf-8"),
                         "Read ./references/materials.md\nUse ./templates/state.md\n")
        for relative in ("references/materials.md", "templates/state.md"):
            self.assertEqual((package / relative).read_bytes(),
                             (self.source / "assets" / relative).read_bytes())
        self.assertEqual((package / "agents/openai.yaml").read_bytes(),
                         (self.skill / "agents/openai.yaml").read_bytes())

    def test_missing_reference_fails_before_any_output(self):
        self.write(self.skill / "SKILL.md", "Read ../../assets/references/missing.md")
        with self.assertRaises(FileNotFoundError):
            builder.build(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_existing_output_is_preserved(self):
        self.write(self.skill / "SKILL.md", "Instructions")
        self.write(self.output / "user.txt", "keep")
        with self.assertRaises(FileExistsError):
            builder.build(self.source, self.output)
        self.assertEqual((self.output / "user.txt").read_text(), "keep")

    def test_unsupported_external_asset_is_rejected(self):
        self.write(self.skill / "SKILL.md", "Read ../../assets/other/item.md")
        with self.assertRaises(ValueError):
            builder.build(self.source, self.output)
        self.assertFalse(self.output.exists())

    def test_output_cannot_overwrite_source_or_live_resource_trees(self):
        self.write(self.skill / "SKILL.md", "Instructions")
        for target in (self.root, self.source, self.skill / "output",
                       self.source / "assets/output"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                builder.build(self.source, target)


if __name__ == "__main__":
    unittest.main()
