---
title: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format
type: docs
weight: 100
url: /net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Possible Usage Scenarios**
Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line

{{< highlight java >}}

 ,,,data1,data2 

{{< /highlight >}}

Here the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, then Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells does not discard leading blank columns and rows on saving but if you want to remove them just like Microsoft Excel does, then Aspose.Cells provides [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/net/cells/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) property. Please set it to **true** and then all the leading blank rows and columns will be discarded on saving.

{{% alert color="primary" %}} 

Prior to the release of Aspose.Cells for .NET 20.4, the default value of [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/net/cells/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) was **false**. Since the 20.4 release, the default value of [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/net/cells/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) is **true.**

{{% /alert %}} 
## **Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format**
The following sample code loads the [source excel file](attachments/25002392/25395207.xlsx) which has two leading blank columns. It first saves the excel file in CSV format without any changes and then it sets [TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://apireference.aspose.com/net/cells/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) property to **true** and saves it again. The screenshot shows the [source excel file](attachments/25002392/25395207.xlsx), [output CSV file without trimming](attachments/25002392/25395209.csv), and the [output CSV file with trimming](attachments/25002392/25395208.csv).



![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
