---
title: Opening Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /python-java/opening-different-microsoft-excel-versions-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX or Encrypted Excel Files.

{{% /alert %}}

## **Opening Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 . You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) class' [**setFileFormat**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat) method to specifies the format using the [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) enumeration.
	
The [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
|CSV|Represents a CSV file|
|EXCEL_97_TO_2003|Represents an Excel 97 - 2003 file|
|XLSX|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file|
|XLSM|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file|
|XLTX|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file|
|XLTM|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro-enabled XLTM file|
|XLSB|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file|
|SPREADSHEET_ML|Represents a SpreadsheetML file|
|TSV|Represents a Tab-separated values file|
|TAB_DELIMITED|Represents a Tab Delimited text file|
|ODS|Represents an ODS file|
|HTML|Represents an HTML file|
|M_HTML|Represents an MHTML file|

### **Opening Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) and set the related attribute for the **LoadOptions** class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Opening Microsoft Excel 97 - 2003 Files**

To open a Microsoft Excel 97 - 2003 file, use [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) and set the related attribute for the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365  XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format, that is, XLSX or XLSB, specify the file path. You can also use [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) and set the related attribute/options of the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Opening Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) and set its attributes and options (for example, give a password) for the template file to be loaded.
A sample file for testing this feature can be downloaded from the following link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells also supports opening password-protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 files.


