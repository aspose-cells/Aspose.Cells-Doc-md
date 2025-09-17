##Render Custom Date Format Pattern g and ge mm dd with C++
Aspose.Cells is a C++ library for working with spreadsheet files that supports rendering dates using custom date format patterns 'g' and 'ge'. This article will describe how to render custom date format patterns using the Aspose.Cells library so that users can control how dates are displayed if they want.
Aspose.Cells is now able to render the custom date format patterns like g, ge.mm.dd and similar. Please check the attached [source excel file](5112361.xlsx) and the [converted PDF](5112360.pdf) by Aspose.Cells for your reference.
The following sample code converts the [source excel file](5112361.xlsx) which contains date values with custom format patterns like g and ge.mm.dd into [output PDF](5112360.pdf).
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
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Create workbook from an existing Excel file
U16String inputFilePath = srcDir + u"SourceFile.xlsx";
Workbook workbook(inputFilePath);
// Save the Excel file as PDF
workbook.Save(outDir + u"CustomDateFormat_out.pdf");
std::cout << "File saved successfully as PDF!" << std::endl;
Aspose::Cells::Cleanup();
}
```
