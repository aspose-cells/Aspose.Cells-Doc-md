﻿---
title: API العام التغييرات في Aspose.Cells 8.2.1
type: docs
weight: 80
url: /ar/net/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.2.0 إلى 8.2.1 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة طريقة GetValidation () للفئة Cell**
يعد التحقق من صحة البيانات إحدى الميزات التي يستخدمها مصممو جداول البيانات لمنع المستخدمين من إدخال قيم غير صالحة في خلية معينة. مع Aspose.Cells for .NET 8.2.1 ، كشف API آلية بسيطة تحدد ما إذا تم تطبيق التحقق من صحة البيانات على خلية. استخدم أسلوب GetValidation للفئة Cell للحصول على أي تحقق مطبق. إذا لم يكن هناك تحقق ، فإن الطريقة ترجع فارغة. وبالمثل ، يمكنك استخدام أسلوب GetValidationInCell لفئة ValidationCollection للحصول على التحقق المطبق على أي خلية من خلال توفير فهارس الصفوف والأعمدة الخاصة بها.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[احصل على تطبيق التحقق من الصحة على Cell](/cells/ar/net/get-validation-applied-on-a-cell/) للمزيد من المعلومات.

{{% /alert %}}
## **تمت إضافة طريقة GetValidationValue () لفئة Cell**
بالإضافة إلى تحديد ما إذا تم تطبيق التحقق من الصحة ، يمكنك أيضًا التحقق مما إذا كانت قيمة معينة تفي بقواعد التحقق من صحة البيانات لخلية معينة. هذه الميزة مفيدة في السيناريوهات عندما تريد التحقق مما إذا كانت القيمة التي تم إدخالها في الخلية تفي بقواعد التحقق من صحة البيانات أثناء التنقل. كشفت Aspose.Cells API طريقة GetValidationValue للفئة Cell. إذا كانت القيمة التي تم إدخالها في خلية لا تفي بقواعد التحقق من صحة البيانات ، تقوم طريقة GetValidationValue للفئة Cell بإرجاع خطأ.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[تحقق من أن Cell القيمة تلبي قواعد التحقق من صحة البيانات](/cells/ar/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **تمت إضافة طريقة التحميل الزائد ToPrinter (إعدادات الطابعة PrinterSettings) لفئة WorkbookRender**
يمكنك استخدام طريقة التحميل الزائد لتقديم المصنف إلى الطابعة عبر إعدادات الطابعة.
