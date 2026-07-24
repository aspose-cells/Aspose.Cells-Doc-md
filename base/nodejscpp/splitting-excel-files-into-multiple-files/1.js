const AsposeCells = require("aspose.cells");

// Define the data directory and file paths
const dataDir = "data/";
const sourcePath = dataDir + "book1.xls";
const outputPath = dataDir + "outputrange.xls";

// Open the source Excel file
const sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Get the first worksheet from the source workbook
const sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
const sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Create a new destination workbook
const destWorkbook = new AsposeCells.Workbook();

// Access the first worksheet in the destination workbook
const destWorksheet = destWorkbook.getWorksheets().get(0);

// Create the destination range at A1 with the same dimensions as the source range
const destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copy the source range to the destination range
destRange.copy(sourceRange);

// Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);