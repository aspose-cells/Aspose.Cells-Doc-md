---
title : "Convert an Excel Chart to Image" 
description : "" 
weight : 20357 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/convert+an+excel+chart+to+image/
---

# Aspose.Cells for .NET : Convert an Excel Chart to Image


Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data. For instance, rather than analyzing columns of worksheet numbers, a chart shows at a glance whether sales are falling or rising, or how actual sales compare to projected sales. People are frequently asked to present statistical and graphical information in an easy to understand and an easy to maintain manner. A picture helps.

Sometimes, charts are needed in an application or web pages. Or it might be needed needed for a Word document, a PDF file, a PowerPoint presentation or some other application. In each case, you want to render the chart as an image so that you can use it elsewhere.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Charts to Images](#converting-charts-to-images)
    *   1.1 [Converting a Pie Chart to an Image File](#converting-a-pie-chart-to-an-image-file)
    *   1.2 [Converting a Column Chart to an Image File](#converting-a-column-chart-to-an-image-file)
{{< /panel >}}
 

 

## Converting Charts to Images

In the examples here, a pie chart and a column char are converted to images.

### Converting a Pie Chart to an Image File

First, create a pie chart in Microsoft Excel and then convert it to an image file with Aspose.Cells. The code in this example creates an EMF image based on the pie chart in the template Microsoft Excel file.

{{< table style="table-striped" >}}
|Output: pie chart image|
|:----|
|![image](5112514.png)|
{{< /table >}}

1.  Create a pie chart in Microsoft Excel :
    1.  Opened a new workbook in Microsoft Excel.
    2.  Input some data into a worksheet.
    3.  Created a pie chart based on the data.
    4.  Save the file.
        
{{< table style="table-striped" >}}
|The input file.|
|:----|
|                ![image](5112512.png)        2.  Download and install Aspose.Cells:    1.  [Download Aspose.Cells for .NET](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/default.aspx).    2.  Install it on your development computer.|
{{< /table >}}

All [Aspose](http://www.aspose.com/) components work in evaluation mode when first installed. The evaluation mode has no time limit and it only injects watermarks into output documents.

1.  Create a project:
    1.  Start Visual Studio.Net.
    2.  Create a new console application. This example uses a C# console application, but you can use VB.NET too.
    3.  Add a reference. This project uses Aspose.Cells so add a reference to Aspose.Cells, for example ...\\Program Files\\Aspose\\Aspose.Cells\\Bin\\Net1.0\\Aspose.Cells.dll
    4.  Write the code that finds and converts the chart. Below is the code used by the component to accomplish the task. Very few lines of code are used.

### Converting a Column Chart to an Image File

First create a column chart in Microsoft Excel and convert it to an image file, as above. After executing the sample code, a JPEG file is created based on the column chart in the template Excel file.

{{< table style="table-striped" >}}
|Output file: a column chart image.|
|:----|
|![image](5112516.png)|
{{< /table >}}

1.  Create a column chart in Microsoft Excel:
    1.  Open a new workbook in Microsoft Excel.
    2.  Input some data into a worksheet.
    3.  Create a column chart based on the data.
    4.  Save the file.
        
{{< table style="table-striped" >}}
|Input file.|
|:----|
|                ![image](5112517.png)        |
{{< /table >}}

1.  Set up a project, with references, as described above.
2.  Convert the chart to an image dynamically. Following is the code used by the component to accomplish the task. The code is similar to the previous one:

