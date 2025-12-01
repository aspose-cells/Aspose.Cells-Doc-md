---
title: Insert a Picture Based on Cell Reference with C++
linktitle: Insert a Picture Based on Cell Reference
type: docs
weight: 150
url: /cpp/insert-a-picture-based-on-cell-reference/
description: Learn how to insert a picture based on cell reference using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).

{{% /alert %}}

## Inserting a Picture Based on Cell Reference

Aspose.Cells supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) method of the [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) object). Specify the cell range by using the [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attribute of the [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object.

### Code Example

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);
    
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
