---
title: العثور على الحد الأقصى للصفوف والأعمدة المدعومة بواسطة تنسيقات XLS و XLSX باستخدام C++
linktitle: العثور على الحد الأقصى للصفوف والأعمدة
type: docs
weight: 20
url: /ar/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: تعلم كيفية العثور على الحد الأقصى للصفوف والأعمدة المدعومة بواسطة تنسيقات XLS و XLSX باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

هناك أعداد مختلفة من الصفوف والأعمدة المدعومة بواسطة تنسيقات Excel. على سبيل المثال، تدعم XLS 65536 صفًا و 256 عمودًا، بينما تدعم XLSX 1048576 صفًا و 16384 عمودًا. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين، يمكنك استخدام الخصائص [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) و [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**

يخلق المثال التالي ملف عمل أولاً بصيغة XLS ثم بصيغة XLSX. بعد الإنشاء، يطبع قيم خصائص [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) و [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). يرجى مراجعة مخرجات وحدة التحكم الخاصة بالكود أدناه للمرجعية.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
