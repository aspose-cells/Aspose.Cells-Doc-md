#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Headers
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Sample data (9 rows)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // Add pivot table at E3 covering A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Fruit -> Row, Amount -> Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Low-level approach: locate the existing Year PivotField in BaseFields
    // and register it in the Page area via PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Refresh so the new page field is reflected in the saved workbook
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}