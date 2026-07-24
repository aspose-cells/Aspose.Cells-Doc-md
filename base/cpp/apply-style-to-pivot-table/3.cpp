#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Data rows
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Assign pivot fields
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Build a Style that will be forced onto every cell of the pivot table
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // Apply FormatAll
    pivotTable.FormatAll(style);

    // Save the workbook
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}