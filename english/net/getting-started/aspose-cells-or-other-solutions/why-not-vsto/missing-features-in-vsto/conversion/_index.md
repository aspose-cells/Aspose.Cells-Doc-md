---
title: Conversion
type: docs
weight: 30
url: /net/conversion/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells' unique feature that provides flexibility in version conversions without affecting work.  
SaveFormat is an enumeration that can convert documents to the extensions given in the table below.

| **Member Name** | **Value** | **Description** |
| :- | :- | :- |
| CSV | 1 | Represents a CSV file. |
| Xlsx | 6 | Represents an XLSX file. |
| Xlsm | 7 | Represents an XLSM file which enables macros. |
| Xltx | 8 | Represents an XLTX file. |
| Xltm | 9 | Represents an XLTM file which enables macros. |
| TabDelimited | 11 | Represents a tab‑delimited text file. |
| Html | 12 | Represents an HTML file. |
| MHtml | 17 | Represents an MHTML file. |
| ODS | 14 | Represents an ODS file. |
| Excel97To2003 | 5 | Represents an Excel 97‑2003 XLS file. |
| SpreadsheetML | 15 | Represents an Excel 2003 XML file. |
| Xlsb | 16 | Represents an XLSB file. |
| Auto | 0 | If saving the file to disk, the file format accords to the extension of the file name. <br>If saving the file to a stream, the file format is XLSX. |
| Unknown | 255 | Represents an unrecognized format; the file cannot be saved. |
| Pdf | 13 | Represents a PDF file. |
| XPS | 20 | Represents an XPS file. |
| TIFF | 21 | Represents a TIFF file. |
| SVG | 22 | Represents an SVG file. |
| Dif | 30 | Represents the Data Interchange Format. |

Below is a code snippet that shows conversion from XLS to XLSX; you can do it vice versa as well.

{{< highlight csharp >}}

Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Download Sample Code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
