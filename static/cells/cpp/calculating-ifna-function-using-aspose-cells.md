##Calculating IFNA function using Aspose.Cells with C++
How to calculate IFNA functions using the Aspose.Cells library with C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the IFNA function and get the result. Finally, we save the modified Excel file to disk.
Aspose.Cells supports the calculation of IFNA Excel function. IFNA function returns the value you specify if the formula returns the #N/A error value; otherwise returns the result of the formula.
## **Calculating IFNA function using Aspose.Cells**
The following sample code illustrates the calculation of IFNA function by Aspose.Cells.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create new workbook
Workbook workbook;
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Add data for VLOOKUP
worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
worksheet.GetCells().Get(u"A3").PutValue(u"Banana");
// Access cell A5 and A6
Cell cellA5 = worksheet.GetCells().Get(u"A5");
Cell cellA6 = worksheet.GetCells().Get(u"A6");
// Assign IFNA formula to A5 and A6
cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");
// Calculate the formula of workbook
workbook.CalculateFormula();
// Print the values of A5 and A6
std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Console Output**
Here is the console output of the above sample code.
Not found
Orange
