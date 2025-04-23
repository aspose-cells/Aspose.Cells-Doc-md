---
title: Вычисление формул с помощью C++
linktitle: Расчет формул
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для вычисления формул в Microsoft Excel с помощью C++. Загружая существующий файл Excel или создавая новый, вы можете использовать предоставленные Aspose.Cells методы для вычисления формулы и получения результата. В конце сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, формулы, вычисления, Прямой расчет формул, Повторный расчет формул, добавление формул.
type: docs
weight: 125
url: /ru/cpp/calculate-formulas/
---

## **Добавление формул и вычисление результатов**

У Aspose.Cells встроен движок вычисления формул. Он может не только пересчитывать импортированные из шаблонов Excel формулы, но и поддерживает вычисление результатов добавленных формул в режиме выполнения.

Aspose.Cells поддерживает большинство формул или функций, входящих в Microsoft Excel (читать [список поддерживаемых функций движка вычислений](/cells/ru/cpp/supported-formula-functions/)). Эти функции можно использовать через API или при создании диаграмм. Aspose.Cells поддерживает обширный набор математических, строковых, булевых, дат/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) или методы [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) для добавления формулы в ячейку. При применении формулы всегда начинайте строку с знака равенства (=), как при создании формулы в Microsoft Excel, и используйте запятую (,) для разделения параметров функции.

Для вычисления результатов формул пользователь может вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который обрабатывает все встроенные формулы в файле Excel. Или вызвать метод [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) класса [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), который обрабатывает формулы на листе. Также можно вызвать метод [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), который обрабатывает формулу отдельной ячейки:

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Важно знать о формулах**

{{% alert color="primary" %}}

Свойство **GetFormula** и методы **SetFormula(...)** класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) работают иначе, чем методы **Calculate** классов [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) и [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Свойство **GetFormula** и методы **SetFormula(...)** просто добавляют формулу в ячейку, но не вычисляют результат во время выполнения. Чтобы получить результат формул, вызовите методы **Calculate**.

{{% /alert %}}

## **Прямое вычисление формулы**

Aspose.Cells имеет встроенный механизм расчета формул. Кроме того, в Aspose.Cells можно вычислять результаты формул непосредственно, импортированных из файла дизайнера.

Иногда нужно вычислить результаты формул напрямую, не добавляя их в лист. Значения ячеек, используемых в формуле, уже существуют в листе, и все, что нужно — это найти результат этих значений на основе формулы Microsoft Excel без добавления самой формулы в лист.

Можно использовать API движка вычислений формул Aspose.Cells для [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) для получения результатов таких формул без добавления их в лист:

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
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Приведенный выше код производит следующий вывод:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Как повторно вычислять формулы**

Когда в рабочей книге много формул и пользователь должен вычислять их повторно с небольшими изменениями, может быть полезно для производительности включить цепочку вычислений формул: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Важно знать**

{{% alert color="primary" %}}

По умолчанию цепочка вычислений отключена. Создание цепочки также требует дополнительного времени, поэтому при первом вычислении формул ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) может потребоваться больше процессорного времени и памяти по сравнению с вычислением формул без цепочки. Если пользователю не нужно повторно вычислять формулы, лучше оставить поведение по умолчанию (вычисление формулы напрямую без создания цепочки вычислений).

{{% /alert %}}

## **Дополнительные темы**
- [Добавление ячеек в окно наблюдения формул Microsoft Excel](/cells/ru/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Вычисление функции IFNA с помощью Aspose.Cells](/cells/ru/cpp/calculating-ifna-function-using-aspose-cells/)
- [Расчет массивной формулы таблиц данных](/cells/ru/cpp/calculation-of-array-formula-of-data-tables/)
- [Расчет функций MINIFS и MAXIFS Excel 2016](/cells/ru/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Уменьшение времени расчета метода Cell.Calculate](/cells/ru/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Реализация пользовательского расчетного механизма для расширения расчетного механизма по умолчанию Aspose.Cells](/cells/ru/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Возвращение диапазона значений с использованием абстрактного расчетного механизма](/cells/ru/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Установка режима расчета формул книги](/cells/ru/cpp/setting-formula-calculation-mode-of-workbook/)
- [Использование функции FormulaText в Aspose.Cells](/cells/ru/cpp/using-formulatext-function-in-aspose-cells/)
