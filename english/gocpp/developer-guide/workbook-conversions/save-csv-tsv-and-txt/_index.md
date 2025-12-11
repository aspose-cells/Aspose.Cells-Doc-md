---
title: Convert Excel to CSV, TSV and Txt with Golang via C++
linktitle: Save as CSV, TSV and Txt
type: docs
weight: 40
url: /go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Easily convert Excel files to CSV, TSV, and TXT formats using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to convert Excel, ODS, JSON, and other format files to CSV, TSV, and TXT.

{{% /alert %}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (e.g., XLS, XLSX, XLSM, XLSB, ODS, etc.) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) is a comma, so do not specify a separator when saving to CSV format.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}

## **Advanced topics**
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)