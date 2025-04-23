---
title: التحقق مما إذا كان مصنف العمل يحتوي على روابط خارجية مخفية باستخدام C++
linktitle: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية
type: docs
weight: 230
url: /ar/cpp/check-if-workbook-contains-hidden-external-links/
description: تعلّم كيفية اكتشاف الروابط الخارجية المخفية في دفاتر عمل Excel باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يحتوي المصنف على روابط خارجية مخفية ولا يمكن عرضها في Microsoft Excel. يسترجع Aspose.Cells جميع الروابط الخارجية سواء كانت مرئية أو مخفية. ومع ذلك، يمكنك التحقق من الخاصية [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) للتحقق مما إذا كان الرابط الخارجي مرئيًا أم لا.

## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**
يفتح الكود النموذجي التالي ملف إكسل [المصدر](5115413.xlsx) الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الروابط في Microsoft Excel، ولكنها موجودة داخل المصنف. بعد طباعة [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) و [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/)، يتم طباعة الخاصية [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/). في مخرجات وحدة التحكم أدناه، سترى أن جميع روابطها الخارجية غير مرئية.

### **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **مخرجات الوحدة**
إليك مخرجات وحدة التحكم للكود العيني أعلاه عند تنفيذه مع [ملف Excel العيني المعطى](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
