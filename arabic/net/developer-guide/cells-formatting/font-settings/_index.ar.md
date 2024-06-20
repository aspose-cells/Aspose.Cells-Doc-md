---
title: إعدادات الخط
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات. تدعم تعيين إعدادات الخط للخلايا، مما يتيح للمستخدمين تخصيص نمط الخط وخصائص الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لتعيين إعدادات خط الخلية.
keywords: Aspose.Cells، Cells، Font Settings، Styles، Properties
type: docs
weight: 30
url: /ar/net/cells-font-settings/
---

{{% alert color="primary" %}}

يمكن التحكم في مظهر النص عن طريق تغيير إعدادات الخط. يمكن أن تتضمن إعدادات الخط الاسم والنمط والحجم واللون وتأثيرات أخرى للخطوط. تدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا تمامًا مثل Microsoft Excel.

{{% /alert %}}

## **تكوين إعدادات الخط**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورق عمل في ملف Excel. يمثل ورق العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) وطرق [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) تُستخدم للحصول على وتعيين نمط تنسيق الخلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) خصائص لتكوين إعدادات الخط.

### **تعيين اسم الخط**

يمكن للمطورين تطبيق أي خط على النص داخل الخلية باستخدام خاصية [اسم](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) الخاصة بكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **تعيين نمط الخط إلى عريض**

يمكن للمطورين جعل النص عريضًا عن طريق ضبط خاصية [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) من كائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) على **صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **تعيين حجم الخط**

قم بتعيين حجم الخط باستخدام خاصية [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **تعيين لون الخط**

استخدم خاصية [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) لتعيين لون الخط. اختر أي لون من تعداد الألوان (جزء من إطار العمل .NET) وقم بتعيينه إلى الخاصية [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **تعيين نوع تسطير الخط**

استخدم خاصية [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) لتسطير النص. تقدم Aspose.Cells مجموعة من أنواع تسطير الخط المحددة مسبقًا في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype)

|**أنواع تسطير الخط**|**الوصف**|
| :- | :- |
|Accounting|تسطير واحد للحساب|
|Double|تسطير مزدوج|
|DoubleAccounting|تسطير حسابي مزدوج|
|None|بدون تسطير|
|Single|تسطير واحد|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **ضبط تأثير شطب**

تطبيق تأثير الشطب عن طريق ضبط خاصية [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) إلى **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **ضبط تأثير الرمز الفرعي**

تطبيق الرمز الفرعي عن طريق ضبط خاصية [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) إلى **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **ضبط تأثير الرمز العلوي على الخط**

يمكن للمطورين تطبيق تأثير الرمز العلوي على الخط عن طريق ضبط خاصية [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) لكائن [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) إلى **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **مواضيع متقدمة**
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/net/apply-superscript-and-subscript-effects-on-fonts/)
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

