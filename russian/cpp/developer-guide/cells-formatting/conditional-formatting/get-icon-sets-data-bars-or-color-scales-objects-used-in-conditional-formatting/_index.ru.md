---
title: Получить объекты набора значков, Data Bars или Color Scales, используемые в условном форматировании, с помощью C++
linktitle: Получить наборы значков, полосы данных или объекты цветовых шкал
description: Aspose.Cells for C++ — это библиотека для работы с файлами таблиц. Она поддерживает использование наборов значков, полос данных и объектов цветовых шкал в условном форматировании для отображения данных из таблиц. В этой статье описывается, как использовать библиотеку Aspose.Cells для получения данных для этих объектов.
keywords: Aspose.Cells, Условное форматирование, Набор значков, Панель данных, Цветовая шкала, Таблица
type: docs
weight: 10
url: /ru/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Иногда необходимо получить используемые в условном форматировании наборы значков в ячейке или диапазоне ячеек и создать на их основе изображение. Возможно, потребуется прочитать полосы данных или цветовые шкалы, используемые в условном форматировании. Aspose.Cells for C++ поддерживает эту функцию.

{{% /alert %}} 

Следующий пример кода показывает, как считать используемые для условного форматирования наборы значков. С помощью простого API Aspose.Cells данные изображения набора значков сохраняются как изображение.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
