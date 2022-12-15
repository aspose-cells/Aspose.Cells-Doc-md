---
title: تنسيق الخلايا
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/net/cells-formatting/
description: قم بتعيين تنسيق الأرقام والحدود ولون الخلفية لملفات Excel على .NET Framework أو .NET Core أو Mono أو الأنظمة الأساسية Xamarin.
---
## **مقدمة**

{{% alert color="primary" %}}

 يوفر Aspose.Cells ملف[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) طرق[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) فئة ، تُستخدم للحصول على / تعيين نمط تنسيق الخلية. يوفر Aspose.Cells أيضًا أ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)صف دراسي.

{{% /alert %}}

## **قم بتنسيق Cells باستخدام أساليب GetStyle و SetStyle**

قم بتطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو المقدمة ، والحدود ، والخطوط ، والمحاذاة الأفقية والرأسية ، ومستوى المسافة البادئة ، واتجاه النص ، وزاوية التدوير والمزيد.

### **استخدام أساليب GetStyle و SetStyle**

 إذا احتاج المطورون إلى تطبيق أنماط تنسيق مختلفة على خلايا مختلفة ، فمن الأفضل الحصول على ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) من الخلية باستخدام[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) الطريقة ، حدد سمات النمط ثم قم بتطبيق التنسيق باستخدام[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)طريقة. يوجد مثال أدناه لتوضيح هذا الأسلوب لتطبيق تنسيقات مختلفة على خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **استخدام نمط الكائن لتنسيق مختلف Cells**

 إذا احتاج المطورون إلى تطبيق نفس نمط التنسيق على خلايا مختلفة ، فيمكنهم استخدامها[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) هدف. يرجى اتباع الخطوات أدناه لاستخدام[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)هدف:

1.  أضف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) عن طريق استدعاء[**خلق نمط**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) طريقة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)صف دراسي
1.  الوصول إلى ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)هدف
1.  قم بتعيين الخصائص / السمات المطلوبة لملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)لتطبيق إعدادات التنسيق المطلوبة
1. قم بتعيين ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)كائن على الخلايا التي تريدها

يمكن أن يؤدي هذا النهج إلى تحسين كفاءة تطبيقاتك بشكل كبير وتوفير الذاكرة أيضًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **استخدام Microsoft Excel 2007 الأنماط المعرفة مسبقًا**

إذا كنت بحاجة إلى تطبيق أنماط تنسيق مختلفة لـ Microsoft Excel 2007 ، فقم بتطبيق الأنماط باستخدام Aspose.Cells API. يوجد مثال أدناه لتوضيح هذا الأسلوب لتطبيق نمط معرف مسبقًا على خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **تنسيق الأحرف المحددة في Cell**

يشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا ، ولكنه يشرح فقط كيفية تنسيق محتوى الخلية بالكامل. ماذا لو كنت تريد تنسيق الأحرف المختارة فقط؟

Aspose.Cells يدعم هذه الميزة أيضًا. يشرح هذا الموضوع كيفية استخدام هذه الميزة بشكل فعال.

### **تنسيق الأحرف المحددة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فئة توفر[**الشخصيات**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)طريقة تأخذ المعلمات التالية لتحديد نطاق من الأحرف داخل خلية:

- **فهرس البداية**، فهرس الحرف الذي يبدأ منه التحديد.
- **عدد الشخصيات**، عدد الأحرف المراد تحديده.

 ال[**الشخصيات**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) تقوم الطريقة بإرجاع مثيل لـ[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)فئة تسمح للمطورين بتنسيق الأحرف بنفس طريقة تنسيق الخلية كما هو موضح أدناه في مثال التعليمات البرمجية. في ملف الإخراج ، في الخلية A1 ، سيتم تنسيق كلمة "زيارة" بالخط الافتراضي ولكن "Aspose!" جريئة وأزرق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 إذا كنت مهتمًا بتنسيق جزء من نص منسق في خلية ، ففكر في استخدام ملحق[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طُرق. ال[[** Cell.GetCharacters **]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) يتم استخدام الطريقة للوصول إلى أجزاء النص ومن ثم يمكن إجراء التعديلات باستخدام[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طريقة بينما**احصل على**تقوم الطريقة بإرجاع مصفوفة من[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) الكائنات التي يمكن معالجتها لتعيين خصائص مختلفة مثل اسم الخط ولون الخط والجرأة وما إلى ذلك**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

{{% /alert %}}

## **تنسيق الصفوف والأعمدة**

في بعض الأحيان ، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. غالبًا ما يستغرق تطبيق التنسيق على الخلايا واحدة تلو الأخرى وقتًا أطول ولا يعد حلاً جيدًا.
لمعالجة هذه المشكلة ، يوفر Aspose.Cells طريقة بسيطة وسريعة تمت مناقشتها بالتفصيل في هذه المقالة.

### **تنسيق الصفوف والأعمدة**

 يوفر Aspose.Cells فئة ، و[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة أ[**صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)مجموعة.

### **تنسيق صف**

 كل عنصر في[**صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) تمثل المجموعة أ[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row) هدف. ال[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row)يقدم الكائن[**تطبيق**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) الطريقة المستخدمة لتعيين تنسيق الصف. لتطبيق نفس التنسيق على صف ، استخدم ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)هدف. توضح الخطوات أدناه كيفية استخدامه.

1.  أضف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يعترض على[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class عن طريق استدعاء[**خلق نمط**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)طريقة.
1.  تعيين[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)خصائص الكائن لتطبيق إعدادات التنسيق.
1.  اجعل السمات ذات الصلة قيد التشغيل لـ[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)هدف.
1. قم بتعيين ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يعترض على[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row)هدف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **تنسيق عمود**

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) توفر المجموعة أيضًا ملف[**الأعمدة**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) مجموعة. كل عنصر في[**الأعمدة**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) تمثل المجموعة أ[**عمودي**](https://reference.aspose.com/cells/net/aspose.cells/column) هدف. على غرار أ[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row) كائن[**عمودي**](https://reference.aspose.com/cells/net/aspose.cells/column) يقدم الكائن أيضًا[**تطبيق**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)طريقة تنسيق العمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **موضوعات مسبقة**
- [إعدادات المحاذاة](/cells/ar/net/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/net/cells-border-settings/)
- [قم بتعيين التنسيقات الشرطية لملفات Excel و ODS.](/cells/ar/net/conditional-formatting/)
- [سمات وألوان Excel](/cells/ar/net/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/net/cells-fill-settings/)
- [إعدادات الخط](/cells/ar/net/cells-font-settings/)
- [تنسيق ورقة العمل Cells في مصنف](/cells/ar/net/format-worksheet-cells-in-a-workbook/)
- [تطبيق نظام التاريخ 1904](/cells/ar/net/implement-1904-date-system/)
- [الدمج والدمج Cells](/cells/ar/net/merging-and-unmerging-cells/)
- [إعدادات الرقم](/cells/ar/net/cells-number-settings/)
- [الحصول على نمط الخلايا وتعيينه](/cells/ar/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

