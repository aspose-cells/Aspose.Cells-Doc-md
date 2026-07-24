#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Step 2: Write sample values into A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Step 4: Add a Column sparkline to the destination cell
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Step 5: Confirm the sparkline type by reading group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Step 6: Save the workbook
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}