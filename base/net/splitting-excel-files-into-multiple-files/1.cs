using System;
using System.IO;
using Aspose.Cells;

// Define the data directory and file paths
string dataDir = "data/";
string sourcePath = dataDir + "book1.xls";
string outputPath = dataDir + "outputrange.xls";

// Open the source Excel file
Workbook sourceWorkbook = new Workbook(sourcePath);

// Get the first worksheet from the source workbook
Worksheet sourceWorksheet = sourceWorkbook.Worksheets[0];

// Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
var sourceRange = sourceWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Create a new destination workbook
Workbook destWorkbook = new Workbook();

// Access the first worksheet in the destination workbook
Worksheet destWorksheet = destWorkbook.Worksheets[0];

// Create the destination range at A1 with the same dimensions as the source range
var destRange = destWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Copy the source range to the destination range
destRange.Copy(sourceRange);

// Save the destination workbook to a new .xls file
destWorkbook.Save(outputPath, SaveFormat.Excel97To2003);