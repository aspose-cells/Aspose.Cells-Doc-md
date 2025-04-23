---
title: 用 Python.NET 在保存为HTML时启用CSS自定义属性
linktitle: 在保存为HTML时启用CSS自定义属性
type: docs
weight: 320
url: /zh/python-net/enable-css-custom-properties-while-saving-to-html/
description: 学习如何在使用 Aspose.Cells for Python via .NET API 将Excel文件保存为HTML时启用CSS自定义属性。
---

## **可能的使用场景**

当你将Excel文件保存为HTML时，针对同一基础图片多次出现的场景，使用CSS自定义属性可以仅保存一次图片数据。这提高了生成的HTML性能。保存为HTML时，使用 [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) 属性并设置为 **True**。

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **在保存为HTML时启用CSS自定义属性**

以下示例代码演示了使用 [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) 属性。当未设置为 True 时的效果截图。可以下载示例Excel文件（50528260.xlsx）和生成的HTML（50528261.zip）以参考。

## **示例代码**

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
