---
title: Opening Different Microsoft Excel Versions Files
type: docs
weight: 20
url: /python-java/opening-different-microsoft-excel-versions-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel version files, such as Microsoft Excel 95/97‑2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX, or encrypted Excel files.

{{% /alert %}}

## **Opening Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95, 97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tab‑Delimited, TSV, CSV, ODS, and so on. Use the constructor or specify the **Workbook** class's **setFileFormat** method to specify the format using the **FileFormatType** enumeration.

The **FileFormatType** enumeration contains many pre‑defined file formats; some of which are given below.

| **File Format Types** | **Description** |
| :- | :- |
| CSV | Represents a CSV file |
| EXCEL_97_TO_2003 | Represents an Excel 97‑2003 file |
| XLSX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file |
| XLSM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file |
| XLTX | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file |
| XLTM | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro‑enabled XLTM file |
| XLSB | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file |
| SPREADSHEET_ML | Represents a SpreadsheetML file |
| TSV | Represents a Tab‑separated values file |
| TAB_DELIMITED | Represents a Tab‑Delimited text file |
| ODS | Represents an ODS file |
| HTML | Represents an HTML file |
| M_HTML | Represents an MHTML file |

### **Opening Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use **LoadOptions** and set the appropriate attribute of the **LoadOptions** class for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Opening Microsoft Excel 97‑2003 Files**

To open a Microsoft Excel 97‑2003 file, use **LoadOptions** and set the appropriate attribute of the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Opening Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 or Office 365 file (XLSX, XLSM, XLSB, etc.), specify the file path. You can also use **LoadOptions** and set the relevant attributes/options of the **LoadOptions** class for the template file to be loaded.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Opening Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use **LoadOptions** and set its attributes and options (for example, provide a password) for the template file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells also supports opening password‑protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, and Office 365 files.
