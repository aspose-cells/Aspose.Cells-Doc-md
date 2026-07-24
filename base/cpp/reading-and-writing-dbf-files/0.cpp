#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}