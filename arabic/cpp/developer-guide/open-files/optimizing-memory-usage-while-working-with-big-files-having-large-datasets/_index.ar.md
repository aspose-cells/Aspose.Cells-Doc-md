---
title: تحسين استهلاك الذاكرة عند العمل مع ملفات كبيرة تحتوي على مجموعات بيانات ضخمة باستخدام C++
linktitle: تحسين استهلاك الذاكرة
type: docs
weight: 180
url: /ar/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: تعلم كيفية تحسين استخدام الذاكرة عند العمل مع ملفات Excel كبيرة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

عند بناء دفتر عمل مع مجموعات بيانات كبيرة، أو قراءة ملف Microsoft Excel كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي التي سيستغرقها العملية دائمًا محل اهتمام. هناك إجراءات يمكن اعتمادها للتعامل مع التحدي. يوفر Aspose.Cells بعض الخيارات القابلة للتكيف واستدعاءات واجهة برمجة التطبيقات ذات الصلة لتقليل وتقليل وتحسين استخدام الذاكرة. بالإضافة إلى ذلك، يمكن أن يساعد في جعل العملية تعمل بكفاءة أكبر وتشغيلها بصورة أسرع.

استخدام الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كتابة ملفات إكسيل الكبيرة**

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **احترس**

الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) يُطبق على جميع الإصدارات. لبعض الحالات، مثل بناء جدول عمل مع مجموعة بيانات كبيرة للخلايا، يمكن أن يُحسن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) استخدام الذاكرة ويُقلل من تكلفة الذاكرة للتطبيق. ومع ذلك، قد يُتدنى أداء هذا الخيار في بعض الحالات الخاصة مثلما يلي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)، [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) و [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون التدهور في الأداء ملحوظًا في وضع *تفضيل الذاكرة* مقارنةً بوضع *طبيعي*.
1. **العمل على أنواع الخلايا المختلفة**: إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغًا، ستكون تكلفة الذاكرة نفسها كوضع *طبيعي* ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا تكون رقمية، بولية وما إلى ذلك، فإن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) سيمنح أداءً أفضل.
