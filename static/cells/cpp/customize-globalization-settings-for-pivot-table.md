##Customize Globalization Settings for Pivot Table with C++
Learn how to customize pivot table globalization settings using Aspose.Cells for C++.
## **Possible Usage Scenarios**
Sometimes you want to customize the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* text as per your requirements. Aspose.Cells for C++ allows you to customize the globalization settings of the pivot table to deal with such scenarios. You can also use this feature to change the labels to other languages like Arabic, Hindi, Polish, etc.
## **Customize Globalization Settings for Pivot Table**
The following sample code explains how to customize globalization settings for the pivot table in C++. It creates a class *CustomPivotTableGlobalizationSettings* derived from the base class [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/) and overrides all necessary methods. These methods return customized text for various pivot table elements. The code then assigns this implementation to the [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) property. The example loads a [source Excel file](40468488.xlsx), refreshes pivot data, and saves it as [output PDF](40468487.pdf). The screenshot below shows customized labels in the output.
![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
class CustomPivotTableGlobalizationSettings : public PivotGlobalizationSettings {
public:
virtual U16String GetTextOfTotal() override {
std::cout << "---------GetPivotTotalName-------------" << std::endl;
return u"AsposeGetPivotTotalName";
}
virtual U16String GetTextOfGrandTotal() override {
std::cout << "---------GetPivotGrandTotalName-------------" << std::endl;
return u"AsposeGetPivotGrandTotalName";
}
virtual U16String GetTextOfMultipleItems() override {
std::cout << "---------GetMultipleItemsName-------------" << std::endl;
return u"AsposeGetMultipleItemsName";
}
virtual U16String GetTextOfAll() override {
std::cout << "---------GetAllName-------------" << std::endl;
return u"AsposeGetAllName";
}
virtual U16String GetTextOfColumnLabels() override {
std::cout << "---------GetColumnLabelsOfPivotTable-------------" << std::endl;
return u"AsposeGetColumnLabelsOfPivotTable";
}
virtual U16String GetTextOfRowLabels() override {
std::cout << "---------GetRowLabelsNameOfPivotTable-------------" << std::endl;
return u"AsposeGetRowLabelsNameOfPivotTable";
}
virtual U16String GetTextOfEmptyData() override {
std::cout << "---------GetEmptyDataName-------------" << std::endl;
return u"(blank)AsposeGetEmptyDataName";
}
virtual U16String GetTextOfSubTotal(PivotFieldSubtotalType subTotalType) override {
std::cout << "---------GetSubTotalName-------------" << std::endl;
switch(subTotalType) {
case PivotFieldSubtotalType::Sum:
return u"AsposeSum";
case PivotFieldSubtotalType::Count:
return u"AsposeCount";
case PivotFieldSubtotalType::Average:
return u"AsposeAverage";
case PivotFieldSubtotalType::Max:
return u"AsposeMax";
case PivotFieldSubtotalType::Min:
return u"AsposeMin";
case PivotFieldSubtotalType::Product:
return u"AsposeProduct";
case PivotFieldSubtotalType::CountNums:
return u"AsposeCount";
case PivotFieldSubtotalType::Stdev:
return u"AsposeStdDev";
case PivotFieldSubtotalType::Stdevp:
return u"AsposeStdDevp";
case PivotFieldSubtotalType::Var:
return u"AsposeVar";
case PivotFieldSubtotalType::Varp:
return u"AsposeVarp";
default:
return u"AsposeSubTotalName";
}
}
};
int main() {
Aspose::Cells::Startup();
U16String srcDir(u"../Data/01_SourceDirectory/");
U16String outDir(u"../Data/02_OutputDirectory/");
Workbook wb(srcDir + u"samplePivotTableGlobalizationSettings.xlsx");
CustomPivotTableGlobalizationSettings customSettings;
wb.GetSettings().GetGlobalizationSettings()->SetPivotSettings(&customSettings);
wb.GetWorksheets().Get(0).SetIsVisible(false);
Worksheet ws = wb.GetWorksheets().Get(1);
PivotTable pt = ws.GetPivotTables().Get(0);
pt.SetRefreshDataFlag(true);
pt.RefreshData();
pt.CalculateData();
pt.SetRefreshDataFlag(false);
PdfSaveOptions options;
options.SetOnePagePerSheet(true);
wb.Save(outDir + u"outputPivotTableGlobalizationSettings.pdf", options);
std::cout << "Pivot table globalization settings applied successfully." << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
