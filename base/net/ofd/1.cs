using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Open an existing Excel workbook from disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Read and display values from selected cells to confirm the file was loaded
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Iterate over the Worksheets collection to enumerate available sheets
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Append a summary header row at the top of the data block
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) Configure PageSetup properties on the worksheet
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) Optionally set the print area for the OFD output
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Save the workbook as an OFD file
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
