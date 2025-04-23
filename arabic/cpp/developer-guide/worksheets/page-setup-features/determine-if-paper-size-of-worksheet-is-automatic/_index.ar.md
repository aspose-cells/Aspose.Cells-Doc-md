---
title: تحديد ما إذا كان حجم ورقة العمل تلقائياً باستخدام C++
linktitle: تحديد ما إذا كان حجم الورق للورقة التفاعلي
type: docs
weight: 90
url: /ar/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: توضح هذه المقالة كيفية استخدام كود عينة من واجهة برمجة التطبيقات أو المكتبة لـ C++ لتحديد ما إذا كان حجم الورق للورقة العمل تلقائيًا.
keywords: تحديد ما إذا كان حجم ورق الورقة تلقائيًا باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

في الغالب، يكون حجم ورق الورقة تلقائيًا. عندما يكون تلقائيًا، غالبًا ما يتم تحديده كـ *Letter*. أحيانًا يحدد المستخدم حجم ورق الورقة حسب متطلباته. في هذه الحالة، لا يكون حجم الورق تلقائيًا. يمكنك معرفة ما إذا كان حجم ورق الورقة تلقائيًا أم لا باستخدام خاصية [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) من فئة **Worksheet**.

## **تحديد ما إذا كان حجم الورق للورقة تلقائي**

الشيفرة العينية المعطاة أدناه تحمل الملفات الإكسل التاليتين

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ويبحث عن ما إذا كان حجم ورق أول ورقة عمل تلقائيًا أم لا. في Microsoft Excel، يمكنك التحقق من ذلك عبر نافذة إعداد الصفحة كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

هذا هو إخراج وحدة التحكم للشيفرة العينية أعلاه عند تنفيذها مع ملفات Excel العينية المعطاة.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
