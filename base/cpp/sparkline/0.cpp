#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Step 3: Build a CellArea pointing to destination cell F1
    CellArea dest;
    dest.StartColumn = 5;   // column F (0-indexed)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1 (0-indexed)
    dest.EndRow = 0;

    // Step 4: Add a Line sparkline from A1:E1 into F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Step 5: Create a red CellsColor and assign it to the sparkline line color
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Step 6: Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Step 7: Save the workbook
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}