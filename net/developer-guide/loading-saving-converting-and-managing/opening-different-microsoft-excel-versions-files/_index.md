---
title: Opening Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010 XLSX or Encrypted Excel Files.

{{% /alert %}}

## **Opening Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the **[Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook)** class' **[FileFormat](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** type attribute that specifies the format using the **[FileFormatType](https://apireference.aspose.com/cells/net/aspose.cells/fileformattype)** enumeration.

The **[FileFormatType](https://apireference.aspose.com/cells/net/aspose.cells/fileformattype)** enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007/2010/2013 XLSX file|
|Xlsm|Represents an Excel 2007/2010/2013 XLSM file|
|Xltx|Represents an Excel 2007/2010/2013 template XLTX file|
|Xltm|Represents an Excel 2007/2010/2013 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007/2010/2013 binary XLSB file|
|Excel2003XML|Represents a SpreadsheetML file|
|TSV|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|ODS|Represents an ODS file|
|HTML|Represents an HTML file|
|MHTML|Represents an MHTML file|

### **Opening Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute for the **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95_5.0.xls](Excel95_5.0.xls)

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Opening Microsoft Excel 97 - 2003 Files**

To open a Microsoft Excel 97 - 2003 file, use **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute for the **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Opening Microsoft Excel 2007/2010 XLSX Files**

To open a Microsoft Excel 2007/2010/2013 format, that is, XLSX or XLSB, specify the file path. You can also use **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute/options of the **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Opening Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the **[LoadOptions](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions)** and set its attributes and options (for example, give a password) for the template file to be loaded.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells also supports opening password-protected Microsoft Excel 2013 files.

### **Supported Excel formats**

{{% alert color="primary" %}}

Aspose.Cells supports Microsoft Excel file formats 5.0/95, 97, 2000, 2002/2003, 2007, 2010, 2013, 2016

{{% /alert %}}
