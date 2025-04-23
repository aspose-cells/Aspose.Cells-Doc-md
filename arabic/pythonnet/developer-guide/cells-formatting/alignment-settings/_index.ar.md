---
title: إعدادات المحاذاة
description: في مكتبة Aspose.Cells لـ Python via .NET، يمكنك استخدام إعدادات محاذاة الخلية لضبط تخطيط وعرض النص. من خلال ضبط إعدادات مثل المحاذاة الأفقية، والمحاذاة الرأسية، وتغليف النص، لديك مزيد من السيطرة على تدفق النص داخل الخلايا. ستوفر لك هذه الوثيقة خطوات مفصلة وأمثلة على الرموز لمساعدتك على فهم كيفية استخدام Aspose.Cells لـ Python via .NET لإعدادات محاذاة الخلايا.
keywords: Aspose.Cells لـ Python via .NET، محاذاة الخلايا، المحاذاة الأفقية، المحاذاة الرأسية، تغليف النص
type: docs
weight: 20
url: /ar/python-net/cells-alignment-settings/
---

## **ضبط إعدادات المحاذاة**

### **إعدادات المحاذاة في Microsoft Excel**

أي شخص قد استخدم Microsoft Excel لتنسيق الخلايا سيكون متعودًا على إعدادات المحاذاة في Microsoft Excel.

كما يمكنك رؤية من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقية وعمودية)
- المسافة البادئة.
- التوجيه.
- التحكم بالنص.
- اتجاه النص.

جميع هذه الإعدادات للمحاذاة مدعومة بالكامل من قبل Aspose.Cells لـ Python via .NET وتناقش بمزيد من التفصيل أدناه.

### **إعدادات المحاذاة في Aspose.Cells لـ Python via .NET**

يقدم Aspose.Cells لـ Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تسمح بالوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

يوفر Aspose.Cells لـ Python via .NET طرق [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) و [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) للفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) التي تُستخدم للحصول على وتعيين تنسيق الخلية. تقدم فئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) خصائص مفيدة لضبط إعدادات المحاذاة.

حدد أي نوع لمحاذاة النص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). أنواع محاذاة النص المحددة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) هي:

|** أنواع محاذاة النص **|** الوصف **|
| :- | :- |
|GENERAL|يمثل محاذاة النص العامة|
|BOTTOM|يمثل محاذاة النص من الأسفل|
|CENTER|يمثل محاذاة النص في الوسط|
|CENTER_ACROSS|يمثل محاذاة النص عبر الوسط|
|DISTRIBUTED|يمثل محاذاة النص الموزع|
|FILL|يمثل ملء محاذاة النص|
|JUSTIFY|يمثل تبرير محاذاة النص|
|LEFT|يمثل محاذاة النص ناحية اليسار|
|RIGHT|يمثل محاذاة النص ناحية اليمين|
|TOP|يمثل محاذاة النص العلوية|
|JUSTIFIED_LOW|يتم محاذاة النص مع ضبط طول الكاشيدة للنص العربي|
|THAI_DISTRIBUTED|توزيع النص التايلاندي بشكل خاص، لأن كل حرف يُعامل ككلمة|

{{% alert color="primary" %}}

يمكنك أيضا تطبيق ضبط التوزيع المبرر باستخدام الخاصية [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed).

{{% /alert %}}

#### **المحاذاة الأفقية**

استخدم خاصية [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) لمحاذاة النص أفقياً.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **المحاذاة الرأسية**

مشابهة للمحاذاة الأفقية، استخدم خاصية [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) لمحاذاة النص عمودياً.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **المسافة البادئة**

من الممكن تعيين مستوى المسافة البادئة للنص في خلية بواسطة خاصية [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **الاتجاه**

حدد اتجاه (دوران) النص في خلية بواسطة خاصية [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

##### **تفاف النص**

يعمل تفاف النص في خلية على جعل النص أسهل قراءة: يتم ضبط ارتفاع الخلية ليتناسب مع جميع النص، بدلاً من قطعه أو تسربه إلى الخلايا المجاورة. ضبط التفاف النص على تشغيل أو إيقاف بواسطة خاصية [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **تقليص للتناسب**

خيار لتفاف النص في حقل هو تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك بضبط خاصية [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) في [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) إلى **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **دمج الخلايا**

مثل Microsoft Excel، يدعم Aspose.Cells for Python via .NET دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells for Python via .NET طريقتين لهذه المهمة. إحداهما هي استدعاء طريقة [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) لمجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). تأخذ طريقة [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

الطريقة الأخرى هي أولاً استدعاء [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) لجمع الخلايا المدمجة. الطريقة [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) في [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) تأخذ نفس مجموعة المعلمات كما في الطريقة [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) المناقشة أعلاه وتعيد [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). الكائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) يوفر أيضاً الطريقة [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) التي تدمج المجموعة المحددة في الكائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

##### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يتم تعيين ترتيب القراءة بواسطة خاصية [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) في كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). يوفر Aspose.Cells for Python via .NET أنواعًا محددة مسبقًا لاتجاه النص في التعداد [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|CONTEXT|ترتيب القراءة متسق مع لغة الحرف المدخل الأول|
|LEFT_TO_RIGHT|ترتيب القراءة من اليسار إلى اليمين|
|RIGHT_TO_LEFT|ترتيب القراءة من اليمين إلى اليسار|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/python-net/line-breaks-and-text-wrapping/)


