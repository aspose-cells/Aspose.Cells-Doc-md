#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // Read the image file into a byte array
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // Convert std::vector to Aspose::Cells::Vector using pointer+size constructor
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Embed the image directly into the cell
    cell.SetEmbeddedImage(imageData);

    // Optionally adjust row height and column width so the embedded image is more visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Column C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Row 6 (index 5)

    // Save the resulting workbook as an .xlsx file
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}