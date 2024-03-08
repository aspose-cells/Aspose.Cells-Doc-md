---
title: 使用工具提示将 Excel 转换为 HTML
type: docs
weight: 200
url: /zh/python-net/convert-excel-to-html-with-tooltip/
description: 本主题向您展示如何使用 Aspose.Cells for Python 通过 NET 将 Excel 转换为带有工具提示的 HTML。
keywords: Python Convert Excel to HTML with tooltip, Convert Excel to HTML with tooltip Python via NET, Python via NET Excel to HTML with tooltip, Python Workbook to HTML with tooltip.
---
##  **使用工具提示将 Excel 转换为 HTML**

在某些情况下，生成的 HTML 中的文本可能会被截断，而您希望在悬停事件上将完整文本显示为工具提示。 Aspose.Cells 通过提供来支持这一点**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)**财产。设置**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)**财产给**真的**将在生成的 HTML 中添加完整的文本作为工具提示。

下图显示了生成的 HTML 文件中的工具提示。

![待办事项：图像_替代_文本](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载[源 Excel 文件](98107416.xlsx)并生成[输出HTML文件](98107417.zip)与工具提示。

示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
