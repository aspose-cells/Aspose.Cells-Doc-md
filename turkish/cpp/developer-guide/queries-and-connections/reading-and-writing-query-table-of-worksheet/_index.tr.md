---
title: Çalışma Sayfasında Sorgu Tablosunu Okuma ve Yazma ile C++
linktitle: Çalışsaydı, Çalışma Sorgusu Tablosu Okuma ve Yazma
type: docs
weight: 40
url: /tr/cpp/reading-and-writing-query-table-of-worksheet/
description: Aspose.Cells kullanarak Excel çalışma sayfalarında sorgu tablolarını nasıl okuyup yazacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, `Worksheet.QueryTables` koleksiyonunu sağlar; bu, indeksle bir `QueryTable` nesnesi döndürür. İki özelliği vardır:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Bunlar her ikisi de Boolean değerlerdir. Microsoft Excel'de **Veri > Bağlantılar > Özellikler** yoluyla görebilirsiniz.

{{% /alert %}}

## Çalışsayfa Sorgu Tablosu Okuma ve Yazma

Aşağıdaki örnek kod, ilk çalışma sayfasındaki ilk `QueryTable`'ı okur ve her iki `QueryTable` özelliğini de yazdırır. Ardından `QueryTable.PreserveFormatting` değerini `true` yapar.

Bu kodda kullanılan kaynak Excel dosyasını ve kod tarafından oluşturulan çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.

- [Kaynak Excel Dosyası](5115533.xlsx)
- [Çıktı Excel Dosyası](5115537.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Konsol Çıktısı

İşte yukarıdaki örnek kodun konsol çıktısı:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Sorgu Tablosu Sonuç Aralığını Alma

Aspose.Cells, bir sorgu tablosunun adresini (yani, hücrelerin sonuç aralığını) okuma seçeneği sunar. Aşağıdaki kod, bir sorgu tablosunun sonuç aralığının adresini okuma özelliğini gösterir. Örnek dosya [buradan](72417290.xlsx) indirilebilir.

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
