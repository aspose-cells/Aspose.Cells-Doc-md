---
title: تجاهل الأنماط للحصول على أداء أفضل في GridWeb
type: docs
weight: 1060
url: /ar/net/aspose-cells-gridweb/ignorestylewithnodata
description: يصف هذا المقال كيفية استخدام IgnoreStyleWithNoData للحصول على أداء أفضل في GridWeb.
keywords: GridWeb,performance
---

## **سيناريوهات الاستخدام المحتملة**
يرجى استخدام خاصية [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) لتحميل الصفوف / الأعمدة المطلوبة بشكل أقل من الدفتر.

## **احصل على أداء أفضل أثناء تحميل الدفتر**
يرجى التحقق من [ملف الإكسل عينة](largerowswithstyle.xlsx) 

عند تعيين IgnoreStyleWithNoData = true؛

كما يمكنك رؤية، فإنه يعرض الصفوف (15) والأعمدة (L)، ولن يعرض الصفوف والأعمدة المستمرة الأخيرة بدون بيانات في الخلايا، وبالتالي سيكون وقت التحميل أقل.

![دفتر بإمكانية تجاهل النمط](ignorestyletrue.png)


عند تعيين IgnoreStyleWithNoData = false؛ (القيمة الافتراضية هي false)

كما يمكنك رؤية، فإنه يعرض صفوفًا أكثر بكثير (حتى 500) وأعمدة (حتى CZ)

من الصف 16 إلى الصف 500، تم تعيين النمط الحدودي لبعض الخلايا، ومع ذلك فإن الخلايا لا تحتوي على بيانات.

من العمود M إلى العمود CZ، تم تعيين النمط الحدودي لبعض الخلايا، ومع ذلك فإن الخلايا لا تحتوي على بيانات.

![دفتر بدون إمكانية تجاهل النمط](ignorestylefalse.png)



