---
title: إعدادات المحاذاة
linktitle: إعدادات المحاذاة
description: في مكتبة Aspose.Cells، يمكنك استخدام إعدادات محاذاة الخلية لضبط تنسيق وتصميم النص باستخدام Node.js عبر C++. توفر هذه الوثيقة خطوات مفصلة وكود نموذجي لاستخدام Aspose.Cells لضبط إعدادات محاذاة الخلية.
keywords: Aspose.Cells، محاذاة الخلية، المحاذاة الأفقية، المحاذاة الرأسية، التفاف النص Node.js عبر C++
type: docs
weight: 20
url: /ar/nodejs-cpp/cells-alignment-settings/
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

 يوفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

يوفر Aspose.Cells طرق [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) و [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) لفئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) التي تُستخدم للحصول على وتعيين تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) خصائص مفيدة لضبط إعدادات المحاذاة.

اختر أي نوع محاذاة نص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype). أنواع محاذاة النص المعرفة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) هي:

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

يمكنك أيضًا تطبيق إعداد التوزيع المبرر باستخدام طريقة [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-).

{{% /alert %}}

#### **المحاذاة الأفقية**

استخدم طريقة [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) لمحاذاة النص أفقيًا.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **المحاذاة الرأسية**

مماثل للمحاذاة الأفقية، استخدم طريقة [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) لمحاذاة النص عموديًا.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **المسافة البادئة**

من الممكن تعيين مستوى المسافة البادئة للنص في خلية باستخدام طريقة [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **الاتجاه**

قم بضبط اتجاه (تدوير) النص في خلية باستخدام طريقة [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

##### **تفاف النص**

جعل النص يتدفق داخل خلية أسهل في القراءة: يتكيف ارتفاع الخلية لاحتواء كل النص، بدلاً من قطعه أو تسربه إلى خلايا مجاورة. قم بتشغيل أو إيقاف تشغيل تدفق النص باستخدام طريقة [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **تقليص للتناسب**

إحدى الخيارات لتغليف النص في حقل هي تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك بضبط طريقة [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **دمج الخلايا**

مثل Microsoft Excel، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. إحدى الطرق هي استدعاء طريقة [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) لمجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). تتطلب طريقة [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


الطريقة الأخرى هي استدعاء أولاً طريقة [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) لمجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) لإنشاء نطاق من الخلايا ليتم دمجها. تتلقى طريقة [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) نفس مجموعة المعلمات كما في الطريقة [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) وتعيد كائن [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). كما يوفر كائن [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) طريقة [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) لدمج النطاق المحدد في كائن [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

##### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يُضبط ترتيب القراءة باستخدام خاصية [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). يوفر Aspose.Cells أنواع اتجاه النص المعرفة مسبقًا في التعداد [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/nodejs-cpp/line-breaks-and-text-wrapping/)

