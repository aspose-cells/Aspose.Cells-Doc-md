#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Populate source data: header row + 9 data rows (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

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

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Step 1: register a new custom pivot table style and capture its index
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Step 2: add a WholeTable element and apply thin black borders on all four sides
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Step 3: add a GrandTotalRow element and apply bold red font
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}