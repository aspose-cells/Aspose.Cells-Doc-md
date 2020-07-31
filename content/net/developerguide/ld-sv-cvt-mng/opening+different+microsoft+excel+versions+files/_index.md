---
title : "Opening Different Microsoft Excel Versions Files" 
description : "" 
weight : 12061 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/opening+different+microsoft+excel+versions+files/
---

# Aspose.Cells for .NET : Opening Different Microsoft Excel Versions Files


Aspose.Cells can open a range of different Microsoft Excel Versions Files, such as Microsoft Excel 95/97 - 2003, SpreadsheetML, Opening Microsoft Excel 2007/2010 XLSX or Encrypted Excel Files.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Opening Files of Different Microsoft Excel Versions](#opening-files-of-different-microsoft-excel-versions)
    *   1.1 [Opening Microsoft Excel 95/5.0 Files](#opening-microsoft-excel-95/5.0-files)
    *   1.2 [Opening Microsoft Excel 97 - 2003 Files](#opening-microsoft-excel-97---2003-files)
    *   1.3 [Opening Microsoft Excel 2007/2010 XLSX Files](#opening-microsoft-excel-2007/2010-xlsx-files)
    *   1.4 [Opening Encrypted Excel Files](#opening-encrypted-excel-files)
    *   1.5 [Unsupported Excel formats](#unsupported-excel-formats)
{{< /panel >}}
 

## Opening Files of Different Microsoft Excel Versions

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95,97, or Microsoft Excel 2007/2010. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS and so on. Use the constructor, or specify the [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class' [FileFormat](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/fileformat) type attribute that specifies the format using the [FileFormatType](https://apireference.aspose.com/net/cells/aspose.cells/fileformattype) enumeration.

The [FileFormatType](https://apireference.aspose.com/net/cells/aspose.cells/fileformattype) enumeration contains many pre-defined file formats some of which are given below.

{{< table style="table-striped" >}}
|File Format Types|Description|
|:----|:----|
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
{{< /table >}}

### Opening Microsoft Excel 95/5.0 Files

To open a Microsoft Excel 95/5.0 file, use [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) and set the related attribute for the [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95\_5.0.xls](https://docs2.aspose.com/cells/net/attachments/5013531/81920920.xls)

### Opening Microsoft Excel 97 - 2003 Files

To open a Microsoft Excel 97 - 2003 file, use [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) and set the related attribute for the [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) class for the template file to be loaded.

### Opening Microsoft Excel 2007/2010 XLSX Files

To open a Microsoft Excel 2007/2010/2013 format, that is, XLSX or XLSB, specify the file path. You can also use [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) and set the related attribute/options of the [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) class for the template file to be loaded.

### Opening Encrypted Excel Files

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the [LoadOptions](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions) and set its attributes and options (for example, give a password) for the template file to be loaded.

  
Aspose.Cells also supports opening password-protected Microsoft Excel 2013 files.

### Unsupported Excel formats

Aspose.Cells supports Microsoft Excel file formats 5.0/95, 97, 2000, 2002/2003, 2007, 2010, 2013, 2016

