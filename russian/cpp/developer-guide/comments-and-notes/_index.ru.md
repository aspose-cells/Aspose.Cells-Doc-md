---
title: Управление комментариями и заметками с помощью C++
linktitle: Комментарии и заметки
type: docs
weight: 128
url: /ru/cpp/comments-and-notes/
description: Вставка и управление комментариями или заметками с Aspose.Cells for C++.
keywords: вставка комментариев, вставка заметок
---

## **Введение**

Комментарии используются для добавления дополнительной информации к ячейкам. Aspose.Cells предоставляет два способа добавления комментариев к ячейкам. Первый - создавать комментарии в файле дизайнера вручную. Затем эти комментарии импортируются с использованием Aspose.Cells. Второй - добавлять комментарии с использованием API Aspose.Cells во время выполнения. В этой теме будет рассмотрено добавление комментариев к ячейкам с использованием API Aspose.Cells. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

Добавление комментария в ячейку, вызвав метод [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) коллекции [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Новый объект [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) может быть получен из коллекции [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/), передав индекс комментария. После доступа к объекту [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/), настроить заметку комментария можно, используя свойство [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) объекта [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add a comment to cell "F5"
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Access the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set the comment note
    comment.SetNote(u"Hello Aspose!");

    // Save the Excel file
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Форматирование комментариев**

Также возможно форматировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

```cpp
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

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding a comment to "F5" cell
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Accessing the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Setting the comment note
    comment.SetNote(u"Hello Aspose!");

    // Setting the font size of a comment to 14
    comment.GetFont().SetSize(14);

    // Setting the font of a comment to bold
    comment.GetFont().SetIsBold(true);

    // Setting the height of the font to 10
    comment.SetHeightCM(10);

    // Setting the width of the font to 2
    comment.SetWidthCM(2);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Добавить изображение в комментарий**

С помощью Microsoft Excel 2007 также возможно иметь изображение в качестве фона комментария к ячейке. В Excel 2007 это можно сделать, выполнив следующие шаги. (Предполагается, что вы уже добавили комментарий к ячейке.)

1. Щелкните правой кнопкой мыши ячейку, содержащую комментарий.
1. Выберите **Показать/скрыть комментарии** и очистите любой текст из комментария.
1. Щелкните по границе комментария, чтобы выбрать его.
1. Выберите **Формат**, затем **Комментарий**.
1. На вкладке **Цвета и линии** разверните список **Цвет**.
1. Нажмите **Изменение заливки**.
1. На вкладке **Изображение** нажмите **Выбрать изображение**.
1. Найдите и выберите изображение.
1. Нажмите **ОК**, пока все диалоговые окна не закроются.

Aspose.Cells также предоставляет эту функцию. Ниже приведен пример кода, который создает файл XLSX с нуля, добавляя комментарий в ячейку "A1" с установленным изображением в качестве его фона.

```c++
#include <Aspose.Cells.h>
#include <fstream>
#include <vector>
#include <iostream>

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);
    CommentCollection comments = sheet.GetComments();

    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");

    Font commentFont = comment.GetFont();
    commentFont.SetName(u"Times New Roman");

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData;
    std::ifstream file(imagePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (file)
    {
        std::streamsize size = file.tellg();
        file.seekg(0, std::ios::beg);
        imageData.resize(size);
        file.read(reinterpret_cast<char*>(imageData.data()), size);
    }
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().SetImageData(data);

    U16String outputPath = outDir + u"book1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook with image comment created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Продвинутые темы**
- [Изменение направления текста комментария](/cells/ru/cpp/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/cpp/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/cpp/how-to-set-comment-background/)
- [Комментарии с цепочкой](/cells/ru/cpp/threaded-comments/)
