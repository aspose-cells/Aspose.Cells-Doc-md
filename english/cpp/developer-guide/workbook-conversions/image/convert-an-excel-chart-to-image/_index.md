---
title: Convert an Excel Chart to Image with C++
linktitle: Convert an Excel Chart to Image
type: docs
weight: 20
url: /cpp/convert-an-excel-chart-to-image/
description: Learn how to convert Excel charts to images using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Charts are visually appealing and make it easy for users to see comparisons, patterns, and trends in data. For instance, rather than analyzing columns of worksheet numbers, a chart shows at a glance whether sales are falling or rising, or how actual sales compare to projected sales. People are frequently asked to present statistical and graphical information in an easy-to-understand and easy-to-maintain manner. A picture helps.

Sometimes, charts are needed in an application or web pages. Or they might be needed for a Word document, a PDF file, a PowerPoint presentation, or some other application. In each case, you want to render the chart as an image so that you can use it elsewhere.

{{% /alert %}}

## **Converting Charts to Images**

In the examples here, a pie chart and a column chart are converted to images.

### **Converting a Pie Chart to an Image File**

First, create a pie chart in Microsoft Excel and then convert it to an image file with Aspose.Cells. The code in this example creates an EMF image based on the pie chart in the template Microsoft Excel file.

|**Output: pie chart image**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Create a pie chart in Microsoft Excel:
   1. Open a new workbook in Microsoft Excel.
   1. Input some data into a worksheet.
   1. Create a pie chart based on the data.
   1. Save the file.

|**The input file.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Download and install Aspose.Cells:
   1. [Download Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Install it on your development computer.

All [Aspose](http://www.aspose.com/) components work in evaluation mode when first installed. The evaluation mode has no time limit and it only injects watermarks into output documents.

1. Create a project:
   1. Start your C++ development environment (e.g., Visual Studio).
   1. Create a new console application.
   1. Add a reference to Aspose.Cells. This project uses Aspose.Cells, so add a reference to the Aspose.Cells library.
   1. Write the code that finds and converts the chart. Below is the code used by the component to accomplish the task. Very few lines of code are used.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Converting a Column Chart to an Image File**

First, create a column chart in Microsoft Excel and convert it to an image file, as above. After executing the sample code, a JPEG file is created based on the column chart in the template Excel file.

|**Output file: a column chart image.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Create a column chart in Microsoft Excel:
   1. Open a new workbook in Microsoft Excel.
   1. Input some data into a worksheet.
   1. Create a column chart based on the data.
   1. Save the file.

|**Input file.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Set up a project, with references, as described above.
1. Convert the chart to an image dynamically. Following is the code used by the component to accomplish the task. The code is similar to the previous one:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}