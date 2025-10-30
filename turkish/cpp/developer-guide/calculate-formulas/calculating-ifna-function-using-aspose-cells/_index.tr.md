---
title: Aspose.Cells kullanılarak C++ ile IFNA fonksiyonunun hesaplanması
linktitle: IFNA fonksiyonunun hesaplanması
description: Aspose.Cells kütüphanesi kullanarak C++ ile IFNA fonksiyonlarını nasıl hesaplayacağınızı anlatır. Var olan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan metodları kullanarak IFNA fonksiyonunu hesaplayabilir ve sonucu alabilirsiniz. Son olarak, değiştirilen Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, IFNA fonksiyonları, hesaplamalar, C++
type: docs
weight: 40
url: /tr/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, IFNA Excel işlevinin hesaplanmasını destekler. IFNA işlevi, formülün #N/A hata değeri döndürmesi durumunda belirttiğiniz değeri döndürür; aksi takdirde formülün sonucunu döndürür.

{{% /alert %}} 

## **Aspose.Cells ile IFNA işlevinin hesaplanması**
Yukarıdaki örnek kod, Aspose.Cells tarafından IFNA işlevinin hesaplanmasını göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
