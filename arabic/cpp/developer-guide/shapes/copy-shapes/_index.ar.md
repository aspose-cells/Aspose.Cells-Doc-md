---
title: نسخ الأشكال بين أوراق العمل باستخدام C++
linktitle: نسخ الأشكال
type: docs
weight: 200
url: /ar/cpp/copy-shapes-between-worksheets/
description: تعلم كيفية نسخ الأشكال والمخططات والأشياء الأخرى المرسومة بين أوراق العمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى نسخ عناصر على ورقة عمل، مثل الصور والمخططات والأشياء الأخرى المرسومة، بين أوراق العمل. يدعم Aspose.Cells هذه الميزة. يمكن نسخ المخططات والصور والأشياء الأخرى بدقة عالية.

يوفر هذا المقال فهمًا مفصلًا لكيفية نسخ الأشكال بين صفحات العمل.

{{% /alert %}}

## **نسخ صورة من ورقة عمل إلى أخرى**

لنسخ صورة من ورقة عمل إلى أخرى، استخدم الطريقة التالية كما هو موضح في الكود العيني أدناه.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PictureCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Picture from the "Picture" worksheet
    Worksheet pictureSheet = workbook.GetWorksheets().Get(u"Picture");
    Picture picturesource = pictureSheet.GetPictures().Get(0);

    // Get picture data
    Vector<uint8_t> pictureData = picturesource.GetData();

    // Copy the picture to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetPictures().Add(picturesource.GetUpperLeftRow(), picturesource.GetUpperLeftColumn(), pictureData, picturesource.GetWidthScale(), picturesource.GetHeightScale());

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Picture copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **نسخ رسم بياني من ورقة عمل إلى أخرى**

يوضح الكود التالي استخدام الطريقة لنسخ رسم بياني من ورقة عمل إلى أخرى.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Chart from the "Chart" worksheet
    Worksheet chartSheet = workbook.GetWorksheets().Get(u"Chart");
    Chart chartSource = chartSheet.GetCharts().Get(0);

    // Get the ChartShape object
    ChartShape cshape = chartSource.GetChartObject();

    // Copy the Chart to the "Result" Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(cshape, 20, 0, 2, 0);

    // Save the Workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **نسخ عناصر التحكم والرسومات الأخرى من ورقة عمل إلى أخرى**

لنسخ عناصر التحكم والكائنات الرسم الأخرى، استخدم طريقة [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) كما هو موضح في المثال أدناه.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample2.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ControlsCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Shapes from the "Control" worksheet
    Worksheet controlSheet = workbook.GetWorksheets().Get(u"Control");
    ShapeCollection shapes = controlSheet.GetShapes();

    // Copy the Textbox to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(shapes.Get(0), 5, 0, 2, 0);

    // Copy the Oval Shape to the Result Worksheet
    resultSheet.GetShapes().AddCopy(shapes.Get(1), 10, 0, 2, 0);

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Shapes copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
