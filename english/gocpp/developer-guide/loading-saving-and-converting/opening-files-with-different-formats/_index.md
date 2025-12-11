---
title: Opening Files with Different Formats
type: docs
weight: 30
url: /go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for Go via C++ API allows you to open/read different formats like XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Using Aspose.Cells, you can open files with different formats. **Aspose.Cells** can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma‑Separated values (CSV), tab‑delimited or tab‑separated values (TSV) files, etc.

If you need to know all supported file formats, please refer to the following pages:  
[Supported File Formats](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Opening Files with Different Formats**

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma‑Separated values (CSV), tab‑delimited or tab‑separated values (TSV), and ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### **Opening SpreadsheetML Files**

SpreadsheetML files are XML representations of spreadsheets including all information about them, such as formatting, formulae, etc. Since Microsoft Excel XP, an XML export option has been added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Opening HTML Files**

Aspose.Cells allows you to open an HTML file into a Workbook object. The HTML file should be Microsoft Excel‑oriented, i.e., MS Excel should be able to open it.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Opening CSV Files**

Comma‑Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double‑quote character. If a field value contains a double‑quote character, it is escaped with a pair of double‑quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain‑text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Sample source files can be downloaded from the following links for testing this feature.

[CustomSeparator.txt](CustomSeparator.txt)

### **Opening Tab Delimited Files**

A tab‑delimited (text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab‑delimited file is a special kind of plain‑text file with a tab between each column.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Opening Tab‑Separated Values (TSV) Files**

A tab‑separated values (TSV) file contains spreadsheet data but without any formatting. It is the same as a tab‑delimited file, with data arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files, as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Opening FODS Files**

A FODS file is a spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files, as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}