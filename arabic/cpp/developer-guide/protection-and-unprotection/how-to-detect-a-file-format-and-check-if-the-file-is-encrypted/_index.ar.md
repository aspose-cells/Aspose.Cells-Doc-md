---
title: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا باستخدام C++
linktitle: كيفية اكتشاف تنسيق الملف والتحقق مما إذا كان الملف مشفرًا
type: docs
weight: 2700
url: /ar/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: تعلّم كيفية اكتشاف تنسيق ملف والتحقق مما إذا كان مشفرًا باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى اكتشاف تنسيق الملف قبل فتحه لأن امتداد الملف لا يضمن أن محتوى الملف مناسب. قد يكون الملف مشفرًا (ملف محمي بكلمة مرور) لذلك، لا يمكن قراءته مباشرة، أو لا ينبغي قراءته. يوفر Aspose.Cells الطريقة الثابتة [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/detectfileformat/) وبعض واجهات برمجة التطبيقات ذات الصلة التي يمكنك استخدامها لمعالجة المستندات.

{{% /alert %}}

الرمز البريدي العيني التالي يوضح كيفية اكتشاف تنسيق الملف (باستخدام مسار الملف) والتحقق من امتداده. يمكنك أيضًا تحديد ما إذا كان الملف مشفرًا.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Detect file format
    FileFormatInfo info = FileFormatUtil::DetectFileFormat(srcDir + u"Book1.xlsx");

    // Gets the detected load format
    std::cout << "The spreadsheet format is: " << FileFormatUtil::LoadFormatToExtension(info.GetLoadFormat()).ToUtf8() << std::endl;

    // Check if the file is encrypted
    std::cout << "The file is encrypted: " << (info.IsEncrypted() ? "true" : "false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
