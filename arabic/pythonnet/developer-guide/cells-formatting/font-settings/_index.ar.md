---
title: إعدادات الخط
description: Aspose.Cells هي مكتبة بايثون للعمل مع ملفات جداول البيانات. تدعم تعيين إعدادات الخط للخلايا، مما يسمح للمستخدمين بتخصيص نمط وخصائص الخط للخلايا. ستقدم هذه المقالة كيفيه استخدام مكتبة Aspose.Cells for Python via .NET لضبط إعدادات خط الخلية.
keywords: Aspose.Cells for Python via .NET، خلايا، إعدادات الخط، أنماط، خصائص
type: docs
weight: 30
url: /ar/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

يمكن التحكم في مظهر النص من خلال تغيير إعدادات الخط. قد تشمل إعدادات الخط الاسم، والنمط، والحجم، واللون، و تأثيرات أخرى. تمامًا كما في Microsoft Excel، تدعم Aspose.Cells for Python via .NET أيضًا تكوين إعدادات الخط للخلايا.

{{% /alert %}}

## **تكوين إعدادات الخط**

توفر Aspose.Cells for Python via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) تمثل ملف إكسل من مايكروسوفت. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). كل عنصر في المجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) وطرق [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) و [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) تُستخدم للحصول على وتعيين نمط تنسيق الخلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) خصائص لتكوين إعدادات الخط.

### **تعيين اسم الخط**

يمكن للمطورين تطبيق أي خط على النص داخل خلية باستخدام خاصية [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **تعيين نمط الخط إلى عريض**

يمكن للمطورين جعل النص عريضًا عن طريق ضبط خاصية [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) من كائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) على **صحيح**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **تعيين حجم الخط**

قم بتعيين حجم الخط باستخدام خاصية [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **تعيين لون الخط**

استخدم خاصية [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) لتعيين لون الخط. اختر أي لون من تعداد الألوان (جزء من إطار العمل .NET) وقم بتعيينه إلى الخاصية [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **تعيين نوع تسطير الخط**

استخدم الخاصية [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) في كائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) لتحتية النص. تقدم مكتبة Aspose.Cells لبايثون via .NET أنواع خط تحتية معرف مسبقاً في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype).

|**أنواع تسطير الخط**|**الوصف**|
| :- | :- |
|المحاسبة|تحتية محاسبة مفردة|
|مزدوج|تحتية مزدوجة|
|محاسبة_مزدوجة|تحتية محاسبة مزدوجة|
|بلا|لا يوجد خط تحت|
|فردي|خط تحت واحد|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **ضبط تأثير شطب**

تطبيق تأثير الشطب عن طريق ضبط خاصية [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) إلى **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **ضبط تأثير الرمز الفرعي**

تطبيق الرمز الفرعي عن طريق ضبط خاصية [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) إلى **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **ضبط تأثير الرمز العلوي على الخط**

يمكن للمطورين تطبيق تأثير الرمز العلوي على الخط عن طريق ضبط خاصية [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) لكائن [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) إلى **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **مواضيع متقدمة**
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


{{< app/cells/assistant language="python-net" >}}
