---
title: إضافة علامة مائية WordArt إلى الرسم البياني باستخدام C++
description: تعلم كيفية استخدام Aspose.Cells for C++ لإضافة علامة مائية WordArt إلى رسم بياني في Microsoft Excel. سيُظهر دليلنا كيفية إنشاء وتوجيه علامة مائية WordArt لتعزيز الجاذبية البصرية والتفرد في الرسم البياني الخاص بك.
keywords: Aspose.Cells for C++، علامة مائية WordArt، علامة مائية للرسم البياني، Microsoft Excel، الجاذبية البصرية، تميز الرسم البياني.
type: docs
weight: 50
url: /ar/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

يمكنك استخدام WordArt لإضافة تأثيرات نص خاصة إلى جداول البيانات. على سبيل المثال، تمدد عنوان، وزين النص، واجعل النص يناسب الشكل المحدد مسبقًا، أو قم بتطبيق النص المتأثر على منطقة الرسم البياني كعلامة مائية. يصبح WordArt كائن يمكنك نقله أو وضعه في جداول البيانات الخاصة بك لإضافة الديكور.

المثال التالي يوضح كيفية إضافة شكل WordArt كعلامة مائية لمنطقة رسم البياني.

{{% /alert %}} 

المثال التالي يوضح كيفية إضافة شكل WordArt كعلامة مائية لمنطقة رسم البياني الحالية.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
