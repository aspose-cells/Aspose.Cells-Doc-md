---
title: تعيين خيارات الطباعة باستخدام Node.js عبر C++
linktitle: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/nodejs-cpp/setting-print-options/
description: يوضح هذا المقال كيفية تعيين خيارات الطباعة بشكل برمجي لميزة إعداد صفحة ورقة العمل في Excel باستخدام واجهة برمجة تطبيقات Node.js ومكتبة C++. يمكنك تعيين منطقة الطباعة، عناوين الطباعة، وترتيب الصفحة.
keywords: تعيين منطقة الطباعة في Excel عبر Node.js باستخدام C++، وتعيين عناوين الطباعة، وترتيب الصفحة في Excel عبر Node.js باستخدام C++
---

{{% alert color="primary" %}}

توفر إعدادات تهيئة الصفحة في ميكروسوفت إكسيل العديد من خيارات الطباعة التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل.

{{% /alert %}}

## **ضبط خيارات الطباعة**

تسمح هذه الخيارات بالطباعة:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

يدعم Aspose.Cells for Node.js via C++ جميع خيارات الطباعة التي تقدمها Microsoft Excel، ويمكن للمطورين بسهولة تكوين هذه الخيارات لأوراق العمل باستخدام الخصائص التي تقدمها فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). يُناقش أدناه بالتفصيل كيفية استخدام هذه الخصائص.

### **تعيين منطقة الطباعة**

اف فعل، منطقة الطباعة تشمل جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين تحديد منطقة الطباعة المحددة لورقة العمل.

لتحديد منطقة طباعة محددة، استخدم خاصية [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) لفئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup). قم بتعيين نطاق الخلايا الذي يحدد منطقة الطباعة لهذه الخاصية.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **تحديد عناوين الطباعة**

تسمح Aspose.Cells لك بتعيين تكرار رؤوس الصف والعمود على جميع الصفحات من ورقة العمل المطبوعة. للقيام بذلك، استخدم خاصيتي [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) و [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) لفئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **تحديد خيارات الطباعة الأخرى**

توفر فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) أيضًا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة الشبكة أم لا.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة عناوين الصفوف والأعمدة أم لا.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة ورقة العمل بالألوان الأسود والأبيض أم لا.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): يحدد ما إذا كان سيتم عرض تعليقات الطباعة على ورقة العمل أم في النهاية.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة الورقة بدون رسومات.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هو معروض، فارغ، شرطة أو غير متوفر.

لتعيين خاصيتي [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) و[**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--)، توفر Aspose.Cells for Node.js via C++ أيضًا عددين من القيم المعرفة مسبقًا، [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) و[**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype)، اللذين يحتويان على قيم معرَّفة مسبقًا ليتم تعيينها على الخصائص [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) و[**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) على التوالي.

القيم المعرف بها مسبقًا في التعداد [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) مدرجة أدناه مع أوصافها.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|PrintInPlace|تحدد طباعة التعليقات كما هي معروضة على ورقة العمل.|
|PrintNoComments|تحدد عدم طباعة التعليقات.|
|PrintSheetEnd|تحدد طباعة التعليقات في نهاية ورقة العمل.|

القيم المعرف بها مسبقًا من تعداد [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) مدرجة أدناه مع أوصافها.

| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|PrintErrorsBlank|يحدد عدم طباعة الأخطاء.
|PrintErrorsDash|يحدد طباعة الأخطاء على شكل "--".
|PrintErrorsDisplayed|يحدد طباعة الأخطاء على النحو الذي يتم عرضه.
|PrintErrorsNA|يحدد طباعة الأخطاء على شكل "#N/A".

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **تحديد ترتيب الصفحة**

تقدم فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) الخاصية [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) التي تُستخدم لترتيب صفحات متعددة من ورقة العمل ليتم طباعتها. هناك احتمالان لترتيب الصفحات على النحو التالي.

- **اسفل ثم يمين:** يطبع جميع الصفحات أسفل الصفحة قبل طباعة أي صفحات على اليمين.
- **يمين ثم أسفل:** يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أسفلها.

تقدم Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype)، يحتوي على جميع أنواع الترتيب المعرفة مسبقًا.

القيم المعرفة مسبقًا في تعداد [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) مدرجة أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|DownThenOver|يمثل ترتيب الطباعة كاسفل ثم يمين.
|OverThenDown|يمثل ترتيب الطباعة كيمين ثم أسفل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
