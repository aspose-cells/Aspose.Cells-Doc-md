---
title : "Convert an XLS File to PDF Format" 
description : "" 
weight : 20358 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/convert+an+xls+file+to+pdf+format/
---

# Aspose.Cells for .NET : Convert an XLS File to PDF Format


PDF (Portable Document Format) represents documents independently of the software, hardware, and operating system used to create those documents. A PDF file can be documents with any combination of text, graphics, and images in a device-independent and resolution-independent manner. PDF files are often compressed, so they take up less space than the original file.

At times, you need to convert a Microsoft Excel file to PDF. For this, you require a fast, secure, accurate and reliable solution that lets you distribute PDF documents around the world. There are numerous conversion tools that can perform this task. But you have to make sure that the layout of the original Excel document is retained in the output PDF file. Images, data formatting, fonts, attributes, colors, page setup settings, text orientation, borders, charts etc. should be rendered accurately and precisely. [Aspose.Cells](http://www.aspose.com/categories/.net-components/aspose.cells-for-.net/default.aspx) ensures high-fidelity conversion.

This document is designed to provide comprehensive understanding of how a Microsoft Excel document (containing images, charts, formatting etc.) can be converted to PDF. To that end, is shows how to create a simple console application in Visual Studio.Net that converts an Excel file to PDF using Aspose.Cells API. The conversion is performed with high degree of precision and accuracy.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Excel to PDF](#converting-excel-to-pdf)
    *   1.1 [The Template Excel File](#the-template-excel-file)
    *   1.2 [Conversion Process](#conversion-process)
    *   1.3 [Result](#result)
{{< /panel >}}
 

 

## Converting Excel to PDF

This example uses an Excel file (SampleInput.xlsx) as a template. The workbook contains worksheets with charts and image. Each worksheet contians different types of formats using fonts, attributes, colors, shading effects and borders. There's a column chart on the first worksheet and an image on the last.

### The Template Excel File

The template file has three worksheets, including charts and image as Media. The first worksheet has charts and last worksheet has an image as shown below in the screenshots.

![](download/thumbnails/5017570/1256716648)

![](download/thumbnails/5017570/1349245484)

The first worksheet **(Sales Forecast)**

The second worksheet **(Sales Report)**

![](download/thumbnails/5017570/17404915)

![](download/thumbnails/5017570/722590035)

The third worksheet **(Data Entry)**

The last worksheet **(Image)**

### Conversion Process

1.  Download and install Aspose.Cells:
    1.  Download Aspose.Cells for .NET.
    2.  Install it on your development computer.
2.  Create a project and add references:
    1.  Start Visual Studio.Net.
    2.  Create a new console application.
    3.  Add a reference to …\\Program Files\\Aspose\\Aspose.Cells\\Bin\\Net1.0\\Aspose.Cells.dll
3.  Add the conversion code to the project:

If the spreadsheet contains formulas, it is best to call `Workbook.CalculateFormula()` just before rendering the spreadsheet to PDF. Doing so ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

### Result

when the above code has been run, a PDF file is created in the Files folder in your application directory.  
The following screenshots show the PDF pages. Note that headers and footers are also retained in the output PDF file.

![](download/thumbnails/5017570/1564930819)

![](download/thumbnails/5017570/1725461310)

The first worksheet **(Sales Forecast)**

The second worksheet **(Sales Report)**

![](download/thumbnails/5017570/791518362)

![](download/thumbnails/5017570/170861991)

The third worksheet **(Data Entry)**

The last worksheet **(Image)**

