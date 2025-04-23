---
title: 用C++减少单元格Calculate方法的计算时间
linktitle: 减少单元格计算时间
description: 本文介绍如何使用Aspose.Cells库来减少Microsoft Excel中单元格计算方法的计算时间。 通过加载现有的Excel文件或创建一个新文件，我们可以使用Aspose.Cells提供的方法来优化单元格计算方法并提高其性能。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 单元格计算方法, 优化, 性能, 减少计算时间
type: docs
weight: 100
url: /zh/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **可能的使用场景**

通常，我们建议用户调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)方法一次，然后获取单个单元格的计算值。但有时候，用户并不想计算整个工作簿，只想计算单个单元格。Aspose.Cells提供了[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)属性，你可以将其设为**false**，这样可以显著减少单个单元格的计算时间。因为当递归属性设为**true**时，所有依赖单元格都会在每次调用时重新计算；当为**false**时，只会计算一次依赖单元格，之后不会重新计算。

## **减少Cell.Calculate()方法的计算时间**

以下示例代码演示了[**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/)属性的用法。请用给定的[示例Excel文件](5113710.xlsx)执行此代码，并查看控制台输出。你会发现，将递归属性设置为**false**会显著降低计算时间。请同时阅读注释，更好理解此属性。

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

## **控制台输出**

这是在我们机器上用给定的[示例Excel文件](5113710.xlsx)执行上述示例代码后的控制台输出。请注意，你的输出可能不同，但将递归属性设为**false**后的耗时总是比设为**true**少。

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
