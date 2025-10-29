---
title: Использование функции FormulaText в Aspose.Cells с C++
linktitle: Использование функции FormulaText
description: В этой статье рассматривается, как использовать функцию FormulaText в библиотеке Aspose.Cells для обработки формул в Microsoft Excel. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать метод, предоставленный Aspose.Cells, для получения и установки текста формулы ячейки и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, функции FormulaText
type: docs
weight: 60
url: /ru/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

Функция FormulaText является функцией Excel 2013 и новее. Она не поддерживается в предыдущих версиях, таких как Excel 2010 или 2007 и т. д. Как следует из названия, она печатает текст формулы, которая присутствует в заданной ячейке. В этой статье мы покажем вам, как использовать эту функцию с помощью Aspose.Cells.

{{% /alert %}} 

В следующем примере показано использование функции FormulaText с Aspose.Cells. В этом коде сначала записывается формула в ячейку A1, а затем печатается текст формулы с помощью FormulaText в ячейке A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
