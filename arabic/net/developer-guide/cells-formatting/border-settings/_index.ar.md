---
title: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells في لغة C# لضبط نمط ولون حدود الخلايا. من خلال ضبط عرض ونمط ولون الحدود، يمكنك السيطرة بشكل أفضل على شكل الخلايا ومظهرها.
keywords: Aspose.Cells, إعدادات حد الخلية, لغة C#, عرض الحد, نمط الحد, لون الحد
type: docs
weight: 40
url: /ar/net/cells-border-settings/
---

## **إضافة حدود إلى الخلايا**

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة الحدود. نوع الحدود يعتمد على مكان إضافته. على سبيل المثال، يعد الحد العلوي هو الحد الذي يتم إضافته إلى الموضع العلوي للخلية. يمكن للمستخدمين أيضاً تعديل نمط الخطوط ولونها.

مع Aspose.Cells، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة كما في Microsoft Excel.

### **إضافة حدود إلى الخلايا**

تقدم Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) المجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تمثل كل عنصر في الفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

يوفر Aspose.Cells الطريقة [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) في فئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). تُستخدم الطريقة [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) لضبط نمط تنسيق الخلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) خصائص لإضافة حدود إلى الخلايا.

#### **إضافة حدود إلى خلية**

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) الخاصة بكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). يتم تمرير نوع الحدود كفهرس إلى المجموعة [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). تم تحديد جميع أنواع الحدود مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).

**تعداد الحدود**

|**أنواع الحدود**|**الوصف**|
| :- | :- |
خط حد فسفلي |BottomBorder||
خط قطري من أعلى اليسار إلى أسفل اليمين |DiagonalDown||
خط قطري من أسفل اليسار إلى أعلى اليمين |DiagonalUp||
خط حد أيسر |LeftBorder||
خط حد أيمن |RightBorder||
خط حد علوي |TopBorder||

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

لضبط لون الحدود، حدد لونا باستخدام تعداد الألوان (جزء من إطار العمل .NET) وقم بتعيينه لخاصية اللون الخاصة بكائن الحدود.

يتم ضبط نمط الخط للحدود عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).

**تعداد CellBorderType**

|**أنماط الخطوط**|**الوصف**|
| :- | :- |
|DashDot| خط متقطع رفيع
|DashDotDot| خط نقطة متقطعة رفيع
خط متقطع |Dashed||
خط منقط |Dotted||
|Double|خط مزدوج|
|Hair|خط رفيع|
|MediumDashDot|خط متقطع متوسط المتنقل|
|MediumDashDotDot|خط متوسط متقطع بالنقاط|
|MediumDashed|خط متوسط متقطع|
|None|لا يوجد خط|
|Medium|خط متوسط|
|SlantedDashDot|خط مائل متوسط متقطع بالنقاط|
|Thick|خط سميك|
|Thin|خط رفيع|
حدد أحد أنماط الخط ثم اسنده لخاصية [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) للكائن [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

يجب أن تقوم بتعيين كل من نمط الخط واللون في نفس الوقت. يجب أن يكون لدى الحواف القطرية الثنائية نفس نمط الخط واللون.

{{% /alert %}}

#### **إضافة حدود لمجموعة من الخلايا**

من الممكن أيضًا إضافة حدود لمجموعة من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أنشئ أولاً مجموعة من الخلايا من خلال استدعاء طريقة [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) لمجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تأخذ الطريقة السمات التالية:

- الصف الأول، الصف الأول من المجموعة.
- العمود الأول، يمثل العمود الأول من المجموعة.
- عدد الصفوف، عدد الصفوف في المجموعة.
- عدد الأعمدة، عدد الأعمدة في المجموعة.

تعيد الطريقة [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) كائن [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)، الذي يحتوي على مجموعة الخلايا المحددة. يوفر الكائن [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) طريقة [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) التي تأخذ السمات التالية لإضافة حد لمجموعة الخلايا:

- **نوع الحد**، نوع الحد، المحدد من تعداد [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- **نمط الخط**، نمط الخط الحدودي، المحدد من التعداد [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- **اللون**، لون الخط، المحدد من تعداد الألوان.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
