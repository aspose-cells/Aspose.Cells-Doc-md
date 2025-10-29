---
title: Отключение средства проверки совместимости в Excel с помощью C++
linktitle: Отключить средство проверки совместимости
type: docs
weight: 170
url: /ru/cpp/disable-compatibility-checker-in-excel/
description: В этой статье показано, как отключить проверку совместимости через API Aspose.Cells for C++.
keywords: Отключение проверки совместимости в C++,Excel, в C++, отключение проверки совместимости в рабочей книге. 
---

## Отключение проверки совместимости в листах Excel на C++

{{% alert color="primary" %}}

Проверка совместимости Microsoft Excel сигнализирует о том, что сохранение файла в более раннем формате файла может вызвать проблемы с функциональностью или потерей достоверности. Проверка совместимости - это функция Microsoft Office Excel 2007 и Microsoft Excel 2010.

Когда вы сохраняете книгу в предыдущей версии, Excel 97 through Excel 2003, из Excel 2007 или Excel 2010, проверка совместимости сканирует книгу, чтобы увидеть, содержит ли она функции, не поддерживаемые более ранней версией. Чтобы помочь вам с принятием решений о том, как обрабатывать проблемы совместимости, проверка совместимости отображает диалоговые окна с выбором. Ее также можно использовать для создания отчета о любых проблемах в книге или отключения функции.

Иногда вам нужно отключить проверку совместимости для конкретной электронной таблицы. С помощью API Aspose.Cells вы можете сделать это программно, чтобы пользователи не раздражались или не путались диалоговым окном проверки совместимости, появляющимся, когда они повторно сохраняют файл в Microsoft Excel вручную.

{{% /alert %}}

## **Как отключить проверку совместимости с помощью Microsoft Excel**

Для отключения проверки совместимости в Microsoft Excel (например, Microsoft Excel 2007/2010):

- (Excel 2007) На кнопке Office нажмите **Подготовка**, затем **Запустить проверку совместимости** и снимите флажок с параметра **Проверять совместимость при сохранении этой книги**.
- (Excel 2010) На вкладке **Файл** нажмите **Сведения**, затем **Проверить наличие проблем**, нажмите **Проверка совместимости**, и, наконец, снимите флажок с **Проверять совместимость при сохранении этой рабочей книги**.

## **Как отключить проверку совместимости с помощью Aspose.Cells API**

Установите свойство [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/) в **False**, чтобы отключить проверку совместимости Microsoft Excel.

### **Примеры кода**

Следующие примеры кода показывают, как отключить проверку совместимости с помощью Aspose.Cells for C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
