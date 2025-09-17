##Finding Absolute Position of Shape inside the Worksheet with C++
Determine the absolute position of a shape in a worksheet using Aspose.Cells with C++.
Sometimes, you need to know the absolute position of a shape in a worksheet. Aspose.Cells provides the [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) and [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) properties for this purpose. These properties return the absolute position of the shape inside the worksheet in pixels.
The following sample code displays the absolute position of the first shape in the worksheet in pixels. The sample code displays the following console output:
Absolute Position of this Shape is (320 , 183)
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Load the sample Excel file inside the workbook object
Workbook workbook(srcDir + u"sample.xlsx");
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access the first shape inside the worksheet
Shape shape = worksheet.GetShapes().Get(0);
// Displays the absolute position of the shape
std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
