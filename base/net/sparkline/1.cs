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

            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }

            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;

            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];

            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);

            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}