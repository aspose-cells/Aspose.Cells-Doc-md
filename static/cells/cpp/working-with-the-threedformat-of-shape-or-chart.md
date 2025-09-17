##Working with the ThreeDFormat of Shape or Chart with C++
Learn how to manipulate the 3-D Format of shapes or charts using Aspose.Cells with C++.
## **Possible Usage Scenarios**
Aspose.Cells provides the [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) property along with the [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) class to work with the 3-D Format of shapes or charts. The [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) class contains different properties that can be set to achieve different results as per application requirements.
## **Working with the ThreeDFormat of Shape or Chart**
The following sample code loads the [source excel file](5115419.xlsx) and accesses the first shape in the first worksheet. It then sets the sub-properties of the [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) property and saves the workbook in the [output excel file](5115410.xlsx).
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
// Load excel file containing a shape
Workbook wb(inputFilePath);
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access first shape
Shape sh = ws.GetShapes().Get(0);
// Apply different three dimensional settings
ThreeDFormat n3df = sh.GetThreeDFormat();
n3df.SetContourWidth(17);
n3df.SetExtrusionHeight(32);
// Save the output excel file in xlsx format
wb.Save(outputFilePath);
std::cout << "3D settings applied successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
