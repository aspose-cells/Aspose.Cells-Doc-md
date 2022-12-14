---
title: 使用工具提示将 Excel 转换为 HTML
type: docs
weight: 200
url: /zh/net/convert-excel-to-html-with-tooltip/
---
## **使用工具提示将 Excel 转换为 HTML**

在某些情况下，生成的 HTML 中的文本可能会被截断，而您希望将完整的文本显示为悬停事件的工具提示。 Aspose.Cells 通过提供支持这一点**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)**财产。设定**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)**财产给**真的**将在生成的 HTML 中添加完整的文本作为工具提示。

下图显示了生成的 HTML 文件中的工具提示。

![待办事项：图片_替代_文本](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载[源文件](98107416.xlsx)并生成[输出 HTML 文件](98107417.zip)与工具提示。

示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
