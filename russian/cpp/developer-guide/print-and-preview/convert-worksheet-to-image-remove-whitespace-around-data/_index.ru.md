---
title: Конвертация листа в изображение — удаление пустого пространства вокруг данных с помощью C++
linktitle: Конвертация листа в изображение — удаление пустого пространства вокруг данных
type: docs
weight: 40
url: /ru/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Узнайте, как конвертировать лист в изображение и удалять пустое пространство вокруг данных с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам может потребоваться представить изображения электронных таблиц в приложениях или веб-страницах. Например, вам может потребоваться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или в другой документ. По сути, вы хотите отобразить электронную таблицу в качестве изображения, чтобы ее можно было вставить в другие приложения. Aspose.Cells позволяет преобразовывать электронные таблицы Microsoft Excel в изображения.

{{% /alert %}}

## **Удалите пустое пространство вокруг данных**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API преобразует электронную таблицу в файл изображения с любыми указанными атрибутами, например, формат изображения, пагинированные листы и т.д. Поддерживается несколько форматов изображений, включая BMP, GIF, JPG, TIFF и EMF.

При использовании функции преобразования листа в изображение по умолчанию создается изображение с пустым пространством, то есть с рамкой. Это можно устранить, установив поля верхней, нижней, левой и правой границы страницы исходного листа в 0 и соответствующим образом указав атрибуты [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

Следующий фрагмент кода удаляет пустое пространство вокруг данных на выходном изображении.

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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
