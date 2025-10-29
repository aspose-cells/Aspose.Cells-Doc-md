---
title: Copier le concepteur du formulaire utilisateur de la macro VBA et le stocker dans le classeur cible avec C++
linktitle: Copier le concepteur du formulaire utilisateur de la macro VBA
type: docs
weight: 130
url: /fr/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Apprenez comment copier le concepteur du formulaire utilisateur de la macro VBA d un modèle vers un classeur cible en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de copier un projet VBA d'un fichier Excel à un autre. Un projet VBA se compose de différents types de modules, tels que Document, Procédural, Designer, etc. Tous les modules peuvent être copiés avec du code simple, mais pour le module Designer, il y a des données supplémentaires appelées Designer Storage qui doivent être accessibles ou copiées. Les deux méthodes suivantes traitent du Designer Storage :

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Copier le stockage de concepteur de formulaire utilisateur de macro VBA du modèle vers le classeur cible**

Veuillez voir le code d'exemple suivant. Il copie le projet VBA du [fichier Excel modèle](50528345.xlsm) dans un classeur vide et le sauvegarde sous le nom de [fichier Excel de sortie](50528346.xlsm). Si vous ouvrez le projet VBA dans le fichier Excel modèle, vous verrez un formulaire utilisateur comme illustré ci-dessous. Le formulaire utilisateur contient un Designer Storage, il sera donc copié en utilisant [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) et [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/) methods.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La capture d'écran suivante montre le fichier Excel de sortie et son contenu, qui ont été copiés du fichier Excel modèle. Lorsque vous cliquez sur le bouton 1, cela ouvre le formulaire utilisateur VBA qui a lui-même un bouton de commande affichant une boîte de message lors du clic.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Code d'exemple**

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
{{< app/cells/assistant language="cpp" >}}
