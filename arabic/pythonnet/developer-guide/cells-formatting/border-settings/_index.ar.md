---
title: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells for Python via .NET في بايثون لتعيين نمط ولون حدود الخلايا. عن طريق تعديل عرض الحد ونمطه ولونه، يمكنك السيطرة بشكل أكبر على مظهر الخلايا وكيفية ظهورها.
keywords: Aspose.Cells for Python via .NET، إعدادات حدود الخلية، عرض حدود بايثون، نمط الحد، لون الحد
type: docs
weight: 40
url: /ar/python-net/cells-border-settings/
---

## **إضافة حدود إلى الخلايا**

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة الحدود. نوع الحدود يعتمد على مكان إضافته. على سبيل المثال، يعد الحد العلوي هو الحد الذي يتم إضافته إلى الموضع العلوي للخلية. يمكن للمستخدمين أيضاً تعديل نمط الخطوط ولونها.

مع Aspose.Cells for Python via .NET، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة مثلما في Microsoft Excel.

### **إضافة حدود إلى الخلايا**

يوفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) المجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) يمثل كائن الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

يوفر Aspose.Cells for Python via .NET الطريقة [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) في فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). تُستخدم طريقة [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) لضبط نمط تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) خصائص لإضافة حدود إلى الخلايا.

#### **إضافة حدود إلى خلية**

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) الخاصة بكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). يتم تمرير نوع الحدود كفهرس إلى المجموعة [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). تم تحديد جميع أنواع الحدود مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).

**تعداد الحدود**

|**أنواع الحدود**|**الوصف**|
| :- | :- |
|BOTTOM_BORDER|خط حدود سفلي|
|DIAGONAL_DOWN|خط قطري من أعلى اليسار إلى أسفل اليمين|
|DIAGONAL_UP|خط قطري من أسفل اليسار إلى أعلى اليمين|
|LEFT_BORDER|خط حدود أيسر|
|RIGHT_BORDER|خط حدود أيمن|
|TOP_BORDER|خط حدود علوي|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

لضبط لون الحدود، حدد لونا باستخدام تعداد الألوان (جزء من إطار العمل .NET) وقم بتعيينه لخاصية اللون الخاصة بكائن الحدود.

يتم ضبط نمط الخط للحدود عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).

**تعداد CellBorderType**

|**أنماط الخطوط**|**الوصف**|
| :- | :- |
|DASH_DOT|خط منقط ناعم|
|DASH_DOT_DOT|خط منقط منقّط ناعم مع نقطتين|
|DASHED|خط منقّط|
|DOTTED|خط منقط|
|DOUBLE|خط مزدوج|
|HAIR|خط شعر رقيقة جدا|
|MEDIUM_DASH_DOT|خط متوسط منقط ناعم|
|MEDIUM_DASH_DOT_DOT|خط متوسط منقط منقط ناعم مع نقطتين|
|MEDIUM_DASHED|خط متوسط منقّط|
|NONE|لا يوجد خط|
|MEDIUM|خط متوسط|
|SLANTED_DASH_DOT|خط منقّط مائل متوسط الخط|
|THICK|خط سميك|
|THIN|خط رفيع|
حدد أحد أنماط الخط ثم اسنده لخاصية [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) للكائن [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

يجب أن تقوم بتعيين كل من نمط الخط واللون في نفس الوقت. يجب أن يكون لدى الحواف القطرية الثنائية نفس نمط الخط واللون.

{{% /alert %}}

#### **إضافة حدود لمجموعة من الخلايا**

من الممكن أيضًا إضافة حدود لمجموعة من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أنشئ أولاً مجموعة من الخلايا من خلال استدعاء طريقة [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) لمجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). تأخذ الطريقة السمات التالية:

- الصف الأول، الصف الأول من المجموعة.
- العمود الأول، يمثل العمود الأول من المجموعة.
- عدد الصفوف، عدد الصفوف في المجموعة.
- عدد الأعمدة، عدد الأعمدة في المجموعة.

تعيد الطريقة [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) كائن [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str)، الذي يحتوي على مجموعة الخلايا المحددة. يوفر الكائن [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) طريقة [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) التي تأخذ السمات التالية لإضافة حد لمجموعة الخلايا:

- **نوع الحد**، نوع الحد، المحدد من تعداد [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- **نمط الخط**، نمط الخط الحدودي، المحدد من التعداد [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- **اللون**، لون الخط، المحدد من تعداد الألوان.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
