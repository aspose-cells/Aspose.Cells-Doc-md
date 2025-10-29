---
title: Загрузить изображение из веба по URL в лист Excel с помощью C++
linktitle: Загрузка веб изображения из URL в рабочий лист Excel
type: docs
weight: 30
url: /ru/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Узнайте, как преобразовать изображение из URL в встроенное изображение Excel с помощью C++ и API Aspose.Cells for C++.
keywords: excel показывать изображение из url, excel url в изображение, показывать изображение в Excel из url, excel вставить изображение из url, преобразовать url в изображение в excel, excel изображение из url, загрузить изображение из url в excel, C++, Excel
---

## Загрузка изображения из URL в рабочий лист Excel

API Aspose.Cells for C++ предоставляет простой способ загрузки изображений из URL в листы Excel. В этой статье объясняется, как загрузить данные изображения в поток памяти и вставить его в лист с помощью Aspose.Cells. Изображение становится встроенным в файл Excel и не требует внешних загрузок при открытии.

## Образец кода

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Для сценариев, требующих постоянно обновляемых изображений из URL, используйте метод, описанный в [Вставить связанное изображение из веб-адреса](/cells/ru/cpp/insert-a-linked-picture-from-web-address/). Этот подход загружает изображение из URL каждый раз при открытии листа.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
