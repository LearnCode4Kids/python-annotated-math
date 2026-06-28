# Python Annotated Math

这是一个基于 annbook 结构的 annotated notebook 课程仓库。

## 目录结构

- `books/`: 课程 Notebook 和 Markdown 页面
- `codes/`: 可复用的示例代码与工具函数
- `papers/`: 论文、讲义或其他参考资料
- `slides/`: 课程幻灯片
- `_build/books/`: 本地构建输出目录

## 常用命令

构建课程网站：

```bash
./book_generate.sh
```

本地预览：

```bash
./book_start.sh
```

GitHub Pages 发布工作流位于 `.github/workflows/pages.yml`。
