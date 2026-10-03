"""Build independently installable skills from current source; never overwrite output."""

import argparse
import re
import shutil
from pathlib import Path

ASSET_REF = re.compile(r"\.\./\.\./assets/((?:templates|references)/[a-z0-9-]+\.md)")


def build(source: Path, output: Path) -> None:
    source = source.resolve()
    output = output.resolve()
    if output == source or source.is_relative_to(output):
        raise ValueError("Output must not contain the source tree")
    if output.is_relative_to(source / "skills") or output.is_relative_to(source / "assets"):
        raise ValueError("Output must not be inside source skills or assets")
    if output.exists():
        raise FileExistsError(f"Output already exists; choose a new directory: {output}")
    skills = sorted((source / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found")
    # Resolve the entire reference set before creating any output.
    plans = []
    for skill in skills:
        body = skill.read_text(encoding="utf-8")
        refs = sorted(set(ASSET_REF.findall(body)))
        resources = [(ref, source / "assets" / ref) for ref in refs]
        for _, resource in resources:
            if not resource.is_file():
                raise FileNotFoundError(resource)
        rewritten = ASSET_REF.sub(r"./\1", body)
        if "../../assets/" in rewritten:
            raise ValueError(f"Unsupported external asset reference: {skill}")
        plans.append((skill, rewritten, resources))
    output.mkdir(parents=True)
    for skill, rewritten, resources in plans:
        destination = output / skill.parent.name
        shutil.copytree(skill.parent, destination)
        (destination / "SKILL.md").write_text(rewritten, encoding="utf-8", newline="\n")
        for ref, resource in resources:
            target = destination / ref
            target.parent.mkdir(exist_ok=True)
            shutil.copy2(resource, target)
    print(f"Built {len(plans)} self-contained skills: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.source, args.output)
