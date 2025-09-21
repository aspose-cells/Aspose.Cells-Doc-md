---
title: Convert XLSX File to PDF Format with Golang via C++
linktitle: Convert XLSX File to PDF Format
type: docs
weight: 30
url: /go-cpp/convert-xlsx-file-to-pdf-format/
description: Learn how to convert Excel files to PDF format using Aspose.Cells for C++ with high precision and accuracy.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) represents documents independently of the software, hardware, and operating system used to create those documents. A PDF file can contain any combination of text, graphics, and images in a device-independent and resolution-independent manner. PDF files are often compressed, so they take up less space than the original file.

At times, you need to convert a Microsoft Excel file to PDF. For this, you require a fast, secure, accurate, and reliable solution that lets you distribute PDF documents around the world. There are numerous conversion tools that can perform this task. But you have to make sure that the layout of the original Excel document is retained in the output PDF file. Images, charts, shapes, data formatting, fonts, attributes, colors, page setup settings, text orientation, borders, charts, etc., should be rendered accurately and precisely. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) ensures high-fidelity conversion.

This document is designed to provide a comprehensive understanding of how a Microsoft Excel document (containing images, charts, formatting, etc.) can be converted to PDF. To that end, it shows how to create a simple console application in C++ that converts an Excel file to PDF using Aspose.Cells API. The conversion is performed with a high degree of precision and accuracy.

{{% /alert %}}

## **Converting Excel to PDF**

This example uses an Excel file (SampleInput.xlsx) as a template. The workbook contains worksheets with charts and images. Each worksheet contains different types of formats using fonts, attributes, colors, shading effects, and borders. There's a column chart on the first worksheet and an image on the last.

### **The Template Excel File**

The template file has three worksheets, including charts and images as Media. The first worksheet has charts, and the last worksheet has an image, as shown below in the screenshots.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|The first worksheet **(Sales Forecast)**|The second worksheet **(Sales Report)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|The third worksheet **(Data Entry)**|The last worksheet **(Image)**|

### **Conversion Process**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call the [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) method just before rendering the spreadsheet to PDF. Doing so ensures that formula-dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}

### **Result**

When the above code has been run, a PDF file is created in the Files folder in your application directory.
The following screenshots show the PDF pages. Note that headers and footers are also retained in the output PDF file.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|The first worksheet **(Sales Forecast)**|The second worksheet **(Sales Report)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|The third worksheet **(Data Entry)**|The last worksheet **(Image)**|