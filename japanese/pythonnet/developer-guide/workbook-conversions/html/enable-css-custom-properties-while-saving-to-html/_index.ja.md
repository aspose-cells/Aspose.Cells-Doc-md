---
title: HTML保存時にCSSカスタムプロパティを有効にする
linktitle: HTML保存時にCSSカスタムプロパティを有効にする方法を学びます。
type: docs
weight: 320
url: /ja/python-net/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for Python via .NET APIを使用して、ExcelファイルをHTMLに保存する際にCSSカスタムプロパティを有効にする方法を学びます。
---

## **可能な使用シナリオ**

HTML保存時にCSSカスタムプロパティを有効にする

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。**

以下のサンプルコードは、[**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/)属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。このコードに使用されたサンプルExcelファイル（50528260.xlsx）と生成されたHTML（50528261.zip）もダウンロードできます。

## **サンプルコード**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
