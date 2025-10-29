---
title: تحويل CSV إلى JSON باستخدام C++
linktitle: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/cpp/convert-csv-to-json/
description: تحويل ملف CSV إلى JSON باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++ سهلة الاستخدام.
keywords: تحويل، تحويل CSV إلى JSON، CSV إلى JSON، CSV، JSON، تحويل CSV إلى JSON C++، كود C++ لتحويل CSV إلى JSON
---

## **تحويل CSV إلى JSON**

يدعم Aspose.Cells تحويل CSV إلى JSON. لهذا، توفر API الفئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). توفر فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) الخيارات لتصدير النطاق إلى JSON. تحتوي فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) على الخصائص التالية.

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/): يشير إلى ما إذا كان النطاق يحتوي على صف رأس.
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/): يشير إلى المسافة البادئة.

تقوم فئة [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) بتصدير JSON باستخدام خيارات التصدير المحددة بواسطة فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

يوضح المثال البرمجي التالي استخدام فئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) لتحميل ملف CSV المصدر (104398879.csv) وطباعة إخراج JSON في وحدة التحكم.

### **الكود المثالي**

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

### **مخرجات الوحدة**
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
