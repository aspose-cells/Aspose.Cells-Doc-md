##Draw Timeline while rendering Excel to PDF with C++
Manage timelines of Excel files with Aspose.Cells with C++.
## **Draw Timeline while rendering Excel to PDF**
If you have an Excel file which has a timeline applied to it and you want to export the Excel to PDF with the timeline settings, Aspose.Cells now supports this by default. You simply export the Excel file with a timeline to PDF, and the generated PDF will show the timeline applied.
The following sample code loads the [sample Excel file](input.xlsx) that contains an existing timeline. It then saves the workbook as [output PDF file](out.pdf). The following screenshot compares the source Excel file and the generated PDF file.
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Load sample Excel file
U16String inputFilePath(u"input.xlsx");
std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);
// Save file to pdf
U16String outputFilePath(u"out.pdf");
wb->Save(outputFilePath, SaveFormat::Pdf);
std::cout << "Workbook saved successfully as PDF!" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
```cpp
#include <aspose.cells.h>
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
// Load the sample Excel file
Workbook workbook(u"input.xlsx");
// Save the workbook as a PDF file
workbook.Save(u"output.pdf", SaveFormat::Pdf);
Aspose::Cells::Cleanup();
return 0;
}
```
