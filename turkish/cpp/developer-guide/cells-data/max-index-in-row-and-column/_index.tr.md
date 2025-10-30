---
title: C++ ile Satırdaki Maksimum Sütun İndeksi ve Sütundaki Maksimum Satır İndeksi Alınması
linktitle: Satırda Maksimum Sütun Endeksini ve Sütunda Maksimum Satır Endeksini Al
type: docs
weight: 600
url: /tr/cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for C++ API kullanarak satırda maksimum sütun indeksini ve sütunda maksimum satır indeksini nasıl alacağınızı öğrenin.
keywords: Satırda Maksimum Sütun İndeksini Alın, Sütunda Maksimum Satır İndeksini Alın, Satırda Maksimum Veri Sütun İndeksini Alın, Sütunda Maksimum Veri Satır İndeksini Alın.
---

## **Olası Kullanım Senaryoları**
Sadece belirli veri alanlarıyla ilgileniyorsanız ve satırlar veya sütunlar üzerinde işlem yapmak istiyorsanız, satır ve sütunların veri aralığını bilmeniz gerekir. Aspose.Cells bu özelliği sunar. Bir satırdaki maksimum sütun indeksini almak için, [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) ve [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) özelliklerini edinebilir, ardından [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) özelliğiyle maksimum sütun indeksini ve maksimum veri sütunu indeksini elde edebilirsiniz. Ancak, bir sütundaki maksimum satır indeksini ve maksimum satır veri indeksini almak için, sütunda bir aralık oluşturmanız, ardından bu aralığı dolaşıp son hücreyi bulmanız ve en sonunda hücredeki [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) özelliğini kullanmanız gerekir.

Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olmak için aşağıdaki özellikler ve yöntemleri sağlar.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Aspose.Cells Kullanarak Satırda Maksimum Sütun İndeksini ve Sütunda Maksimum Satır İndeksini Alın**
Bu örnek aşağıdakileri göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Maksimum sütun dizinini ve maksimum veri sütun dizinini elde etmek için satırı alın.
1. Hücre üzerindeki [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) özniteliğini alın.
1. Sütuna dayalı bir aralık oluşturun.
1. İteratörü alın ve aralığı gezin.
1. Hücre üzerindeki [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) özniteliğini alın.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
