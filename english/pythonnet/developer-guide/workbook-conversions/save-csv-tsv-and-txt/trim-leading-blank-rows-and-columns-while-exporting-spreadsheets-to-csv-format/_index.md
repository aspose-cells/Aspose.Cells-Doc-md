---
title: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format
type: docs
weight: 100
url: /python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format by using Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, your Excel or CSV file has leading blank columns or rows. For example, consider this line

{{< highlight java >}}
 ,,,data1,data2
{{< /highlight >}}

Here the first three cells or columns are blank. When you open such a CSV file in Microsoft Excel, Microsoft Excel discards these leading blank rows and columns.

By default, Aspose.Cells for Python via .NET does not discard leading blank columns and rows when saving, but if you want to remove them, just as Microsoft Excel does, Aspose.Cells for Python via .NET provides [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) property. Please set it to **true** and all the leading blank rows and columns will be discarded on saving.

{{% alert color="primary" %}}

Prior to the release of Aspose.Cells for Python via .NET 20.4, the default value of [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) was **false**. Since the 20.4 release, the default value of [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) is **true**.

{{% /alert %}}

## **Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format**

The following sample code loads the [source Excel file](sampleTrimBlankColumns.xlsx) which has two leading blank columns. It first saves the Excel file in CSV format without any changes, and then sets the [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) property to **true** and saves it again. The screenshot shows the [source Excel file](sampleTrimBlankColumns.xlsx), the [output CSV file without trimming](outputWithoutTrimBlankColumns.csv), and the [output CSV file with trimming](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
