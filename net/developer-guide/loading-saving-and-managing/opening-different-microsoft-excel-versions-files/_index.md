---
title: Opening Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX or Encrypted Excel Files.

{{% /alert %}}

## **Opening Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 . You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** class' **[FileFormat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** type attribute that specifies the format using the **[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)** enumeration.

The **[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)** enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
|Csv|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file|
|Xlsm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file|
|Xltx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file|
|Xltm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file|
|SpreadsheetML|Represents a SpreadsheetML file|
|Tsv|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|Ods|Represents an ODS file|
|Html|Represents an HTML file|
|Mhtml|Represents an MHTML file|

### **Opening Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute for the **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95_5.0.xls](Excel95_5.0.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Opening Microsoft Excel 97 - 2003 Files**

To open a Microsoft Excel 97 - 2003 file, use **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute for the **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365  XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format, that is, XLSX or XLSB, specify the file path. You can also use **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** and set the related attribute/options of the **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Opening Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the **[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** and set its attributes and options (for example, give a password) for the template file to be loaded.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells also supports opening password-protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 files.


