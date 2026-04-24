---
title: Open Different Microsoft Excel Versions Files  
type: docs  
weight: 20  
url: /nodejs-java/opening-different-microsoft-excel-versions-files/  
description: This article explains how to open different Excel versions files using Aspose.Cells for Node.js via Java API.  
keywords: Node.js via Java Open Different Microsoft Excel files, How do I open Encrypted Excel Files.  
ai_search_scope: cells_nodejsjava  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via Java can open a range of different Microsoft Excel version files, such as Microsoft Excel 95/97‐2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX, or encrypted Excel files.  

{{% /alert %}}

## **How to Open Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95, 97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS, and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/nodejs/workbook) class's **FileFormat** type attribute that specifies the format using the **FileFormatType** enumeration.

The **FileFormatType** enumeration contains many pre‐defined file formats; some of which are given below.

| **File Format Types** | **Description** |
| :- | :- |
| CSV | Represents a CSV file |
| EXCEL_97_TO_2003 | Represents an Excel 97‐2003 file |
| XLSX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file |
| XLSM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file |
| XLTX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file |
| XLTM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro‐enabled XLTM file |
| XLSB | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file |
| SPREADSHEET_ML | Represents a SpreadsheetML file |
| TSV | Represents a tab‐separated values file |
| TAB_DELIMITED | Represents a tab‐delimited text file |
| ODS | Represents an ODS file |
| HTML | Represents an HTML file |
| M_HTML | Represents an MHTML file |

### **Open Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use **LoadOptions** and set the appropriate attribute for the **LoadOptions** class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningMicrosoftExcel95Files-1.js" >}}

### **Open Microsoft Excel 97‐2003 Files**

To open a Microsoft Excel 97‐2003 file, use **LoadOptions** and set the appropriate attribute for the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningMicrosoftExcel972003Files-1.js" >}}

### **Open Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format (XLSX or XLSB), specify the file path. You can also use **LoadOptions** and set the related options of the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.js" >}}

### **Open Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use **LoadOptions** and set its attributes and options (for example, provide a password) for the template file to be loaded.  
A sample file for testing this feature can be downloaded from the following link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Files-Handling-OpeningEncryptedExcelFiles-1.js" >}}

Aspose.Cells for Node.js via Java also supports opening password‐protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, and Office 365 files.  

<!--{{< app/cells/assistant language="csharp" >}}-->