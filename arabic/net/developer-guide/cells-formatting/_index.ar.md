---
title: تنسيق الخلايا
description: تعلم كيفية تنسيق وتنسيق الخلايا في Aspose.Cells for .NET، بما في ذلك تنسيق الأرقام، وتنسيق التاريخ، وأنماط الخط، وخيارات أنماط الخلية الأخرى. سيساعدك دليلنا على إنشاء جداول بيانات جذابة وتحترفية.
keywords: Aspose.Cells for .NET، تنسيق الخلية، تنسيقها، تنسيق الأرقام، تنسيق التاريخ، نمط الخط، خيارات نمط الخلية، جدول بيانات، إنشاء، مظهر احترافي، تنسيق الصفوف والأعمدة.
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/net/cells-formatting/
---

## **مقدمة**

{{% alert color="primary" %}}

توفر Aspose.Cells طرق [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) من فئة [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell)، المستخدمة للحصول على/تعيين نمط التنسيق لخلية. توفر Aspose.Cells أيضًا فئة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{% /alert %}}

## **كيفية تنسيق الخلايا باستخدام أساليب GetStyle و SetStyle**

تطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو الأمامية، الحدود، الخطوط، المحاور الأفقية والعمودية، مستوى المسافة البادئة، اتجاه النص، زاوية الدوران والمزيد.

### **كيفية استخدام أساليب GetStyle و SetStyle**

إذا كان المطورون بحاجة لتطبيق أنماط تنسيق مختلفة إلى خلايا مختلفة، فإنه من الأفضل الحصول على [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) للخلية باستخدام الطريقة [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)، تحديد سمات النمط ثم تطبيق التنسيق باستخدام الطريقة [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle). يُظهر المثال التالي هذا النهج لتطبيق تنسيقات مختلفة على خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **كيفية استخدام كائن النمط لتنسيق خلايا مختلفة**

إذا كان المطورون بحاجة لتطبيق نفس النمط التنسيقي على خلايا مختلفة، فيمكنهم استخدام [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). يرجى اتباع الخطوات التالية لاستخدام [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style):

1. إضافة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) باستدعاء طريقة [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) من فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)
2. الوصول إلى كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) الذي تمت إضافته حديثًا
3. تعيين خصائص/سمات [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) المطلوبة لتطبيق إعدادات التنسيق المرغوبة
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) المكون وتهيئته إلى الخلايا المرغوبة

يمكن أن يحسن هذا النهج بشكل كبير كفاءة تطبيقاتك ويوفر ذاكرة أيضًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **كيفية استخدام أنماط Microsoft Excel 2007 المحددة مسبقًا**

إذا كنت بحاجة لتطبيق أنماط تنسيق مختلفة لـ Microsoft Excel 2007، فقم بتطبيق الأنماط باستخدام واجهة برمجة التطبيقات Aspose.Cells. يُظهر المثال التالي هذا النهج لتطبيق نمط محدد مسبقًا على خلية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **كيفية تنسيق الأحرف المحددة في خلية**

تشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا، لكنها تشرح فقط كيفية تنسيق كل مضمون الخلية. ماذا إذا كنت ترغب في تنسيق الأحرف المحددة فقط؟

تدعم Aspose.Cells هذه الميزة أيضًا. يشرح هذا الموضوع كيفية استخدام هذه الميزة بشكل فعال.

### **كيفية تنسيق الأحرف المحددة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة عمل ممثلة بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) يمثل كائنا من الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

توفر الفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) الطريقة [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) التي تأخذ المعلمات التالية لتحديد نطاق الحروف داخل خلية:

- **فهرس البداية**, وهو فهرس الحرف الذي يبدأ منه التحديد.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

تعيد الطريقة [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) مثيلًا للفئة [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) التي تسمح للمطورين بتنسيق الحروف بنفس الطريقة التي يفعلون بها مع الخلية كما هو موضح أدناه في مثال الكود. في ملف الإخراج، في الخلية A1، سيتم تنسيق الكلمة 'زيارة' بالخط الأمامي ولكن كلمة 'Aspose!' ستكون سمينة وزرقاء.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

إذا كنت مهتمًا بتنسيق جزء من Rich Text في خلية، فكر في استخدام الطرق [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) و [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). الطريقة [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) تُستخدم للوصول إلى أجزاء النص وبعد ذلك يمكن إجراء التعديلات باستخدام الطريقة [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) بينما تُعيد الطريقة **Get** مصفوفة من [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) آلاف التي يمكن تلاعبها لتعيين خصائص مختلفة مثل اسم الخط، لون الخط، السميك، إلخ. ويمكن استخدام الطريقة **Set** لتطبيق التغييرات.

{{% /alert %}}

## **كيفية تنسيق الصفوف والأعمدة**

في بعض الأحيان، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. تطبيق التنسيق على الخلايا واحدة تلو الأخرى غالبًا ما يستغرق وقتا أطول وليس حلا جيدًا.
لحل هذه المشكلة، يوفر Aspose.Cells طريقة بسيطة وسريعة يتم مناقشتها بالتفصيل في هذا المقال.

### **تنسيق الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة عمل ممثلة بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows).

### **كيفية تنسيق صف**

كل عنصر في مجموعة [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) يمثل كائن [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row). يقدم كائن [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) الطريقة [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) المستخدمة لتعيين تنسيق الصف. لتطبيق نفس التنسيق على الصف، استخدم كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). توضح الخطوات أدناه كيفية استخدامه.

1. أضف كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) إلى الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) عن طريق استدعاء طريقته [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle).
1. ضبط خصائص كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) لتطبيق إعدادات التنسيق.
1. جعل السمات ذات الصلة ON لكائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).
1. تعيين كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) المكون إلى الكائن [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) المكون.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **كيفية تنسيق عمود**

توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) أيضًا مجموعة [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns). كل عنصر في مجموعة [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) يمثل كائن [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column). على غرار كائن [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)، يقدم كائن [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) أيضًا الطريقة [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) لتنسيق عمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/net/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/net/cells-border-settings/)
- [ضبط الصيغ الشرطية لملفات Excel وODS.](/cells/ar/net/conditional-formatting/)
- [ثيمات وألوان Excel](/cells/ar/net/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/net/cells-fill-settings/)
- [إعدادات الخطوط](/cells/ar/net/cells-font-settings/)
- [تنسيق خلايا ورق عمل في بيان عمل](/cells/ar/net/format-worksheet-cells-in-a-workbook/)
- [تنفيذ نظام التاريخ 1904](/cells/ar/net/implement-1904-date-system/)
- [دمج وفصل الخلايا](/cells/ar/net/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/net/cells-number-settings/)
- [الحصول على وتعيين النمط للخلايا](/cells/ar/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
