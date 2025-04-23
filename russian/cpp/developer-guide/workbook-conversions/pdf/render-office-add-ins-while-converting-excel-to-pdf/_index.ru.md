---
title: Отрисовка дополнений Office при конвертации Excel в PDF с C++
linktitle: Рендеринг офисных надстроек при преобразовании Excel в PDF
type: docs
weight: 100
url: /ru/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Узнайте, как отображать дополнения Office при конвертации Excel файлов в PDF с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Ранее Aspose.Cells не могла отображать дополнения Office при сохранении Excel-файла в PDF. Теперь Aspose.Cells правильно отображает их. Для этого не требуется использовать какие-либо особые методы или свойства. Просто сохраните ваш Excel-файл в формат PDF, и дополнения Office будут отображены.

## **Рендеринг офисных надстроек при преобразовании Excel в PDF**

Следующий пример кода сохраняет [образец файла Excel](60489769.xlsx), содержащий офисные дополнения. Посмотрите [выводной PDF, созданный с предыдущей версии, то есть 17.11](60489770.pdf) и [выводной PDF, созданный с новой версии, то есть 17.12 и последующие](60489771.pdf). Вывод предыдущей версии — пустой PDF, а новая версия показывает офисное дополнение.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
