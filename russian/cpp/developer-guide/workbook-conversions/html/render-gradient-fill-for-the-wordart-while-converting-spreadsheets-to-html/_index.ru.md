---
title: Визуализировать градиентную заливку WordArt при преобразовании таблиц в HTML с помощью C++
linktitle: Отображение градиентной заливки для WordArt при преобразовании электронных таблиц в HTML
type: docs
weight: 90
url: /ru/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Научитесь отображать градиентную заливку WordArt при преобразовании таблиц в HTML с помощью C++.
---

## **Возможные сценарии использования**
До Aspose.Cells 17.1 Aspose.Cells не отображал градиентную заливку словоArt при преобразовании файла Excel в формат HTML. С выпуском Aspose.Cells 17.1 поддерживается градиентная заливка словоArt. На следующем скриншоте сравнивается эффект градиентной заливки при преобразовании файла Excel с использованием Aspose.Cells 17.1 и более старой версии.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Отображение градиентного заполнения для WordArt при конвертации электронных таблиц в HTML**
Следующий образец кода преобразует [исходный файл Excel](22774111.xlsx) в [выходной формат HTML](22774109.zip). Исходный файл Excel содержит объект WordArt с градиентной заливкой, как показано на приведенном выше скриншоте.
## **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
