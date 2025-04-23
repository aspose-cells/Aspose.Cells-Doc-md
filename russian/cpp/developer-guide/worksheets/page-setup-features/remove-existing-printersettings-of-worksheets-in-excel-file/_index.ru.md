---
title: Удалить существующие настройки принтера листов Excel с помощью C++
linktitle: Удалить существующие настройки принтера листов
type: docs
weight: 60
url: /ru/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Узнайте, как программно удалять существующие настройки принтера листа внутри файла Excel через объект Page Setup с помощью Aspose.Cells и C++.
keywords: удалить настройки принтера листа c++, удалить настройки принтера листа Excel c++
---

## **Возможные сценарии использования**
Иногда разработчики хотят предотвратить Excel от включения файлов настроек принтера *.bin* в сохраненные файлы XLSX. Файлы настроек принтера расположены в папке *“[file "root"]\xl\printerSettings”.* В этом документе объясняется, как удалить существующие настройки принтера с использованием Aspose.Cells APIs.

## **Удаление текущих настроек принтера на листах Excel**
Aspose.Cells позволяет удалять существующие настройки принтера, указанные для различных листов в файле Excel. В приведенном ниже образце кода показано, как удалить существующие настройки принтера для всех листов в книге. Пожалуйста, ознакомьтесь с [образцом файла Excel](45056020.xlsx), [выходным файлом Excel](45056021.xlsx), выводом консоли, а также скриншотами для справки.

## **Снимок экрана**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

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

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Вывод в консоль**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
