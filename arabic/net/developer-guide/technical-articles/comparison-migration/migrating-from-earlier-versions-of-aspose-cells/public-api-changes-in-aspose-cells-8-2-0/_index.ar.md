---
title: API العام التغييرات في Aspose.Cells 8.2.0
type: docs
weight: 70
url: /ar/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.1.2 إلى 8.2.0 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية MultiThreadReading للفئة Cells**
مع Aspose.Cells for .NET 8.2.0 ، تمت إضافة خاصية MultiThreadReading إلى الفئة Cells من أجل توفير آلية أكثر قوة لقراءة قيم الخلايا ذات الخيوط المتعددة في وقت واحد. يؤدي تعيين خاصية Boolean type إلى true في التطبيق متعدد مؤشرات الترابط إلى التأكد من أن كل مؤشر ترابط سيتلقى قيمة الخلايا الصحيحة.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[اقرأ Cells القيم في بيئة متعددة الخيوط في نفس الوقت](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) للمزيد من المعلومات.

{{% /alert %}}
## **تمت إضافة الأحمال الزائدة لطرق AutoFitRows و AutoFitColumns**
 تمت إضافة أحمال زائدة جديدة لـ AutoFitRows & AutoFitColumns إلى فئة ورقة العمل ، مما يسمح للمطورين بملاءمة الصفوف والأعمدة تلقائيًا بناءً على نطاقاتهم الخاصة أثناء تمرير مثيل لفئة AutoFitterOptions.

تواقيع الطرق المذكورة هي كما يلي:

1. AutoFitRows (int startRow، int endRow، AutoFitterOptions options)
1. AutoFitColumns (int firstColumn، int lastColumn، AutoFitterOptions options)

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[احتواء تلقائي للصفوف والأعمدة](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
