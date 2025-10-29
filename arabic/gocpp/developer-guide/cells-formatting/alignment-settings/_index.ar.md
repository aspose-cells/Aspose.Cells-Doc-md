---
title: إعدادات المحاذاة مع Golang عبر C++
linktitle: إعدادات المحاذاة
description: في مكتبة Aspose.Cells، يمكنك استخدام إعدادات محاذاة الخلية لضبط التخطيط وعرض النص. من خلال ضبط الإعدادات مثل المحاذاة الأفقية، المحاذاة العمودية والتفاف النص، ستحصل على مزيد من التحكم في كيفية تدفق النص في الخلايا. ستوفر لك هذه الوثيقة خطوات مفصلة وشيفرة عينية لمساعدتك في فهم كيفية استخدام Aspose.Cells لإعدادات محاذاة الخلية بسرعة.
keywords: Aspose.Cells، إعدادات محاذاة الخلية، المحاذاة الأفقية، المحاذاة العمودية، التفاف النص
type: docs
weight: 20
url: /ar/go-cpp/cells-alignment-settings/
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

كل إعدادات المحاذاة هذه مدعومة تمامًا بواسطة Aspose.Cells ويتم مناقشتها بمزيد من التفصيل أدناه.

### **إعدادات المحاذاة في Aspose.Cells**

توفر Aspose.Cells فئةً تُمثِّل ملف Excel تدعى [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثِّل ورقة عمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). يُمثِّل كل عنصر في مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر Aspose.Cells الأساليب [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) و [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) لفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) والتي تُستخدم للحصول على تنسيق الخلية وتعيينه. توفر الفئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص مفيدة لتكوين إعدادات المحاذاة.

حدد أي نوع لمحاذاة النص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/). أنواع محاذاة النص المحددة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) هي:

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

يمكنك أيضا تطبيق ضبط التوزيع المبرر باستخدام الخاصية [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/).

{{% /alert %}}

#### **المحاذاة الأفقية**

استخدم خاصية [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/) لمحاذاة النص أفقياً.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **المحاذاة الرأسية**

مشابهة للمحاذاة الأفقية، استخدم خاصية [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/) لمحاذاة النص عمودياً.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **المسافة البادئة**

من الممكن تعيين مستوى المسافة البادئة للنص في خلية بواسطة خاصية [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **الاتجاه**

حدد اتجاه (دوران) النص في خلية بواسطة خاصية [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

##### **تفاف النص**

يعمل تفاف النص في خلية على جعل النص أسهل قراءة: يتم ضبط ارتفاع الخلية ليتناسب مع جميع النص، بدلاً من قطعه أو تسربه إلى الخلايا المجاورة. ضبط التفاف النص على تشغيل أو إيقاف بواسطة خاصية [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **تقليص للتناسب**

خيار لتفاف النص في حقل هو تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك بضبط خاصية [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) في [**Style**](https://reference.aspose.com/cells/go-cpp/style/) إلى **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **دمج الخلايا**

مثل Microsoft Excel ، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. طريقة واحدة هي استدعاء [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) في مجموعة [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/). تأخذ [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) الوسيلة المعاملات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
الطريقة الأخرى هي أولاً استدعاء [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) لجمع الخلايا المدمجة. الطريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) في [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) تأخذ نفس مجموعة المعلمات كما في الطريقة [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) المناقشة أعلاه وتعيد [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). الكائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) يوفر أيضاً الطريقة [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) التي تدمج المجموعة المحددة في الكائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يتم تعيين ترتيب القراءة باستخدام خاصية [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) 'الكائن [**Style**](https://reference.aspose.com/cells/go-cpp/style/)'. توفر Aspose.Cells أنواع توجيه نص محددة مسبقًا في تعداد [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/cpp/line-breaks-and-text-wrapping/)
