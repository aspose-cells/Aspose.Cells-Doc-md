---
title: التعامل مع إعدادات الخط
linktitle: إعدادات الخط
type: docs
weight: 20
url: /ar/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

يمكن التحكم في مظهر وشعور النص عن طريق تغيير إعدادات الخط الخاصة به. تشمل هذه الإعدادات قد يكون اسمها ونمطها وحجمها ولونها وتأثيرات أخرى للخطوط كما هو موضح أدناه في الشكل:

**إعدادات الخط في Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

تدعم Aspose.Cells أيضًا مثل Microsoft Excel تكوين إعدادات الخط للخلايا.

{{% /alert %}} 
## **تكوين إعدادات الخط**
توفر Aspose.Cells صنفًا، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) الذي يمثل ملف Microsoft Excel. يحتوي صنف [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثّل ورقة العمل باستخدام صنف [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). يوفر صنف [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) يمثل كائن من صنف [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

توفر Aspose.Cells صنف [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) الخاص بطريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) التي تستخدم لتعيين تنسيق الخلية. كما يوفر كائن صنف [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) خصائص لتكوين إعدادات الخط.

يوضح هذا المقال كيفية:

- [تطبيق خط معين على النص.](/cells/ar/java/dealing-with-font-settings/)
- [تعيين النص إلى الخط العريض](/cells/ar/java/dealing-with-font-settings/).
- [تعيين حجم الخط](/cells/ar/java/dealing-with-font-settings/).
- [تعيين لون الخط](/cells/ar/java/dealing-with-font-settings/).
- [تسطير النص](/cells/ar/java/dealing-with-font-settings/).
- [إلغاء خط النص](/cells/ar/java/dealing-with-font-settings/).
- [تعيين النص إلى الفرعي](/cells/ar/java/dealing-with-font-settings/).
- [تعيين النص إلى السوبر](/cells/ar/java/dealing-with-font-settings/).
### **تعيين اسم الخط**
تطبيق خط معين على النص في الخلايا باستخدام [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) الخاصية [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) كائن.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **تعيين نمط الخط إلى عريض**
تعيين النص إلى الخط العريض عن طريق تعيين [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) الخاصية [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) كائن إلى **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **تعيين حجم الخط**
تعيين حجم الخط باستخدام [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) الخاصية [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) كائن.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **تعيين نوع تسطير الخط**
تسطير النص باستخدام [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) الخاصية [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) كائن. تقدم Aspose.Cells أنواع تسطير الخط المحددة مسبقًا في تعداد الـ [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType).

|**أنواع تسطير الخط**|**الوصف**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|بدون تسطير|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|تسطير أحادي|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|خط مزدوج تحته|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|خط أحادي تحته للمحاسبة|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|خط مزدوج للمحاسبة تحته|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|تحته مشطوف|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|تحته خط متقطع سميك نقطة نقطة|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|تحته خط متقطع سميك نقطة|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|تحته خط متقطع سميك|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|تحته خط طويل متقطع|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|تحته خط طويل سميك متقطع|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|شَر{شَرشَرِ} Dash-Dot Underline|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|شَر{شَرشَرِ} Dash-Dot-Dot Underline|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|شَر{شَرشَرِ} Dotted Underline|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|شَر{شَرشَرِ} Thick Dotted Underline|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|شَر{شَرشَرِ} Thick Underline|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|شَر{شَرشَرِ} Wave Underline|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|شَر{شَرشَرِ} Double Wave Underline|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|شَر{شَرشَرِ} Heavy Wave Underline|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|تحت الخط Underline Non-Space Characters Only|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **تعيين لون الخط**
اضبط لون الخط باستخدام [كائن الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) و [خاصية setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color). اختر أي لون من تعداد [اللون](https://reference.aspose.com/cells/java/com.aspose.cells/Color) وقم بتعيين اللون المحدد ل[كائن الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) باستخدام [خاصية setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **ضبط تأثير اليتيمة على النص**
يمكنك تطبيق اليتيمة على النص باستخدام خاصية [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) في كائن [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **ضبط النص الفرعي**
قم بجعل النص فوق السطر باستخدام خاصية [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) في كائن [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **ضبط النص العلوي**
قم بتطبيق النص العلوي على النص باستخدام خاصية [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) في كائن [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **مواضيع متقدمة**
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/java/apply-superscript-and-subscript-effects-on-fonts/)
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
