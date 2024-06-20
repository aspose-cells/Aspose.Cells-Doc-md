---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 110
url: /ar/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر العمل بمجموعات بيانات كبيرة، أو قراءة ملف إكسل كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي الذي سيتم الاحتفاظ به دائمًا قلقًا. هناك إجراءات يمكن اتخاذها للتكيف مع التحدي. تقدم Aspose.Cells بعض الخيارات والمكالمات واجهة برمجة التطبيقات ذات الصلة لتقليل وخفض وتحسين استخدام الذاكرة. كما يمكن أن تساعد العملية على العمل بشكل أكثر كفاءة وتشغيل أسرع.

استخدم الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) لتحسين استخدام الذاكرة المستخدمة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن حفظ مبلغ معين من الذاكرة مقارنة باستخدام الإعداد الافتراضي [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **كتابة ملفات إكسيل الكبيرة**

توضح المثال التالي كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **احترس**

يتم تطبيق الخيار الافتراضي، [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)، لجميع الإصدارات. بالنسبة لبعض الحالات، مثل بناء دفتر عمل بمجموعة بيانات كبيرة للخلايا، قد يحسن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) استخدام الذاكرة ويقلل من التكلفة الإجمالية للذاكرة للتطبيق. ومع ذلك، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة مثل التالي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) و [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون هناك تدهور أداء ملحوظ لوضع [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) مقارنة بوضع [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).
1. **العمل على أنواع مختلفة من الخلايا**: إذا كان معظم الخلايا تحتوي على قيم سلسلة أو صيغ، فإن تكلفة الذاكرة ستكون نفسها كوضع [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا هي رقمية، بوليانية وما إلى ذلك، فإن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) سيعطي أداءً أفضل.
