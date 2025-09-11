---
title: Opening Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX or Encrypted Excel Files.

{{% /alert %}}

## **Opening Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 . You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/) method to specifies the format using the [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) enumeration.
	
The [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
|FileFormatType_CSV|Represents a CSV file|
|FileFormatType_Excel97To2003|Represents an Excel 97 - 2003 file|
|FileFormatType_Xlsx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file|
|FileFormatType_Xlsm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file|
|FileFormatType_Xltx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file|
|FileFormatType_Xltm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro-enabled XLTM file|
|FileFormatType_Xlsb|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file|
|FileFormatType_SpreadsheetML|Represents a SpreadsheetML file|
|FileFormatType_Tsv|Represents a Tab-separated values file|
|FileFormatType_TabDelimited|Represents a Tab Delimited text file|
|FileFormatType_Ods|Represents an ODS file|
|FileFormatType_Html|Represents an HTML file|
|FileFormatType_MHtml|Represents an MHTML file|

### **Opening Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute for the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Opening Microsoft Excel 97 - 2003 Files**

To open a Microsoft Excel 97 - 2003 file, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute for the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365  XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format, that is, XLSX or XLSB, specify the file path. You can also use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) and set the related attribute/options of the [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) class for the template file to be loaded.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells also supports opening password-protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 files.


{{< app/cells/assistant language="cpp" >}}