---
title: Convert Excel to CSV, TSV, and TXT
linktitle: Save as CSV, TSV, and TXT
type: docs
weight: 40
url: /net/convert-excel-to-csv-tsv-and-txt/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to convert Excel, ODS, JSON, and other formatted files to CSV, TSV, and TXT.

{{% /alert %}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (e.g., XLS, XLSX, XLSM, XLSB, ODS, etc.) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) is a comma, so do not specify a separator if saving to CSV format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have customized delimiters between its data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Advanced topics**
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="csharp" >}}
