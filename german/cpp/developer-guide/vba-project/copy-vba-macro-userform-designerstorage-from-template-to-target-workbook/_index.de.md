---
title: Kopieren Sie den VBA Makro UserForm DesignerStorage von Vorlage in Ziel Arbeitsmappe mit C++
linktitle: VBA Makro UserForm DesignerStorage kopieren
type: docs
weight: 130
url: /de/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Erfahren Sie, wie Sie den VBA Makro UserForm DesignerStorage mit Aspose.Cells for C++ von einer Vorlage in eine Zielarbeitsmappe kopieren.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es, ein VBA-Projekt von einer Excel-Datei in eine andere zu kopieren. Ein VBA-Projekt besteht aus verschiedenen Modultypen wie Dokument, Procedural, Designer usw. Alle Module können mit einfachem Code kopiert werden, aber für das Designer-Modul gibt es zusätzliche Daten namens Designer Storage, die zugänglich oder kopiert werden müssen. Die folgenden zwei Methoden befassen sich mit Designer Storage:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei**

Bitte sehen Sie sich den folgenden Beispielcode an. Er kopiert das VBA-Projekt aus der [Vorlagen-Excel-Datei](50528345.xlsm) in eine leere Arbeitsmappe und speichert sie als [Ausgabedatei Excel](50528346.xlsm). Wenn Sie das VBA-Projekt in der Vorlage-Excel-Datei öffnen, sehen Sie ein Userform wie unten gezeigt. Das Userform besteht aus Designer Storage, das mit [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) und [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/) Methoden kopiert wird.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Das folgende Screenshot zeigt die Ausgabedatei Excel und deren Inhalte, die aus der Vorlage-Excel-Datei kopiert wurden. Wenn Sie auf Button 1 klicken, öffnet sich das VBA-Userform, das einen Befehlsknopf enthält, der bei Klick eine Meldung anzeigt.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Beispielcode**

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
