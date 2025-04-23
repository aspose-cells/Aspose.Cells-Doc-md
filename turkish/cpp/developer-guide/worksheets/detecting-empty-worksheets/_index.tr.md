---
title: Boş çalışma sayfalarını tespit etme C++ ile
linktitle: Boş Çalışsayfası Bulma
type: docs
weight: 410
url: /tr/cpp/detecting-empty-worksheets/
description: Bu makale, Aspose.Cells kütüphanesiyle C++ API kullanarak Excel çalışma kitaplarındaki boş çalışma sayfalarını programlı olarak nasıl tespit edeceğinizi gösterir.
keywords: Boş çalışma sayfasını tespit etme C++, boş Excel çalışma sayfasını bulma C++ ile
---

## **Doldurulmuş Hücreleri Kontrol Etme**

Çalışma sayfaları, değerlerle doldurulmuş bir veya daha fazla hücreye sahip olabilir; bu değerler basit (metin, sayısal, tarih/zaman) veya formül ya da formüle dayalı olabilir. Bu durumda, belirli bir çalışma sayfasının boş olup olmadığını kolayca tespit edebilirsiniz. Kontrol etmemiz gereken tek şey [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) veya [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) özellikleridir. Yukarıda belirtilen özellikler sıfır veya pozitif değer döndürüyorsa, bir veya daha fazla hücre doldurulmuştur. Ancak, herhangi biri -1 döndürürse, bu, belirtilen çalışma sayfasında hiç hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}}

Satır ve sütun koleksiyonlarının sıfır tabanlı indeksleri vardır, bu nedenle satır 0 ve sütun 0'deki bir hücre, çalışma sayfasındaki ilk hücreyi, yani A1'i temsil eder.

{{% /alert %}}

## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**

Değerleri olan tüm hücreler otomatik olarak başlatılır. Ancak, bir çalışma sayfasında yalnızca biçimlendirme uygulanmış hücreler olabilir. Bu durumda, [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) veya [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) özellikleri -1 döndürür, bu da herhangi bir doldurulmuş değer olmadığını gösterir. Ancak, hücre biçimlendirmesi nedeniyle başlatılmış hücreler bu yöntemle tespit edilemez. Bir çalışma sayfasında boş başlatılmış hücrelerin olup olmadığını kontrol etmek için, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonundan alınan sayıcı üzerinde `MoveNext` yönteminin kullanılması önerilir. Eğer `MoveNext` **true** dönerse, bu, belirtilen çalışma sayfasında bir veya daha fazla başlatılmış hücre olduğunu gösterir.

## **Şekilleri Kontrol Etme**

Belirli bir çalışma sayfasında herhangi bir şekil, nesne, kontrol, grafik, resim vb. bulunup bulunmadığını kontrol edebilirsiniz; örneğin, şemaların veya şekillerin olup olmadığını [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/) özelliğine bakarak anlayabilirsiniz. Pozitif değer, çalışma sayfasında şekil olduğunu gösterir.

## **Programlama Örneği**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
