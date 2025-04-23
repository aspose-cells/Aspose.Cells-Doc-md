---
title: Копировать форму макроса VBA UserForm DesignerStorage из шаблона в целевую рабочую книгу с помощью C++
linktitle: Копировать форму макроса VBA UserForm DesignerStorage
type: docs
weight: 130
url: /ru/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Узнайте, как копировать VBA Macro UserForm DesignerStorage из шаблона в целевую рабочую книгу с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет копировать проект VBA из одного файла Excel в другой. Проект VBA состоит из различных типов модулей, таких как Документ, Процедурный, Дизайнерский и т.д. Все модули можно копировать простым кодом, но для модуля Дизайнера требуется дополнительно получить или скопировать данные, называемые Designer Storage. Следующие два метода работают с Designer Storage:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу**

Пожалуйста, посмотрите следующий пример кода. Он копирует VBA-проект из [шаблонного файла Excel](50528345.xlsm) в пустую рабочую книгу и сохраняет его как [выходной файл Excel](50528346.xlsm). Если открыть VBA-проект внутри шаблонного файла Excel, вы увидите форму пользователя, как показано ниже. Форма пользователя состоит из Designer Storage, поэтому она будет скопирована с использованием методов [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) и [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Следующий скриншот показывает выходной файл Excel и его содержимое, скопированные из шаблонного файла Excel. При нажатии на кнопку 1 откроется форма VBA User Form, которая сама содержит командную кнопку, показывающую сообщение при нажатии.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Образец кода**

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
