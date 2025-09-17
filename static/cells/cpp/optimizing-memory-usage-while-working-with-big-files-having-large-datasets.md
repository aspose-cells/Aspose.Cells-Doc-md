##Optimizing Memory Usage while Working with Big Files having Large Datasets with C++
Learn how to optimize memory usage when working with large Excel files using Aspose.Cells with C++.
When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures that can be adapted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce and optimize memory use. Also, it can help the process work more efficiently and run faster.
Use the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) option to optimize memory use for cells data and decrease the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).
## **Optimizing Memory**
### **Reading Large Excel Files**
The following example shows how to read a large Microsoft Excel file in optimized mode.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Specify the LoadOptions
LoadOptions opt;
// Set the memory preferences
opt.SetMemorySetting(MemorySetting::MemoryPreference);
// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
Workbook wb(srcDir + u"Book1.xlsx", opt);
std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Writing Large Excel Files**
The following example shows how to write a large dataset to a worksheet in an optimized mode.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Instantiate a new Workbook
Workbook wb;
// Set the memory preferences
// Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);
// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
// To change the memory setting of existing sheets, please change memory setting for them manually:
Cells cells = wb.GetWorksheets().Get(0).GetCells();
cells.SetMemorySetting(MemorySetting::MemoryPreference);
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
Aspose::Cells::Cleanup();
return 0;
}
```
## **Caution**
The default option, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) option may optimize the memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases such as follow.
1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the Enumerator acquired from [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) and [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), the performance would be maximized with [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Inserting & Deleting Cells & Rows**: Please note that if there are lots of insert/delete operations for Cells/Rows, the performance degradation will be notable for *MemoryPreference* mode as compared to the *Normal* mode.
1. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as *Normal* mode but if there are lots of empty cells, or cell values are numeric, bool and so on, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) option will give better performance.
