---
title: إعدادات المحاذاة
type: docs
weight: 20
url: /ar/java/cells-alignment-settings/
---

## **ضبط إعدادات المحاذاة**

## **إعدادات المحاذاة في Microsoft Excel**

أي شخص قد استخدم Microsoft Excel لتنسيق الخلايا سيكون متعودًا على إعدادات المحاذاة في Microsoft Excel.

كما يمكنك رؤية من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقية وعمودية)
- المسافة البادئة.
- التوجيه.
- التحكم بالنص.
- اتجاه النص.

كل إعدادات المحاذاة هذه مدعومة تمامًا بواسطة Aspose.Cells ويتم مناقشتها بمزيد من التفصيل أدناه.

## **إعدادات المحاذاة في Aspose.Cells**

توفر Aspose.Cells الأساليب [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) و [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) لفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) والتي تُستخدم للحصول على تنسيق الخلية وتعيينه. توفر الفئة [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) خصائص مفيدة لتكوين إعدادات المحاذاة.

حدد أي نوع لمحاذاة النص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). أنواع محاذاة النص المحددة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) هي:

|** أنواع محاذاة النص **|** الوصف **|
| :- | :- |
|Bottom|يمثل محاذاة النص السفلي
|Center|يمثل محاذاة النص الوسطية
|CenterAcross|تمثل محاذاة النص في وسط النص|
|Distributed|تمثل توزيع محاذاة النص|
|Fill|تمثل ملء محاذاة النص|
|General|تمثل محاذاة النص العامة|
|Justify|تمثل محاذاة النص التبريري|
|Left|يمثل محاذاة النص اليسار|
|Right|يمثل محاذاة النص اليمين|
|Top|يمثل محاذاة النص العلوي|
|JustifiedLow|يُحاذي النص بطول كاشيدا معدل للنص العربي.|
|ThaiDistributed|يوزع النص التايلاندي خصوصًا، لأن كل حرف يُعامل ككلمة.|

{{% alert color="primary" %}}

يمكنك أيضا تطبيق ضبط التوزيع المبرر باستخدام الخاصية [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed).

{{% /alert %}}

## **المحاذاة الأفقية والرأسية والمسافة البادئة**

استخدم الخاصية [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) لمحاذاة النص أفقيًا والخاصية [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) لمحاذاة النص عموديًا.
من الممكن تعيين مستوى البادئة للنص في الخلية باستخدام الخاصية [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) 
ويؤثر ذلك فقط عندما تكون المحاذاة الأفقية يمينًا أو يسارًا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **الاتجاه**

قم بتعيين الاتجاه (الدوران) للنص في خلية باستخدام الخاصية [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

### **تفاف النص**

تجعل التفاف النص في خلية أمر قراءته أسهل: يتكيف ارتفاع الخلية ليتناسب مع كل النص بدلاً من قطعه أو تسربه إلى الخلايا المجاورة. قم بتعيين تفاف النص على أو قبالة باستخدام الخاصية [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **تقليص للتناسب**

خيار لتفاف النص في الحقل هو تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك عن طريق تعيين الخاصية [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit). إلى **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **دمج الخلايا**

مثل Microsoft Excel، تدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. توفر Aspose.Cells طريقتين لهذه المهمة. الطريقة الأولى هي استدعاء الطريقة [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-). تأخذ الطريقة المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يتم تحديد ترتيب القراءة بواسطة خاصية [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). يوفر Aspose.Cells أنواع توجيه النص المحددة مسبقًا في تعداد [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/java/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/java/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="java" >}}
