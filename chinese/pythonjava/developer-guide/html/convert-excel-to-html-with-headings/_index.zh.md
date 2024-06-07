---
title: 将 Excel 转换为带有标头的 HTML
type: docs
weight: 10
url: /zh/python-java/convert-excel-to-html-with-headings/
---

## **将 Excel 转换为带有标头的 HTML**
Aspose.Cells提供了在将Excel转换为HTML时导出行和列标题的选项。可以通过API提供的[HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings)属性来实现。[HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings)的默认值为**False**。将**True**作为参数传递以在输出的HTML文件中呈现标题。以下图片显示了以下代码生成的输出文件。

![todo:image_alt_text](PrintHeadings.jpg)

以下示例代码演示了如何使用[HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings)属性来在输出的HTML文件中呈现标题。
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}
