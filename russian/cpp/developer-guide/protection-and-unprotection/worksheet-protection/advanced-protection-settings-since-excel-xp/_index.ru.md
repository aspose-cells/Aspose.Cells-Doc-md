---
title: Расширенные настройки защиты с версии Excel XP и выше с помощью C++
linktitle: Расширенные настройки защиты с Excel XP
type: docs
weight: 30
url: /ru/cpp/advanced-protection-settings-since-excel-xp/
description: Узнайте, как применять расширенные настройки защиты в файлах Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

С момента выпуска Excel 2002 или XP, Microsoft добавила множество расширенных настроек защиты.

{{% /alert %}}

## **Введение**

Эти настройки защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Редактировать содержимое, объекты или сценарии.
- Форматировать ячейки, строки или столбцы.
- Вставлять строки, столбцы или гиперссылки.
- Выбирать заблокированные или разблокированные ячейки.
- Использовать сводные таблицы и многое другое.

Aspose.Cells поддерживает все продвинутые настройки защиты, предлагаемые Excel XP или более поздними версиями.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защитить лист**. Будет отображено диалоговое окно.

Чтобы просмотреть доступные настройки защиты в Excel 2016:

1. В меню **Файл** выберите **Защита книги**, а затем **Защитить текущий лист**.
1. Выберите **Защитить лист** в меню **Проверка**.

Следующие шаги откроют диалоговое окно, в котором вы можете разрешить или ограничить функции листа или применить пароль к листу.

### **Настройки расширенной защиты с использованием Aspose.Cells**

Aspose.Cells поддерживает все расширенные настройки защиты.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет свойство [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/), которое используется для применения этих расширенных настроек защиты. Свойство [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) является объектом класса [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/), который инкапсулирует несколько булевых свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Пожалуйста, не вызывайте метод [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) при использовании свойства [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). Также сохраните файл в форматах Excel97To2003 или Xlsx, потому что расширенные настройки защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить редактирование ячеек пользователями, ячейки должны быть защищены (заблокированы) перед применением любых настроек защиты. В противном случае, ячейки могут редактироваться даже если лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалог:

|**Диалог для блокировки ячеек в Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Также возможно заблокировать ячейки с помощью API Aspose.Cells. Каждая ячейка может иметь формат [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), который содержит логическое свойство [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Установите свойство [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) в **true** или **false**, чтобы заблокировать или разблокировать ячейку.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
