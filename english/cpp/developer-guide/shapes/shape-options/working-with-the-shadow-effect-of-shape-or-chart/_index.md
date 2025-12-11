---
title: Working with the Shadow Effect of Shape or Chart with C++
linktitle: Working with the Shadow Effect of Shape or Chart
type: docs
weight: 220
url: /cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Learn how to manipulate the shadow effect of shapes or charts using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) method along with the [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) class to work with the shadow effect of shapes or charts. The [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) class contains the following properties which can be set to achieve different results as per application requirements.

- [GetAngle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getangle/)
- [GetBlur()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getblur/)
- [GetColor()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getcolor/)
- [GetDistance()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getdistance/)
- [GetPresetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)
- [GetSize()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getsize/)
- [GetTransparency()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/gettransparency/)

## **Working with the Shadow Effect of Shape or Chart**
The following sample code loads the [source Excel file](5115425.xlsx), accesses the first shape in the first worksheet, sets the sub‑properties of the [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) property, and then saves the workbook to the [output Excel file](5115411.xlsx).

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the shadow effect of the shape: set its Angle, Blur, Distance, and Transparency properties
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
{{< app/cells/assistant language="cpp" >}}
