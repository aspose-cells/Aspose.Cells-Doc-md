---
title: C++ ile Sorgu Tablo Veri Kaynağıyla Tablo Okuma ve Yazma
linktitle: Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma
type: docs
weight: 30
url: /tr/cpp/read-and-write-table-with-query-table-data-source/
description: Aspose.Cells for C++ kullanarak SorguTable ı veri kaynağı olarak kullanarak tabloları nasıl okuyup yazacağınızı öğrenin.
---

## **Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma**
Aspose.Cells ile, SorguTable'ı veri kaynağı olarak kullanan bir tabloyu okuyup yazabilirsiniz. Bu özellik XLS dosyaları için de desteklenmektedir. Aşağıdaki kod parçası, önce tabloyu okuyup toplamlar satırını ekleyerek bu tür bir tabloyu okuma ve yazmayı gösterir.

```cpp
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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Kaynak ve çıktı Excel dosyaları referans amaçlı eklenmiştir.

[Kaynak Dosya](96928091.xls)

[Çıkış Dosyası](96928092.xls)
{{< app/cells/assistant language="cpp" >}}
