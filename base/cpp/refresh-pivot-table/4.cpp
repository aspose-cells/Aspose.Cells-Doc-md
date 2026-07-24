#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // In Aspose.Cells, pivot tables created from the same source range 
    // automatically share the same PivotCache
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // Get all pivot tables on the worksheet (which share the cache)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}