---
title: إعدادات الحد مع Golang عبر C++
linktitle: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells في C++ لضبط نمط ولون حدود الخلايا. من خلال تعديل العرض والنمط واللون للحدود، يمكنك التحكم بشكل أكبر في مظهر الخلايا وظهورها.
keywords: Aspose.Cells، إعدادات حدود الخلايا، C++، عرض الحد، نمط الحد، لون الحد
type: docs
weight: 40
url: /ar/go-cpp/cells-border-settings/
---

## **إضافة حدود إلى الخلايا**

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال، الحد العلوي هو الحد المضاف إلى أعلى موضع من الخلية. يمكن للمستخدمين أيضًا تعديل نمط وخطوط الألوان للحدود.

مع Aspose.Cells، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة كما في Microsoft Excel.

### **إضافة حدود إلى الخلايا**

توفر مكتبة Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) يمثل كائن من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

يقدم Aspose.Cells طريقة [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) في فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). تُستخدم طريقة [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) لتعيين نمط تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص لإضافة حدود إلى الخلايا.

#### **إضافة حدود إلى خلية**

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) من كائن [**Style**](https://reference.aspose.com/cells/go-cpp/style/). يُمرر نوع الحد كفهرس إلى مجموعة [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). جميع أنواع الحدود معرفَة مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**تعداد الحدود**

| **أنواع الحدود** | **الوصف** |
|------------------|-----------------|
| الحد السفلي     | خط الحد السفلي |
| القطع القطري للأسفل     | خط قطري من أعلى اليسار إلى أسفل اليمين |
| القطع القطري للأعلى       | خط قطري من أسفل اليسار إلى أعلى اليمين |
| الحد الأيسر       | خط الحد الأيسر |
| الحد الأيمن      | خط الحد الأيمن |
| الحد العلوي        | خط الحد العلوي |

تخزن مجموعة [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) جميع الحدود. يُمثل كل حد في مجموعة [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) بواسطة كائن [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) يوفر خصيتين، [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) و[**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) لضبط لون الخط ونمط الحد على التوالي.

لضبط لون خط الحد، اختر لونًا باستخدام تعداد اللون وقم بتعيينه لخاصية لون كائن الحد.

يتم ضبط نمط خط الحد عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).

**تعداد CellBorderType**

| **أنماط الخطوط**       | **الوصف**               |
|------------------------|-------------------------------|
| DashedDot               | خط مخطوط رفيع مغير |
| DashedDotDot            | خط مخطوط مع خطقطار رفيع |
| Dashed                | خط مخطط |
| Dotted                | خط نقطي |
| Double                | خط مزدوج |
| Hair                  | خط شعر |
| MediumDashDot         | خط مخطوط متوسط |
| MediumDashDotDot      | خط مخطوط مخطط متوسط |
| MediumDashed          | خط مخطط متوسط |
| None                  | بدون خط |
| Medium                | خط متوسط |
| SlantedDashDot        | خط مائل مخطوط متوسط |
| Thick                 | خط سميك |
| Thin                  | خط رقيق |

اختر أحد أنماط الخط ثم قم بتعيينه إلى خاصية [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) لكائن [**Border**](https://reference.aspose.com/cells/go-cpp/border/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

يجب تعيين كل من نمط الخط ولونه في نفس الوقت. يجب أن يكون لنظامي الخطوط القطرية نفس النمط واللون.

{{% /alert %}}

#### **إضافة حدود لمجموعة من الخلايا**

من الممكن أيضًا إضافة حدود لنطاق من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أولاً، أنشئ نطاق خلايا عبر استدعاء طريقة [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) لمجموعة [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/). تأخذ المعلمات التالية:

- الصف الأول، الصف الأول من المجموعة.
- العمود الأول، يمثل العمود الأول من المجموعة.
- عدد الصفوف، عدد الصفوف في المجموعة.
- عدد الأعمدة، عدد الأعمدة في المجموعة.

تعيد طريقة [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) كائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)، الذي يحتوي على النطاق المحدد من الخلايا. يوفر كائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) طريقة [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) التي تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

- **نوع الحد**، نوع الحد، مختار من تعداد [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/).
- **نمط الخط**، نمط خط الحد، مختار من تعداد [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).
- **اللون**، لون الخط، المحدد من تعداد الألوان.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
