---
title: محور التاريخ
description: تعلم كيفية إدارة محور التاريخ في Aspose.Cells for .NET. سيساعدك دليلنا على فهم كيفية العمل مع تنسيقات التاريخ المختلفة ومقاييس الوقت وتردد تسميات العلامات.
keywords: Aspose.Cells for .NET، محور التاريخ، إدارة، تنسيقات التاريخ، مقاييس الوقت، تردد تسميات العلامات.
type: docs
weight: 200
url: /ar/net/date-axis/
---

## **سيناريوهات الاستخدام المحتملة**
عند إنشاء رسم بياني من بيانات ورقة العمل التي تستخدم تواريخ، ويتم رسم التواريخ على طول المحور الأفقي (الفئة) في الرسم البياني، يقوم Aspose.cells تلقائيًا بتغيير المحور الفئة إلى محور تاريخ (مقياس زمني).
يعرض محور التاريخ التواريخ وفقًا للترتيب الزمني بفواصل زمنية محددة أو وحدات قاعدية، مثل عدد الأيام، أو الأشهر، أو السنوات، حتى إذا كانت التواريخ على ورقة العمل ليست بترتيب تسلسلي أو بنفس الوحدات القاعدية.
بشكل افتراضي، يحدد Aspose.cells وحدات الأساس لمحور التاريخ بناءً على أصغر فرق بين أي تاريخين في بيانات ورقة العمل. على سبيل المثال، إذا كانت لديك بيانات لأسعار الأسهم حيث أصغر فرق بين التواريخ هو سبعة أيام، فإن Excel يضبط الوحدة الأساسية على الأيام، ولكن يمكنك تغيير الوحدة الأساسية إلى أشهر أو سنوات إذا كنت ترغب في رؤية أداء السهم على مدى فترة زمنية أطول.
## **معاملة محور التاريخ مثل Microsoft Excel**
يرجى الاطلاع على الكود النموذجي التالي الذي ينشئ ملف إكسل جديد ويضع قيم الرسم البياني في الورقة العمل الأولى. 
ثم نضيف رسم بياني ونعين نوع الـ [**Axis**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
إلى [**TimeScale**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) ومن ثم نضبط الوحدات الأساسية على الأيام.

![todo:image_alt_text](excel.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
{{< app/cells/assistant language="csharp" >}}
