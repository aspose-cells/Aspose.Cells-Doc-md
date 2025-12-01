---
title: Opening Files with Different Formats
type: docs
weight: 30
url: /python-net/opening-files-with-different-formats/
description: Aspose.Cells for Python via .NET API allows you to open/read different formats like XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Using Aspose.Cells for Python via .NET you can open files with different formats. Aspose.Cells for Python via .NET can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files etc.

If you need to know all supported file formats, please refer to the following pages:
[Supported File Formats](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Opening Files with Different Formats**

Aspose.Cells for Python via .NET allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV), ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### **Opening SpreadsheetML Files**

SpreadsheetML files are XML representations of spreadsheets including all information about it, such as formatting, formulae etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Opening HTML Files**

Aspose.Cells for Python via .NET allows you to open HTML file into Workbook object. The HTML file should Microsoft Excel oriented i.e MS-Excel should be able to open it.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Opening CSV Files**

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells for Python via .NET API which is demonstrated in the code example given below.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Opening Tab Delimited Files**

Tab delimited (Text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Opening Tab-Separated Values (TSV) Files**

Tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same with Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells for Python via .NET can read SXC files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Opening FODS Files**

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells for Python via .NET can read FODS files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
