---
title: Ускорение времени вычисления метода Cell.Calculate с помощью C++
linktitle: Ускорение времени вычисления Cell.Calculate
description: Эта статья рассказывает о том, как использовать библиотеку Aspose.Cells для снижения времени вычисления методов вычисления ячейки в Microsoft Excel. Загружая существующий файл Excel или создавая новый, мы можем использовать методы, предоставленные Aspose.Cells, для оптимизации метода вычисления ячейки и улучшения его производительности. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, методы вычисления ячейки, оптимизация, производительность, снижение времени вычисления
type: docs
weight: 100
url: /ru/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Возможные сценарии использования**

Обычно мы рекомендуем пользователям вызывать метод [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) один раз и затем получать рассчитанные значения отдельных ячеек. Но иногда пользователи не хотят вычислять всю книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells предоставляет свойство [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/), которое можно установить в **false**, что значительно уменьшит время вычисления отдельных ячеек. Потому что при установленном свойстве recursive в **true**, все зависимые ячейки пересчитываются при каждом вызове. Но при значении **false** зависимые ячейки вычисляются только один раз и не пересчитываются при последующих вызовах.

## **Уменьшение времени вычисления метода Cell.Calculate()**

Следующий пример иллюстрирует использование свойства [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/). Пожалуйста, выполните этот код с указанным [образцом файла Excel](5113710.xlsx) и проверьте вывод в консоли. Вы заметите, что установка свойства recursive в **false** значительно ускоряет вычисление. Также читайте комментарии для лучшего понимания этого свойства.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Вывод в консоль**

Это вывод консоли вышеуказанного кода при выполнении его с указанным [образцом файла Excel](5113710.xlsx) на нашей машине. Обратите внимание, что ваш вывод может отличаться, но затраченное время после установки свойства recursive в **false** всегда будет меньше, чем при его установке в **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
