#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Header row: Fruit / Year / Amount
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Data rows
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Add the first pivot table "Pivot1" anchored at cell E3, source range A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Assign fields for Pivot1
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Add a SECOND pivot table "Pivot2" anchored at E15 using the SAME source range A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Assign the same fields for Pivot2
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Modify several Amount cell values in the source data to simulate a data change
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Refresh the shared PivotCache by refreshing the pivot table data
    pivotTable1.RefreshData();

    // Save the workbook
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}