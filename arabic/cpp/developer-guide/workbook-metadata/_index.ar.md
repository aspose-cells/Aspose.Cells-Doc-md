---
title: استخدام WorkbookMetadata مع C++
linktitle: بيانات السجل الحصري
type: docs
weight: 320
url: /ar/cpp/using-workbookmetadata/
description: تعلم كيفية استخدام WorkbookMetadata لتحرير خصائص المستند المخصصة لملف العمل باستخدام C++ مع Aspose.Cells.
---

{{% alert color="primary" %}}

يتيح لك Aspose.Cells تحميل نسخة خفيفة من ملف العمل إلى الذاكرة لتحرير معلومات البيانات الوصفية الخاصة به. يرجى استخدام فئة [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) لتحميل ملف العمل.

{{% /alert %}}

يستخدم المثال التالي للفئة [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/) لتحرير خصائص المستند المخصصة لملف العمل. بمجرد فتح ملف العمل باستخدام فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، ستتمكن من قراءة خصائص المستند. إليك مثال على الكود باستخدام فئة [**WorkbookMetadata**](https://reference.aspose.com/cells/cpp/aspose.cells.metadata/workbookmetadata/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Metadata;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    MetadataOptions options(MetadataType::Document_Properties);
    WorkbookMetadata meta(srcDir + u"Sample1.xlsx", options);

    meta.GetCustomDocumentProperties().Add(u"test", u"test");

    meta.Save(srcDir + u"Sample2.out.xlsx");

    Workbook w(srcDir + u"Sample2.out.xlsx");

    std::cout << w.GetCustomDocumentProperties().Get(u"test").ToString().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```
