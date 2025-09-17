##Specifying Significant Digits to be Stored in Excel File with C++
Learn how to specify significant digits to be stored in Excel files using Aspose.Cells with C++.
## **Possible Usage Scenarios**
By default, Aspose.Cells stores 17 significant digits of double values inside the Excel file, unlike MS-Excel which stores only 15 significant digits. You can change the default behavior of Aspose.Cells from 17 significant digits to 15 significant digits using the [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) property.
## **Specifying Significant Digits to be stored in Excel file**
The following sample code enforces Aspose.Cells to use 15 significant digits while storing double values inside the Excel file. Please check the [output Excel file](22774105.xlsx). Change its extension to .zip and unzip it, and you will see that only 15 significant digits are stored inside the Excel file. The following screenshot explains the effect of the [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) property on the output Excel file.
![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)
## **Sample Code**
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
// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
CellsHelper::SetSignificantDigits(15);
// Create workbook
Workbook workbook;
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access cell A1
Cell c = worksheet.GetCells().Get(u"A1");
// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.PutValue(1234567890.123451711);
// Save the workbook
workbook.Save(outDir + u"out_SignificantDigits.xlsx");
std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;
Aspose::Cells::Cleanup();
}
```
