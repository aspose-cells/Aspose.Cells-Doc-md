---
title: Управление изображениями с помощью C++
linktitle: Управление изображениями
type: docs
weight: 10
url: /ru/cpp/managing-pictures/
description: Добавляйте, позиционируйте и управляйте изображениями в таблицах с помощью API Aspose.Cells for C++.
---

Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более подробно об этом будет рассказано в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображение, отображающее содержимое определенных ячеек.

## **Добавление изображений**

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:
 Просто вызовите метод [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) объекта [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (обернутого в объект [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Метод [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) принимает следующие параметры:

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения с полным путем.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Позиционирование изображений**

Существует два возможных способа контроля позиционирования изображений с помощью Aspose.Cells:

- Пропорциональное позиционирование: определение положения пропорционально высоте и ширине строки.
- Абсолютное позиционирование: задайте точное расположение на странице, например, 40 пикселей слева и 20 пикселей ниже края ячейки.

### **Пропорциональное позиционирование**

Разработчики могут позиционировать изображения пропорционально высоте строки и ширине столбца, используя свойства [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) и [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) объекта [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Объект [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) можно получить, передав его индекс картинки в [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/). Этот пример размещает изображение в ячейке F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Абсолютное позиционирование**

Разработчики могут также абсолютно позиционировать изображения, используя свойства [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) и [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) объекта [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). В этом примере изображение размещается в ячейке F6, 60 пикселей слева и 10 пикселей сверху от ячейки.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вставка изображения на основе ссылки на ячейку**

Aspose.Cells позволяет отображать содержимое ячейки листа в виде изображения. Можно связать изображение с ячейкой, содержащей данные, которые нужно отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, внесенные в данные в этой ячейке или диапазоне ячеек, автоматически отобразятся в графическом объекте.

Добавьте изображение на лист, вызвав метод [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) объекта [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (обертка в объект [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Укажите диапазон ячеек с помощью атрибута [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) объекта [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Добавление набора условных значков с текстом ячейки](/cells/ru/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Вставить привязанное изображение из веб-адреса](/cells/ru/cpp/insert-a-linked-picture-from-web-address/)
- [Вставить изображение на основе ссылки на ячейку](/cells/ru/cpp/insert-a-picture-based-on-cell-reference/)
- [Загрузка веб-изображения из URL в лист Excel](/cells/ru/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
