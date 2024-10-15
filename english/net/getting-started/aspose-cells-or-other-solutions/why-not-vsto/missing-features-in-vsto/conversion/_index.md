---
title: Conversion
type: docs
weight: 30
url: /net/conversion/
---

Aspose.Cells unique feature that provide flexibility in version conversions without affecting work.
SaveFormat is enumeration that can convert document in the extensions given below in table.

|**Member Name** |**Value** |**Description** |
| :- | :- | :- |
|CSV |1 |Represents a CSV file. |
|Xlsx |6 |Represents an xlsx file. |
|Xlsm |7 |Represents an xlsm file which enable macros. |
|Xltx |8 |Represents an xltx file. |
|Xltm |9 |Represents an xltm file which enable macros. |
|TabDelimited |11 |Represents a tab delimited text file. |
|Html |12 |Represents a html file. |
|MHtml |17 |Represents a mhtml file. |
|ODS |14 |Represents a ods file. |
|Excel97To2003 |5 |Represents an Excel97-2003 xls file. |
|SpreadsheetML |15 |Represents an Excel 2003 xml file. |
|Xlsb |16 |Represents an xlsb file. |
|Auto |0 |If saving the file to the disk,the file format format accords to the extesion of the file name. <br>If saving the file to the stream, the file format is xlsx. |
|Unknown |255 |Represents unrecognized format, cannot be saved. |
|Pdf |13 |Represents a Pdf file. |
|XPS |20 |Represents an XPS file. |
|TIFF |21 |Represents an TIFF file. |
|SVG |22 |Represents an SVG file. |
|Dif |30 |Data Interchange Format. |
Below is code snippet that shows conversion from xls to xlsx you can do it vice versa as well

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Download Sample Code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}