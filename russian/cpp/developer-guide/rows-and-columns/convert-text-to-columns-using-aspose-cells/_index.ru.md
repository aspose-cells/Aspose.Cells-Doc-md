---
title: Преобразование текста в столбцы с помощью Aspose.Cells и C++
linktitle: Преобразование текста в столбцы
type: docs
weight: 30
url: /ru/cpp/convert-text-to-columns-using-aspose-cells/
description: Узнайте, как преобразовать текст в столбцы в файлах Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете преобразовать ваш текст в столбцы с использованием Microsoft Excel. Эта функция доступна в разделе *Инструменты данных* на вкладке *Данные*. Для разделения содержимого столбца на несколько столбцов данные должны содержать определенный разделитель, такой как запятая (или любой другой символ), на основе которого Microsoft Excel разделяет содержимое ячейки на несколько ячеек. Aspose.Cells также предоставляет эту функцию с помощью метода [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/).

## **Преобразование текста в столбцы с использованием Aspose.Cells**

Следующий пример кода показывает использование метода [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/). В коде сначала добавляются имена нескольких людей в столбец A первого листа. Имя и фамилия разделены пробелом. Затем применяется метод [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) к столбцу A и сохраняется как выходной файл Excel. Если открыть [выходной файл Excel](25395213.xlsx), вы увидите, что имена находятся в столбце A, а фамилии — в столбце B, как это показано на скриншоте.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Образец кода**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
