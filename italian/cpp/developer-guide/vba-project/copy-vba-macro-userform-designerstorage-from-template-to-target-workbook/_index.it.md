---
title: Copia il Macro VBA UserForm DesignerStorage dal modello al workbook di destinazione con C++
linktitle: Copia il Macro VBA UserForm DesignerStorage
type: docs
weight: 130
url: /it/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Impara come copiare il Macro VBA UserForm DesignerStorage da un modello a un workbook di destinazione usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells permette di copiare un progetto VBA da un file Excel all’altro. Un progetto VBA consiste di vari tipi di moduli, come Document, Procedurale, Designer, ecc. Tutti i moduli possono essere copiati con codice semplice, ma per il modulo Designer, ci sono dati extra chiamati Designer Storage che devono essere accessibili o copiati. I seguenti due metodi riguardano il Designer Storage:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione**

Consulta il seguente esempio di codice. Copia il progetto VBA dal [file Excel modello](50528345.xlsm) in una cartella vuota e lo salva come [file Excel di output](50528346.xlsm). Se apri il progetto VBA all'interno del file Excel modello, vedrai un User Form come mostrato di seguito. Il User Form consiste di Designer Storage, quindi verrà copiato utilizzando i metodi [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) e [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

lo screenshot seguente mostra il file Excel di output e il suo contenuto, copiato dal file Excel modello. Quando fai clic sul Pulsante 1, si apre il User Form VBA che ha un pulsante di comando che mostra un messaggio quando cliccato.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Codice di Esempio**

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
