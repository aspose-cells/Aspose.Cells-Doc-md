#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Populate the source data with header row (Fruit, Year, Amount)
    // and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Assign fields: Fruit -> Rows, Year -> Columns, Amount -> Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Apply the legacy XLS preset autoformat "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Save the workbook in legacy .xls format
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}