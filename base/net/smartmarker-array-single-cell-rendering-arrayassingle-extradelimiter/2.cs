using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // Section 1: Default Smart Marker - values spread horizontally across cells
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Bind the data source and process Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Save the resulting workbook
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}