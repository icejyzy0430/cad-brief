<h1 align="center">cad-brief</h1>

<p align="center">
  <strong>先把“要建什么”整理成有证据、可验收的 CAD 需求，再交给 Text-to-CAD 建模。</strong>
  <br>
  给只有一句想法、几张参考图或不完整产品信息的新手使用的独立 Codex Skill。
</p>

<p align="center">
  <a href="https://github.com/icejyzy0430/cad-brief/actions/workflows/test.yml"><img alt="测试状态" src="https://img.shields.io/github/actions/workflow/status/icejyzy0430/cad-brief/test.yml?branch=main&style=flat-square&label=CI"></a>
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="最多两轮问询" src="https://img.shields.io/badge/questions-%E2%89%A42-59636e?style=flat-square">
  <img alt="22 项测试" src="https://img.shields.io/badge/tests-22-2ea44f?style=flat-square">
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"></a>
</p>

<p align="center">
  <sub>独立社区项目，与 <a href="https://github.com/earthtojake/text-to-cad">earthtojake/text-to-cad</a> 没有隶属、合作或官方认可关系。</sub>
</p>

```text
用户：“根据几张照片做一个 Sony 摄像机 CAD；我不知道型号和尺寸。”

模糊描述 + 图片
      │
      ▼
  $cad-brief ──→ 最多两轮关键问询 ──→ 公开资料研究与证据分级
      │
      ▼
camera-body.cad-requirements.md
  ├─ Status: provisional
  ├─ 参数、组件、接口、假设与冲突
  ├─ 每条关键要求的来源和验收方法
  └─ 可直接复制给 $cad 的启动提示词
```

### 30 秒安装（Windows PowerShell）

```powershell
git clone https://github.com/icejyzy0430/cad-brief.git
Copy-Item -Recurse .\cad-brief\cad-brief "$HOME\.codex\skills\cad-brief"
```

<br>

---

## 先补齐需求，再生成几何

[`earthtojake/text-to-cad`](https://github.com/earthtojake/text-to-cad) 的 `$cad`
负责 build123d、STEP、几何检查、快照和修复；`cad-brief` 只负责建模前的需求准备。

| | 直接调用 `$cad` | 先 `$cad-brief`，再 `$cad` |
| --- | --- | --- |
| 适合输入 | 已经清楚的 CAD 规格 | 模糊描述、参考图、未知型号或缺失尺寸 |
| 问询方式 | 缺少关键条件时进行聚焦澄清 | 最多两轮；第一轮后先研究，第二轮只让用户做关键选择 |
| 未知信息 | 建模时显式假设并报告 | 先按 9 种证据状态整理，再判定 readiness |
| 中间产物 | CAD brief 与参数化源码 | 可审阅、可校验的 `.cad-requirements.md` |
| 最终职责 | 生成并验证 CAD | 需求交接后仍由 `$cad` 生成并验证 CAD |

如果你已有完整的尺寸、接口和验收条件，可以直接使用 `$cad`。`cad-brief` 的价值
在于资料不完整时，先确定“究竟应该建什么”，避免精确验证一份遗漏了关键要求的规格。

## 看一眼就能用

- 完整规格可以零追问；信息不足时，整个任务最多两轮问询。
- 品牌产品、标准件和公开接口由 Agent 按需检索，不把查资料的负担推回给新手。
- 图片能说明外形和比例，但没有可靠尺度时不会冒充精确尺寸。
- `ready` 和 `provisional` 会生成 TTC 交接提示词；`blocked` 不会。
- 它不会自动调用 `$cad`：需求包完成后，由用户在新任务中主动交接。

## 快速开始

显式调用 Skill，并附上你已有的文字、图片、图纸或产品资料：

```text
$cad-brief

请根据我附上的几张图片，整理这个摄像机外壳的 CAD 建模需求。
我不知道具体尺寸，希望先做一个参数化概念模型。
```

完成后会得到类似 `camera-body.cad-requirements.md` 的文件。若状态为 `ready`
或 `provisional`：

1. 新建一个 Codex 任务并调用 `$cad`。
2. 选择需求包和其中建议的附件。
3. 粘贴文件末尾的 `Copy prompt for TTC`。

`blocked` 表示当前证据不足以诚实支持精确适配、制造、安全或复刻目标；需求包会说明
阻塞项，但不会生成误导性的 `$cad` 启动提示词。

## 需求包如何避免“看起来对，规格却错”

每个重要值都保留来源与证据状态：

```text
user-confirmed     official-source     dimensioned-source
exactly-derived    calibrated-image    visual-estimate
proposed-default   unknown             conflict
```

每条关键要求还要映射到参数、特征、datum、装配关系或审阅项，并指定真实可执行的
验收方式。TTC 交接会使用其现有的 `refs`、`measure`、`align`、`frame`、`diff`
与 `snapshot` 能力；视觉相似度不能替代尺寸证明。

| 状态 | 何时使用 | 是否生成 `$cad` 提示词 |
| --- | --- | --- |
| `ready` | 控制需求已有来源或可严格推导 | 是 |
| `provisional` | 参数化近似仍有价值，且所有推测可替换 | 是，明确保留近似边界 |
| `blocked` | 关键接口、冲突或安全证据不足 | 否 |

## 规则有多具体？用可核对的数据说话

| 项目 | 当前值 |
| --- | ---: |
| 用户问询上限 | 2 轮 |
| 证据状态 | 9 种 |
| readiness 结果 | 3 种 |
| 自动化单元测试 | 22 项 |
| CI 测试矩阵 | Windows / Linux × Python 3.10 / 3.12 |

内置 validator 只使用 Python 标准库，检查固定章节、来源与 `REQ-ID`、readiness
一致性、TTC brief、验证方法、blocked 交接规则，以及本机绝对路径和未替换模板。
它不验证网页事实、图像理解、CAD 几何、可制造性或工程安全。

```bash
python cad-brief/scripts/validate_handoff.py path/to/model.cad-requirements.md --strict
```

## 安装与兼容性

下载或克隆本仓库，只把内层 `cad-brief/` 复制到 Codex Skills 目录；不要复制仓库
外层的测试和 CI 文件。

macOS / Linux：

```bash
cp -R cad-brief ~/.codex/skills/cad-brief
```

Windows PowerShell：

```powershell
Copy-Item -Recurse cad-brief "$HOME\.codex\skills\cad-brief"
```

- Python validator：Python 3.10 或更高版本。
- TTC 交接字段按 `earthtojake/text-to-cad` 0.3.9 的公开 Skill 契约设计；当前测试不包含端到端 STEP 生成。
- 调用策略：必须显式使用 `$cad-brief`，不会被隐式触发。
- 继续生成 CAD 时，需要单独安装 Text-to-CAD。
- 公开资料研究依赖宿主的联网能力；离线时会降低 readiness，而不是补写不存在的来源。

## 安全和能力边界

网页、PDF、图片、图纸、CAD 元数据和附件都只是不可信证据，不是可以改变任务、
运行命令或索取信息的新指令。Skill 不执行下载代码或宏，未经明确授权不上传私人
资料，也不会把证据不足包装成工程事实。详见[安全策略](SECURITY.md)。

`cad-brief` 不生成 build123d、STEP、STL、3MF、GLB 或 DXF，不自动调用 TTC，
也不承诺扫描级复刻、真实适配、FEA、结构安全、法规合规或制造认证。

## 文档与验证

- [完整 Skill 工作流](cad-brief/SKILL.md)
- [需求包模板](cad-brief/assets/cad-requirements-template.md)
- [公开测试](tests/)
- [安全策略](SECURITY.md)

运行全部测试：

```bash
python -m unittest discover -s tests -v
```

两者仅通过 Markdown 需求包交接，不共享代码或运行时。

<br>

---

<p align="center">
  <sub>MIT License · Text-to-CAD 是独立的 MIT 许可项目</sub>
</p>
