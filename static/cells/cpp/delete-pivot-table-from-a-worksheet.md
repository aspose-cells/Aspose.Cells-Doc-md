##Delete Pivot Table from a Worksheet with C++
C++ code to remove PivotTable for Excel Worksheets using Aspose.Cells.
Aspose.Cells provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) method to delete the pivot table using pivot table object and [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) method to delete pivot table object using its position inside the pivot table collection.
The following sample code deletes two pivot tables from the worksheet. First it removes pivot table using [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) method and then it removes pivot table using [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) method.
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"source.xlsx";
// Path of output Excel file
U16String outputFilePath = outDir + u"output_out.xlsx";
// Create workbook object from source Excel file
Workbook workbook(inputFilePath);
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access the first pivot table object
PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
// Remove pivot table using pivot table object
worksheet.GetPivotTables().Remove(pivotTable);
// OR you can remove pivot table using pivot table position by uncommenting below line
// worksheet.GetPivotTables().RemoveAt(0);
// Save the workbook
workbook.Save(outputFilePath);
std::cout << "Pivot table removed successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
