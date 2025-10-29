---
title: تنسيق الخلايا
description: تعلم كيفية تنسيق وتجميل الخلايا في Aspose.Cells for Python via .NET، بما في ذلك تنسيق الأرقام، تنسيق التاريخ، أنماط الخط، وخيارات تنسيق الخلايا الأخرى. سيساعدك دليلنا على إنشاء جداول بيانات جذابة وذات مظهر احترافي.
keywords: Aspose.Cells for Python via .NET، تنسيق الخلايا، تصميم، تنسيق الأرقام، تنسيق التاريخ، نمط الخط، خيارات تنسيق الخلايا، جدول بيانات، إنشاء، مظهر احترافي، تنسيق الصفوف والأعمدة.
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/python-net/cells-formatting/
---

## **مقدمة**

{{% alert color="primary" %}}

يقدم Aspose.Cells for Python via .NET طرق [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) و [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) من فئة [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell)، المستخدمة للحصول على/ضبط نمط تنسيق الخلية. كما توفر Aspose.Cells for Python via .NET فئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{% /alert %}}

## **كيفية تنسيق الخلايا باستخدام أساليب GetStyle و SetStyle**

تطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو الأمامية، الحدود، الخطوط، المحاور الأفقية والعمودية، مستوى المسافة البادئة، اتجاه النص، زاوية الدوران والمزيد.

### **كيفية استخدام أساليب GetStyle و SetStyle**

إذا كان المطورون بحاجة لتطبيق أنماط تنسيق مختلفة إلى خلايا مختلفة، فإنه من الأفضل الحصول على [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) للخلية باستخدام الطريقة [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)، تحديد سمات النمط ثم تطبيق التنسيق باستخدام الطريقة [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style). يُظهر المثال التالي هذا النهج لتطبيق تنسيقات مختلفة على خلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **كيفية استخدام كائن النمط لتنسيق خلايا مختلفة**

إذا كان المطورون بحاجة لتطبيق نفس النمط التنسيقي على خلايا مختلفة، فيمكنهم استخدام [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). يرجى اتباع الخطوات التالية لاستخدام [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style):

1. إضافة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) باستدعاء طريقة [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) من فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)
2. الوصول إلى كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) الذي تمت إضافته حديثًا
3. تعيين خصائص/سمات [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) المطلوبة لتطبيق إعدادات التنسيق المرغوبة
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) المكون وتهيئته إلى الخلايا المرغوبة

يمكن أن يحسن هذا النهج بشكل كبير كفاءة تطبيقاتك ويوفر ذاكرة أيضًا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **كيفية استخدام أنماط Microsoft Excel 2007 المحددة مسبقًا**

إذا كنت بحاجة إلى تطبيق أنماط تنسيق مختلفة على Microsoft Excel 2007، استخدم طريقة التطبيق باستخدام API الخاص بـ Aspose.Cells for Python via .NET. يُوضح المثال أدناه كيفية تطبيق نمط معرف مسبقًا على خلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **كيفية تنسيق الأحرف المحددة في خلية**

تشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا، لكنها تشرح فقط كيفية تنسيق كل مضمون الخلية. ماذا إذا كنت ترغب في تنسيق الأحرف المحددة فقط؟

يدعم Aspose.Cells لبايثون via .NET أيضًا هذه الميزة. يشرح هذا الموضوع كيف نستخدم هذه الميزة بشكل فعال.

### **كيفية تنسيق الأحرف المحددة**

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) يمثل كائن من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

توفر الفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) الطريقة [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) التي تأخذ المعلمات التالية لتحديد نطاق الحروف داخل خلية:

- **فهرس البداية**, وهو فهرس الحرف الذي يبدأ منه التحديد.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

تعيد الطريقة [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) مثيلًا للفئة [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) التي تسمح للمطورين بتنسيق الحروف بنفس الطريقة التي يفعلون بها مع الخلية كما هو موضح أدناه في مثال الكود. في ملف الإخراج، في الخلية A1، سيتم تنسيق الكلمة 'زيارة' بالخط الأمامي ولكن كلمة 'Aspose!' ستكون سمينة وزرقاء.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

إذا كنت مهتمًا بتنسيق جزء من نص غني في خلية، فكر في استخدام أساليب [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) & [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). يُستخدم الأسلوب [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) للوصول إلى أجزاء النص ثم يمكن إجراء التعديلات باستخدام أسلوب [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters)، بينما يُرجع أسلوب **Get** مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) يمكن التلاعب بها لتعيين خصائص مختلفة مثل نوع الخط، لون الخط، سمك الخط، وغيرها، ويمكن استخدام أسلوب **Set** لتطبيق التغييرات.

{{% /alert %}}

## **كيفية تنسيق الصفوف والأعمدة**

في بعض الأحيان، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. تطبيق التنسيق على الخلايا واحدة تلو الأخرى غالبًا ما يستغرق وقتا أطول وليس حلا جيدًا.
لمعالجة هذه المشكلة، يوفر Aspose.Cells لبايثون via .NET طريقة بسيطة وسريعة نوقشت بالتفصيل في هذا المقال.

### **تنسيق الصفوف والأعمدة**

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). توفر مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) مجموعة [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows).

### **كيفية تنسيق صف**

كل عنصر في مجموعة [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) يمثل كائن [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row). يقدم كائن [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) الطريقة [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) المستخدمة لتعيين تنسيق الصف. لتطبيق نفس التنسيق على الصف، استخدم كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). توضح الخطوات أدناه كيفية استخدامه.

1. أضف كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) إلى الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) عن طريق استدعاء طريقته [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style).
1. ضبط خصائص كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) لتطبيق إعدادات التنسيق.
1. جعل السمات ذات الصلة ON لكائن [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).
1. تعيين كائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) المكون إلى الكائن [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) المكون.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **كيفية تنسيق عمود**

توفر مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) أيضًا مجموعة [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns). كل عنصر في مجموعة [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) يمثل كائن [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column). على غرار كائن [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)، يقدم كائن [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) أيضًا الطريقة [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) لتنسيق عمود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/python-net/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/python-net/cells-border-settings/)
- [ضبط الصيغ الشرطية لملفات Excel وODS.](/cells/ar/python-net/conditional-formatting/)
- [ثيمات وألوان Excel](/cells/ar/python-net/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/python-net/cells-fill-settings/)
- [إعدادات الخطوط](/cells/ar/python-net/cells-font-settings/)
- [تنسيق خلايا ورق عمل في بيان عمل](/cells/ar/python-net/format-worksheet-cells-in-a-workbook/)
- [تنفيذ نظام التاريخ 1904](/cells/ar/python-net/implement-1904-date-system/)
- [دمج وفصل الخلايا](/cells/ar/python-net/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/python-net/cells-number-settings/)
- [الحصول على وتعيين النمط للخلايا](/cells/ar/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="python-net" >}}
