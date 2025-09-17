##Link Cells to XML Map Elements with C++
Learn how to link cells to XML Map elements using Aspose.Cells with C++.
## **Possible Usage Scenarios**
You can link your cells to XML Map elements using Aspose.Cells. Please use the [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) method for this purpose.
## **Link Cells to Xml Map Elements**
The following sample code loads the [source excel file](5115471.xlsx) which contains XML Map and then links cells A1, B2, C3, D4, E5, and F6 to XML Map elements FIELD1, FIELD2, FIELD4, FIELD5, FIELD7, and FIELD8 respectively and then saves the workbook in [output excel file](5115467.xlsx).
If you open the [output excel file](5115467.xlsx) and click the Developer > Source button, you will see the cells are linked with XML Map elements and they will also be highlighted by Microsoft Excel as shown in this image.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Load sample workbook
Workbook wb(srcDir + u"sample.xlsx");
// Access the Xml Map inside it
XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Map FIELD1 and FIELD2 to cell A1 and B2
ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");
// Map FIELD4 and FIELD5 to cell C3 and D4
ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");
// Map FIELD7 and FIELD8 to cell E5 and F6
ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");
// Save the workbook in xlsx format
wb.Save(outDir + u"output.xlsx");
std::cout << "Workbook saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
