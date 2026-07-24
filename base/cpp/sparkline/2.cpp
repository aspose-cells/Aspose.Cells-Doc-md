#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1
    dest.EndRow = 0;

    // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Step 5: Customize the sparkline group
    // Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Set the high-point color to green
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Set the low-point color to red
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Set the negative-point color to orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Set the default series color (used for positive bars)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Step 6: Save the workbook
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}