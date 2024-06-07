---
title: 以带有工具提示的方式将 Excel 转换为 HTML
type: docs
weight: 200
url: /zh/python-net/convert-excel-to-html-with-tooltip/
description: 这个主题向您展示如何使用Aspose.Cells for Python通过.NET将Excel转换为带工具提示的HTML。
keywords: Python将Excel转换为带工具提示的HTML，使用Python通过.NET将Excel转换为带工具提示的HTML，使用Python通过.NET将Excel转换为带工具提示的HTML，Python工作簿转为带工具提示的HTML。
---

## **以带有工具提示的方式将 Excel 转换为 HTML**

在生成的HTML中可能会出现文本被截断的情况，您想要在悬停事件中显示完整文本作为工具提示。Aspose.Cells支持此功能，通过提供**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)**属性。将**[HtmlSaveOptions.add_tooltip_text](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/)**属性设置为**true**将在生成的HTML中添加完整文本作为工具提示。

下图显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下示例代码加载 [源 Excel 文件](98107416.xlsx) 并生成带有工具提示的 [输出 HTML 文件](98107417.zip)。

示例代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
