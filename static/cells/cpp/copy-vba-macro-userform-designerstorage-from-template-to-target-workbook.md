##Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook with C++
Learn how to copy VBA Macro UserForm DesignerStorage from a template to a target workbook using Aspose.Cells for C++.
## **Possible Usage Scenarios**
Aspose.Cells allows you to copy a VBA project from one Excel file into another Excel file. A VBA project consists of various types of modules, such as Document, Procedural, Designer, etc. All modules can be copied with simple code, but for the Designer module, there is some extra data called Designer Storage that needs to be accessed or copied. The following two methods deal with Designer Storage:
- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)
## **Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook**
Please see the following sample code. It copies the VBA project from the [template Excel file](50528345.xlsm) into an empty workbook and saves it as the [output Excel file](50528346.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) and [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/) methods.
The following screenshot shows the output Excel file and its contents which were copied from the template Excel file. When you click on the Button 1, it opens up the VBA User Form which itself has a command button that shows a message box on clicking.
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook target;
Workbook templateFile(srcDir + u"sampleDesignerForm.xlsm");
WorksheetCollection templateSheets = templateFile.GetWorksheets();
WorksheetCollection targetSheets = target.GetWorksheets();
for (int i = 0; i < templateSheets.GetCount(); ++i)
{
Worksheet ws = templateSheets.Get(i);
if (ws.GetType() == SheetType::Worksheet)
{
Worksheet s = targetSheets.Add(ws.GetName());
s.Copy(ws);
s.GetCells().Get(u"A2").PutValue(u"VBA Macro and User Form copied from template to target.");
}
}
VbaProject templateVbaProject = templateFile.GetVbaProject();
VbaProject targetVbaProject = target.GetVbaProject();
VbaModuleCollection templateModules = templateVbaProject.GetModules();
for (int i = 0; i < templateModules.GetCount(); ++i)
{
VbaModule vbaItem = templateModules.Get(i);
if (vbaItem.GetName() == u"ThisWorkbook")
{
targetVbaProject.GetModules().Get(u"ThisWorkbook").SetCodes(vbaItem.GetCodes());
}
else
{
std::wcout << reinterpret_cast<const wchar_t*>(vbaItem.GetName().GetData()) << std::endl;
int vbaMod = 0;
Worksheet sheet = targetSheets.GetSheetByCodeName(vbaItem.GetName());
if (sheet.IsNull())
{
vbaMod = targetVbaProject.GetModules().Add(vbaItem.GetType(), vbaItem.GetName());
}
else
{
vbaMod = targetVbaProject.GetModules().Add(sheet);
}
targetVbaProject.GetModules().Get(vbaMod).SetCodes(vbaItem.GetCodes());
if (vbaItem.GetType() == VbaModuleType::Designer)
{
Vector<uint8_t> designerStorage = templateVbaProject.GetModules().GetDesignerStorage(vbaItem.GetName());
targetVbaProject.GetModules().AddDesignerStorage(vbaItem.GetName(), designerStorage);
}
}
}
target.Save(outDir + u"outputDesignerForm.xlsm", SaveFormat::Xlsm);
Aspose::Cells::Cleanup();
}
```
