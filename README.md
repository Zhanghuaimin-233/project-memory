# Project Memory

帮助 Agent 用较少的阅读正确接续工作。只有能减少重复解释、错误接续或重复调查的信息，才值得维护。

四个按需使用的 Agent Skills，可以贯穿开发过程，但不替代需求分析、设计、编码、测试和发布。普通小修可能一个都不用；长期任务可以多次保存和恢复，再在需要时收尾。

## 四个入口

| Skill | 什么时候用 | 完成意味着什么 |
| --- | --- | --- |
| [setup-project-memory](skills/setup-project-memory/SKILL.md) | 新项目缺必要说明，或旧项目入口、当前方案混乱 | 能找到并使用正确的信息 |
| [checkpoint-project-task](skills/checkpoint-project-task/SKILL.md) | 暂停、换会话或换 Agent，现场有难以恢复的信息 | 下一位 Agent 能定位现场并正确继续 |
| [resume-project-task](skills/resume-project-task/SKILL.md) | 接手或继续未完成任务 | 根据当前现场恢复正确下一步 |
| [neat-freak](skills/neat-freak/SKILL.md) | 阶段或任务收尾，或同步受影响的文档 | 本次工作影响的信息不再误导后续行动 |

```text
$setup-project-memory 解决这个项目旧计划和当前入口的冲突
$checkpoint-project-task 暂停前保存下一会话需要的现场
$resume-project-task 继续上次未完成的任务
$neat-freak 收尾这次改动，同步实际受影响的说明
```

没有必须依次调用的流程。每个 Skill 都允许零新增 Markdown；已有信息足够时，也允许零改动结束。不会为了“不写文档”另外生成一份判断报告。

## Plan 和 STATE 怎样配合

Plan 保存当前有效的目标、约束、验收和执行安排；STATE 保存继续工作需要的现场。两者都按需要创建，也可以复用项目已有的等价入口。

- 步骤或实现方法改变，直接重写 Plan 的相关段落，移除失效指令。不能通过编辑悄悄缩减已承诺的目标或验收。
- 整体方案需要替换，或用户要求保留原版时，可以新建 Plan。旧版保留正文并标明 `superseded`、链接新版；新版说明替代来源，独立承接剩余范围和必要约束。STATE 和活跃入口只指向当前版本。
- 详细展开当前阶段，远期阶段保留目标、依赖和验收轮廓。Plan 不累积执行日志或补丁附录。
- STATE 不复制完整待办、规格、完成历史和测试记录。留下会影响下一步的信息，如未决问题、重要失败路线、未提交工作、部分迁移和结果未知的外部请求。
- 每次检查点淘汰已解决阻塞、失效下一步和已被 Plan 吸收的偏差。代码、测试或已保存的 Git 历史足以恢复的内容无需另存；唯一证据尚未保存时不能直接删掉。
- 链接是按需检索入口，不是必须全文读取的清单。恢复时先读目标、关键约束和当前相关部分，遇到冲突再扩大调查。

同一任务需要检查点时复用同一份 STATE；没有检查点也可以从现有材料恢复，不必先补文件。没有 Plan 的简单任务可在短检查点中保留剩余范围，不为配套而新建计划书。

## 日常信息如何处理

优先更新已有位置。当前任务必做项留在当前计划或待办，不能移入 Backlog 后宣布完成。值得避免遗忘的独立后续工作可以直接写入已有 Backlog；用户说“记一下”就做最小记录，无需调用独立路由 Skill。外部 Issue 写入遵循当前授权。

难以重做的调查才需要 Report；非直观且可能复用的结论才需要 Knowledge；独立规格只有在持续被依赖、并且比代码或测试提供额外解释时才值得维护。用户可见说明过期就直接修正，不必等待整个任务结束。没有这些需求，就不创建对应文件。

文档与代码冲突时先判断是文档漂移还是实现违背约定。普通收尾只检查本次影响的范围，不默认盘点整个仓库、修改平台记忆或清理 worktree。

## 安装与分发

核心是与模型无关的 Markdown；不依赖外部插件、MCP 或运行时。`main` 使用共享可选模板；`codex/self-contained-skill-packages` 分支在每个引用模板的 Skill 内携带模板，可单独复制安装。

### Codex

将仓库放在本机 marketplace 源中，例如 `%USERPROFILE%\plugins\project-memory`。在已有 personal marketplace 的 `plugins` 列表中注册：

```json
{
  "name": "project-memory",
  "source": { "source": "local", "path": "./plugins/project-memory" },
  "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
  "category": "Productivity"
}
```

安装已注册的插件：

```powershell
codex plugin add project-memory@personal
codex plugin list
```

更新后新建会话，使新的 Skill 元数据进入上下文。安装状态和启用状态分别以产品列表为准。

### 其他 Agent

支持完整 Skill 包的工具可保留仓库的 `skills/` 和 `assets/` 相对关系；只支持单个 Skill 的工具使用自包含分支。OpenCode 使用自包含 Agent Skills，不需要空的 JavaScript hook 插件。

### 从六入口版本升级

- `bootstrap-project-memory` 和 `adopt-project-memory` 合并为 `setup-project-memory`。
- `route-project-memory` 退出分发，日常记录直接在合适位置完成。
- `closeout-project-task` 与洁癖的有效方法融合为包内 `neat-freak`，不串联外部收尾流程。
- `checkpoint-project-task` 和 `resume-project-task` 名称保留，行为改为最小保存和按需恢复。

安装时移除本插件退役的入口，避免新旧规则同时加载。已有独立 neat-freak 的用户应选择一个来源或同步为相同实现，不必执行两轮收尾。既有项目无需批量迁移目录；下次确实涉及相应规则时，再修正旧的强制路由、必填栏目和退役 Skill 引用。项目或用户的明确约定优先。

## 维护验证

检查四个 Skill 的元数据、插件清单和模板引用。用实际场景检查普通小修是否零新增文档、反复交接是否保住未完成范围而不累积历史、替代计划是否只有一个当前入口。不能仅以文件变短就声称节省了实际运行 token。

自包含目录可由当前源码生成到一个新的输出目录：

```powershell
python scripts/build_self_contained.py --output build/self-contained
```

行为样例见 [evals/scenarios.json](evals/scenarios.json)。

## 许可证

[MIT](LICENSE)
