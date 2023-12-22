---
title: إعدادات الخط
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات. وهو يدعم ضبط إعدادات الخط للخلايا، مما يسمح للمستخدمين بتخصيص نمط الخط وخصائص الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لتعيين إعدادات خط الخلية.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /ar/net/cells-font-settings/
---
{{% alert color="primary" %}}

يمكن التحكم في شكل النص ومظهره عن طريق تغيير إعدادات الخط. قد تتضمن إعدادات الخط الاسم والنمط والحجم واللون والتأثيرات الأخرى للخطوط. تمامًا مثل Microsoft Excel، يدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا.

{{% /alert %}}

##  **تكوين إعدادات الخط**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 Aspose.Cells يوفر[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل'[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) الأساليب المستخدمة للحصول على نمط تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر الفئة خصائص لتكوين إعدادات الخط.

###  **تحديد اسم الخط**

 يمكن للمطورين تطبيق أي خط على النص داخل الخلية باستخدام[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[اسم](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **ضبط نمط الخط على غامق**

 يمكن للمطورين جعل النص غامقًا عن طريق تعيين[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)الخاصية إلى *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **تحديد حجم الخط**

اضبط حجم الخط باستخدام[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**مقاس**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **تحديد لون الخط**

استخدم ال[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**لون**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)خاصية تحديد لون الخط. حدد أي لون من تعداد الألوان (جزء من إطار عمل .NET) وقم بتعيينه إلى[**لون**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **تحديد نوع الخط المسطر**

استخدم ال[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**تسطير**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)خاصية تسطير النص. يقدم Aspose.Cells العديد من أنواع الخطوط التي تحتها خطوط محددة مسبقًا في ملف[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) تعداد.

|**أنواع التسطير الخط**|**وصف**|
| :- | :- |
|محاسبة|تسطير محاسبة واحد|
|مزدوج|تسطير مزدوج|
|حساب مزدوج|تسطير المحاسبة المزدوجة|
|لا أحد|لا يوجد تسطير|
|أعزب|تسطير واحد|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **تحديد تأثير الضربة القاضية**

تطبيق الإضراب عن طريق تحديد[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) أشياء[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)الخاصية إلى *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **تحديد تأثير منخفض**

تطبيق منخفض عن طريق تحديد[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)أشياء[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)الخاصية إلى *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **تحديد تأثير مرتفع على الخط**

 يمكن للمطورين تطبيق تأثير الخط المرتفع على الخط عن طريق تعيين[**مرتفع**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) ملكية[**النمط.الخط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)اعترض على *صحيح**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **مواضيع متقدمة**
- [تطبيق التأثيرات المرتفعة والمنخفضة على الخطوط](/cells/ar/net/apply-superscript-and-subscript-effects-on-fonts/)
- [احصل على قائمة الخطوط المستخدمة في جدول البيانات أو المصنف](/cells/ar/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

