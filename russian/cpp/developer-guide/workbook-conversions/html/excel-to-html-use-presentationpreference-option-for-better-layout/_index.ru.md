---
title: Преобразование Excel в HTML  Использование опции PresentationPreference для лучшей разметки с помощью C++
linktitle: Excel в HTML  Используйте опцию PresentationPreference для лучшего макета
type: docs
weight: 220
url: /ru/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Узнайте, как улучшить разметку при сохранении Excel в HTML с помощью C++.
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет полезное свойство HtmlSaveOptions.PresentationPreference для разработчиков, которым необходимо получить лучшее оформление при сохранении файла Microsoft Excel в форматах HTML или MHT. Значение по умолчанию свойства - false. Мы рекомендуем установить это свойство в true, чтобы получить более привлекательное оформление отчетов Excel.

{{% /alert %}} 

Пожалуйста, ознакомьтесь с примером кода ниже, демонстрирующим отображение HTML-файла из отчета Excel с предпочтением презентации.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
