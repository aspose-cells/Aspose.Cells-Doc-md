---
title: Convert XLSX File to PDF Format
type: docs
weight: 30
url: /python-net/convert-xlsx-file-to-pdf-format/
description: Learn how to Convert XLSX File to PDF Format with Aspose.Cells for Python via .NET API.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---

{{% alert color="primary" %}}

PDF (Portable Document Format) represents documents independently of the software, hardware, and operating system used to create those documents. A PDF file can be documents with any combination of text, graphics, and images in a device-independent and resolution-independent manner. PDF files are often compressed, so they take up less space than the original file.

At times, you need to convert a Microsoft Excel file to PDF. For this, you require a fast, secure, accurate and reliable solution that lets you distribute PDF documents around the world. There are numerous conversion tools that can perform this task. But you have to make sure that the layout of the original Excel document is retained in the output PDF file. Images, charts, shapes, data formatting, fonts, attributes, colors, page setup settings, text orientation, borders, charts etc. should be rendered accurately and precisely. [Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) ensures high-fidelity conversion.

This document is designed to provide comprehensive understanding of how a Microsoft Excel document (containing images, charts, formatting etc.) can be converted to PDF. To that end, is shows how to create a simple console application in Visual Studio.Net that converts an Excel file to PDF using Aspose.Cells for Python via .NET API. The conversion is performed with high degree of precision and accuracy.

{{% /alert %}}

## **Converting Excel to PDF**

This example uses an Excel file (SampleInput.xlsx) as a template. The workbook contains worksheets with charts and image. Each worksheet contains different types of formats using fonts, attributes, colors, shading effects and borders. There's a column chart on the first worksheet and an image on the last.

### **The Template Excel File**

The template file has three worksheets, including charts and image as Media. The first worksheet has charts and last worksheet has an image as shown below in the screenshots.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|The first worksheet **(Sales Forecast)**|The second worksheet **(Sales Report)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|The third worksheet **(Data Entry)**|The last worksheet **(Image)**|

### **Conversion Process**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) method just before rendering the spreadsheet to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}

### **Result**

When the above code has been run, a PDF file is created in the Files folder in your application directory.
The following screenshots show the PDF pages. Note that headers and footers are also retained in the output PDF file.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|The first worksheet **(Sales Forecast)**|The second worksheet **(Sales Report)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|The third worksheet **(Data Entry)**|The last worksheet **(Image)**|
{{< app/cells/assistant language="python-net" >}}