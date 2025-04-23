---
title: Объединение и разделение ячеек с помощью C++
linktitle: Объединение и разъединение ячеек
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц, которая поддерживает объединение и разделение ячеек. Эта статья расскажет, как объединять и разделять ячейки с помощью библиотеки Aspose.Cells и как настраивать стиль объединенной ячейки.
keywords: Aspose.Cells, библиотека C++, таблицы, объединение ячеек, разделение ячеек, настройки стилей, пользовательские стили
type: docs
weight: 190
url: /ru/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает эту функцию и также может объединять ячейки в листе. Вы также можете разъединить или разделить объединенные ячейки. Ссылка на объединенную ячейку - это ссылка на верхнюю левую ячейку в изначально выбранном диапазоне.

{{% /alert %}} 

## **Введение**
Не всегда нужно иметь одинаковое количество ячеек в каждой строке или столбце. Например, вы можете захотеть поместить заголовок в ячейку, которая охватывает несколько столбцов. Или, если создаете счет-фактуру, вам может понадобиться меньше столбцов для итоговой суммы. Чтобы объединить несколько ячеек в одну, объедините их. Microsoft Excel позволяет пользователям выбирать файлы и объединять их, чтобы структурировать электронную таблицу так, как им нужно.

{{% alert color="primary" %}} 

Обратите внимание, что при объединении ячеек сохраняются данные только в верхней левой ячейке. Если в других ячейках диапазона есть данные, эти данные будут удалены.
Форматирование также основано на ссылочной ячейке, поэтому при объединении ячеек форматируются с настройками верхней левой ячейки в диапазоне. При разъединении новые ячейки сохраняют свои исходные настройки формата.

{{% /alert %}} 

## **Объединение ячеек в листе**
### **Объединение ячеек в Microsoft Excel**
Следующие шаги описывают, как объединить ячейки в электронной таблице с использованием MS Excel.

1. Копируйте данные, которые вы хотите в верхнюю левую ячейку в пределах диапазона.
1. Выберите ячейки, которые вы хотите объединить.
1. Чтобы объединить ячейки в строке или столбце и центрировать содержимое ячейки, нажмите на значок **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Объединение ячеек с помощью Aspose.Cells**
Класс `Aspose::Cells::Cells` содержит полезные методы для этой задачи. Например, метод `Merge()` объединяет ячейки в пределах указанного диапазона в одну.

В следующем примере показано, как объединить ячейки (C6:E7) в электронной таблице.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Разъединение (разделение) объединенных ячеек**
### **Использование Microsoft Excel**
Следующие шаги описывают, как разделить объединенные ячейки с помощью Microsoft Excel.

1. Выберите объединенную ячейку.
   Когда ячейки были объединены, на панели инструментов **Форматирование** выбрано **Объединить и центрировать**.
1. Нажмите на **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Использование Aspose.Cells**
 Класс `Aspose::Cells::Cells` имеет метод `UnMerge()`, который распаковывает ячейки в их исходное состояние. Метод распаковывает ячейки, используя ссылку на ячейку в объединенном диапазоне.

Приведенный ниже пример показывает, как разделить объединенные ячейки (C6). Пример использует файл, созданный в предыдущем примере, и разбивает объединенные ячейки.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Обнаружение объединенных ячеек в листе](/cells/ru/cpp/detect-merged-cells-in-a-worksheet/)
