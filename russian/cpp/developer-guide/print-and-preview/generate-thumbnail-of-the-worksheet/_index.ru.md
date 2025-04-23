---
title: Создание миниатюры рабочего листа с помощью C++
linktitle: Генерация миниатюры листа
type: docs
weight: 110
url: /ru/cpp/generate-thumbnail-of-the-worksheet/
description: Создавайте миниатюры рабочих листов как изображения с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Генерация миниатюр листов может быть полезна. Миниатюра - это небольшое изображение, которое можно вставить в документ Word или презентацию PowerPoint, чтобы показать предварительный просмотр содержимого листа. Ее также можно добавить на веб-страницу с ссылкой для загрузки оригинального документа и использовать во многих других целях.

{{% /alert %}} 

Aspose.Cells for C++ позволяет выводить рабочие листы в файлы изображений, что делает создание миниатюр простым. Следующий пример показывает, как выводить рабочие листы в файлы изображений с помощью C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
