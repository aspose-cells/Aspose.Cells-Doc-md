---
title: 将 Excel 转换为带有工具提示的 HTML
type: docs
weight: 200
url: /zh/python-net/convert-excel-to-html-with-tooltip/
description: 本主题向您展示了如何使用 Aspose.Cells for Python via NET 将 Excel 转换为带有工具提示的 HTML。
keywords: 使用 Python 将 Excel 转换为带有工具提示的 HTML，使用 Python 将 Excel 转换为带有工具提示的 HTML via NET，Python via NET 将 Excel 转换为带有工具提示的 HTML，Python 将工作簿转换为带有工具提示的 HTML。
---

## **将 Excel 转换为带有工具提示的 HTML**

在生成的 HTML 中可能出现文字被截断的情况，您希望在悬停事件中以提示框的方式显示完整的文字。Aspose.Cells 通过提供 [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) 属性来支持此功能。将 [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) 属性设置为 **true** 将在生成的 HTML 中添加完整的文字提示。

以下图片显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载 [源 Excel 文件](98107416.xlsx) 并生成带有工具提示的 [输出 HTML 文件](98107417.zip)。

示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
