---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.2.0
type: docs
weight: 80
url: /ar/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.1.2 إلى 8.2.0، التي قد تكون مهمة لمطوري الوحدات/التطبيقات. ويتضمن ليس فقط أساليب الواجهة العامة الجديدة والمحدثة، ولكن أيضًا وصفًا لأي تغييرات في السلوك الداخلي في Aspose.Cells.

{{% /alert %}} 
## **إضافة خاصية MultiThreadReading لفئة الخلايا**
مع Aspose.Cells for Java 8.2.0، تمت إضافة خاصية MultiThreadReading لفئة الخلايا من أجل توفير آلية أقوى لقراءة قيم الخلايا باستخدام خيوط متعددة بشكل متزامن. يضمن ضبط الخاصية من نوع البيان التعبيري إلى صحيح في التطبيق متعدد الخيوط أن يحصل كل خيط على قيمة الخلية الصحيحة.

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل حول [قراءة قيم الخلايا بتزامن في بيئة متعددة الخيوط](/cells/ar/java/reading-cell-values-in-multiple-threads-simultaneously/) لمزيد من المعلومات.

{{% /alert %}}
## **إضافة الإرتجافات لطرق autoFitRows و autoFitColumns**
تمت إضافة إصدارات جديدة لـ autoFitRows و autoFitColumns إلى فئة الورقة العمل، مما يسمح للمطورين بضبط تلقائي للصفوف والأعمدة بناءً على نطاقاتهم الخاصة أثناء تمرير نسخة من فئة AutoFitterOptions. 

توقيعات الأساليب المذكورة أعلاه كما يلي:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل على [تكييف الصفوف والأعمدة تلقائيًا](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
