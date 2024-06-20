---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 180
url: /ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر عمل مع مجموعات بيانات كبيرة، أو قراءة ملف Microsoft Excel كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي التي سيستغرقها العملية دائمًا محل اهتمام. هناك إجراءات يمكن اعتمادها للتعامل مع التحدي. يوفر Aspose.Cells بعض الخيارات القابلة للتكيف واستدعاءات واجهة برمجة التطبيقات ذات الصلة لتقليل وتقليل وتحسين استخدام الذاكرة. بالإضافة إلى ذلك، يمكن أن يساعد في جعل العملية تعمل بكفاءة أكبر وتشغيلها بصورة أسرع.

استخدام الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **كتابة ملفات إكسيل الكبيرة**

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **احترس**

الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) يُطبق على جميع الإصدارات. لبعض الحالات، مثل بناء جدول عمل مع مجموعة بيانات كبيرة للخلايا، يمكن أن يُحسن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) استخدام الذاكرة ويُقلل من تكلفة الذاكرة للتطبيق. ومع ذلك، قد يُتدنى أداء هذا الخيار في بعض الحالات الخاصة مثلما يلي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)، [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) و [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون التدهور في الأداء ملحوظًا في وضع *تفضيل الذاكرة* مقارنةً بوضع *طبيعي*.
1. **العمل على أنواع الخلايا المختلفة**: إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغًا، ستكون تكلفة الذاكرة نفسها كوضع *طبيعي* ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا تكون رقمية، بولية وما إلى ذلك، فإن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) سيمنح أداءً أفضل.
