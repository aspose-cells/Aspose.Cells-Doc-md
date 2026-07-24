import com.aspose.cells.*;

// Define the data directory and file paths
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// Open the source Excel file
Workbook sourceWorkbook = new Workbook(sourcePath);

// Get the first worksheet from the source workbook
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Create a new destination workbook
Workbook destWorkbook = new Workbook();

// Access the first worksheet in the destination workbook
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// Create the destination range at A1 with the same dimensions as the source range
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copy the source range to the destination range
destRange.copy(sourceRange);

// Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);