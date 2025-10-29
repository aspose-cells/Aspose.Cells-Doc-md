---
title: كيفية التصفية للفراغات أو غير الفراغات باستخدام C++
linktitle: كيفية تصفية الخانات الفارغة أو غير الفارغة
type: docs
weight: 85
url: /ar/cpp/how-to-filter-blanks-and-non-blanks/
description: تعلم كيفية تصفية الفراغات وغير الفراغات باستخدام API رقم Aspose.Cells for C++.
keywords: تصفية الخانات الفارغة، تصفية الخانات غير الفارغة، تصفية الخانات الفارغة في ورق العمل، تصفية الخانات غير الفارغة في ورق العمل، تصفية الخانات الفارغة في إكسل، تصفية الخانات غير الفارغة في إكسل، تصفية الخانات الفارغة وغير الفارغة في إكسل
---

## **سيناريوهات الاستخدام المحتملة**
تصفية البيانات في إكسل هي أداة قيمة تعزز تحليل البيانات واستكشافها وعرضها عن طريق تمكين المستخدمين من التركيز على مجموعات محددة من البيانات استنادًا إلى معاييرهم، مما يجعل عملية تلاعب البيانات الشاملة وعملية التفسير أكثر كفاءة وفعالية.

## **كيفية تصفية الخانات الفارغة أو غير الفارغة في إكسل**
في إكسل، يمكنك بسهولة تصفية الخانات الفارغة أو غير الفارغة باستخدام خيارات التصفية. إليك كيف يمكنك القيام بذلك:

### **كيفية تصفية الخانات الفارغة في إكسل**
1. تحديد النطاق: انقر على حرف رأس العمود لتحديد العمود بأكمله أو حدد النطاق الذي تريد تصفية الخانات الفارغة فيه.
1. فتح قائمة التصفية: انتقل إلى علامة "البيانات" في شريط الأدوات.
<br>
<image src="1.png" width="70%" />
1. خيارات التصفية: انقر على زر "تصفية". سيتم إضافة أسهم تصفية إلى النطاق المحدد.
1. تصفية الخانات الفارغة: انقر على سهم التصفية في العمود الذي تريد تصفية الخانات الفارغة فيه. قم بإلغاء تحديد جميع الخيارات باستثناء "فارغة" وانقر على موافق. ستقوم هذه الخطوة بعرض الخانات الفارغة فقط في ذلك العمود.
<br>
<image src="2.png" width="70%" />
1. النتيجة كما يلي:
<br>
<image src="3.png" width="70%" />

### **كيفية تصفية الخلايا الغير فارغة في اكسل**
1. حدد النطاق: انقر على حرف رأس العمود لتحديد العمود بأكمله أو حدد النطاق الذي ترغب في تصفية الخلايا الغير فارغة فيه.
1. فتح قائمة التصفية: انتقل إلى علامة "البيانات" في شريط الأدوات.
<br>
<image src="1.png" width="70%" />
1. خيارات التصفية: انقر على زر "تصفية". سيتم إضافة أسهم تصفية إلى النطاق المحدد.
1. تصفية الخلايا الغير فارغة: انقر على سهم التصفية في العمود الذي ترغب في تصفية الخلايا الغير فارغة فيه. قم بإلغاء تحديد جميع الخيارات ما عدا "الغير فارغة" أو "مخصص" وقم بتعيين الشروط وفقًا لذلك. انقر على موافق. سيتم عرض الخلايا المحتوية على قيم في تلك العمود فقط.
<br>
<image src="4.png" width="70%" />
1. النتيجة كما يلي:
<br>
<image src="5.png" width="70%" />

## **كيفية تصفية الخلايا الفارغة باستخدام Aspose.Cells**
إذا كانت العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة، ويتطلب التصفية لاختيار تلك الصفوف فقط حيث توجد خلايا فارغة، يمكن استخدام دالتي [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) و [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) كما هو موضح أدناه. 

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](sample.xlsx) الذي يحتوي على بيانات وهمية. يستخدم الكود النموذجي ثلاثة أساليب لتصفية الخانات الفارغة. ثم يقوم بحفظ الدفتر كملف اكسل [ملف الانتاج](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **كيفية تصفية الخلايا الغير فارغة باستخدام Aspose.Cells**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف إكسل العينة](sample.xlsx) والذي يحتوي على بعض البيانات الوهمية. بعد تحميل الملف، استدعي دالة [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) لتصفية البيانات غير الفارغة، وأخيرًا احفظ المصنف كـ [ملف إكسل الناتج](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


{{< app/cells/assistant language="cpp" >}}
