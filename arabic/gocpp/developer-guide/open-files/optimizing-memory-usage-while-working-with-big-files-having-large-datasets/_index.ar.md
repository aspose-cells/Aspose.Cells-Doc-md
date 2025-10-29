---
title: تحسين استهلاك الذاكرة عند العمل مع ملفات إكسل كبيرة تحتوي على مجموعات بيانات ضخمة باستخدام Golang عبر C++
linktitle: تحسين استهلاك الذاكرة
type: docs
weight: 180
url: /ar/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: تعلم كيفية تحسين استهلاك الذاكرة عند العمل مع ملفات إكسل كبيرة باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

عند بناء دفتر عمل مع مجموعات بيانات كبيرة، أو قراءة ملف Microsoft Excel كبير، يكون المبلغ الإجمالي لذاكرة الوصول العشوائي التي سيستغرقها العملية دائمًا محل اهتمام. هناك إجراءات يمكن اعتمادها للتعامل مع التحدي. يوفر Aspose.Cells بعض الخيارات القابلة للتكيف واستدعاءات واجهة برمجة التطبيقات ذات الصلة لتقليل وتقليل وتحسين استخدام الذاكرة. بالإضافة إلى ذلك، يمكن أن يساعد في جعل العملية تعمل بكفاءة أكبر وتشغيلها بصورة أسرع.

استخدام الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **كتابة ملفات إكسيل الكبيرة**

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **احترس**

الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/) يُطبق على جميع الإصدارات. لبعض الحالات، مثل بناء جدول عمل مع مجموعة بيانات كبيرة للخلايا، يمكن أن يُحسن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) استخدام الذاكرة ويُقلل من تكلفة الذاكرة للتطبيق. ومع ذلك، قد يُتدنى أداء هذا الخيار في بعض الحالات الخاصة مثلما يلي.

1. **الوصول العشوائي والمتكرر إلى الخلايا**: أكثر تسلسل فعالية للوصول إلى مجموعة الخلايا هو الخلية بالخلية في صف واحد، ثم صف بعد صف. خاصة إذا أمكنك الوصول إلى الصفوف/الخلايا من خلال المدرج المصرف من [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/)، [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) و [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)، سيتم تحقيق أقصى أداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من عمليات الإدراج/الحذف للخلايا/الصفوف، سيكون التدهور في الأداء ملحوظًا في وضع *تفضيل الذاكرة* مقارنةً بوضع *طبيعي*.
1. **العمل على أنواع الخلايا المختلفة**: إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغًا، ستكون تكلفة الذاكرة نفسها كوضع *طبيعي* ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو قيم الخلايا تكون رقمية، بولية وما إلى ذلك، فإن الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) سيمنح أداءً أفضل.
