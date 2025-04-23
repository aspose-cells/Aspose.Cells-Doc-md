---
title: C++ ile Hücre Aralığını Birleştirme veya Birleştirmeyi Kaldırma
linktitle: Hücre Aralığını Birleştirin veya Ayırın
type: docs
weight: 190
url: /tr/cpp/merge-or-unmerge-range-of-cells/
description: Excel de C++ kodu ile bir aralıktaki Hücreleri Birleştir ve Birleştirmeyi Kaldır.
keywords: c++ ile hücreleri birleştir ve ayır, c++ ile hücreleri birleştir ve ayır, c++ kullanarak aralıkta hücreleri birleştir ve ayır, c++ ile hücreleri ara ve ayır, excel de hücreleri birleştir ve ayır, c++ ile excel de hücreleri birleştir ve ayır, c++ ile excel de hücreleri birleştir, c++ ile excel de hücreleri birleştir, c++ kullanarak hücreleri birleştir, c++ kullanarak hücreleri ayır
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak hücre aralığını birleştirmek veya bölmek için [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) ve [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) yöntemlerini kullanabilirsiniz. Bu makale, bir hücre aralığını tek bir hücreye birleştirmenin nasıl gerçekleştirileceğini açıklar.

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod ilk olarak A1:D4 aralığını oluşturur, ardından [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) metodunu kullanarak aralıktaki hücreleri tek bir hücreye birleştirir. Benzer şekilde, hücreleri bölmek için bir aralık oluşturup [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) metodunu çağırabilirsiniz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
