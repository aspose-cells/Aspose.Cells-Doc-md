---
title: Convert Excel to Markdown
type: docs
weight: 20
url: /net/convert-excel-to-markdown/
---

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass **[SaveFormat.Markdown](https://apireference.aspose.com/cells/net/aspose.cells/saveformat)** as the second parameter of **[Workbook.Save](https://apireference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** method. You may also use **[MarkdownSaveOptions](https://apireference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** class to specify additional settings for exporting worksheet to Markdown.

## **Live Example**
Aspose.Cells for .NET presents you online free application [“Convert Excel to Markdown”](https://products.aspose.app/cells/conversion/excel-to-md), where you may try to investigate the functionality and quality it works.
<div>
{{% cells-convert excel-to-md %}}
</div>

## **Convert Excel Workbook to Markdown**
The following code example demonstrates exporting active worksheet to Markdown by using **[SaveFormat.Markdown](https://apireference.aspose.com/cells/net/aspose.cells/saveformat)** enumeration member.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}