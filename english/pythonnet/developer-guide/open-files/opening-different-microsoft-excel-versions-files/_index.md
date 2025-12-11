---
title: Open Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /python-net/opening-different-microsoft-excel-versions-files/
description: This article explains how to open different Excel versions files using Aspose.Cells for Python via .NET API.
keywords: Python Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET can open a range of different Microsoft Excel versions files, such as Microsoft Excel 95/97‑2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX, or encrypted Excel files.

{{% /alert %}}

## **How to Open Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95/97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tab‑Delimited or TSV, CSV, ODS, and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class' [**file_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/file_format) type attribute that specifies the format using the [**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype) enumeration.

The [**FileFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformattype) enumeration contains many pre‑defined file formats; some of which are given below.

| **File Format Types** | **Description** |
| :- | :- |
| CSV | Represents a CSV file |
| Excel97To2003 | Represents an Excel 97‑2003 file |
| XLSX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file |
| XLSM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file |
| XLTX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template (XLTX) file |
| XLTM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro‑enabled (XLTM) file |
| XLSB | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary (XLSB) file |
| SpreadsheetML | Represents a SpreadsheetML file |
| TSV | Represents a tab‑separated values file |
| TabDelimited | Represents a tab‑delimited text file |
| ODS | Represents an ODS file |
| HTML | Represents an HTML file |
| MHTML | Represents an MHTML file |

### **Open Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and set the appropriate attribute of the LoadOptions class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel95Files-1.py" >}}

### **Open Microsoft Excel 97‑2003 Files**

To open a Microsoft Excel 97‑2003 file, use [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and set the appropriate attribute of the LoadOptions class for the template file to be loaded.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel972003Files-1.py" >}}

### **Open Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 format (XLSX or XLSB), specify the file path. You can also use [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and set the related attributes/options of the LoadOptions class for the template file to be loaded.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningMicrosoftExcel2007XlsxFiles-1.py" >}}

### **Open Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use the [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and set its attributes and options (for example, provide a password) for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningEncryptedExcelFiles-1.py" >}}

Aspose.Cells also supports opening password‑protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, and Office 365 files.

{{< app/cells/assistant language="python-net" >}}
