---
title: Конвертация дат в японский формат с помощью C++
linktitle: Преобразование дат в японские даты
type: docs
weight: 350
url: /ru/cpp/convert-dates-to-japanese-dates/
description: Узнайте, как преобразовать григорианские даты в японские, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

В Японском календаре новая эра начинается с правления нового императора. 1 мая 2019 года во власти появился новый император, с этого момента закончилась эра Хэйсэй и началась эпоха Рэйва.

{{% /alert %}}

Aspose.Cells предоставляет способ конвертировать григорианские даты в японские. Во время этой конвертации также учитываются изменения в эпохе. Следующий пример кода преобразует исходный Excel-файл (90112015.xlsx) с григорианскими датами в PDF (90112016.pdf) с японскими датами, как показано на изображении ниже.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
