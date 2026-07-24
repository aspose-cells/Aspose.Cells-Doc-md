#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Prepare data source
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Create workbook and get first worksheet
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Section 1: Default Smart Marker - values spread horizontally across cells
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Bind the data source and process Smart Markers
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Save the resulting workbook
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}