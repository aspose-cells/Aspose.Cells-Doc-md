---
title: 将 Excel 转换为带有工具提示的 HTML
type: docs
weight: 150
url: /zh/java/convert-excel-to-html-with-tooltip/
---

## **将 Excel 转换为带有工具提示的 HTML**

在生成的HTML中，可能会出现文本被截断的情况，你希望在悬停事件上显示完整的文本作为工具提示。Aspose.Cells通过提供**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**属性来支持此功能。将**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**属性设置为**true**，将在生成的HTML中添加完整的文本作为工具提示。

以下图片显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码样本加载了[source excel file](AddTooltipToHtmlSample.xlsx)并生成了带有工具提示的[output HTML file](AddTooltipToHtmlSample_out.zip)。

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
