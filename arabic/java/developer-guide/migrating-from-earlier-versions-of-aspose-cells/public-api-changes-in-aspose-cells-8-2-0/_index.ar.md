---
title: API العام التغييرات في Aspose.Cells 8.2.0
type: docs
weight: 80
url: /ar/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.1.2 إلى 8.2.0 ، والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة خاصية MultiThreadReading للفئة Cells**
مع Aspose.Cells for Java 8.2.0 ، تمت إضافة خاصية MultiThreadReading إلى الفئة Cells من أجل توفير آلية أكثر قوة لقراءة قيم الخلايا ذات الخيوط المتعددة في وقت واحد. يؤدي تعيين خاصية Boolean type إلى true في التطبيق متعدد مؤشرات الترابط إلى التأكد من أن كل مؤشر ترابط سيتلقى قيمة الخلايا الصحيحة.

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[اقرأ Cells القيم في بيئة متعددة الخيوط في نفس الوقت](/cells/ar/java/reading-cell-values-in-multiple-threads-simultaneously/) للمزيد من المعلومات.

{{% /alert %}}
## **تمت إضافة الأحمال الزائدة لطرق autoFitRows و autoFitColumns**
 تمت إضافة أحمال زائدة جديدة لـ autoFitRows & autoFitColumns إلى فئة ورقة العمل ، مما يسمح للمطورين بملاءمة الصفوف والأعمدة تلقائيًا بناءً على نطاقاتهم الخاصة أثناء تمرير مثيل لفئة AutoFitterOptions.

تواقيع الطرق المذكورة هي كما يلي:

1. autoFitRows (int startRow، int endRow، AutoFitterOptions options)
1. autoFitColumns (int firstColumn ، int lastColumn ، خيارات AutoFitterOptions)

{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[احتواء تلقائي للصفوف والأعمدة](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
