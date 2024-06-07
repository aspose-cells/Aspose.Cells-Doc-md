---
title: 以带有工具提示的方式将 Excel 转换为 HTML
type: docs
weight: 150
url: /zh/java/convert-excel-to-html-with-tooltip/
---

## **以带有工具提示的方式将 Excel 转换为 HTML**

可能存在文本在生成的 HTML 中被截断的情况，您希望在悬停事件上显示完整文本作为工具提示。Aspose.Cells 通过提供 **[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)** 属性来支持此功能。将 **[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)** 属性设置为 **true** 将在生成的 HTML 中添加完整文本作为工具提示。

下图显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载了 [源 Excel 文件](AddTooltipToHtmlSample.xlsx) 并生成了带有工具提示的 [输出 HTML 文件](AddTooltipToHtmlSample_out.zip)。

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
