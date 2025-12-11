---
title: Copy Shapes between Worksheets with C++
linktitle: Copy Shapes
type: docs
weight: 200
url: /cpp/copy-shapes-between-worksheets/
description: Learn how to copy shapes, charts, and other drawing objects between worksheets using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to copy elements on a worksheet, for example, pictures, charts, and other drawing objects, between worksheets. Aspose.Cells supports this feature. Charts, images, and other objects can be copied with the highest degree of precision.

This article gives you a detailed understanding of how to copy shapes between worksheets.

{{% /alert %}}

## **Copying a Picture from One Worksheet to Another**

To copy a picture from one worksheet to another, use the [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) method as shown in the sample code below.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"PictureCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the picture from the "Picture" worksheet
    Worksheet pictureSheet = workbook.GetWorksheets().Get(u"Picture");
    Picture pictureSource = pictureSheet.GetPictures().Get(0);

    // Get picture data
    Vector<uint8_t> pictureData = pictureSource.GetData();

    // Copy the picture to the Result worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetPictures().Add(pictureSource.GetUpperLeftRow(), pictureSource.GetUpperLeftColumn(), pictureData, pictureSource.GetWidthScale(), pictureSource.GetHeightScale());

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Picture copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Copy a Chart from One Worksheet to Another**

The following code demonstrates the use of [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) method to copy a chart from one worksheet to another.

```cpp
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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"ChartCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the chart from the "Chart" worksheet
    Worksheet chartSheet = workbook.GetWorksheets().Get(u"Chart");
    Chart chartSource = chartSheet.GetCharts().Get(0);

    // Get the ChartShape object
    ChartShape cshape = chartSource.GetChartObject();

    // Copy the chart to the "Result" worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(cshape, 20, 0, 2, 0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Copy Controls and Other Drawing Objects from One Worksheet to Another**

To copy controls and other drawing objects, use the [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) method as shown in the example below.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample2.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"ControlsCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the shapes from the "Control" worksheet
    Worksheet controlSheet = workbook.GetWorksheets().Get(u"Control");
    ShapeCollection shapes = controlSheet.GetShapes();

    // Copy the textbox to the Result worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(shapes.Get(0), 5, 0, 2, 0);

    // Copy the oval shape to the Result worksheet
    resultSheet.GetShapes().AddCopy(shapes.Get(1), 10, 0, 2, 0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Shapes copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
