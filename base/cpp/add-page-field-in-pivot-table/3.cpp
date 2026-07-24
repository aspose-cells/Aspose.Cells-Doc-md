#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}