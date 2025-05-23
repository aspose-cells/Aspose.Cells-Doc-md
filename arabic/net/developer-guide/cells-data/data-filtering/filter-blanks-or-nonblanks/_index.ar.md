---
title: كيفية تصفية الخانات الفارغة أو غير الفارغة
type: docs
weight: 85
url: /ar/net/how-to-filter-blanks-and-non-blanks/
description: تعلم كيفية تصفية الخانات الفارغة وغير الفارغة باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
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
إذا كان العمود يحتوي على نصوص بحيث تكون بعض الخلايا فارغة، ويتطلب التصفية تحديد تلك الصفوف فقط التي تحتوي على الخلايا الفارغة، يمكن استخدام الدوال [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) و [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) كما هو موضح أدناه. 

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](sample.xlsx) الذي يحتوي على بيانات وهمية. يستخدم الكود النموذجي ثلاثة أساليب لتصفية الخانات الفارغة. ثم يقوم بحفظ الدفتر كملف اكسل [ملف الانتاج](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **كيفية تصفية الخلايا الغير فارغة باستخدام Aspose.Cells**

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](sample.xlsx) الذي يحتوي على بيانات وهمية. بعد تحميل الملف، استدعِ الدالة [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) لتصفية البيانات غير الفارغة، وأخيرًا حفظ الدفتر كملف اكسل [ملف الانتاج](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

{{< app/cells/assistant language="csharp" >}}
