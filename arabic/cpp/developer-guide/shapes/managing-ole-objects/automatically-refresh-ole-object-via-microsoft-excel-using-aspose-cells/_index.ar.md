---
title: تحديث تلقائي لكائن OLE عبر Microsoft Excel باستخدام ++C
linktitle: تحديث تلقائي لكائن OLE
type: docs
weight: 270
url: /ar/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: تعلم كيف تقوم بتحديث كائنات OLE تلقائيًا في Microsoft Excel باستخدام Aspose.Cells مع ++C.
---

{{% alert color="primary" %}}

توفر Aspose.Cells الخاصية [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) لتحديث كائن OLE عند فتح ملف إكسل في Microsoft Excel. بفضل هذه الخاصية، ستعرض صورة OLE الصحيحة التي أنشأها Microsoft Excel.

{{% /alert %}}

الكود النموذجي التالي يحمل [ملف إكسل النموذجي](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. في الواقع، كائن OLE هو مستند Microsoft Word، لكن ملف إكسل النموذجي يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ومع ذلك، إذا فتحت ملف إكسل الناتج ([5115225.xlsx](#))، ستلاحظ أن Microsoft Excel يعرض صورة OLE الصحيحة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
