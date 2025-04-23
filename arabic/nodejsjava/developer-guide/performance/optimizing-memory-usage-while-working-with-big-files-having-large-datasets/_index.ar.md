---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 110
url: /ar/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر العمل بمجموعات بيانات كبيرة، أو قراءة ملف إكسل كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي الذي سيتم الاحتفاظ به دائمًا قلقًا. هناك إجراءات يمكن اتخاذها للتكيف مع التحدي. تقدم Aspose.Cells بعض الخيارات والمكالمات واجهة برمجة التطبيقات ذات الصلة لتقليل وخفض وتحسين استخدام الذاكرة. كما يمكن أن تساعد العملية على العمل بشكل أكثر كفاءة وتشغيل أسرع.

استخدم الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) لتحسين استخدام الذاكرة المستخدمة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن حفظ مبلغ معين من الذاكرة مقارنة باستخدام الإعداد الافتراضي [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **تحسين الذاكرة**

يوضح المثال التالي كيفية تحسين استخدام الذاكرة أثناء العمل مع مجموعات بيانات كبيرة في Aspose.Cells لـ Node.js via Java.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "optimize-memory-usage-while-working-with-large-data.js" >}}

## **احترس**

يتم تطبيق الخيار الافتراضي، [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)، لجميع الإصدارات. بالنسبة لبعض الحالات، مثل بناء دفتر عمل بمجموعة بيانات كبيرة للخلايا، قد يحسن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) استخدام الذاكرة ويقلل من التكلفة الإجمالية للذاكرة للتطبيق. ومع ذلك، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة مثل التالي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) و [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون هناك تدهور أداء ملحوظ لوضع [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) مقارنة بوضع [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).
1. **العمل على أنواع مختلفة من الخلايا**: إذا كان معظم الخلايا تحتوي على قيم سلسلة أو صيغ، فإن تكلفة الذاكرة ستكون نفسها كوضع [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا هي رقمية، بوليانية وما إلى ذلك، فإن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) سيعطي أداءً أفضل.

