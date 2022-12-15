---
title: 使用工具提示将 Excel 转换为 HTML
type: docs
weight: 150
url: /zh/java/convert-excel-to-html-with-tooltip/
---
## **使用工具提示将 Excel 转换为 HTML**

在某些情况下，生成的 HTML 中的文本可能会被截断，而您希望将完整的文本显示为悬停事件的工具提示。 Aspose.Cells 通过提供支持这一点**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**财产。设定**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**财产给**真的**将在生成的 HTML 中添加完整的文本作为工具提示。

下图显示了生成的 HTML 文件中的工具提示。

![待办事项：图像_替代_文本](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载[源文件](AddTooltipToHtmlSample.xlsx)并生成[输出 HTML 文件](AddTooltipToHtmlSample_out.zip)与工具提示。

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
