# Obsidian Study Helper V0 版本报告

2026 年 11 月 14 日

V0 已部署到本机 Obsidian 的 `helper_instance_0`。从首页进入示例课、打开 Concept note、查看图表，再跳到 Worksheet 的指定题目并展开答案，这条路径已在 Obsidian 桌面端走通。下一轮用 `STA302` 的一周真实资料，检查建课、归档、写笔记和复习的操作成本。

## V0 已交付

| 部分 | 现在可以做什么 |
| --- | --- |
| 课程导航 | 从 `Home.md` 进入课程，再按 Course → Module → Concept 浏览。`DEMO101` 提供一个 Module 和三个 Concept，分别讲 Conditional mean、Residuals 和 Constant variance。 |
| 资料管理 | 用 `Materials/Inbox/` 暂存下载，按 Slides、Handwritten、Handouts、Images、Video、Audio 或 Other 归档。通过 Source note 记原件、PDF 页码或视频时间戳，并从 Concept 链回出处。 |
| 知识点呈现 | 示例展示 Wiki links、heading 和 block 引用、数学公式、Mermaid、图片、指定页 PDF、内嵌 MP4 和外部视频。 |
| 练习与错题 | 有 Worksheet、Assignment、Practice Exam 示例。每份练习用一篇 note，每道题有独立 heading、折叠 Solution 和知识点链接。`DEMO101` 的 Practice 页用 `#review/missed` 查询待重做的题。 |
| 课程复用 | 有 `Blank-Course`、五份笔记模板和 `Tools/new_course.py`。支持手动复制或用 Python 生成课程目录，首页入口手动加入。 |
| 交互实验 | Variance lab 用同一个滑块联动 observations 和 residuals 两张图。可在桌面浏览器打开 HTML，或按说明启动本地 server 后在笔记内操作。实验笔记附静态图和模型说明。 |
| 部署与维护 | `starter/StudyVault/` 是模板源，`helper_instance_0/` 是实际试用 Vault。已配置 Templates、Wiki links、自动更新链接及笔记旁的 `_assets` 附件目录。`helper_instance_0/` 在 `.gitignore` 中，V0 模板仍是本地未提交的变更。多端同步和备份恢复步骤见部署指南。 |

使用入口见 [README.md](README.md)。配置、同步与恢复步骤见 [Deployment-Guide.md](starter/Deployment-Guide.md)。

## 已验证的范围

| 验证方式 | 结果 |
| --- | --- |
| Obsidian 桌面端 | `Home → DEMO101 → Linear regression assumptions → Constant variance → Worksheet 01 · Q02` 跳转成功。知识点图片显示，Q02 的错题标签可见，Solution 可以展开。 |
| 本地文件与配置 | 核对了部署后笔记的内部链接、heading 和 block targets、PDF 引用页码，以及 PDF、PNG、MP4 文件和 Obsidian 设置。 |
| 临时 Vault 副本 | `new_course.py` 成功生成 `STA302-2026F`，写入课程属性并输出首页链接。重复使用同一课程 ID 会报错并保留已有课程。 |
| Simulation JavaScript | 在模拟 DOM 中验证了两图重绘、同一 observation 的联动高亮与动画启停。桌面浏览器操作和 Obsidian 内嵌显示待验收。 |

## 接下来怎么测

| 优先级 | 测试任务 | 通过标准 |
| --- | --- | --- |
| 1 | 用 `STA302-2026F` 跑一周真实资料。建课并加到 Home，导入一份 slides、一份手写 PDF 和一份 worksheet，写一篇 Concept 和一道代表题。 | 从 Home 能找到本周内容；从 Concept 能打开正确的原件页，随后跳到对应题目。每份原件只归档一次。 |
| 1 | 把一道题标为 `#review/missed`，在 Practice 查到题号，重做后改为 `#review/resolved`。新课需把示例查询改成自己的课程路径。 | 待重做列表能定位到正确的题，改标签后该题从列表移除。题目与 Solution 仍可打开。 |
| 2 | 在 Obsidian 插入 Concept、Source 和 Question 模板，粘贴截图。建第二门测试课，保留同名的 `Course.md`、`Module.md` 和 `Worksheet-01.md`，再在 Obsidian 里重命名一个 Concept。 | 模板可选、截图进笔记旁的 `_assets`、同名笔记不会跳错课、改名后已有链接仍能打开。 |
| 2 | 在 Reading view 检查悬浮预览、PDF 第 1 页和第 2 页、本地 MP4 播放。运行 Variance lab，先在浏览器拖动滑块，再试笔记内嵌。 | 预览能读到目标内容，PDF 以指定页打开，MP4 可以播放；浏览器和笔记中的实验都能操作，两张图随同一个滑块更新。 |
| 3 | 选定一种同步方式后，在第二台设备编辑一篇测试笔记并打开附件。用独立目录做一次备份恢复。 | 两台设备能往返看到编辑并打开 PDF；恢复副本离线可读，笔记和 PDF 都能打开。 |

### 第一次试用的最小范围

建议先完成优先级 1。在录入完资料后关掉当前笔记，从 `Home.md` 重新找回一条定义、它的原始页码和一道错题。逐项记下实际点击路径、找不到的资料，以及需要反复手填的字段。

## V1 的改动依据

- 如果每门课都要重填相同的索引、首页链接或错题查询路径，先简化新课初始化。
- 如果从 Concept 经常找不回原件页或时间戳，调整 Source 模板和 Concepts 的引用方式。
- 如果查找和归档顺畅，再用一门结构不同的课检验通用性，例如用 EAS151 测音频、例句与短练习，或用 CSC343 测 SQL、schema diagrams 和较长题目。
