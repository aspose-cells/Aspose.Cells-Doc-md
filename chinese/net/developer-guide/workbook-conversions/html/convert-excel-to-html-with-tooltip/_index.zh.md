---
title: 将 Excel 转换为带有工具提示的 HTML
type: docs
weight: 200
url: /zh/net/convert-excel-to-html-with-tooltip/
---

## **将 Excel 转换为带有工具提示的 HTML**

在生成的 HTML 中可能会出现文本被截断的情况，您希望在悬停事件上显示完整的文本作为工具提示。 Aspose.Cells 通过提供 **[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** 属性来支持这一点。 将 **[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** 属性设置为 **true** 将在生成的 HTML 中添加完整的文本作为工具提示。

以下图片显示了生成的 HTML 文件中的工具提示。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

以下代码示例加载 [源 Excel 文件](98107416.xlsx) 并生成带有工具提示的 [输出 HTML 文件](98107417.zip)。

示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
