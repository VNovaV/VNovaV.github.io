#!/usr/bin/env python3
"""由可编辑的 editor.html 重新生成只读公开主页 index.html。

原理：editor.html 与 index.html 共享同一份代码，仅 READONLY 开关不同。
本脚本把 editor.html 中 `const READONLY=false;` 翻转为 `true` 后写入 index.html。
"""
import sys

SRC = "editor.html"
DST = "index.html"
FLAG_OFF = "const READONLY=false;"
FLAG_ON = "const READONLY=true;"


def main():
    try:
        with open(SRC, encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        print(f"找不到 {SRC}，请在站点根目录运行本脚本", file=sys.stderr)
        sys.exit(1)

    if FLAG_OFF not in src:
        print(f"错误：{SRC} 中未找到 `{FLAG_OFF}`，请确认文件未被改动。", file=sys.stderr)
        sys.exit(1)

    dst = src.replace(FLAG_OFF, FLAG_ON, 1)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(dst)
    print(f"已生成只读主页：{DST}（READONLY=true）")


if __name__ == "__main__":
    main()
