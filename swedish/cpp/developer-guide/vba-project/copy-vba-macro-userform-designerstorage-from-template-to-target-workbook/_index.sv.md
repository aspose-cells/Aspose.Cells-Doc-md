---
title: Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok med C++
linktitle: Kopiera VBA Macro UserForm DesignerStorage
type: docs
weight: 130
url: /sv/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Lär dig hur du kopierar VBA Macro UserForm DesignerStorage från en mall till en målarbetsbok med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells gör det möjligt att kopiera ett VBA-projekt från en Excel-fil till en annan. Ett VBA-projekt består av olika typer av moduler, såsom Dokument, Procedur, Designer, etc. Alla moduler kan kopieras med enkel kod, men för Designer-modulen finns ytterligare data kallad Designer Storage som måste nås eller kopieras. Följande två metoder hanterar Designer Storage:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**

Se följande kodexempel. Det kopierar VBA-projektet från [mallens Excel-fil](50528345.xlsm) till en tom arbetsbok och sparar den som [utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet i mallen för Excel-fil ser du en användarform som visas nedan. User Form består av Designer Storage, så den kommer att kopieras med hjälp av [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)- och [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)-metoder.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Följande skärmbild visar utdata Excel-filen och dess innehåll som kopierades från mall Excel-filen. När du klickar på Knapp 1 öppnas VBA-användarformuläret som i sig har en kommando-knapp som visar ett meddelandefönster vid klick.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Exempelkod**

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
