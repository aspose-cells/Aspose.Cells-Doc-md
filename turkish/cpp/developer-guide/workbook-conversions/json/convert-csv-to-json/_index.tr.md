---
title: CSV yi C++ ile JSON a dönüştür
linktitle: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/cpp/convert-csv-to-json/
description: Basit kullanımlı Aspose.Cells for C++ API sini kullanarak CSV dosyasını JSON a dönüştürün.
keywords: Dönüştür, CSV yi JSON a Dönüştür, CSV to JSON, CSV, JSON, CSV yi JSON a Dönüştür C++, C++ kodu CSV yi JSON a dönüştürmek için
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'yi JSON'a dönüştürmeyi destekler. Bunun için API [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) sınıfı, JSON'e dışa aktarım için aralık seçenekleri sunar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) sınıfının aşağıdaki özellikleri vardır.

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/): Girintiyi gösterir.

[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıfı, JSON'u [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) sınıfıyla belirlenen dışa aktarma seçeneklerini kullanarak dışa aktarır.

Aşağıdaki kod örneği, [kaynak CSV dosyasını](104398879.csv) yüklemek için [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını kullanmayı ve JSON çıkışını konsolda yazdırmayı göstermektedir.

### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options for CSV format
    LoadOptions loadOptions(LoadFormat::Csv);

    // Load CSV file
    Workbook workbook(srcDir + u"SampleCsv.csv", loadOptions);

    // Get the last cell in the worksheet
    Cell lastCell = workbook.GetWorksheets().Get(0).GetCells().GetLastCell();

    // Set JsonSaveOptions
    JsonSaveOptions jsonSaveOptions;

    // Create a range from the first cell to the last cell
    Range range = workbook.GetWorksheets().Get(0).GetCells().CreateRange(0, 0, lastCell.GetRow() + 1, lastCell.GetColumn() + 1);

    // Export the range to JSON
    U16String data = JsonUtility::ExportRangeToJson(range, jsonSaveOptions);

    // Print JSON
    std::cout << data.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsol Çıktısı**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
