---
title: تنسيق الخلايا
description: تعرف على كيفية تنسيق الخلايا ونمطها في Aspose.Cells for .NET، بما في ذلك تنسيق الأرقام وتنسيق التاريخ وأنماط الخطوط وخيارات أنماط الخلايا الأخرى. سيساعدك دليلنا على إنشاء جداول بيانات جذابة وذات مظهر احترافي.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/net/cells-formatting/
---
##  **مقدمة**

{{% alert color="primary" %}}

 Aspose.Cells يوفر[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) أساليب[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) فئة، تستخدم للحصول على/تعيين نمط التنسيق للخلية. Aspose.Cells يوفر أيضًا أ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)فصل.

{{% /alert %}}

##  **كيفية تنسيق Cells باستخدام أساليب GetStyle وSetStyle**

قم بتطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو المقدمة والحدود والخطوط والمحاذاة الأفقية والرأسية ومستوى المسافة البادئة واتجاه النص وزاوية التدوير وغير ذلك الكثير.

###  **كيفية استخدام طريقتي GetStyle وSetStyle**

 إذا كان المطورون بحاجة إلى تطبيق أنماط تنسيق مختلفة على خلايا مختلفة، فمن الأفضل الحصول على[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) من الخلية باستخدام[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) الطريقة، حدد سمات النمط ثم قم بتطبيق التنسيق باستخدام[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)طريقة. يوجد أدناه مثال لتوضيح هذا الأسلوب لتطبيق التنسيقات المختلفة على الخلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **كيفية استخدام كائن النمط لتنسيق مختلف Cells**

 إذا احتاج المطورون إلى تطبيق نفس نمط التنسيق على خلايا مختلفة، فيمكنهم استخدامه[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) هدف. يرجى اتباع الخطوات أدناه لاستخدام[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)هدف:

1.  أضف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) كائن عن طريق استدعاء[**كريت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) طريقة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فصل
1.  الوصول إلى المضافة حديثا[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  قم بتعيين الخصائص/السمات المطلوبة لـ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)كائن لتطبيق إعدادات التنسيق المطلوبة
1.  تعيين تكوينه[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)الاعتراض على الخلايا المطلوبة

يمكن لهذا الأسلوب تحسين كفاءة تطبيقاتك بشكل كبير وتوفير الذاكرة أيضًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **كيفية استخدام Microsoft Excel 2007 الأنماط المحددة مسبقًا**

إذا كنت بحاجة إلى تطبيق أنماط تنسيق مختلفة لـ Microsoft Excel 2007، فقم بتطبيق الأنماط باستخدام Aspose.Cells API. ويرد مثال أدناه لتوضيح هذا الأسلوب لتطبيق نمط محدد مسبقًا على خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **كيفية تنسيق الأحرف المحددة في Cell**

يشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا، ولكنه يشرح فقط كيفية تنسيق محتوى الخلية بالكامل. ماذا لو كنت تريد تنسيق الأحرف المحددة فقط؟

Aspose.Cells يدعم هذه الميزة أيضًا. يشرح هذا الموضوع كيفية استخدام هذه الميزة بفعالية.

###  **كيفية تنسيق الأحرف المحددة**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الطبقة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) يوفر الفصل[**الشخصيات**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)الطريقة التي تأخذ المعلمات التالية لتحديد نطاق من الأحرف داخل الخلية:

- *فهرس البداية**، فهرس الحرف الذي يبدأ منه الاختيار.
- *عدد الأحرف**، عدد الأحرف المراد تحديدها.

 ال[**الشخصيات**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) تقوم الطريقة بإرجاع مثيل لـ[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)فئة تسمح للمطورين بتنسيق الأحرف بنفس الطريقة التي يقومون بها بالخلية كما هو موضح أدناه في مثال التعليمات البرمجية. في ملف الإخراج، في الخلية A1، سيتم تنسيق كلمة "زيارة" بالخط الافتراضي ولكن "Aspose!" جريء وأزرق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

إذا كنت مهتمًا بتنسيق جزء من النص المنسق في خلية، ففكر في استخدام[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) طُرق. ال[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) يتم استخدام الطريقة للوصول إلى أجزاء النص ومن ثم يمكن إجراء التعديلات باستخدام[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) الطريقة في حين أن**يحصل** تقوم الطريقة بإرجاع مجموعة من[**إعداد الخط**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) الكائنات التي يمكن معالجتها لتعيين خصائص مختلفة مثل اسم الخط ولون الخط والخط الغامق وما إلى ذلك**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

{{% /alert %}}

##  **كيفية تنسيق الصفوف والأعمدة**

في بعض الأحيان، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. غالبًا ما يستغرق تطبيق التنسيق على الخلايا واحدة تلو الأخرى وقتًا أطول ولا يعد حلاً جيدًا.
ولمعالجة هذه المشكلة، يوفر Aspose.Cells طريقة بسيطة وسريعة تمت مناقشتها بالتفصيل في هذه المقالة.

###  **تنسيق الصفوف والأعمدة**

 Aspose.Cells يوفر فئة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) توفر المجموعة أ[**الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)مجموعة.

###  **كيفية تنسيق صف**

 كل عنصر في[**الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) جمع يمثل أ[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row) هدف. ال[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row)يقدم الكائن[**تطبيق ستايل**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) الطريقة المستخدمة لتعيين تنسيق الصف. لتطبيق نفس التنسيق على صف، استخدم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)هدف. توضح الخطوات أدناه كيفية استخدامه.

1.  أضف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يعترض على[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة عن طريق استدعاء لها[**كريت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)طريقة.
1.  تعيين[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)خصائص الكائن لتطبيق إعدادات التنسيق.
1.  قم بتشغيل السمات ذات الصلة لـ[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)هدف.
1.  تعيين تكوينه[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يعترض على[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row)هدف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **كيفية تنسيق العمود**

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) توفر المجموعة أيضًا أ[**أعمدة**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) مجموعة. كل عنصر في[**أعمدة**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) جمع يمثل أ[**عمود**](https://reference.aspose.com/cells/net/aspose.cells/column) هدف. تشبه أ[**صف**](https://reference.aspose.com/cells/net/aspose.cells/row) الكائن،[**عمود**](https://reference.aspose.com/cells/net/aspose.cells/column) يقدم الكائن أيضًا[**تطبيق ستايل**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)طريقة تنسيق العمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/net/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/net/cells-border-settings/)
- [قم بتعيين التنسيقات الشرطية لملفات Excel وODS.](/cells/ar/net/conditional-formatting/)
- [سمات وألوان Excel](/cells/ar/net/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/net/cells-fill-settings/)
- [إعدادات الخط](/cells/ar/net/cells-font-settings/)
- [تنسيق ورقة العمل Cells في مصنف](/cells/ar/net/format-worksheet-cells-in-a-workbook/)
- [تطبيق نظام التاريخ 1904](/cells/ar/net/implement-1904-date-system/)
- [دمج وفك Cells](/cells/ar/net/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/net/cells-number-settings/)
- [الحصول على النمط وتعيينه للخلايا](/cells/ar/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

