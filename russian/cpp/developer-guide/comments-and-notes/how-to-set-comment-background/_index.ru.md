---
title: Как изменить фон в комментарии в Excel с помощью C++
linktitle: Фон комментария
type: docs
weight: 190
url: /ru/cpp/how-to-set-comment-background/
description: Как изменить цвет комментария в Excel. Как вставить изображение или картинку в комментарий в Excel с помощью C++.
keywords: добавить изображение вкладыш цвет комментария фон excel
---

{{% alert color="primary" %}}

Комментарии добавляются в ячейки для фиксации комментариев: будь то детали работы формулы, источник значения или вопросы проверяющих. Комментарии играют важную роль при обсуждении или рецензировании документов несколькими людьми в разное время. Как различить комментарии разных людей? Да, можно установить разный цвет фона для каждого комментария. Но при обработке большого количества документов и комментариев вручную это становится проблемой. К счастью, [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) предоставляет API, который позволяет выполнять это программно.

{{% /alert %}}

## **Как изменить цвет комментария в Excel**

Если вам не нужен стандартный фон у комментариев, вы можете заменить его на интересующий вас цвет. Как изменить цвет фона для области комментария в Excel?

Следующий код покажет, как использовать [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) для добавления желаемого фона комментария на ваш выбор.

Здесь подготовлен [пример файла](exmaple.xlsx) для вас. Этот файл используется для инициализации объекта Workbook в приведенном ниже коде.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"exmaple.xlsx";
    Workbook book(inputPath);

    Worksheet worksheet = book.GetWorksheets().Get(0);
    Comment comment = worksheet.GetComments().Get(0);

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().GetSolidFill().SetColor(Color::Red());

    U16String outputPath = outDir + u"result.xlsx";
    book.Save(outputPath);

    std::cout << "Comment color changed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Выполните указанный выше код, и вы получите [выходной файл](result.xlsx).

## **Как вставить изображение в комментарий в Excel**

Microsoft Excel позволяет настраивать внешний вид таблиц практически по всему спектру. Можно даже добавить фоновое изображение к комментариям. Добавление фона может быть эстетичным выбором или способствовать укреплению бренда.

Пример ниже создает XLSX-файл с нуля с помощью API [**Aspose.Cells**](https://products.aspose.com/cells/cpp/) и добавляет комментарий с фоновым изображением в ячейку A1.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include <vector>
#include <cstdint>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a Workbook
    Workbook workbook;

    // Get a reference of comments collection with the first sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    CommentCollection comments = worksheet.GetComments();

    // Add a comment to cell A1
    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");
    Font font = comment.GetFont();
    font.SetName(u"Times New Roman");

    // Load an image into stream
    U16String imagePath = srcDir + u"image2.jpg";
    std::vector<uint8_t> imageData;
    // Assume image loading logic here
    // For simplicity, we assume imageData is populated with the image bytes

    // Set image data to the shape associated with the comment
    CommentShape commentShape = comment.GetCommentShape();
    commentShape.GetFill().SetImageData(Aspose::Cells::Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    U16String outputPath = outDir + u"commentwithpicture1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with comment and image!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
