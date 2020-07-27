+++
title = "Convert an XLS File to PDF Format" 
description = "" 
weight = 20358 
+++

Aspose.Cells for .NET : Convert an XLS File to PDF Format  

# Aspose.Cells for .NET : Convert an XLS File to PDF Format


PDF (Portable Document Format) represents documents independently of the software, hardware, and operating system used to create those documents. A PDF file can be documents with any combination of text, graphics, and images in a device-independent and resolution-independent manner. PDF files are often compressed, so they take up less space than the original file.

At times, you need to convert a Microsoft Excel file to PDF. For this, you require a fast, secure, accurate and reliable solution that lets you distribute PDF documents around the world. There are numerous conversion tools that can perform this task. But you have to make sure that the layout of the original Excel document is retained in the output PDF file. Images, data formatting, fonts, attributes, colors, page setup settings, text orientation, borders, charts etc. should be rendered accurately and precisely. [Aspose.Cells](http://www.aspose.com/categories/.net-components/aspose.cells-for-.net/default.aspx) ensures high-fidelity conversion.

This document is designed to provide comprehensive understanding of how a Microsoft Excel document (containing images, charts, formatting etc.) can be converted to PDF. To that end, is shows how to create a simple console application in Visual Studio.Net that converts an Excel file to PDF using Aspose.Cells API. The conversion is performed with high degree of precision and accuracy.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Excel to PDF](#ConvertanXLSFiletoPDFFormat-ConvertingExceltoPDF)
    *   1.1 [The Template Excel File](#ConvertanXLSFiletoPDFFormat-TheTemplateExcelFile)
    *   1.2 [Conversion Process](#ConvertanXLSFiletoPDFFormat-ConversionProcess)
    *   1.3 [Result](#ConvertanXLSFiletoPDFFormat-Result)
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

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-001.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112491.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-002.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112492.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-003.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112493.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-004.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112494.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-005.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112495.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-006.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112496.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-007.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112497.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-008.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112498.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Format-009.png](https://docs2.aspose.com/cells/net/attachments/5017570/5112499.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115145.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115144.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115139.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115137.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115136.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115143.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115134.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115135.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115128.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet4.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115129.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115141.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115140.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115132.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted4.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115133.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115130.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115131.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115126.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted4.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115127.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115325.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115326.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115327.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Sheet4.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115138.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted1.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115328.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted2.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115329.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted3.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115330.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Convert an XLS File to PDF Converted4.png](https://docs2.aspose.com/cells/net/attachments/5017570/5115142.png) (image/png)  

