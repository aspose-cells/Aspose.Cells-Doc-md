---
title: إعدادات المحاذاة
description: في مكتبة Aspose.Cells، يمكنك استخدام إعدادات محاذاة الخلية لضبط تخطيط النص وعرضه. من خلال ضبط الإعدادات مثل المحاذاة الأفقية والمحاذاة الرأسية والتفاف النص، لديك المزيد من التحكم في كيفية تدفق النص في الخلايا. سيزودك هذا المستند بخطوات تفصيلية ونموذج للتعليمات البرمجية لمساعدتك على فهم كيفية استخدام Aspose.Cells بسرعة لإعدادات محاذاة الخلية.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /ar/net/cells-alignment-settings/
---
##  **تكوين إعدادات المحاذاة**

###  **إعدادات المحاذاة في Microsoft إكسل**

أي شخص استخدم Microsoft Excel لتنسيق الخلايا سيكون على دراية بإعدادات المحاذاة في Microsoft Excel.

كما ترون من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقي وعمودي)
- المسافة الفارغة.
- توجيه.
- التحكم بالنص.
- اتجاه النص.

جميع إعدادات المحاذاة هذه مدعومة بالكامل بواسطة Aspose.Cells وستتم مناقشتها بمزيد من التفاصيل أدناه.

###  **إعدادات المحاذاة في Aspose.Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، الذي يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 Aspose.Cells يوفر[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) طرق ل[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فئة يتم استخدامها للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر الفئة خصائص مفيدة لتكوين إعدادات المحاذاة.

 حدد أي نوع محاذاة النص باستخدام[**نوع محاذاة النص**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) تعداد. أنواع محاذاة النص المحددة مسبقًا في[**نوع محاذاة النص**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)التعداد هي:

|**أنواع محاذاة النص**|**وصف**|
| :- | :- |
|قاع|يمثل محاذاة النص السفلي|
|مركز|يمثل محاذاة النص المركزي|
|CenterAcross|يمثل المركز عبر محاذاة النص|
|وزعت|يمثل محاذاة النص الموزعة|
|يملأ|يمثل محاذاة نص التعبئة|
|عام|يمثل محاذاة النص العامة|
|يبرر|يمثل تبرير محاذاة النص|
|غادر|يمثل محاذاة النص الأيسر|
|يمين|يمثل محاذاة النص الصحيح|
|قمة|يمثل محاذاة النص العلوي|
|مبرر منخفض|محاذاة النص بطول الكشيدة المعدل للنص العربي.|
|التايلاندية الموزعة|يوزع النص التايلاندي بشكل خاص، لأنه يتم التعامل مع كل حرف على أنه كلمة.|

{{% alert color="primary" %}}

 يمكنك أيضًا تطبيق إعداد الضبط الموزع باستخدام[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) ملكية.

{{% /alert %}}

####  **المحاذاة الأفقية**

 استخدم ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**المحاذاة الأفقية**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)خاصية محاذاة النص أفقيا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **انحياز عمودي**

 على غرار المحاذاة الأفقية، استخدم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**انحياز عمودي**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)خاصية محاذاة النص عموديا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **المسافة الفارغة**

 من الممكن ضبط مستوى المسافة البادئة للنص في الخلية باستخدام الامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**مستوى المسافة البادئة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **توجيه**

 قم بتعيين اتجاه (تدوير) النص في الخلية باستخدام الامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**زاوية الدوران**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **التحكم بالنص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص والتقليص ليناسب وخيارات التنسيق الأخرى.

#####  **التفاف النص**

 يؤدي التفاف النص في خلية إلى تسهيل القراءة: حيث يتم ضبط ارتفاع الخلية ليناسب النص بأكمله، بدلاً من قطعه أو امتداده إلى الخلايا المجاورة. قم بتعيين التفاف النص أو إيقاف تشغيله باستخدام[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **تقلص لتناسب**

 أحد خيارات التفاف النص في الحقل هو تقليص حجم النص ليناسب أبعاد الخلية. ويتم ذلك عن طريق تعيين[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)الخاصية إلى *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **دمج Cells**

 مثل Microsoft Excel، Aspose.Cells يدعم دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. إحدى الطرق هي الاتصال بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) طريقة. ال[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)تأخذ الطريقة المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث يبدأ الدمج.
- العمود الأول: العمود الأول من حيث يبدأ الدمج.
- عدد الصفوف: عدد الصفوف المراد دمجها.
- عدد الأعمدة: عدد الأعمدة المراد دمجها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

الطريقة الأخرى هي الاتصال أولاً بـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) المجموعة[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) طريقة لإنشاء نطاق من الخلايا المراد دمجها. ال[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) الطريقة التي تمت مناقشتها أعلاه وإرجاع أ[**يتراوح**](https://reference.aspose.com/cells/net/aspose.cells/range) هدف. ال[**يتراوح**](https://reference.aspose.com/cells/net/aspose.cells/range) يوفر الكائن أيضًا[**دمج**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) الطريقة التي تدمج النطاق المحدد في[**يتراوح**](https://reference.aspose.com/cells/net/aspose.cells/range)هدف.

#####  **اتجاه النص**

من الممكن ضبط ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب المرئي الذي يتم به عرض الأحرف والكلمات وما إلى ذلك. على سبيل المثال، اللغة الإنجليزية هي لغة من اليسار إلى اليمين بينما اللغة العربية هي لغة من اليمين إلى اليسار.

 يتم ضبط ترتيب القراءة باستخدام[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**اتجاه النص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) ملكية. يوفر Aspose.Cells أنواع اتجاه النص المحددة مسبقًا في ملف[**نوع اتجاه النص**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)تعداد.

|**أنواع اتجاه النص**|**وصف**|
| :- | :- |
|سياق|ترتيب القراءة يتوافق مع لغة الحرف الذي تم إدخاله لأول مرة|
|من اليسار إلى اليمين|ترتيب القراءة من اليسار إلى اليمين|
|من اليمين الى اليسار|ترتيب القراءة من اليمين إلى اليسار|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **مواضيع متقدمة**
- [قم بتغيير المحاذاة Cells واحتفظ بالتنسيق الموجود](/cells/ar/net/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل الأسطر والتفاف النص](/cells/ar/net/line-breaks-and-text-wrapping/)

