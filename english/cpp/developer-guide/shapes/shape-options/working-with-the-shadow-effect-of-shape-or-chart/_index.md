---
title: Working with the Shadow Effect of Shape or Chart with C++
linktitle: Working with the Shadow Effect of Shape or Chart
type: docs
weight: 220
url: /cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Learn how to manipulate the shadow effect of shapes or charts using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [Shape::get_ShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/get_shadoweffect/) method along with the [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) class to work with the shadow effect of shapes or charts. The [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) class contains the following properties which can be set to achieve different results as per application requirements.

- [Angle](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_angle/)
- [Blur](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_blur/)
- [Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_color/)
- [Distance](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_distance/)
- [PresetType](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_presettype/)
- [Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_size/)
- [Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/get_transparency/)

## **Working with the Shadow Effect of Shape or Chart**
The following sample code loads the [source excel file](5115425.xlsx) and accesses the first shape in the first worksheet and sets the sub-properties of [Shape::get_ShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/get_shadoweffect/) property and then saves the workbook in the [output excel file](5115411.xlsx).

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape, Set its Angle, Blur, Distance and Transparency properties
    ShadowEffect se = sh.GetShadowEffect();
    se.SetAngle(150);
    se.SetBlur(4);
    se.SetDistance(45);
    se.SetTransparency(0.3);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Shadow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```