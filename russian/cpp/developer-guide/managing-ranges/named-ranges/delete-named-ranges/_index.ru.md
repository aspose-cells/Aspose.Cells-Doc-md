---
title: Удаление именованных диапазонов с помощью C++
linktitle: Удалить именованные диапазоны
type: docs
weight: 90
url: /ru/cpp/delete-named-ranges/
description: Узнайте, как удалять определённые имена или именованные диапазоны из файлов Excel или OpenOffice, используя Aspose.Cells for C++.
---

## **Введение**
Если в файлах Excel слишком много определенных имен или именованных диапазонов, некоторые из них придется очистить, чтобы они больше не использовались.

## **Удалить именованный диапазон в MS Excel**

Для удаления именованного диапазона из Excel следуйте этим шагам:
1. Откройте Microsoft Excel и откройте книгу, которая содержит именованный диапазон.
2. Перейдите на вкладку "Формулы" на ленте Excel.
3. Нажмите кнопку "Менеджер имен" в группе "Определенные имена". Это откроет диалоговое окно Менеджер имен.
4. В диалоговом окне Менеджер имен выберите именованный диапазон, который вы хотите удалить.
5. Нажмите кнопку "Удалить". Подтвердите удаление по запросу.
6. Нажмите кнопку "Закрыть", чтобы закрыть диалоговое окно Менеджер имен.
7. Сохраните книгу, чтобы сохранить внесенные изменения.

## **Удаление именованного диапазона с помощью Aspose.Cells for C++**
С помощью Aspose.Cells for C++ вы можете удалять именованные диапазоны или определённые имена по [тексты](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/) или [индексу](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) в списке.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Примечание: если определенное имя используется в формулах, его невозможно удалить. Мы можем удалить только формулу определенного имени.

## **Удаляет несколько именованных диапазонов**
При удалении определенного имени нужно проверить, используется ли оно во всех формулах в файле.
Чтобы повысить производительность удаления именованных диапазонов, мы можем удалять их группами.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Удаление дублированных определенных имен**
Некоторые файлы Excel повреждаются, потому что некоторые определенные имена дублируются. Поэтому мы можем удалить эти дублирующиеся имена для восстановления файла.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
