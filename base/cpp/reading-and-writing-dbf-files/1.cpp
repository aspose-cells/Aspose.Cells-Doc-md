#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Column headers
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // Data row 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // Data row 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // Data row 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // Data row 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // Data row 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // Set column widths for better readability
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}