---
title: إعدادات المحاذاة
type: docs
weight: 20
url: /ar/java/cells-alignment-settings/
---
## **تكوين إعدادات المحاذاة**

## **إعدادات المحاذاة في Microsoft Excel**

أي شخص استخدم Microsoft Excel لتنسيق الخلايا سيكون على دراية بإعدادات المحاذاة في Microsoft Excel.

كما ترى من الشكل أعلاه ، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقيًا وعموديًا)
- المسافة الفارغة.
- توجيه.
- التحكم بالنص.
- اتجاه النص.

يتم دعم كافة إعدادات المحاذاة هذه بالكامل بواسطة Aspose.Cells وتتم مناقشتها بمزيد من التفاصيل أدناه.

## **إعدادات المحاذاة في Aspose.Cells**

 يوفر Aspose.Cells[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) و[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) طرق[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) فئة تُستخدم للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/java/com.aspose.cells/style)توفر class خصائص مفيدة لتكوين إعدادات المحاذاة.

 حدد أي نوع من أنواع محاذاة النص باستخدام امتداد[**نوع النص**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) تعداد. أنواع محاذاة النص المحددة مسبقًا في ملف[**نوع النص**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)العد هي:

|**أنواع محاذاة النص**|**وصف**|
|:- |:- |
|الأسفل|يمثل محاذاة النص السفلي|
|مركز|يمثل مركز محاذاة النص|
|CenterAcross|يمثل المركز عبر محاذاة النص|
|وزعت|يمثل محاذاة النص الموزع|
|يملأ|يمثل محاذاة النص التعبئة|
|عام|يمثل محاذاة نص عامة|
|يبرر|التمثيلات تضبط محاذاة النص|
|اليسار|يمثل محاذاة النص الأيسر|
|الصحيح|يمثل محاذاة النص الصحيحة|
|قمة|يمثل محاذاة النص العلوي|
|مبرر منخفض|يحاذي النص بطول الكشيدة المعدل للنص العربي.|
|التايلاندية الموزعة|يوزع النص التايلاندي بشكل خاص ، لأنه يتم التعامل مع كل حرف على أنه كلمة.|

{{% alert color="primary" %}}

 يمكنك أيضًا تطبيق إعداد الضبط الموزع باستخدام امتداد[**الأسلوب. يبرره ويوزع**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) منشأه.

{{% /alert %}}

## **المحاذاة الأفقية والعمودية والمسافة البادئة**

 استخدم ال[**المحاذاة الأفقية**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) لمحاذاة النص أفقيًا و[**انحياز عمودي**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)لمحاذاة النص عموديًا.
 من الممكن تعيين مستوى المسافة البادئة للنص في خلية بامتداد[**مستوى المسافة البادئة**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) منشأه
و tt فقط عندما تكون المحاذاة الأفقية لليسار أو لليمين.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **توجيه**

 عيّن اتجاه (تدوير) النص في خلية بامتداد[**زاوية الدوران**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **التحكم بالنص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص ، وتقليص حجمه للاحتواء وخيارات التنسيق الأخرى.

### **التفاف النص**

 يسهل التفاف النص في خلية القراءة: يتم ضبط ارتفاع الخلية لاحتواء النص بالكامل ، بدلاً من قطعه أو امتداده إلى الخلايا المجاورة. قم بتعيين التفاف النص أو إيقاف تشغيله بامتداد[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **تقلص لتناسب**

 يتمثل أحد خيارات التفاف النص في حقل في تقليص حجم النص ليلائم أبعاد الخلية. يتم ذلك عن طريق تحديد ملف[**يتقلص ليساوي الحجم**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) منشأه. إلى**حقيقي**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **دمج Cells**

 مثل Microsoft Excel ، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. طريقة واحدة لاستدعاء[**دمج**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) طريقة. تأخذ الطريقة المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف المراد دمجها.
- عدد الأعمدة: عدد الأعمدة المراد دمجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **اتجاه النص**

من الممكن ضبط ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب المرئي الذي يتم به عرض الأحرف والكلمات وما إلى ذلك. على سبيل المثال ، اللغة الإنجليزية هي لغة من اليسار إلى اليمين بينما اللغة العربية هي لغة من اليمين إلى اليسار.

 يتم تعيين ترتيب القراءة مع[**اتجاه النص**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) منشأه. يوفر Aspose.Cells أنواع اتجاهات النص المحددة مسبقًا في ملف[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)تعداد.

|**أنواع اتجاه النص**|**وصف**|
|:- |:- |
|سياق|ترتيب القراءة المتوافق مع لغة أول حرف تم إدخاله|
|من اليسار إلى اليمين|ترتيب القراءة من اليسار إلى اليمين|
|من اليمين الى اليسار|ترتيب القراءة من اليمين إلى اليسار|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **موضوعات مسبقة**
- [قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود](/cells/ar/java/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل الأسطر وتغليف النص](/cells/ar/java/line-breaks-and-text-wrapping/)
