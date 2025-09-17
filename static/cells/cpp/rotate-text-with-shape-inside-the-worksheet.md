##Rotate Text with Shape inside the Worksheet with C++
Learn how to control text rotation with shapes in Excel worksheets using Aspose.Cells for C++.
## **Possible Usage Scenarios**
You can add text inside any shape using Microsoft Excel. If you add a shape using the very old Microsoft Excel 2003, then the text will not rotate with the shape. However, if you add a shape using newer versions of Microsoft Excel, such as 2007, 2010, 2013, or 2016, the text will rotate with the shape. You can control whether the text should rotate with the shape or not using the [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) property. The default value of this property is **true**, which means the text will rotate with the shape. If you set it to **false**, the text will not rotate with the shape.
## **Rotate Text with Shape inside the Worksheet**
The following sample code loads the [sample Excel file](64716896.xlsx) that contains a triangle shape, and its text rotates with the shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) property to **false** and saves it as the [output Excel file](64716897.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on the sample Excel file for reference.
![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Load sample Excel file
Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access cell B4 and add message inside it
Cell b4 = ws.GetCells().Get(u"B4");
b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");
// Access first shape
Shape sh = ws.GetShapes().Get(0);
// Access shape text alignment
ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();
// Do not rotate text with shape by setting RotateTextWithShape as false
shapeTextAlignment.SetRotateTextWithShape(false);
// Save the output Excel file
wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");
Aspose::Cells::Cleanup();
}
```
