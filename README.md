# VNovaV.github.io

个人作品集站点（3D 角色建模方向），由 GitHub Pages 自动托管：

👉 https://VNovaV.github.io

## 这是什么

一个 3D 角色作品集单页应用，采用「**展示 / 编辑分离**」结构：

| 文件 | 给谁 | 说明 |
|------|------|------|
| `index.html` | 所有人（公开主页） | **只读展示页**：访客只能看，不能改文字/图片 |
| `editor.html` | 仅你自己 | **可编辑编辑器**：上传图片、改文字、切配色、导出 |
| `assets/` | — | 固定图片文件（`p01.jpg`…`p10.jpg`），由 `index.html` 相对路径引用 |

- 点格子上传图片（或拖拽），自动存入浏览器本地（IndexedDB）
- 文字均可双击/直接编辑（作品名、章节、图片说明等）
- 右上角可切换 4 套配色：纸白 / 墨黑 / 暖米 / 深蓝
- 滚动有入场动画与图片视差效果
- 内容自动保存在本地，刷新不丢

## 公开主页为什么访客改不了

`index.html` 在加载时进入只读模式（`READONLY=true`）：
页面会移除所有 `contenteditable`、隐藏上传/删除/新增/重置/导出等按钮，
未配置固定图的空格子也会被隐藏。访客看到的是干净的作品展示页。

## 如何更新公开主页

公开内容以仓库为准。两种改法：

1. **换图 / 加图（最简单）**：把图片放进 `assets/`，告诉我文件名与要替换的格子，
   我在 `editor.html` 里改对应 `src`（`assets/xxx.jpg`），重新生成 `index.html` 并推送。
2. **导出静态页**：用 `editor.html` 编辑好后点「导出静态页」下载 `index.html`（图片内嵌），
   把文件发我，我替换公开主页。

> 注：浏览器本地编辑（IndexedDB / localStorage）只是你个人草稿，不会影响公开站点；
> 要让别人看到改动，必须更新仓库里的文件并重新推送。

## 本地预览

```bash
python -m http.server 8000
# 然后访问 http://localhost:8000        （只读主页）
#          http://localhost:8000/editor.html （编辑器）
```

## 从编辑器重新生成只读主页（维护用）

`editor.html` 与 `index.html` 共享同一份代码，仅 `READONLY` 开关不同。
修改 `editor.html` 后，用以下命令重新生成 `index.html`：

```bash
python build_readonly.py
```

## 目录结构

```
.
├── index.html      # 公开只读展示页（READONLY=true）
├── editor.html     # 可编辑编辑器（READONLY=false）
├── build_readonly.py  # 由 editor.html 重新生成 index.html 的脚本
├── assets/         # 固定图片（p01.jpg … p10.jpg）
└── README.md
```
