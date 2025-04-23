---
title: Рисование временной шкалы при рендеринге Excel в PDF с помощью C++
linktitle: Отображение временной шкалы при преобразовании Excel в PDF
type: docs
weight: 60
url: /ru/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Управляйте временными шкалами Excel файлов с помощью Aspose.Cells и C++.
keywords: Преобразование временной шкалы в PDF без использования Office 2013, Office 2016, Office 2019 и Office 365
---

## **Отображение временной шкалы при преобразовании Excel в PDF**
Если у вас есть Excel файл с прикрепленной временной шкалой и вы хотите экспортировать его в PDF с сохранением настроек временной шкалы, Aspose.Cells поддерживает это по умолчанию. Просто экспортируйте файл с временной шкалой в PDF, и созданный PDF покажет примененную временную шкалу.

Приведенный ниже образец кода загружает [образец Excel-файла](input.xlsx), содержащий существующую временную шкалу. Затем он сохраняет книгу как [файл PDF на выходе](out.pdf). На следующем снимке экрана сравниваются исходный файл Excel и сгенерированный PDF-файл.

<img src="out.png" width="60%">

## **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

