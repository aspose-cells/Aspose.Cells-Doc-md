---
title: إضافة ورقات العمل
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: يقدم هذا المقال كيفية إضافة ورقة عمل (GridWorksheet) في GridWeb.
---

{{% alert color="primary" %}} 

تعتبر ورقات العمل جزءًا أساسيًا من Aspose.Cells.GridWeb. يتم إدارة وتخزين جميع البيانات في شكل ورقات عمل. يسمح Aspose.Cells.GridWeb للمطورين بإضافة ورقة عمل أو أكثر إلى عنصر تحكم Aspose.Cells.GridWeb. يوضح هذا الموضوع الطرق البسيطة لإضافة ورقات عمل إلى Aspose.Cells.GridWeb.

{{% /alert %}} 
## **إضافة ورقة عمل**
### **دون تحديد اسم الورقة**
أبسط طريقة لإضافة ورقة عمل إلى Aspose.Cells.GridWeb هي استدعاء طريقة الإضافة في مجموعة GridWorksheetCollection في عنصر تحكم GridWeb. يؤدي ذلك إلى إنشاء ورقات عمل تستخدم أسماء افتراضية (مثل Sheet1، Sheet2، Sheet3 وهلم جرا) وإضافتها إلى عنصر تحكم GridWeb.

**النتيجة: تمت إضافة ورقة عمل بالاسم الافتراضي إلى GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

تُعيد طريقة الإضافة فهرس الورقة العمل الجديدة الذي يمكن استخدامه للوصول إلى نسخة من هذه الورقة العمل. لمزيد من التفاصيل حول كيفية الوصول إلى الورقات العمل، اقرأ [الوصول إلى الورقات العمل](/cells/ar/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **بتحديد اسم الورقة**
لإضافة ورقة عمل باسم محدد إلى عنصر تحكم GridWeb بدلاً من استخدام مخطط الأسماء الافتراضي، استدعِ الإصدار المعتمد من الوسيطة الإضافية التي تأخذ اسم SheetName المحدد. على سبيل المثال، يضيف المثال أدناه ورقة عمل تحت اسم Invoice.

**النتيجة: تمت إضافة ورقة عمل بالاسم المحدد إلى GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

تقبل طريقة الإضافة اسم الورقة العمل بشكل نصي وتُعيد نسخة من GridWorksheet.

{{% /alert %}}
