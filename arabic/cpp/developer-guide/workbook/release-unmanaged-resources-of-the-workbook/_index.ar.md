---
title: تحرير موارد غير مدارة الخاص بدفتر العمل باستخدام C++
linktitle: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 310
url: /ar/cpp/release-unmanaged-resources-of-the-workbook/
description: تعلم كيف تفرج عن الموارد غير المدارة الخاصة بدفتر العمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells الأسلوب [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) لتحرير الموارد غير المُدارة لكائن [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). نمط التخلص يُستخدم فقط للكائنات التي تصل إلى الموارد غير المُدارة، مثل مقابض الملف والأنابيب، مقابض التسجيل، مقابض الانتظار أو المؤشرات إلى مجموعات من الذاكرة غير المُدارة. وذلك لأن مجمع المخلفات فعّال لاسترداد الكائنات المُدارة غير المستخدمة بشكل كبير، ولكنه غير قادر على استرداد الكائنات غير المُدارة.

{{% /alert %}}

يطبق كائن [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الآن واجهة *IDisposable* التي تحتوي على طريقة واحدة [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). يمكنك إما استدعاء طريقة [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) مباشرة أو يمكنك استخدام بيان *Using* لاستدعاء هذه الطريقة تلقائيًا.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
