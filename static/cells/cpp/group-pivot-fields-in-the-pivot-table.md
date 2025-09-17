##Group Pivot Fields in the Pivot Table with C++
Learn how to group pivot fields in a pivot table using Aspose.Cells for C++.
## **Possible Usage Scenarios**
Microsoft Excel allows you to group pivot fields of the pivot table. When there is a large amount of data related to a pivot field, it is often useful to group them into sections. Aspose.Cells also provides this feature using the [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/) method.
## **Group Pivot Fields in the Pivot Table**
The following sample code loads the [sample Excel file](64716818.xlsx) and performs grouping on the first pivot field using the [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/) method. It then refreshes and calculates data of the pivot table and saves the workbook as [output Excel file](64716817.xlsx). The screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the first pivot field is now grouped by months and quarters.
![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"../Data/01_SourceDirectory/");
U16String outDir(u"../Data/02_OutputDirectory/");
Workbook wb(srcDir + u"sampleGroupPivotFieldsInPivotTable.xlsx");
Worksheet ws = wb.GetWorksheets().Get(1);
PivotTable pt = ws.GetPivotTables().Get(0);
Date dtStart{ 2023, 12, 31, 0, 0, 0, 0 };
Date dtEnd{ 2025, 9, 5 , 0, 0, 0, 0 };
Vector<PivotGroupByType> groupTypeList{
PivotGroupByType::Months,
PivotGroupByType::Quarters
};
PivotField field = pt.GetRowFields().Get(0);
field.GroupBy(dtStart, dtEnd, groupTypeList, 1, true);
pt.RefreshData();
pt.CalculateData();
wb.Save(outDir + u"outputGroupPivotFieldsInPivotTable2.xlsx");
std::cout << "Pivot field grouped successfully." << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
