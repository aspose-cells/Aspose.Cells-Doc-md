---
title: Opening Files with Different Formats
type: docs
weight: 30
url: /net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API allows you to open/read different formats like XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Using Aspose.Cells you can open files with different formats. **Aspose.Cells** can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files etc.

If you need to know all supported file formats, please refer to the following pages:
[Supported File Formats](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Opening Files with Different Formats**

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV), ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### **Opening SpreadsheetML Files**

SpreadsheetML files are XML representations of spreadsheets including all information about it, such as formatting, formulae etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Opening HTML Files**

Aspose.Cells allows you to open HTML file into Workbook object. The HTML file should Microsoft Excel oriented i.e MS-Excel should be able to open it.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Opening CSV Files**

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Using preferred parser**

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose **TxtLoadOptions.PreferredParsers** is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Opening Tab Delimited Files**

Tab delimited (Text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Opening Tab-Separated Values (TSV) Files**

Tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same with Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}

### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Opening FODS Files**

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}