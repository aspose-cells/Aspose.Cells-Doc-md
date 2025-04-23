---
title: C++ ile Aralıktan Adres, Hücre Sayısı, Ofset, Tüm Sütun ve Tüm Satır Alın
linktitle: Aralık ın adresini, hücre sayısını, ofsetini, tüm sütunu ve tüm satırı alın
type: docs
weight: 330
url: /tr/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Aspose.Cells for C++ kullanarak bir aralığın adresini, hücre sayısını, ofsetini, tüm sütunu ve tüm satırını nasıl alacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, Excel aralıklarıyla çalışmayı kolaylaştıran çeşitli yardımcı yöntemlere sahip `Range` nesnesi sağlar. Bu makale, `Range` nesnesinin aşağıdaki yöntem veya özelliklerinin kullanımını göstermektedir:

- **Adres**

  Aralığın adresini alır.

- **Hücre Sayısı**

  Aralıktaki toplam hücre sayısını alır.

- **Ofset**

  Ofset kullanarak aralık alır.

- **Tüm Sütun**

  Belirtilen aralığı içeren tüm sütun(lar)ı temsil eden `Range` nesnesini alır.

- **Tüm Satır**

  Belirtilen aralığı içeren tüm satır(lar)ı temsil eden `Range` nesnesini alır.

## **Aralıkın Adresi, Hücre Sayısı, Ofset, Tüm Sütun ve Tüm Satırını Alın**
Yukarıda tartışılan yöntemlerin ve özelliklerin kullanımını açıklayan aşağıdaki örnek kodu inceleyin. Referans olarak aşağıdaki kodun konsol çıktısına bakabilirsiniz.

## **Örnek Kod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
