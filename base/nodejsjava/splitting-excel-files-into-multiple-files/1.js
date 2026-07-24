let sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Get the first worksheet from the source workbook
let sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
let sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Create a new destination workbook
let destWorkbook = new AsposeCells.Workbook();

// Access the first worksheet in the destination workbook
let destWorksheet = destWorkbook.getWorksheets().get(0);

// Create the destination range at A1 with the same dimensions as the source range
let destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copy the source range to the destination range
destRange.copy(sourceRange);

// Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);