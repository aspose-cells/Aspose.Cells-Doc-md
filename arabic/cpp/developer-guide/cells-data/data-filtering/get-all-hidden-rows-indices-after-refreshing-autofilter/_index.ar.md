---
title: احصل على جميع مؤشرات الصفوف المخفية بعد تحديث autoFilter باستخدام C++
linktitle: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة.
type: docs
weight: 320
url: /ar/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: تعلم كيفية الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث autoFilter باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية، الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية، استرداد كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية
---

## **سيناريوهات الاستخدام المحتملة**

عند تطبيق تصفية تلقائية على خلايا الورقة، يتم إخفاء بعض الصفوف تلقائيًا. ولكن قد يكون الحال أن بعض الصفوف قد تم إخفاؤها يدويًا بالفعل من قبل مستخدم اكسل ولا تكون قد تمت إخفاؤها بواسطة التصفية التلقائية. لذلك من الصعب معرفة أي من الصفوف تم إخفاؤها بواسطة التصفية التلقائية وأي منهم تم إخفاؤها يدويًا من قبل مستخدم اكسل. وتتعامل Aspose.Cells مع هذه المشكلة باستخدام الطريقة int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/). تُرجع هذه الطريقة فهارس الصفوف لكافة الصفوف التي تم إخفاؤها بواسطة التصفية التلقائية وليس يدويًا بواسطة مستخدم اكسل.

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](64716909.xlsx) الذي يحتوي على بعض الصفوف التي تم إخفاؤها يدويًا بواسطة مستخدم اكسل. يُطبق الكود تصفية تلقائية ويقوم بتحديثها باستخدام الطريقة int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) التي ترجع فهارس الصفوف المخفية بواسطة التصفية التلقائية. ثم يُطبع الفهارس للصفوف المخفية على وحدة التحكم مع أسماء الخلايا والقيم.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
