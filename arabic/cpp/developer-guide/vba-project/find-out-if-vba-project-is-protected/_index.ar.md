---  
title: اكتشف إذا كان مشروع VBA محميًا باستخدام C++  
linktitle: اكتشاف ما إذا كان المشروع VBA محميًا  
type: docs  
weight: 20  
url: /ar/cpp/find-out-if-vba-project-is-protected/  
description: تحقق مما إذا كان مشروع VBA لملف إكسل محميًا باستخدام Aspose.Cells مع C++.  
---  

## **اكتشف إذا ما كان مشروع VBA محميًا في C++**

يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف إكسل الخاص بك محميًا أم لا باستخدام Aspose.Cells property [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/).

## **الكود المثالي**

يقوم الرمز العملي التالي بإنشاء دفتر عمل ثم يتحقق مما إذا كان مشروع VBA محميًا أم لا. ثم يقوم بحماية مشروع VBA ويعيد التحقق مما إذا كان محميًا أم لا. يرجى مراجعة الناتج في وحدة التحكم كمرجع. قبل الحماية، يعيد [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) القيمة **خطأ** ولكن بعد الحماية، يعيد القيمة **صحيح**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
