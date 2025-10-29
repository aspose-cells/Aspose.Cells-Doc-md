---
title: تنسيق الخلايا باستخدام Node.js عبر C++
description: تعلم كيفية تنسيق وتجميل الخلايا في Aspose.Cells for Node.js via C++، بما في ذلك تنسيق الأرقام، تنسيق التاريخ، أنماط الخط، وخيارات نمط الخلية الأخرى. ستساعدك دليلك على إنشاء جداول بيانات جذابة واحترافية المظهر.
keywords: Aspose.Cells for Node.js via C++، تنسيق الخلايا، التجميل، تنسيق الأرقام، تنسيق التاريخ، نمط الخط، خيارات نمط الخلية، جدول بيانات، إنشاء، مظهر احترافي، تنسيق الصفوف والأعمدة.
linktitle: تنسيق الخلايا
type: docs
weight: 120
url: /ar/nodejs-cpp/cells-formatting/
---

## **مقدمة**

{{% alert color="primary" %}}

يوفر Aspose.Cells الطرق [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) و[**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) من فئة [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)، المستخدمة للحصول على/تعيين نمط تنسيق الخلية. كما توفر Aspose.Cells فئة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{% /alert %}}

## **كيفية تنسيق الخلايا باستخدام أساليب GetStyle و SetStyle**

تطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو الأمامية، الحدود، الخطوط، المحاور الأفقية والعمودية، مستوى المسافة البادئة، اتجاه النص، زاوية الدوران والمزيد.

### **كيفية استخدام أساليب GetStyle و SetStyle**

إذا كان المطورون بحاجة إلى تطبيق أنماط تنسيق مختلفة على خلايا مختلفة، فمن الأفضل استرجاع [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) للخلية عبر طريقة [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)، تحديد سمات النمط، ثم تطبيق التنسيق باستخدام طريقة [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-). يُعطى المثال أدناه ليوضح هذا النهج لتطبيق تنسيقات متنوعة على خلية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **كيفية استخدام كائن النمط لتنسيق خلايا مختلفة**

إذا كان المطورون بحاجة إلى تطبيق نمط تنسيق نفسه على خلايا مختلفة، يمكنهم استخدام كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). يرجى اتباع الخطوات أدناه لاستخدام كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style):

1. أضف كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) عن طريق استدعاء طريقة [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) الخاصة بفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)
2. الوصول إلى كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) المضاف حديثًا
3. تعيين الخصائص/السمات المرغوبة لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) لتطبيق الإعدادات التنسيقية المطلوبة
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) المُعدّل للخلايا المرغوبة

يمكن أن يحسن هذا النهج بشكل كبير كفاءة تطبيقاتك ويوفر ذاكرة أيضًا.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **كيفية استخدام أنماط Microsoft Excel 2007 المحددة مسبقًا**

إذا كنت بحاجة لتطبيق أنماط تنسيق مختلفة لـ Microsoft Excel 2007، فقم بتطبيق الأنماط باستخدام واجهة برمجة التطبيقات Aspose.Cells. يُظهر المثال التالي هذا النهج لتطبيق نمط محدد مسبقًا على خلية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **كيفية تنسيق الأحرف المحددة في خلية**

تشرح التعامل مع إعدادات الخط كيفية تنسيق النص في الخلايا، لكنها تشرح فقط كيفية تنسيق كل مضمون الخلية. ماذا إذا كنت ترغب في تنسيق الأحرف المحددة فقط؟

يدعم Aspose.Cells هذه الميزة أيضًا. يوضح هذا الموضوع كيفية استخدام هذه الميزة بشكل فعال.

### **كيفية تنسيق الأحرف المحددة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف إكسل من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل الورقة بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). يمثل كل عنصر في مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) كائن من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

تقدم فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) طريقة [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) التي تستقبل المعلمات التالية لاختيار نطاق من الأحرف داخل خلية:

- **فهرس البداية**, وهو فهرس الحرف الذي يبدأ منه التحديد.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

تعيد طريقة [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) نسخة من فئة [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) التي تسمح للمطورين بتنسيق الأحرف بنفس طريقة تنسيق خلية كما هو موضح أدناه في مثال التعليمات البرمجية. في الملف الناتج، في خلية A1، سيتم تنسيق كلمة 'Visit' باستخدام الخط الافتراضي ولكن 'Aspose!' بخط عريض وأزرق.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

إذا كنت مهتمًا بتنسيق جزء من النص الغني في خلية، فكر في استخدام طريقتي [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) و [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). تُستخدم طريقة [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) للوصول إلى أجزاء النص، ثم يمكن إجراء التعديلات باستخدام طريقة [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)، بينما تُرجع طريقة **Get** مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) يمكن التلاعب بها لكي تعيين خصائص مختلفة مثل اسم الخط، لون الخط، العريض، إلى آخره، ويمكن استخدام طريقة **Set** لتطبيق التغييرات.

{{% /alert %}}

## **كيفية تنسيق الصفوف والأعمدة**

في بعض الأحيان، يحتاج المطورون إلى تطبيق نفس التنسيق على الصفوف أو الأعمدة. تطبيق التنسيق على الخلايا واحدة تلو الأخرى غالبًا ما يستغرق وقتا أطول وليس حلا جيدًا.
لحل هذه المشكلة، يوفر Aspose.Cells طريقة بسيطة وسريعة يتم مناقشتها بالتفصيل في هذا المقال.

### **تنسيق الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف إكسل من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). توفر مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) مجموعة [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--).

### **كيفية تنسيق صف**

كل عنصر في مجموعة [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) يمثل كائن [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row). يوفر كائن [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) المستخدمة لضبط تنسيق الصف. لتطبيق التنسيق نفسه على صف، استخدم كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). تظهر الخطوات أدناه كيفية استخدامه.

1. أضف كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) إلى فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) عن طريق استدعاء طريقة [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--).
2. تعيين خصائص كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) لتطبيق إعدادات التنسيق.
3. تفعيل السمات ذات الصلة على كائن [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).
4. تعيين كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) المُعدّل إلى كائن [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **كيفية تنسيق عمود**

توفر مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) أيضًا مجموعة [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--). يمثل كل عنصر في مجموعة [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) كائن [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column). مماثل لكائن [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)، توفر كائن [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) أيضًا طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) لتنسيق عمود.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/nodejs-cpp/cells-alignment-settings/)
- [إعدادات الحدود](/cells/ar/nodejs-cpp/cells-border-settings/)
- [ضبط الصيغ الشرطية لملفات Excel وODS.](/cells/ar/nodejs-cpp/conditional-formatting/)
- [ثيمات وألوان Excel](/cells/ar/nodejs-cpp/excel-themes-and-colors/)
- [إعدادات التعبئة](/cells/ar/nodejs-cpp/cells-fill-settings/)
- [إعدادات الخطوط](/cells/ar/nodejs-cpp/cells-font-settings/)
- [تنسيق خلايا ورق عمل في بيان عمل](/cells/ar/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [تنفيذ نظام التاريخ 1904](/cells/ar/nodejs-cpp/implement-1904-date-system/)
- [دمج وفصل الخلايا](/cells/ar/nodejs-cpp/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/nodejs-cpp/cells-number-settings/)
- [الحصول على وتعيين النمط للخلايا](/cells/ar/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="nodejs-cpp" >}}
