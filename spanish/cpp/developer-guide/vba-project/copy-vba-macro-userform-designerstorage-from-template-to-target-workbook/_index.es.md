---
title: Copiar Diseñador del formulario de usuario de macro VBA desde la plantilla al libro de trabajo destino con C++
linktitle: Copiar Diseñador del formulario de usuario de macro VBA
type: docs
weight: 130
url: /es/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Aprende cómo copiar el Diseñador del Formulario de usuario del macro VBA desde una plantilla a un libro de trabajo destino usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Aspose.Cells te permite copiar un proyecto VBA de un archivo Excel a otro archivo Excel. Un proyecto VBA consta de varios tipos de módulos, como Documentos, Procedimientos, Diseñador, etc. Todos los módulos se pueden copiar con código simple, pero para el módulo Diseñador, hay datos adicionales llamados Almacenamiento del Diseñador que necesitan ser accedidos o copiados. Los siguientes dos métodos tratan con el Almacenamiento del Diseñador:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino**

Por favor, vea el siguiente código de muestra. Copia el proyecto VBA del [archivo de Excel plantilla](50528345.xlsm) en un libro en blanco y lo guarda como el [archivo de Excel de salida](50528346.xlsm). Si abre el proyecto VBA dentro del archivo de Excel plantilla, verá un Formulario de usuario como se muestra abajo. El Formulario de usuario consiste en Almacenamiento del Diseñador, por lo que se copiará usando [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) y [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/) métodos.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La siguiente captura de pantalla muestra el archivo de Excel de salida y su contenido que fue copiado del archivo de Excel plantilla. Cuando hace clic en el Botón 1, se abre el Formulario de usuario VBA que tiene un botón de comando que muestra un cuadro de mensaje al hacer clic.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Código de muestra**

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
