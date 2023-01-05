---
title: أضف أوراق العمل
type: docs
weight: 20
url: /ar/net/add-worksheets/
---
{{% alert color="primary" %}} 

تعتبر أوراق العمل جزءًا لا يتجزأ من Aspose.Cells.GridWeb. تتم إدارة جميع البيانات وتخزينها في شكل أوراق عمل. Aspose.Cells.GridWeb يسمح للمطورين بإضافة ورقة عمل واحدة أو أكثر إلى عنصر تحكم Aspose.Cells.GridWeb. يعرض هذا الموضوع طرقًا بسيطة لإضافة أوراق عمل إلى Aspose.Cells.GridWeb.

{{% /alert %}} 
## **إضافة ورقة عمل**
### **بدون تحديد اسم الورقة**
إن أبسط طريقة لإضافة ورقة عمل إلى Aspose.Cells.GridWeb هي استدعاء طريقة Add لمجموعة GridWorksheetCollection في عنصر تحكم GridWeb. يؤدي هذا إلى إنشاء أوراق عمل تستخدم أسماء افتراضية (أي ورقة 1 ، ورقة 2 ، ورقة 3 وما إلى ذلك) وإضافتها إلى عنصر تحكم GridWeb.

**الإخراج: تمت إضافة ورقة عمل بالاسم الافتراضي إلى GridWeb** 

![ما يجب القيام به: image_بديل_نص](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 تقوم طريقة الإضافة بإرجاع فهرس ورقة العمل الجديدة الذي يمكن استخدامه للوصول إلى مثيل ورقة العمل هذه. لمزيد من التفاصيل حول كيفية الوصول إلى أوراق العمل ، اقرأ[أوراق العمل الوصول](/cells/ar/net/access-worksheets/).

{{% /alert %}} 
### **مع اسم الورقة المحدد**
لإضافة ورقة عمل باسم محدد إلى عنصر تحكم GridWeb بدلاً من استخدام نظام التسمية الافتراضي ، قم باستدعاء إصدار محمّل بشكل زائد من الأسلوب Add الذي يأخذ اسم الورقة المحدد. على سبيل المثال ، يضيف المثال أدناه ورقة عمل باسم الفاتورة.

**الإخراج: تمت إضافة ورقة عمل باسم محدد إلى GridWeb** 

![ما يجب القيام به: image_بديل_نص](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

طريقة Add التي تقبل اسم ورقة العمل كسلسلة ترجع مثيل GridWorksheet.

{{% /alert %}}
