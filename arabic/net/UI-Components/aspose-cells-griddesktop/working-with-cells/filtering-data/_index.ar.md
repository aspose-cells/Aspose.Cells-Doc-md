---
title: تصفية البيانات
type: docs
weight: 100
url: /ar/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,filter,filter data,AutoFilter,RowFilterr
description: يقدم هذا المقال كيفية تصفية البيانات في ورقة العمل في GridDesktop.
---

{{% alert color="primary" %}} 

يوفر Aspose.Cells.GridDesktop ميزات تصفية التلقائي وتصفية البيانات المخصصة للمستخدمين. باستخدام هذه الميزات، يمكنك أن تجد وسيلة لتحديد العناصر فقط من ورقة العمل التي ترغب في عرضها في قائمة. علاوة على ذلك، يُسمح لك بتصفية العناصر في القائمة وفقًا لمعايير محددة. يمكنك تصفية النصوص والأرقام أو التواريخ باستخدام ميزة التصفية التلقائية / تصفية البيانات المخصصة.

يمكنك استخدام سمة **EnableAutoFilter** من فئة **RowFilterSettings** لتمكين ميزة التصفية التلقائية لتحكم GridDesktop. توجد بعض الخصائص الأخرى للفئة التي يمكنك استخدامها، على سبيل المثال **HeaderRow**، **StartRow** و **EndRow** لتحديد رأس الصف وبداية ونهاية فهرس الصف. تُستخدم الخاصية **Criteria** لتعيين المعايير التصفية المخصصة. الفئة تحتوي أيضًا على طريقة تسمى **FilterRows** للحصول على الصفوف المصفاة بناءً على المعايير المعطاة.

يدعم GridDesktop أيضًا سمة البحث من نوع "contains" (غير الحساسة لحالة الأحرف) في RowFilter. يمكنك استخدام خاصية **IgnoreCase** لفئة **GridColumn** لتحديد سمة حساسية الحالة حسب احتياجك. يمكنك أيضًا استخدام خاصية تُسمى **IsStartWithCriteria** لفئة **GridColumn** للإشارة ما إذا كان يستخدم RowFilter معيار StartWith على عمود؛ تم تعيين القيمة الافتراضية للخاصية إلى false.

{{% /alert %}} 
## **تصفية البيانات**
نقوم بتطبيق كل من ميزتي التصفية التلقائية وتصفية البيانات المخصصة في هذا المثال. نقوم بملء بعض قائمة البيانات في GridDesktop، وتمكين ميزة التصفية التلقائية، ثم البحث في الصفوف المصفاة بناءً على بعض المعايير.
### **تصفية تلقائية**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **تصفية البيانات المخصصة**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
