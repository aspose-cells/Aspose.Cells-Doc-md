---
title: أشكال في المخططات باستخدام Node.js عبر C++
linktitle: الأشكال في الرسوم البيانية
description: تعلم كيفية استخدام Aspose.Cells for Node.js via C++ لإضافة عناصر تحكم وتخصيص المخططات في Microsoft Excel. يوضح هذا الدليل كيفية التعامل مع عناصر المخطط، وضبط التنسيق، وتحسين المظهر والوظائف العامة لمخططاتك.
keywords: Aspose.Cells for Node.js via C++، عناصر تحكم المخطط، تخصيص المخطط، Microsoft Excel، عناصر المخطط، التنسيق.
type: docs
weight: 70
url: /ar/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
أحيانًا تحتاج إلى إدراج كائنات الرسم مثل التسميات وصناديق النص والصور وما إلى ذلك في رسم بياني. يمكن لـ Aspose.Cells إضافة عناصر التحكم إلى رسم بياني في وقت التشغيل.
{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لتقديم معلومات للمستخدمين حول محتوى جدول بيانات. تسمح Aspose.Cells لك بإضافة وتلاعب التسميات حتى في الرسوم البيانية.

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) طريقة تسمى [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-) تُستخدَم لإضافة عنصر تحكم تسمية إلى رسم بياني. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- العرض - عرض التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.

تعيد الطريقة كائن [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/). فئة [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) تمثل تسمية في الرسم البياني. لديها بعض الأعضاء المهمة.

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (خاصية) - تحدد سلسلة تسمية التسمية.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (خاصية) - تحدد سمات لون التعبئة.

المثال التالي يوضح كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. وفيما يلي الشفرة الأصلية لإضافة تسمية إلى الرسم البياني. يتم إنشاء الناتج التالي عند تنفيذ الشفرة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

أحد الطرق لتسليط الضوء على معلومات مهمة في تقرير هو استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. توفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) طريقة تسمى [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) ، التي تُستخدم لإضافة عنصر تحكم مربع نص إلى رسم بياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

تُرجع الطريقة كائنًا [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/). صف الفصل [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) يمثل عنصر تحكم مربع نص في الرسم البياني.

المثال التالي يوضح كيفية إضافة مربع نص إلى رسم بياني. يستخدم المثال الملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج مربع نص في الرسم البياني لعرض عنوان الرسم البياني. يتم إنشاء الشفرة الأصلية لإضافة مربع نص إلى الرسم البياني أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **إضافة صورة إلى الرسم البياني**

تسمح Aspose.Cells لك بإدراج الصور في الرسم البياني. على سبيل المثال ، أضف صورة لتسليط الضوء على الرسم البياني أو محتوياته بمعنى أكبر ، أو قم بإدراج ملف صورة العلامة التجارية.

يوفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) طريقة تسمى [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) ، والتي تُستخدم لإضافة كائن صورة إلى الرسم البياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

تُرجع الطريقة كائنًا [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). صف الفصل [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) يمثل كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف التصميمي السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني. أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **إضافة خانة اختيار في الرسم البياني**

تسمح Aspose.Cells بإدراج خانات الاختيار في ورقة الرسم البياني باستخدام تعداد [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/). يوضح المثال التالي إضافة خانة اختيار إلى ورقة الرسم البياني.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_1.jpg)

الملف الناتج (101089316.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **مواضيع متقدمة**
- [إضافة علامة مائية WordArt إلى الرسم البياني](/cells/ar/nodejs-cpp/add-wordart-watermark-to-chart/)

