---
title: تحسين استخدام الذاكرة أثناء العمل مع الملفات الكبيرة التي تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 180
url: /ar/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

عند إنشاء مصنف بمجموعات بيانات كبيرة ، أو قراءة ملف إكسل Microsoft كبير ، فإن الحجم الإجمالي لذاكرة الوصول العشوائي التي ستستغرقها العملية دائمًا ما يكون مصدر قلق. هناك تدابير يمكن تكييفها لمواجهة التحدي. يوفر Aspose.Cells بعض الخيارات ذات الصلة ومكالمات API لخفض وتقليل وتحسين استخدام الذاكرة. أيضًا ، يمكن أن يساعد العملية على العمل بكفاءة أكبر وتشغيل أسرع.

 استخدم ال[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) خيار لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند إنشاء مجموعة بيانات كبيرة للخلايا ، يمكنها توفير قدر معين من الذاكرة مقارنة باستخدام الإعداد الافتراضي ([**إعداد الذاكرة**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات إكسل الكبيرة**

يوضح المثال التالي كيفية قراءة ملف Excel كبير Microsoft في الوضع الأمثل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **كتابة ملفات إكسل كبيرة**

يوضح المثال التالي كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل في وضع محسن.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **حذر**

 الخيار الافتراضي ،[**إعداد الذاكرة**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)يتم تطبيقه على جميع الإصدارات. بالنسبة لبعض المواقف ، مثل إنشاء مصنف بمجموعة بيانات كبيرة للخلايا ، فإن ملف[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)الخيار قد يحسن استخدام الذاكرة ويقلل من تكلفة الذاكرة للتطبيق. ومع ذلك ، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة مثل المتابعة.

1. **يتم الدخول على Cells بشكل عشوائي ومتكرر** : التسلسل الأكثر فاعلية للوصول إلى مجموعة الخلايا هو خلية بخلية في صف واحد ، ثم صفًا بصف. على وجه الخصوص ، إذا قمت بالوصول إلى الصفوف / الخلايا التي تم الحصول عليها من Enumerator[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**مجموعة RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) و[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row) ، سيتم تعظيم الأداء مع[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **إدراج وحذف Cells الصفوف** : يرجى ملاحظة أنه إذا كان هناك الكثير من عمليات الإدراج / الحذف لـ Cells / Rows ، فسيكون تدهور الأداء ملحوظًا في*الذاكرة التفضيل* الوضع بالمقارنة مع*طبيعي*الوضع.
1. **تعمل بأنواع Cell مختلفة** : إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغ ، فستكون تكلفة الذاكرة هي نفسها*طبيعي* الوضع ولكن إذا كان هناك عدد كبير من الخلايا الفارغة ، أو إذا كانت قيم الخلايا رقمية أو منطقية وما إلى ذلك ، فإن ملف[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)سيعطي الخيار أداء أفضل.
