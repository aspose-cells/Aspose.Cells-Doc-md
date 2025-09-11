---
title: Convert the Smart Art to Group Shape with C++
linktitle: Convert the Smart Art to Group Shape
type: docs
weight: 200
url: /cpp/convert-the-smart-art-to-group-shape/
description: Learn how to convert Smart Art Shape into Group Shape using Aspose.Cells for C++ and access individual parts of the group shape.
---

## **Possible Usage Scenarios**

You can convert Smart Art Shape into Group Shape using the [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/) method. It will enable you to handle smart art shape like a group shape. Consequently, you will have access to the individual parts or shapes of the group shape.

## **Convert the Smart Art to Group Shape**

The following sample code loads the [sample Excel file](55541793.xlsx) containing a smart art shape as shown in this screenshot. It then converts the smart art shape into group shape and prints the Shape::IsGroup property. Please see the console output of the sample code given below.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}