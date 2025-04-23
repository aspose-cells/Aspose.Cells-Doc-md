---
title: Найти, является ли лист диалоговым с помощью C++
linktitle: Проверить, является ли рабочий лист диалоговым листом
type: docs
weight: 90
url: /ru/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Диалоговый лист — устаревший формат листа. Эта статья содержит инструкции и пример кода для определения программным путем, является ли лист Excel Диалоговым листом, используя API C++.
keywords: найти тип листа Excel диалог C++, диалоговый лист C++
---

## **Возможные сценарии использования**

Диалоговый лист - это старый формат листа, который содержит диалоговое окно. Такой лист мог быть вставлен в старой версии Microsoft Excel, например, в 2003 году, как показано на этом скриншоте. Его также можно вставить с помощью VBA в новых версиях, например, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

 Вы можете определить, является ли лист диалоговым или другим типом листа, с помощью свойства [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/), предоставляемого Aspose.Cells. Если он возвращает значение перечисления [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/), значит, это диалоговый лист.

## **Определить, является ли рабочий лист диалоговым листом**

 Следующий шаблонный код загружает [пример файла Excel](64716820.xlsx), содержащий диалоговый лист. Он проверяет свойство [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/), сравнивает его с [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) и выводит сообщение. Для получения дополнительной информации смотрите вывод в консоль приведенного ниже примера кода.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
