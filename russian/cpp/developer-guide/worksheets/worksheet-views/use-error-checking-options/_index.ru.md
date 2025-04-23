---
title: Используйте параметры проверки ошибок с помощью C++
linktitle: Использование опций проверки ошибок
type: docs
weight: 140
url: /ru/cpp/use-error-checking-options/
description: В этой статье вы найдете пример кода, который программно использует параметры проверки ошибок листов Excel, например, números, сохранённые как текст, с помощью API или библиотеки C++.
keywords: номер магазина как текст в Excel с использованием C++, проверка ошибок в настройках Excel C++
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям определять параметры и правила проверки ошибок. Пользователи часто видят проверки ошибок при создании формул – небольшой треугольник в верхнем правом углу ячейки подствечивает, если в ячейке есть проблема. Excel предоставляет информацию, которая помогает пользователям исправить распространенные проблемы.

{{% /alert %}}

## **Типы ошибок**

Ошибки, которые означают, что формула не может вернуть результат – например, деление числа на ноль – требуют немедленного внимания, и в ячейке отображается значение ошибки. Нажав на зеленый треугольник, отображается восклицательный знак, и нажав на него, открывается список опций.

Ошибка может быть исправлена с помощью опций или проигнорирована. Игнорирование ошибки означает, что она больше не появится при последующих проверках ошибок.

Aspose.Cells предоставляет функции опций проверки ошибок. Класс [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) управляет различными типами проверок ошибок, например, числа, хранящиеся как текст, ошибки при вычислении формулы и ошибки проверки. Используйте перечисление [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/), чтобы установить желаемую проверку ошибок.

## **Числа, сохраненные как текст**

Иногда числа могут быть отформатированы и сохранены в ячейках как текст. Это может вызвать проблемы с вычислениями или привести к непонятным порядкам сортировки. Числа, отформатированные как текст, выровнены влево, а не вправо, в ячейке. Если формула, которая должна выполнить математическую операцию с ячейками, не возвращает значение, следует проверить выравнивание в ячейках, на которые ссылается формула - некоторые или все эти ячейки могут быть числами, отформатированными как текст.

Вы можете использовать опции проверки ошибок, чтобы быстро преобразовать числа, сохраненные как текст, в реальные числа. В Microsoft Excel 2003:

1. На меню **Инструменты** щелкните **Параметры**.
1. Выберите вкладку Проверка ошибок.
   Опция **Число сохранено как текст** установлена по умолчанию.
1. Отключить ее.

Приведенный ниже образец кода показывает, как отключить опцию проверки ошибок чисел, сохраненных как текст, для листа в файле-шаблоне XLS, используя API Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
