---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.2.0
type: docs
weight: 70
url: /ar/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.1.2 إلى 8.2.0، التي قد تكون مهمة لمطوري الوحدات/التطبيقات. ويتضمن ليس فقط أساليب الواجهة العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الداخلي في Aspose.Cells.

{{% /alert %}} 
## **إضافة خاصية MultiThreadReading لفئة الخلايا**
مع Aspose.Cells for .NET 8.2.0، تمت إضافة الخاصية MultiThreadReading لفئة الخلايا لتوفير آلية أكثر صلابة لقراءة قيم الخلايا بمواضيع متعددة بشكل متزامن. يضمن تعيين الخاصية من النوع البولياني إلى true في التطبيق متعدد الخيوط التأكد من حصول كل خيط على قيم الخلايا الصحيحة.

{{% alert color="primary" %}} 

الرجاء التحقق من المقال المفصل عن [قراءة قيم الخلايا بشكل متزامن في بيئة متعددة الخيوط](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) لمزيد من المعلومات.

{{% /alert %}}
## **تمت إضافة نسخ جديدة لأساليب AutoFitRows وAutoFitColumns**
تمت إضافة نسخ جديدة لأساليب AutoFitRows وAutoFitColumns لفئة الورقة العمل، مما يتيح للمطورين تلقائياً تناسب الصفوف والأعمدة بناءً على نطاقاتها المعنية أثناء تمرير مثيل لفئة AutoFitterOptions. 

توقيعات الأساليب المذكورة أعلاه كما يلي:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل عن [تناسب الصفوف والأعمدة تلقائياً](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
