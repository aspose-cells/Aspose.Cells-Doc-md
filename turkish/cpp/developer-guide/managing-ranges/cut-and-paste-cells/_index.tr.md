---
title: C++ ile Kes ve Yapıştır Aralık
linktitle: Aralığı Kırparak ve Yapıştırarak
type: docs
weight: 130
url: /tr/cpp/cut-and-paste-cells/
description: Aspose.Cells for C++ kullanarak çalışma sayfası içinde hücreleri nasıl kesip yapıştıracağınızı öğrenin.
---

## **Hücreleri Kırp ve Yapıştır**

Aspose.Cells, [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) metodunu ve [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonunu kullanarak çalışma sayfasındaki hücreleri kesip yapıştırma yeteneği sağlar. [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) metodu aşağıdaki parametreleri kabul eder.

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): Kesilecek hücrelerin aralığı.
- Satır Dizini: Hücreleri eklemek için satırın dizini.
- Sütun Dizini: Hücreleri eklemek için sütunun dizini.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): Sütunların kaydırma yönü.

Aşağıdaki örnek, çalışma sayfası üzerinde hücreleri kesip yapıştırmayı gösterir.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
