using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Define the data directory and file paths
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Open the source Excel file
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Get the first worksheet from the source workbook
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Create a new destination workbook
    Workbook destWorkbook;

    // Access the first worksheet in the destination workbook
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Create the destination range at A1 with the same dimensions as the source range
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Copy the source range to the destination range
    destRange.Copy(sourceRange);

    // Save the destination workbook to a new .xls file
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}