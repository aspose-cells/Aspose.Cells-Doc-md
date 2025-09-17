##Copy Sparkline by Specifying Data Range and Location of Sparkline Group with C++
Learn how to copy sparklines by specifying data range and location using Aspose.Cells for C++.
Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells supports this feature.
To copy a sparkline to other cells in Microsoft Excel:
1. Select the cell containing the sparkline.
1. Select **Edit Data** from the **Sparkline** section of the **Design** tab.
1. Select **Edit Group Location & Data**.
1. Specify the data range and location.
1. Click **OK**.
Aspose.Cells provides the `SparklineCollection.Add(dataRange, row, column)` method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations in the sparkline group. Finally, it writes the output Excel file on disk which is also shown in the screenshot above.
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
// Create workbook from source Excel file
Workbook workbook(srcDir + u"source.xlsx");
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access the first sparkline group
SparklineGroup group = worksheet.GetSparklineGroups().Get(0);
// Add Data Ranges and Locations inside this sparkline group
group.GetSparklines().Add(u"D5:O5", 4, 15);
group.GetSparklines().Add(u"D6:O6", 5, 15);
group.GetSparklines().Add(u"D7:O7", 6, 15);
group.GetSparklines().Add(u"D8:O8", 7, 15);
// Save the workbook
workbook.Save(outDir + u"output_out.xlsx");
std::cout << "Sparklines added successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
