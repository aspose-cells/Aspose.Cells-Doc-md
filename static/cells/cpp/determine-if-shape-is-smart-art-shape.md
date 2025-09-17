##Determine if Shape is Smart Art Shape with C++
Learn how to determine if a shape is a Smart Art Shape using Aspose.Cells for C++.
## **Possible Usage Scenarios**
Smart Art Shapes are special shapes in Microsoft Excel that allow you to create complex diagrams automatically. You can find if the shape is a smart art shape or normal shape using [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) property.
## **Determine if Shape is Smart Art Shape**
The following sample code loads the [sample Excel file](55541792.xlsx) containing a smart art shape as shown in this screenshot. It then prints the value of [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) property of the first shape. Please see the console output of the sample code given below.
![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
int main()
{
Aspose::Cells::Startup();
// Load the sample smart art shape - Excel file
U16String inputFilePath(u"sampleSmartArtShape.xlsx");
Workbook wb(inputFilePath);
// Access first worksheet
WorksheetCollection sheets = wb.GetWorksheets();
Worksheet ws = sheets.Get(0);
// Access first shape
ShapeCollection shapes = ws.GetShapes();
Shape sh = shapes.Get(0);
// Determine if shape is smart art
std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Console Output**
Is Smart Art Shape: True
