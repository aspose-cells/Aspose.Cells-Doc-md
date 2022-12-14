---
title: إعدادات المحاذاة
type: docs
weight: 20
url: /ar/net/cells-alignment-settings/
---
## **تكوين إعدادات المحاذاة**

### **إعدادات المحاذاة في Microsoft Excel**

أي شخص استخدم Microsoft Excel لتنسيق الخلايا سيكون على دراية بإعدادات المحاذاة في Microsoft Excel.

كما ترى من الشكل أعلاه ، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقيًا وعموديًا)
- المسافة الفارغة.
- توجيه.
- التحكم بالنص.
- اتجاه النص.

يتم دعم كافة إعدادات المحاذاة هذه بالكامل بواسطة Aspose.Cells وتتم مناقشتها بمزيد من التفاصيل أدناه.

### **إعدادات المحاذاة في Aspose.Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) طرق[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فئة تُستخدم للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر class خصائص مفيدة لتكوين إعدادات المحاذاة.

 حدد أي نوع من أنواع محاذاة النص باستخدام امتداد[**نوع النص**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) تعداد. أنواع محاذاة النص المحددة مسبقًا في ملف[**نوع النص**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)العد هي:

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

 يمكنك أيضًا تطبيق إعداد الضبط الموزع باستخدام امتداد[**الأسلوب. يبرره ويوزع**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) منشأه.

{{% /alert %}}

#### **المحاذاة الأفقية**

 استخدم ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**المحاذاة الأفقية**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)لمحاذاة النص أفقيًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **انحياز عمودي**

 على غرار المحاذاة الأفقية ، استخدم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**انحياز عمودي**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)لمحاذاة النص عموديًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **المسافة الفارغة**

 من الممكن تعيين مستوى المسافة البادئة للنص في خلية بامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**مستوى المسافة البادئة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **توجيه**

 عيّن اتجاه (تدوير) النص في خلية بامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**زاوية الدوران**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **التحكم بالنص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص ، وتقليص حجمه للاحتواء وخيارات التنسيق الأخرى.

##### **التفاف النص**

 يسهل التفاف النص في خلية القراءة: يتم ضبط ارتفاع الخلية لاحتواء النص بالكامل ، بدلاً من قطعه أو امتداده إلى الخلايا المجاورة. قم بتعيين التفاف النص أو إيقاف تشغيله بامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **تقلص لتناسب**

 يتمثل أحد خيارات التفاف النص في حقل في تقليص حجم النص ليلائم أبعاد الخلية. يتم ذلك عن طريق تحديد ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) الملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **دمج Cells**

 مثل Microsoft Excel ، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. طريقة واحدة لاستدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) طريقة. ال[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)تأخذ الطريقة المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف المراد دمجها.
- عدد الأعمدة: عدد الأعمدة المراد دمجها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 الطريقة الأخرى هي استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) طريقة لإنشاء نطاق من الخلايا المراد دمجها. ال[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) الطريقة التي تمت مناقشتها أعلاه وإرجاع أ[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) هدف. ال[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) يوفر الكائن أيضًا ملف[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) الأسلوب الذي يدمج النطاق المحدد في[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range)هدف.

##### **اتجاه النص**

من الممكن ضبط ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب المرئي الذي يتم به عرض الأحرف والكلمات وما إلى ذلك. على سبيل المثال ، اللغة الإنجليزية هي لغة من اليسار إلى اليمين بينما اللغة العربية هي لغة من اليمين إلى اليسار.

 يتم تعيين ترتيب القراءة مع[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**اتجاه النص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) منشأه. يوفر Aspose.Cells أنواع اتجاهات النص المحددة مسبقًا في ملف[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)تعداد.

|**أنواع اتجاه النص**|**وصف**|
|:- |:- |
|سياق|ترتيب القراءة المتوافق مع لغة أول حرف تم إدخاله|
|من اليسار إلى اليمين|ترتيب القراءة من اليسار إلى اليمين|
|من اليمين الى اليسار|ترتيب القراءة من اليمين إلى اليسار|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **موضوعات مسبقة**
- [قم بتغيير Cells المحاذاة والاحتفاظ بالتنسيق الموجود](/cells/ar/net/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل الأسطر وتغليف النص](/cells/ar/net/line-breaks-and-text-wrapping/)

