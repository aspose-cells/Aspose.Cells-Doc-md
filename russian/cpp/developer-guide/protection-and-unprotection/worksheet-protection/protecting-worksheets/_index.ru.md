---
title: Защита листов с помощью C++
linktitle: Защита листов
type: docs
weight: 10
url: /ru/cpp/protecting-worksheets/
description: Узнайте, как защитить листы, строки, столбцы и отдельные ячейки в файлах Microsoft Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Когда лист защищен, пользователи не могут выполнять определенные действия. Например, вводить данные, вставлять или удалять строки или столбцы и т.д.

{{% /alert %}}

## **Защита листов**

### **Введение**

Основные параметры защиты в Microsoft Excel:

- Содержимое
- Объекты
- Сценарии

Защита листов не скрывает и не защищает конфиденциальные данные, поэтому это отличается от шифрования файлов. Обычно защита листа подходит для ознакомительных целей. Она предотвращает изменение данных, содержимого и форматирования в листе.

### **Защита листа**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет метод [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/), который используется для применения защиты на листе. Метод [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) принимает следующие параметры:

- Тип защиты, тип защиты, применяемый для листа. Тип защиты применяется с помощью перечисления [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/).
- Новый пароль, новый пароль, используемый для защиты листа.
- Старый пароль, старый пароль, если лист уже защищен паролем. Если лист еще не защищен, то просто передайте null.

Перечисление [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) содержит следующие предопределенные типы защиты:

|**Типы защиты**|**Описание**|
| :- | :- |
|All|Пользователь не может изменять ничего на этом листе|
|Contents|Пользователь не может вводить данные на этом листе|
|Objects|Пользователь не может изменять рисуночные объекты|
|Scenarios|Пользователь не может изменять сохраненные сценарии|
|Structure|Пользователь не может изменять структуру|
|Windows|Защита применяется к окнам|
|None|Никакая защита не применяется|

Приведенный ниже пример показывает, как защитить лист паролем.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Как только указанный выше код используется для защиты листа, вы можете проверить защиту на листе, открыв его. После открытия файла и попытки добавить данные на лист, вы увидите следующий диалог:

|**Предупреждение о том, что пользователь не может изменять лист**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Для работы на листе снимите защиту листа, выбрав **Защита**, затем **Снять защиту таблицы** из меню **Инструменты**.

После выбора пункта меню Снять защиту таблицы откроется диалоговое окно, призывающее вас ввести пароль, чтобы вы могли работать на листе, как показано ниже:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Защита нескольких ячеек на листе c помощью Microsoft Excel**

Могут быть определенные сценарии, когда вам нужно заблокировать только несколько ячеек на листе. Если вы хотите заблокировать определенные ячейки на листе, вам нужно разблокировать все остальные ячейки на листе. Все ячейки на листе уже инициализированы для блокировки, вы можете проверить это, открыв любой файл Excel в MS Excel и нажав **Формат | Ячейки...**, чтобы показать диалоговое окно **Формат ячеек**, а затем щелкнув вкладку **Защита** и убедившись, что флажок "Заблокирован" по умолчанию установлен.

Следующие пункты описывают, как заблокировать несколько ячеек с помощью MS Excel. Этот метод применим к Microsoft Office Excel 97, 2000, 2002, 2003 и более новым версиям.

1. Выберите весь лист, нажав кнопку **Выбрать все** (серый прямоугольник над номером строки для строки 1 и слева от буквы столбца A).
1. Щелкните **Ячейки** на вкладке **Формат**, щелкните вкладку **Защита**, а затем снимите отметку с **Заблокировано**.
   Это разблокирует все ячейки на листе.
   Если команда **Ячейки** недоступна, части листа могут уже быть заблокированы. На меню **Инструменты** наведите указатель на **Защита**, а затем щелкните **Снять защиту листа**.
1. Выберите только ячейки, которые вы хотите заблокировать, и повторите шаг 2, но на этот раз установите флажок **Заблокировано**.
1. На меню **Инструменты** наведите указатель на **Защита**, щелкните **Защитить лист** и затем щелкните **OK**.
1. В диалоговом окне **Защитить лист** у вас есть возможность указать пароль и выбрать элементы, которые пользователь сможет изменить.

### **Защита нескольких ячеек на листе с использованием Aspose Cells**

В этом методе мы используем только Aspose.Cells API для выполнения этой задачи.

Пример: В следующем примере показано, как защитить несколько ячеек на листе. Сначала разблокировать все ячейки на листе, а затем заблокировать 3 ячейки (A1, B1, C1). Наконец, защитить лист. Объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) содержит свойство логического типа [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Вы можете установить свойство [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) в значение true или false и применить метод *Column/Row.ApplyStyle()* для блокировки или разблокировки строки/столбца с выбранными атрибутами.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Защита строки на листе**

Aspose.Cells позволяет легко заблокировать любую строку на листе. Здесь мы можем использовать метод [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) класса [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), чтобы применить [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) к определенной строке на листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) и объект [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), содержащий все члены, связанные с применяемым форматированием.

В следующем примере показано, как защитить строку на листе. Сначала разблокировать все ячейки на листе, затем заблокировать первую строку. Наконец, защитить лист. Объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) содержит свойство логического типа [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Вы можете установить свойство [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) в значение true или false, чтобы заблокировать или разблокировать строку/столбец с использованием объекта [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Защита столбца на листе**

Aspose.Cells позволяет легко заблокировать любой столбец на листе. Здесь мы можем использовать метод [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) класса [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/), чтобы применить [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) к определенному столбцу на листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) и объект [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), содержащий все члены, связанные с применяемым форматированием.

В следующем примере показано, как защитить столбец на листе. Сначала разблокировать все ячейки на листе, затем заблокировать первый столбец. Наконец, защитить лист. Объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) содержит свойство логического типа [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Вы можете установить свойство [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) в значение true или false, чтобы заблокировать или разблокировать строку/столбец с использованием объекта [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Разрешить пользователям редактировать диапазоны**

В следующем примере показано, как разрешить пользователям редактировать диапазон в защищенном листе.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
