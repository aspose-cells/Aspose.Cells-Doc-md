##Read and Write Table with Query Table Data Source with C++
Learn how to read and write tables with QueryTable as a data source using Aspose.Cells for C++.
## **Read and Write Table with Query Table Data Source**
With Aspose.Cells, you can read and write a table which has a QueryTable as a data source. The support for this feature also exists for XLS files. The following code snippet demonstrates reading and writing such a table by first reading the table and then modifying it to add the totals row.
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
// Load workbook object
Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");
// Get the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Get the first ListObject (Table) in the worksheet
ListObject table = worksheet.GetListObjects().Get(0);
// Check the data source type if it is query table
if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
{
table.SetShowTotals(true);
}
// Save the file
workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");
std::cout << "File saved successfully." << std::endl;
Aspose::Cells::Cleanup();
}
```
The source and output Excel files are attached for reference.
[Source File](96928091.xls)
[Output File](96928092.xls)
