---
title: كشف ما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام C++
linktitle: الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور
type: docs
weight: 360
url: /ar/cpp/detect-if-worksheet-is-password-protected/
description: تعلم كيفية الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

من الممكن حماية دفاتر العمل وورقات العمل بشكل منفصل. على سبيل المثال، قد تحتوي ورقة العمل على واحدة أو أكثر من أوراق العمل المحمية بكلمة مرور، ومع ذلك، قد يكون دفتر العمل نفسه محميًا أو لا. توفر واجهات برمجة التطبيقات Aspose.Cells الوسائل للكشف عما إذا كانت ورقة العمل معينة محمية بكلمة مرور أم لا. يوضح هذا المقال استخدام API Aspose.Cells for C++ لتحقيق نفس الشيء.

{{% /alert %}}

لقد كشف Aspose.Cells for C++ عن الخاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) لاكتشاف ما إذا كانت ورقة العمل محمية بكلمة مرور أم لا. تعيد الخاصية [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) من نوع Boolean **true** إذا كانت [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) محمية بكلمة مرور و **false** إذا لم تكن كذلك.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
