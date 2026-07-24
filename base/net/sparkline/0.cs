using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;

            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}