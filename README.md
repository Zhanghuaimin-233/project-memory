# Project Memory

建立并维护准确、易查、易理解、易更新的项目资料，让人和 Agent 能接手项目并正确继续开发。资料可以是说明、图表、Wiki、知识地图或运行证据；形式按用途选择，只有能减少重复解释、错误接续或重复调查的信息才值得维护。

四个按需使用的 Agent Skills，可以贯穿开发过程。用户决定工作意图和会话边界，Agent 负责选择、核对与维护必要资料。普通小修可能一个都不用；长期任务可以多次保存和恢复，再在需要时收尾。插件不替代需求分析、设计、编码、测试和发布，也不自动决定何时开启新会话。

## 四个入口

| Skill | 什么时候用 | 完成意味着什么 |
| --- | --- | --- |
| [setup-project-memory](skills/setup-project-memory/SKILL.md) | 建立新项目资料、接管旧项目，或明确审查项目资料 | 能按当前目的理解项目、查证关键认识并找到工作入口 |
| [checkpoint-project-task](skills/checkpoint-project-task/SKILL.md) | 暂停、换会话或换 Agent，现场有难以恢复的信息 | 下一位 Agent 能定位现场并正确继续 |
| [resume-project-task](skills/resume-project-task/SKILL.md) | 接手或继续明确的未完成任务 | 选读相关资料，结合当前现场恢复正确下一步 |
| [closeout-project-task](skills/closeout-project-task/SKILL.md) | 阶段或任务收尾，或同步本次影响的资料 | 相关说明、图表与其他视图准确，完成边界清楚 |

```text
$setup-project-memory 帮我接手这个项目，只补影响理解和继续开发的资料
$checkpoint-project-task 暂停前保存下一会话需要的现场
$resume-project-task 继续上次未完成的任务
$closeout-project-task 收尾这次改动，同步受影响的说明、流程图和 Wiki
```

没有必须依次调用的流程，也不按输出格式增加入口。新会话不代表恢复旧任务，旧项目不必重新 setup；意图不清时先澄清。已有资料足够时可以零改动；必要的图或解释也不应因追求文件少而省略。不会为了“不写文档”另外生成一份判断报告。

## 按用途选择资料

一套一致的项目资料可以跨多个文件和格式。优先使用项目已有位置与工具，让资料离开本轮聊天或插件安装目录也能使用。

| 要解决的问题 | 可选形式 |
| --- | --- |
| 如何运行、配置、排错 | 说明、命令、输入输出示例 |
| 模块如何协作、数据怎样流动 | 架构图、流程图、时序图 |
| 为什么选择或否决某条路线 | 相关方案旁的决定、理由与适用条件 |
| 主题和关系多，线性入口难以查找 | 链接的 Wiki 页面、能追到来源的知识地图 |
| 如何继续当前任务 | 简短现场与必要证据定位 |

这些是选择依据，不是交付清单。知识地图的关系需要依据，不能把目录连线当成项目理解。重要结论区分用户决定、验证事实和暂定判断；同一事实明确主要维护位置，其他表达从它派生或链接回来。图表保留可编辑源或生成数据，修改时同步受影响视图。无法重建的旧视图明确失效范围，不假称已同步完成。

取舍与维护示例见 [项目资料参考](skills/setup-project-memory/references/project-materials.md)，仅在需要时阅读，不强制项目建立 Wiki、地图或新目录。

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

重要决定确认或稳定事实变化后，在当前授权范围内更新已有资料及受影响视图，不必等用户再次提醒或等到收尾。项目确有需要时，可将这一小段日常约定合入已有规则；Skill 安装本身不保证每轮都加载，也不提供后台监听或自动保存。没有影响理解或行动的新信息时，不逐轮记日志或反复改写。

当前任务必做项留在当前计划或待办，不能移入 Backlog 后宣布完成。值得避免遗忘的独立后续工作可以直接写入已有 Backlog；用户说“记一下”就做最小记录，无需调用独立路由 Skill。外部 Issue 写入遵循当前授权。

难以重做的调查才需要 Report；非直观且可能复用的结论才需要 Knowledge；独立规格只有在持续被依赖、并且比代码或测试提供额外解释时才值得维护。用户可见说明过期就直接修正，不必等待整个任务结束。没有这些需求，就不创建对应文件。

资料与代码冲突时先判断是资料漂移还是实现违背约定。普通收尾只检查本次影响的范围，独立的项目资料审查使用 setup；不自动串联全仓治理、平台记忆修改或 worktree 清理。

## 安装与分发

以可独立使用的 Skills 为核心，包含按需参考和可选模板；项目产物的形式不限于 Markdown。核心流程不依赖外部插件、MCP 或运行时，具体资料的制作与查看沿用可用工具。只有重复的机械步骤确有收益时才增加辅助脚本，不预建知识数据库或后台服务。

`main` 使用共享参考和模板；`codex/self-contained-skill-packages` 分支把每个 Skill 引用的资源放进该 Skill，可单独复制安装。

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
- `closeout-project-task` 保留名称，吸收核对、去重与知识整理方法，作为包内独立收尾 Skill，不串联外部收尾流程。
- `checkpoint-project-task` 和 `resume-project-task` 名称保留，行为改为最小保存和按需恢复。

安装时移除本插件退役的入口，避免新旧规则同时加载。若曾安装包内 `neat-freak`，将其替换为 `closeout-project-task`。独立 `neat-freak` 由其自己的来源维护，本插件不覆盖它，也不要求调用它；任务收尾使用本插件入口，明确调用“洁癖”或 `/neat` 时使用独立 Skill。既有项目无需批量迁移目录；下次确实涉及相应规则时，再修正旧的强制路由、必填栏目和退役 Skill 引用。项目或用户的明确约定优先。

## 维护验证

检查四个 Skill 的元数据、插件清单和参考/模板引用。用实际场景检查接手者能否理解目标、关系、关键理由、状态与下一步；检查多种表达是否一致、交接是否保住剩余验收、已有资料足够时是否保持不变。图表需检查实际呈现，链接和关系需有依据；不能仅以文件变短、图更多或复制成功宣称有效，也不能冒称节省了未测量的 token。

自包含目录可由当前源码生成到一个新的输出目录：

```powershell
python scripts/build_self_contained.py --output build/self-contained
python -m unittest discover -s tests
```

行为样例见 [evals/scenarios.json](evals/scenarios.json)。

## 许可证

[MIT](LICENSE)
