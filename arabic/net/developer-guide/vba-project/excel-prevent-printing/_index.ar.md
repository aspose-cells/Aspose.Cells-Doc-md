---
title: كيفية منع المستخدمين من طباعة ملف Excel
type: docs
weight: 600
url: /ar/net/how-to-prevent-printing-excel/
description: تعرف على كيفية منع المستخدمين من الطباعة على برنامج Excel من خلال Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **سيناريوهات الاستخدام المحتملة**
في عملنا اليومي، قد تكون هناك بعض المعلومات المهمة في ملف Excel، وحفاظًا على البيانات الداخلية المنتشرة، لن تسمح لنا الشركة بطباعتها. سيخبرك هذا المستند بكيفية منع الآخرين من طباعة ملفات Excel.

##  **كيفية منع المستخدمين من طباعة الملفات في MS-Excel**
يمكنك تطبيق كود VBA التالي لحماية ملفك المحدد المراد طباعته.
1. افتح مصنفك الذي لا تسمح للآخرين بطباعته.
1. حدد علامة التبويب "المطور" في شريط Excel وانقر فوق الزر "عرض الرمز" في قسم "عناصر التحكم". وبدلاً من ذلك، يمكنك الضغط باستمرار على المفاتيح ALT + F11 لفتح نافذة Visual Basic for Applications Microsoft.
<br>
<img src="1.png" width=70% />
1. ثم في Project Explorer الأيسر، انقر نقرًا مزدوجًا فوق ThisWorkbook لفتح الوحدة، وأضف بعض رموز vba.
<br>
<img src="2.png" width=70% />
1. ثم احفظ هذا الرمز وأغلقه، ثم انتقل إلى الخلف في المصنف، والآن عندما تقوم بطباعة ملف العينة، لن يُسمح بطباعته وستحصل على مربع التحذير التالي:
<br>
<img src="3.png" width=70% />

##  **كيفية منع المستخدمين من طباعة ملف Excel باستخدام Aspose.Cells for .NET**

يوضح نموذج التعليمات البرمجية التالي كيفية منع المستخدمين من طباعة ملف Excel:

1.  حمل ال[ملف عينة](sample.xlsx).
1. احصل على كائن VbaModuleCollection من خاصية VbaProject الخاصة بالمصنف.
1. احصل على كائن VbaModule عبر اسم "ThisWorkbook".
1. قم بتعيين خاصية الرموز لـ VbaModule.
1.  احفظ ملف العينة في[تنسيق xlsm](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}