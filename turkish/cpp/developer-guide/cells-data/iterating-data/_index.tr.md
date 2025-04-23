---
title: Enumeratörleri C++ ile nerede ve nasıl kullanılır?
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/cpp/how-and-where-to-use-enumerators/
description: Aspose.Cells for C++ API kullanarak Tuna ve Nereye Enumeratörleri kullanmayı öğrenin.
keywords: Numaralandırıcıları Nasıl Kullanılır, Hücreler Numaralandırıcı, Satırlar Numaralandırıcı, Sütunlar Numaralandırıcı
---

{{% alert color="primary" %}}

Bir enumerator, bir kapsayıcı veya koleksiyon üzerinde gezinme yeteneği sağlayan bir nesnedir. Enumeratörler, koleksiyondaki veriyi okumak için kullanılabilir, ancak temel koleksiyonu değiştirmek için kullanılamazlar, oysa IEnumerable, bir GetEnumerator yöntemi tanımlayan arayüzdür ve bu da koleksiyona yalnızca okunabilir erişim sağlar.

Aspose.Cells API'ları bir dizi numaralandırıcı sağlar, ancak bu makale genellikle aşağıda listelenen üç türü tartışmaktadır.

1. Hücreler Numaralandırıcı
1. Satırlar Numaralandırıcı
1. Sütunlar Numaralandırıcı

{{% /alert %}}

## **Numaralandırıcıları Nasıl Kullanılır**

### **Hücreler Numaralandırıcı**

Hücreler Numaralandırıcısına erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. İşte hücreler numaralandırıcısını döndüren yöntemler.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücre koleksiyonunu gezinmeyi sağlayan numaralandırıcıyı döndürür.

{{% alert color="primary" %}}

Hücreleri gezinirken koleksiyon değiştirilmemelidir (bir hücreyi yeni bir şekilde oluşturan işlemler veya var olan bir hücreyi sildiren işlemler). Aksi takdirde, numaralandırıcı tüm hücreleri doğru bir şekilde gezinemeyebilir (bazı öğeler tekrarlanabilir veya atlanabilir).

{{% /alert %}}

Aşağıdaki kod örneği, Hücreler koleksiyonu için IEnumerator arabirimi uygulamasını göstermektedir.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Satırlar Numaralandırıcı**

Rows Enumeratörü, [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) için IEnumerator arayüzünün uygulanmasını gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Sütunlar Al**

Sütunlar, [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/) için Get yönteminin uygulanmasını gösterir.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Numaralandırıcıları Nerede Kullanılacağı**

Numaralandırıcıları kullanmanın avantajlarını tartışmak için, gerçek bir zaman örneği ele alalım.

**Senaryo**

Bir uygulamanın gereksinimlerinden biri, belirli bir [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) içindeki tüm hücreleri gezinerek değerlerini okumaktır. Bu amacı gerçekleştirmek için birkaç yöntem gösterilmiştir.

### **Görüntü Aralığı Kullanarak**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **MaxDataRow & MaxDataColumn Kullanarak**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıda bahsedilen her iki yaklaşımın da, tüm hücreleri döngü içinde dolaşarak hücre değerlerini okuma mantığına daha veya daha az benzer olduğunu gözlemleyebilirsiniz. Bu, aşağıda tartışılan birçok nedenden biri olabilir.

1. [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) ve [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) gibi API'ler, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satırlar x sütunlar) büyükse, bu API'leri kullanmak performans düşüşüne neden olabilir.
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.
1. Hücreye döngü içinde Cells satır, sütun olarak erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olabilir, bu da sonunda OutOfMemoryException'a neden olabilir.

## **Sonuç**

Yukarıda belirtilen gerçeklere dayanarak, aşağıdakiler, numaralandırıcıların kullanılması gereken olası senaryolarıdır.

1. Yalnızca hücre koleksiyonunun salt okunur erişimi gereklidir, yani; gereksinim yalnızca hücreleri incelemektir.
1. Birçok hücrenin dolaşılması gereklidir.
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar dolaşılmalıdır.
