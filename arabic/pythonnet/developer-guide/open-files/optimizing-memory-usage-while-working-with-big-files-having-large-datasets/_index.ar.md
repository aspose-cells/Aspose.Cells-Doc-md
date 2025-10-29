---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 180
url: /ar/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر عمل بمجموعات بيانات كبيرة، أو قراءة ملف إكسل كبير، فإن مقدار الـRAM الذي ستحتاجه العملية دائمًا ما يكون مصدر قلق. هناك تدابير يمكن تكييفها لمواجهة التحدي. يوفر Aspose.Cells لـ Python via .NET بعض الخيارات ذات الصلة ونداءات API لتقليل، تقليل وتحسين استخدام الذاكرة. كما يمكنه مساعدة العملية على العمل بكفاءة أكبر وتشغيلها بشكل أسرع.

استخدام الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **كتابة ملفات إكسيل الكبيرة**

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **احترس**

الخيار الافتراضي، [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) يُطبق على جميع الإصدارات. لبعض الحالات، مثل بناء جدول عمل مع مجموعة بيانات كبيرة للخلايا، يمكن أن يُحسن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) استخدام الذاكرة ويُقلل من تكلفة الذاكرة للتطبيق. ومع ذلك، قد يُتدنى أداء هذا الخيار في بعض الحالات الخاصة مثلما يلي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)، [**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection) و [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون التدهور في الأداء ملحوظًا في وضع *تفضيل الذاكرة* مقارنةً بوضع *طبيعي*.
1. **العمل على أنواع الخلايا المختلفة**: إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغًا، ستكون تكلفة الذاكرة نفسها كوضع *طبيعي* ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا تكون رقمية، بولية وما إلى ذلك، فإن الخيار [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) سيمنح أداءً أفضل.

{{< app/cells/assistant language="python-net" >}}
