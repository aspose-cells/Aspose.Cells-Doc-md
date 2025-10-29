---
title: Добавить гиперссылки на изображение с помощью C++
linktitle: Добавление гиперссылок изображений
type: docs
weight: 140
url: /ru/cpp/add-image-hyperlinks/
description: Узнайте, как добавлять гиперссылки на изображения через API Aspose.Cells for C++.
keywords: Добавить гиперссылки на изображения, вставить гиперссылки на изображения
---

{{% alert color="primary" %}} 

Гиперссылки полезны для доступа к информации на других листах или на веб-сайтах. Microsoft Excel позволяет пользователям добавлять гиперссылки на текст в ячейках и на изображения. Гиперссылки на изображения могут упростить навигацию по листу, например, как кнопки Далее и Назад или логотипы, ведущие на определенные сайты. В этом документе объясняется, как вставить гиперссылки на изображения на листе с помощью Aspose.Cells.

{{% /alert %}} 

Aspose.Cells позволяет добавлять гиперссылки на изображения в электронные таблицы во время выполнения. Возможно установить и изменить подсказку экрана и адрес ссылки. В следующем примере кода показано, как добавить гиперссылку на изображение на лист.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
