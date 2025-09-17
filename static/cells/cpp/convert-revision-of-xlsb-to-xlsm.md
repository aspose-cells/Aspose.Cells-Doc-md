##Convert Revision of XLSB to XLSM with C++
Learn to convert revisions of XLSB files into XLSM format using Aspose.Cells with C++.
Aspose.Cells now supports the full conversion of revisions of XLSB files into XLSM files. Revisions are found inside the path \xl\revisions. You can view them by changing your XLSB file extension to ZIP. The \xl\revisions path contains files ending with .bin extensions.
When you convert your XLSB file into XLSM file using Aspose.Cells, these .bin files successfully convert to .xml files as shown in these two screenshots.
The following code sample shows you how to convert the XLSB file into XLSM format using Aspose.Cells.
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
// Path of input excel file
U16String inputFilePath = srcDir + u"sample.xlsb";
// Create workbook from the input file
Workbook workbook(inputFilePath);
// Save Workbook to XLSM format
workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);
std::cout << "Workbook saved successfully in XLSM format!" << std::endl;
Aspose::Cells::Cleanup();
}
```
