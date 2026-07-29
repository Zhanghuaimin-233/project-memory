# Project Memory

一个面向个人长期项目的 Codex 插件，用最小文档体系维护当前事实、跨会话任务状态和可复用项目经验。

它不要求固定的大型文档框架，也不依赖其他插件、MCP、Hook 或外部服务。

## 五个 Skill

| Skill | 何时使用 | 主要结果 |
| --- | --- | --- |
| `bootstrap-project-memory` | 新项目或几乎没有长期文档 | 建立 README、Agent 路由和持续文档合同 |
| `adopt-project-memory` | 已有文档杂乱、重复或权威冲突 | 接管现有文档地基并恢复当前入口 |
| `checkpoint-project-task` | 未完成长期任务准备切换会话 | 重写唯一的任务状态快照 |
| `resume-project-task` | 新会话继续未完成任务 | 用真实仓库现场校准 State 并恢复工作 |
| `closeout-project-task` | 任务或明确阶段已经完成 | 同步当前事实、提炼知识并让任务材料退出 active |

## 核心模型

```text
当前事实  → Project / 当前状态文档
稳定合同  → Spec
实施意图  → Plan
任务现实  → State
调查证据  → Report
复用经验  → Knowledge
失效材料  → Archive
```

- Plan 记录“准备怎么做”，State 记录“现在实际做到哪里”。
- 一个逻辑任务只维护一份 State，不按会话创建交接副本。
- Knowledge 只保存非直观、可能复发或未来维护必须知道的经验。
- 同一当前事实只保留一个主要入口，不创建 `final-new`、`v2-final` 一类平行版本。
- 没有真实内容时不创建空知识库、空规格目录或空归档体系。

## 安装

Codex 通过已配置的 marketplace 安装本地插件。下面以个人 marketplace 为例。

### 1. 克隆源码

PowerShell：

```powershell
git clone https://github.com/Zhanghuaimin-233/project-memory.git "$env:USERPROFILE\plugins\project-memory"
```

### 2. 注册到个人 marketplace

确保 `%USERPROFILE%\.agents\plugins\marketplace.json` 中存在以下插件条目：

```json
{
  "name": "project-memory",
  "source": {
    "source": "local",
    "path": "./plugins/project-memory"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

`source.path` 相对于用户目录解析，因此对应上一步的 `%USERPROFILE%\plugins\project-memory`。

### 3. 安装

```powershell
codex plugin add project-memory@personal
```

安装或更新后新建一个 Codex 任务，使新的 Skill 元数据进入上下文。

## 使用示例

```text
$bootstrap-project-memory 初始化这个新项目的文档体系

$adopt-project-memory 接管并整理这个已有项目的文档体系

$checkpoint-project-task 为当前未完成任务保存跨会话检查点

$resume-project-task 恢复上次未完成的任务

$closeout-project-task 结算这个已完成任务并沉淀项目经验
```

插件只管理项目文档记忆和任务连续性，不会自动提交、推送、发布或清理无关工作区。

## 目录

```text
.codex-plugin/plugin.json
skills/
  bootstrap-project-memory/
  adopt-project-memory/
  checkpoint-project-task/
  resume-project-task/
  closeout-project-task/
assets/templates/
  docs-readme.md
  agents-document-routing.md
  task-state.md
```

## 许可证

[MIT](LICENSE)
