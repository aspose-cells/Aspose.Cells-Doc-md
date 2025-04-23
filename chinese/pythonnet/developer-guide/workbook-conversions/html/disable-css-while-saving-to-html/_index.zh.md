---
title: 在用 Python.NET 保存为HTML时禁用CSS
linktitle: 在保存为HTML时禁用CSS
type: docs
weight: 320
url: /zh/python-net/disable-css-while-saving-to-html/
description: 学习如何在使用 Aspose.Cells for Python via .NET API 将Excel文件保存为HTML格式时禁用CSS样式。
---

## **可能的使用场景**

当你将Excel文件保存为单页HTML时，CSS元素通常会嵌入HTML文件中，位于HEAD部分。如果你将此文件作为邮件内容/正文附件使用，大多数电子邮件客户端会剥离CSS元素，导致显示异常。Aspose.Cells for Python via .NET API推出了一个选项，允许你选择性禁用CSS，从而将样式直接应用到HTML元素中。如果你希望将HTML用作电子邮件正文，请使用 [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) 属性并设置为 **True**。

## **在保存为HTML时禁用CSS**

以下示例代码演示了 [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) 属性的用法。

## **示例代码**

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
