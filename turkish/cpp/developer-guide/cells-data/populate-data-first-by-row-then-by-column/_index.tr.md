---
title: Önce Satır, sonra Sütun şeklinde Veri Doldurun
linktitle: Verileri Önce Satır, Sonra Sütun Olarak Doldur
type: docs
weight: 1000
url: /tr/cpp/populate-data-first-by-row-then-by-column/
description: Aspose.Cells for C++ API kullanarak önce satır sonra sütun şeklinde Veri Doldurmayı öğrenin.
keywords: Verileri Önce Satır Satır Sütun Sütun Doldur, Verileri Önce Satır Satır Sütun Sütun Ekleyin, Verileri Önce Satır Satır Sütun Sütun Ekleyin, Yüksek Performanslı Veri Ekleme, Yüksek Performanslı Veri Ekleme
---

{{% alert color="primary" %}} 

Bir elektronik tabloya verileri önce satır, sonra sütun olarak doldurmak genel performansı iyileştirir.

{{% /alert %}} 

A1, B1, A2, B2 şeklinde veri yerleştirmek, A1, A2, B1, B2 şeklinde yerleştirmekten daha hızlıdır. Eğer bir çalışma sayfasında çok fazla hücre varsa ve ikinci sırayı takip ediyorsanız, yani verileri satır satır dolduruyorsanız, bu ipucu programı çok daha hızlı hale getirebilir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
