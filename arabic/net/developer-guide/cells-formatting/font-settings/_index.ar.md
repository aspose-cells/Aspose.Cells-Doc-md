---
title: إعدادات الخط
type: docs
weight: 30
url: /ar/net/cells-font-settings/
---
{{% alert color="primary" %}}

يمكن التحكم في شكل النص وأسلوبه من خلال تغيير إعدادات الخط. قد تتضمن إعدادات الخط الاسم والنمط والحجم واللون والتأثيرات الأخرى للخطوط. تمامًا مثل Microsoft Excel ، يدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا.

{{% /alert %}}

## **تكوين إعدادات الخط**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells ملف[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) الأساليب المستخدمة للحصول على نمط تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر فئة خصائص لتكوين إعدادات الخط.

### **تعيين اسم الخط**

 يمكن للمطورين تطبيق أي خط على نص داخل خلية باستخدام[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[اسم](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **تعيين نمط الخط إلى غامق**

 يمكن للمطورين جعل النص غامقًا عن طريق تعيين[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) ملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **ضبط حجم الخط**

اضبط حجم الخط بامتداد[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**بحجم**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **ضبط لون الخط**

استخدم ال[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**اللون**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)خاصية لتعيين لون الخط. حدد أي لون من تعداد اللون (جزء من إطار عمل .NET) وقم بتعيينه إلى[**اللون**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **تعيين نوع تسطير الخط**

استخدم ال[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**تسطير**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)خاصية لتسطير النص. يوفر Aspose.Cells أنواعًا مختلفة من تسطير الخط المعرفة مسبقًا في تنسيق[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) تعداد.

|**أنواع تسطير الخط**|**وصف**|
|:- |:- |
|محاسبة|تسطير محاسبة واحد|
|مزدوج|تسطير مزدوج|
|حساب مزدوج|تسطير مزدوج المحاسبة|
|لا أحد|بدون تسطير|
|غير مرتبطة|تسطير واحد|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **إعداد تأثير الشطب**

تطبيق الشطب عن طريق ضبط[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)ملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **إعداد تأثير منخفض**

تطبيق منخفض عن طريق تعيين[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) ملكية ل**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **إعداد تأثير الكتابة المرتفعة على الخط**

 يمكن للمطورين تطبيق تأثير الكتابة المرتفعة على الخط عن طريق تعيين ملف[**هو مرتفع**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) ممتلكات[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) يعترض على**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **موضوعات مسبقة**
- [تطبيق تأثيرات الكتابة المرتفعة والمنخفضة على الخطوط](/cells/ar/net/apply-superscript-and-subscript-effects-on-fonts/)
- [احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف](/cells/ar/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

