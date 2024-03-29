---
title: محور التاريخ
description: تعرف على كيفية إدارة محور التاريخ في Aspose.Cells for Java. سيساعدك دليلنا على فهم كيفية العمل مع تنسيقات التاريخ المختلفة والمقاييس الزمنية وترددات علامات التجزئة.
keywords: Aspose.Cells for Java, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /ar/java/date-axis/
---
##  **سيناريوهات الاستخدام المحتملة**
عندما تقوم بإنشاء مخطط من بيانات ورقة العمل التي تستخدم التواريخ، ويتم رسم التواريخ على طول المحور الأفقي (الفئة) في المخطط، يقوم Aspose.cells بتغيير محور الفئة تلقائيًا إلى محور التاريخ (مقياس الوقت).
يعرض محور التاريخ التواريخ بترتيب زمني على فترات زمنية محددة أو وحدات أساسية، مثل عدد الأيام أو الأشهر أو السنوات، حتى لو لم تكن التواريخ الموجودة في ورقة العمل بترتيب تسلسلي أو في نفس الوحدات الأساسية.
افتراضيًا، يحدد Aspose.cells الوحدات الأساسية لمحور التاريخ بناءً على أصغر اختلاف بين أي تاريخين في بيانات ورقة العمل. على سبيل المثال، إذا كانت لديك بيانات لأسعار الأسهم حيث يكون أصغر فرق بين التواريخ هو سبعة أيام، فسيقوم Excel بتعيين الوحدة الأساسية إلى أيام، ولكن يمكنك تغيير الوحدة الأساسية إلى أشهر أو سنوات إذا كنت تريد الاطلاع على أداء السهم على مدى فترة أطول من الزمن.
##  **التعامل مع محور التاريخ مثل Microsoft Excel**
 الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يقوم بإنشاء ملف Excel جديد ووضع قيم المخطط في ورقة العمل الأولى.
 ثم نضيف مخططًا ونحدد نوع الملف[**محور**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
 ل[**مقياس زمني**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) ثم قم بتعيين الوحدات الأساسية إلى أيام.

![ما يجب القيام به:image_alt_text](excel.png)

 ينشئ نموذج التعليمات البرمجية التالي[إخراج ملف إكسل](DateAxis.xlsx).

##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
