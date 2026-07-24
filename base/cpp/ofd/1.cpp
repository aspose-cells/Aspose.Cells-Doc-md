#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Open an existing Excel workbook from disk
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Read and display values from selected cells to confirm the file was loaded
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Iterate over the Worksheets collection to enumerate available sheets
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Optionally update a timestamp cell to reflect the conversion
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Append a summary header row at the top of the data block
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Configure PageSetup properties on the worksheet
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Optionally set the print area for the OFD output
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Save the workbook as an OFD file
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}