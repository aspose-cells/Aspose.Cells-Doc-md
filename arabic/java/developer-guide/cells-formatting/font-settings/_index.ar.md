---
title: التعامل مع إعدادات الخط
linktitle: إعدادات الخط
type: docs
weight: 20
url: /ar/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

يمكن التحكم في شكل النص وأسلوبه من خلال تغيير إعدادات الخط. قد تتضمن إعدادات الخط هذه الاسم والنمط والحجم واللون والتأثيرات الأخرى للخطوط كما هو موضح أدناه في الشكل:

**إعدادات الخط في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](dealing-with-font-settings_1.png)

تمامًا مثل Microsoft Excel ، يدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا.

{{% /alert %}} 
## **تكوين إعدادات الخط**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells ملف[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي'[مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) الطريقة المستخدمة لتعيين تنسيق الخلية. أيضا ، موضوع[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style)توفر فئة خصائص لتكوين إعدادات الخط.

يوضح هذا المقال كيفية:

- [تطبيق خط معين على النص.](/cells/ar/java/dealing-with-font-settings/)
- [تعيين النص إلى غامق](/cells/ar/java/dealing-with-font-settings/).
- [اضبط حجم الخط](/cells/ar/java/dealing-with-font-settings/).
- [اضبط لون الخط](/cells/ar/java/dealing-with-font-settings/).
- [تسطير النص](/cells/ar/java/dealing-with-font-settings/).
- [نص مشطوب](/cells/ar/java/dealing-with-font-settings/).
- [تعيين النص إلى منخفض](/cells/ar/java/dealing-with-font-settings/).
- [تعيين النص إلى نص مرتفع](/cells/ar/java/dealing-with-font-settings/).
### **تعيين اسم الخط**
 تطبيق خط معين على النص في الخلايا باستخدام[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[اسم مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **تعيين نمط الخط إلى غامق**
 قم بتعيين النص إلى غامق عن طريق تعيين[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) الملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **ضبط حجم الخط**
 اضبط حجم الخط باستخدام ملف[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[ضبط الحجم](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **تعيين نوع تسطير الخط**
 تسطير النص بامتداد[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[وضع السطر](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) منشأه. يوفر Aspose.Cells أنواعًا مختلفة من تسطير الخط المعرفة مسبقًا في تنسيق[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)تعداد.

|**أنواع تسطير الخط**|**وصف**|
|:- |:- |
|[لا أحد](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|بدون تسطير|
|[غير مرتبطة](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|تسطير واحد|
|[مزدوج](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|تسطير مزدوج|
|[محاسبة](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|تسطير محاسبة واحد|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|تسطير مزدوج المحاسبة|
|[اندفاع](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|تسطير متقطع|
|[اندفاع_نقطة_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|تسطير ثخين - نقطة - نقطة|
|[اندفاع_نقطة_ثقيل](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|تسطير نقطي سميك|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|تسطير متقطع سميك|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|تسطير متقطع طويل|
|[اندفاع_طويل_ثقيل](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|تسطير متقطع سميك طويل|
|[نقطة شرطة](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|تسطير شرطة نقطة|
|[نقطة_نقطة_اندفاع](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|تسطير شرطة نقطية|
|[منقط](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|تسطير منقط|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|تسطير منقط سميك|
|[ثقيل](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|تسطير سميك|
|[لوح](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|تسطير الموجة|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|تسطير موجة مزدوجة|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|تسطير مموج كثيف|
|` `[كلمات](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|تسطير الأحرف بدون مسافة فقط|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **ضبط لون الخط**
 اضبط لون الخط بامتداد[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) منشأه. حدد أي لون من ملف[اللون](https://reference.aspose.com/cells/java/com.aspose.cells/Color) تعداد وتعيين اللون المحدد إلى[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **ضبط تأثير الشطب على النص**
 نص مشطوب بامتداد[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **إعداد منخفض**
 جعل النص مرتفعًا باستخدام[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[تعيين](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **إعداد مرتفع**
 تطبيق نص مرتفع على النص بامتداد[الخط](https://reference.aspose.com/cells/java/com.aspose.cells/Font) أشياء[تعيين](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **موضوعات مسبقة**
- [تطبيق تأثيرات الكتابة المرتفعة والمنخفضة على الخطوط](/cells/ar/java/apply-superscript-and-subscript-effects-on-fonts/)
- [احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف](/cells/ar/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
