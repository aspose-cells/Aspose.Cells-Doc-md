---
title: Excel Dosyasını AutoFill Aralığıyla Doldurun C++ ile
linktitle: Otomatik Doldurma Aralığı
type: docs
weight: 105
url: /tr/cpp/autofill-ranges/
description: İşte Aspose.Cells kullanarak belirtilen bir aralıktaki otomatik doldurma işlemini nasıl gerçekleştireceğinizi öğrenin.
---

## **Belirtilen Aralıkta Otomatik Doldurma İşlemini Gerçekleştirin**

Excel'de bir aralık seçin, fareyi sağ-alt köşeye taşıyın ve "+" işaretini sürükleyerek verileri otomatik doldurun.

## **Aspose.Cells ile Otomatik Doldurma Aralıkları**

Aşağıdaki örnek, bir Aralık üzerinde OtomDoldurma işleminin nasıl gerçekleştirileceğini gösterir. İşlevi test etmek için indirilebilecek örnek dosya burada:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
