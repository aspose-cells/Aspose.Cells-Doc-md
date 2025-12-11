---
title: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format
type: docs
weight: 100
url: /net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line

{{< highlight java >}}
,,,data1,data2
{{< /highlight >}}

Here, the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells does not discard leading blank columns and rows on saving, but if you want to remove them just like Microsoft Excel does, Aspose.Cells provides the [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) property. Set it to **true**, and all the leading blank rows and columns will be discarded on saving.

{{% alert color="primary" %}}
Prior to the release of Aspose.Cells for .NET 20.4, the default value of [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) was **false**. Since the 20.4 release, the default value of [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) is **true**.
{{% /alert %}}

## **Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format**

The following sample code loads the [source Excel file](sampleTrimBlankColumns.xlsx), which has two leading blank columns. It first saves the Excel file in CSV format without any changes, and then sets the [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) property to **true** and saves it again. The screenshot shows the [source Excel file](sampleTrimBlankColumns.xlsx), the [output CSV file without trimming](outputWithoutTrimBlankColumns.csv), and the [output CSV file with trimming](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
