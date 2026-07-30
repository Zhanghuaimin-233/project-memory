---
name: bootstrap-project-memory
description: 为新项目或几乎没有长期文档的项目建立最小、可持续的项目记忆入口。用于用户要求初始化项目文档、建立 README/AGENTS/docs 结构、制定后续新文档落位规则，或在编码前为全新仓库建立文档地基。不要用于已有大量杂乱文档的项目（使用 adopt-project-memory）、未完成任务的会话交接（使用 checkpoint-project-task）或任务完成后的文档同步、知识提炼与归档（使用 closeout-project-task）。
---

# 初始化项目记忆

为新项目建立足够用、不会提前膨胀的文档地基。让后续人和 Agent 始终知道项目现在是什么、文档应该放哪里、什么时候才值得创建新文档。

## 完成标准

完成后必须具备：

- 面向人的项目入口；
- 面向 Agent 的常驻规则与文档路由；
- 一份项目级文档合同，持续指导后续文档创建；
- 明确的当前事实入口，或明确说明当前项目尚只有愿景；
- 没有为尚不存在的内容创建空知识库、空规格目录或空归档体系；
- 所有新链接可解析，现有用户内容未被覆盖。

## 1. 先读取现场

在写入前：

1. 确认项目根、仓库边界和用户要求。
2. 读取现有 README、AGENTS/CLAUDE、项目清单、入口代码和 Git 状态。
3. 判断项目是否已经有承担相同职责的文件。
4. 若已有大量长期文档或权威冲突，停止 bootstrap，改用 `adopt-project-memory`。

不要因“初始化”覆盖已有 README 或规则文件。对现有内容使用局部编辑。

## 2. 确定最小文档地基

默认候选为：

```text
README.md
AGENTS.md
docs/README.md
docs/PROJECT.md（仅在没有等价当前入口且已有内容可写时）
```

按现场调整：

- README 面向人：项目是什么、当前能做什么、如何开始。
- AGENTS 面向 Agent：不可从代码推断的边界、验证方式、文档路由。
- `docs/README.md` 是文档目录的持续合同：路径职责、创建条件、命名、生命周期和索引规则。
- 当前状态文档可以沿用现有的 `PROJECT.md`、实施手册、architecture 或同等文件。

不要提前创建：

```text
KNOWLEDGE.md
knowledge/
specs/
plans/
reports/
work/
archive/
```

只有第一份真实内容需要它们时才创建。

## 3. 写入持续文档合同

写入前完整读取本 Skill 自带的模板：

- `./templates/docs-readme.md`
- `./templates/agents-document-routing.md`

模板是候选骨架，不是必须逐字复制。根据项目已有名称和目录删减，不创建不存在的类别。

文档合同必须至少回答：

- 当前权威入口在哪里；
- 新文档先按什么类型判断；
- 哪些文档使用稳定名称，哪些使用日期；
- Plan、State、Report、Knowledge 和 Archive 分别负责什么；
- 任务级要求如何从 Plan 流向 State，以及独立 Spec 必须同时满足持续性和独立价值门槛；
- 哪些文件必须进入索引，哪些只需留在目录；
- 任务完成后文档如何提升、归档或删除；
- 文档与代码、测试或运行结果冲突时如何调查。

在 AGENTS 中只放短路由、工作方式和少量所有任务都必须知道的护栏，不复制完整产品、数据或接口合同。若已有 CLAUDE.md、AGENT.md 或其他平台入口，复用项目声明的真身或创建薄指针，不维护多份详细规则。

## 4. 区分愿景与实现

项目刚开始时允许记录愿景、MVP 和拟议范围，但必须显式区分：

```text
proposed | planned | in_progress | verified | released | deferred | superseded
```

不要把讨论结论、MVP 愿景或未来计划写成已实现能力。状态可以用正文说明，不要求所有文件增加 front matter。

## 5. 保持幂等

再次调用本 Skill 时：

- 更新已有“文档路由/文档维护”章节，不追加第二份；
- 复用现有 `docs/README.md` 或等价索引；
- 不重复创建当前状态文档；
- 不因模板升级重写用户的项目说明；
- 路由发生变化时同时修正死链接。

## 6. 验证

完成前：

1. 回读所有改动。
2. 检查 Markdown 相对链接。
3. 确认同一当前事实没有被新复制到多处。
4. 确认 README 与 AGENTS 的受众职责不同。
5. 检查 Git diff 和未关联改动；不要自动暂存、提交或推送。
6. 报告创建、复用和刻意未创建的文件，以及仍需用户决定的项目。

任务已进入开发收尾时不要继续扩大本 Skill；使用 `closeout-project-task` 执行完成态文档结算。本 Skill 不要求或调用任何外部插件。
