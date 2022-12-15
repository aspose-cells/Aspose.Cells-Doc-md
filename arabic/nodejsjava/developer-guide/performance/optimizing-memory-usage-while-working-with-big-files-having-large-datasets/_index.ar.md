---
title: تحسين استخدام الذاكرة أثناء العمل مع الملفات الكبيرة التي تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 110
url: /ar/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

عند إنشاء مصنف بمجموعات بيانات كبيرة ، أو قراءة ملف إكسل Microsoft كبير ، فإن الحجم الإجمالي لذاكرة الوصول العشوائي التي ستستغرقها العملية دائمًا ما يكون مصدر قلق. هناك تدابير يمكن تكييفها لمواجهة التحدي. يوفر Aspose.Cells بعض الخيارات ذات الصلة ومكالمات API لخفض وتقليل وتحسين استخدام الذاكرة. أيضًا ، يمكن أن يساعد العملية على العمل بكفاءة أكبر وتشغيل أسرع.

 يستخدم[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) خيار لتحسين الذاكرة المستخدمة لبيانات الخلايا لتقليل التكلفة الإجمالية للذاكرة. عند إنشاء مجموعة بيانات كبيرة للخلايا ، يمكن أن يوفر قدرًا معينًا من الذاكرة مقارنة باستخدام الإعداد الافتراضي[**إعداد الذاكرة**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **تحسين الذاكرة**

يوضح المثال التالي كيفية تحسين استخدام الذاكرة أثناء العمل مع البيانات الكبيرة في Aspose.Cells for Node.js via Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **حذر**

 الخيار الافتراضي ،[**إعداد الذاكرة**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)يتم تطبيقه على جميع الإصدارات. بالنسبة لبعض المواقف ، مثل إنشاء مصنف بمجموعة بيانات كبيرة للخلايا ، فإن ملف[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)الخيار قد يحسن استخدام الذاكرة ويقلل من تكلفة الذاكرة للتطبيق. ومع ذلك ، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة مثل المتابعة.

1. **يتم الدخول على Cells بشكل عشوائي ومتكرر** : التسلسل الأكثر فاعلية للوصول إلى مجموعة الخلايا هو خلية بخلية في صف واحد ، ثم صفًا بصف. على وجه الخصوص ، إذا قمت بالوصول إلى الصفوف / الخلايا التي تم الحصول عليها من Enumerator[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**مجموعة RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) و[**صف**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) ، سيتم تعظيم الأداء مع[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **إدراج وحذف Cells الصفوف** : يرجى ملاحظة أنه إذا كان هناك الكثير من عمليات الإدراج / الحذف لـ Cells / Rows ، فسيكون تدهور الأداء ملحوظًا في[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) الوضع بالمقارنة مع[**إعداد الذاكرة**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)الوضع.
1. **تعمل بأنواع Cell مختلفة** : إذا كانت معظم الخلايا تحتوي على قيم سلسلة أو صيغ ، فستكون تكلفة الذاكرة هي نفسها[**إعداد الذاكرة**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)الوضع ولكن إذا كان هناك عدد كبير من الخلايا الفارغة ، أو إذا كانت قيم الخلايا رقمية أو منطقية وما إلى ذلك ، فإن ملف[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)سيعطي الخيار أداء أفضل.

