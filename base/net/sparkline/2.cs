using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;

            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}