#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}