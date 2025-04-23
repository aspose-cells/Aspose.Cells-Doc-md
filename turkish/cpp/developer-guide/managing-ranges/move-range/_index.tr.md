---
title: C++ ile Worksheet te Hücre Aralığını Taşıma
linktitle: Çalışma Sayfasında Hücre Aralığını Taşıma
type: docs
weight: 370
url: /tr/cpp/move-range-of-cells-in-a-worksheet/
description: Aspose.Cells kullanarak C++ ile çalışma sayfasında hücre aralığını nasıl hareket ettireceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bu makale, bir çalışma sayfasında hücrelerin bir aralığını nasıl taşıyacağını gösterir.

{{% /alert %}}

## **Çalışma Sayfasında Hücre Aralığını Taşıma**
Örnek kod, görevi göstermek için bir şablon dosyası kullanır.

**Giriş dosyası**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Lütfen A1:B5 aralığındaki hücreleri C1:D5'e taşıyan oluşturulan dosyayı inceleyin.

**Çıkış dosyası**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
