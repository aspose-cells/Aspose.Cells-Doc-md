---
title: Opening Files with Different Formats
type: docs
weight: 30
url: /nodejs-java/opening-files-with-different-formats/
description: Aspose.Cells for Node.js via Java API allows you to open/read different formats like XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Using Aspose.Cells you can open files with different formats. **Aspose.Cells** can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma‐Separated values (CSV), Tab Delimited or Tab‐Separated values (TSV) files, etc.

If you need to know all supported file formats, please refer to the following page:
[Supported File Formats](https://docs.aspose.com/cells/nodejs-java/supported-file-formats/)

{{% /alert %}}

## **Opening Files with Different Formats**

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma‐Separated values (CSV), Tab Delimited or Tab‐Separated values (TSV), ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### **Opening SpreadsheetML Files**

SpreadsheetML files are XML representations of spreadsheets including all information about them, such as formatting, formulae, etc. Since Microsoft Excel XP, an XML export option has been added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningSpreadsheetMLFiles-1.js" >}}

### **Opening HTML Files**

Aspose.Cells allows you to open an HTML file into a Workbook object. The HTML file should be Microsoft Excel‐oriented, i.e., MS‐Excel should be able to open it.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningHTMLFile-1.js" >}}

### **Opening CSV Files**

Comma‐Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double‐quote character. If a field value contains a double‐quote character, it is escaped with a pair of double‐quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningCSVFiles-1.js" >}}

#### **Opening CSV files and replacing invalid characters**

In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API, which is demonstrated in the code example given below.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.js" >}}

<!--

#### **Using preferred parser**

It is not always necessary to use the default parser settings when opening CSV files. Sometimes importing a CSV file does not produce the expected output, such as an incorrect date format or improper handling of empty fields. For this purpose, **TxtLoadOptions.PreferredParsers** is available to provide a preferred parser for parsing different data types as required. The following sample code demonstrates the usage of the preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningCSVFilesWithPreferredParser-1.js" >}}

-->

### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningTextFilewithCustomSeparator-1.js" >}}

### **Opening Tab Delimited Files**

Tab delimited (Text) files contain spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningTabDelimitedFiles-1.js" >}}

### **Opening Tab‐Separated Values (TSV) Files**

Tab‐separated values (TSV) files contain spreadsheet data but without any formatting. They are the same as Tab‐Delimited files, where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningTSVFiles-1.js" >}}

### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningSXCFiles-1.js" >}}

### **Opening FODS Files**

A FODS file is a spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningFODSFiles-1.js" >}}

<!--{{< app/cells/assistant language="csharp" >}}-->