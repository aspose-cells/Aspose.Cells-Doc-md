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

توفر Aspose.Cells فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) وطريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-)، والتي تُستخدم لضبط تنسيق الخلية. كما توفر كائنات فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) خصائص لتكوين إعدادات الخط.

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
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|تسطير حسابي مزدوج|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|تحته مشطوف|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|تسطير دقيقتين دايرين سميكتين|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|تسطير داير سميك|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|تسطير منقوط سميك|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|تسطير طويل منقوط|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|تسطير طويل منقوط سميك|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|تسطير نقطي داير|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|تسطير نقطتين داير|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|شَر{شَرشَرِ} Dotted Underline|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|تسطير منقوط سميك|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|شَر{شَرشَرِ} Thick Underline|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|شَر{شَرشَرِ} Wave Underline|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|تسطير متموج مزدوج|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|تسطير متموج سميك|
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
{{< app/cells/assistant language="java" >}}
