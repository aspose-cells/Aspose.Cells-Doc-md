---
title: HTML保存時にCSSを無効にするPython.NETを使用する設定
linktitle: HTML保存時にCSSを無効にする
type: docs
weight: 320
url: /ja/python-net/disable-css-while-saving-to-html/
description: Aspose.Cells for Python via .NET APIを使用し、ExcelファイルをHTML形式で保存する際にCSSスタイルを無効にする方法を学びます。
---

## **可能な使用シナリオ**

Excelファイルを単一ページHTMLに保存すると、通常CSS要素はHTMLファイルに埋め込まれ、HEADセクションに配置されます。このファイルをメールの内容/bodyとして添付する場合、多くのメールクライアントでCSS要素が削除され、不適切なレンダリングが発生します。Aspose.Cells for Python via .NET APIは、スタイルを直接HTML要素内に適用できるオプションを導入しています。メールの内容/bodyとしてHTMLを設定したい場合は、[**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) プロパティを設定して**True**にしてください。

## **HTML保存時にCSSを無効にする**

次のサンプルコードは、[**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) プロパティの使用例を示しています。

## **サンプルコード**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
