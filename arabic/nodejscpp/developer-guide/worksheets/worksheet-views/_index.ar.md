---
title: طرق عرض ورقة العمل باستخدام node.js عبر C++
linktitle: عروض الورقة العمل
type: docs
weight: 40
url: /ar/nodejs-cpp/worksheet-views/
description: ستصف هذه المقالة كيفية استخدام Node.js وواجهة برمجة التطبيقات الخاصة بـ Node.js للتفاعل مع معاينة فاصل الصفحة لملف Excel وأوراق العمل. العمل مع الألواح المقسمة، الألواح المجمدة، وعامل التكبير.
---

## **معاينة كسر الصفحة**

يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

 العرض العادي هو عرض افتراضي لورقة العمل. معاينة فاصل الصفحة هي عرض تحرير يعرض ورقة العمل كما ستُطبع. تظهر معاينة فاصل الصفحة البيانات التي ستذهب على كل صفحة حتى تتمكن من تعديل منطقة الطباعة وفواصل الصفحة. باستخدام Aspose.Cells for Node.js via C++، يمكن للمطورين تفعيل وضع العرض العادي أو معاينة فاصل الصفحة.

### **التحكم في أوضاع العرض**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

يتمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتمكين العرض العادي أو وضع معاينة فواصل الصفحات، استخدم [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مع [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) هو خاصية منطقية، مما يعني أنه يمكنها تخزين قيمة صحيحة أو خاطئة فقط.

#### **تمكين العرض العادي**

قم بتعيين صفحة العمل إلى العرض العادي عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) الخاصية في فئة [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) إلى **false**.

#### **تمكين معاينة كسر الصفحة**

يمكن تعيين أي صفحة عمل إلى وضع معاينة فواصل الصفحات عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) الخاصية في فئة [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) إلى **true**. بذلك يقوم بتبديل صفحة العمل من العرض العادي إلى معاينة فواصل الصفحات.

يلي أدناه مثال كامل يوضح كيفية استخدام [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) لتمكين وضع معاينة فواصل الصفحات لأول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل من فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). يتم تبديل العرض إلى معاينة فواصل الصفحات لأول ورقة عمل عن طريق ضبط [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) إلى **true**. يتم حفظ الملف المعدل باسم output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **عامل التكبير**

### **استخدام Microsoft Excel**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

### **Aspose.Cells وعامل التكبير**

تسمح Aspose.Cells للمطورين بتعيين عامل تكبير الورقة.
توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

تمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتعيين عامل تكبير الورقة، استخدم [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) في فئة [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--). يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (صحيحة) إلى الخاصية [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--).

 يتضح أدناه مثال كامل يوضح كيفية استخدام الخاصية [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) لضبط عامل التكبير لورقة العمل الأولى في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل للفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). تُعين عامل التكبير للورقة العمل الأولى على 75 ويتم حفظ الملف المعدل ك output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **تجميد الألواح**

### **استخدام Microsoft Excel**

تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

### **Aspose.Cells & تجميد الألواح**

تسمح Aspose.Cells للمطورين بتطبيق تجميد الألواح على ورق العمل أثناء التشغيل.

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة واسعة من الخواص والطرق لإدارة أوراق العمل. لضبط الألواح المجمدة، استدعِ طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) من فئة ورقة العمل. تأخذ طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوح الأيسر.

يتم فتح ملف book1.xls بالاتصال ببناء الفئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) أثناء إنشائه وتجميد عدد قليل من الصفوف والأعمدة في الورقة العمل الأولى. يتم حفظ الملف المعدل ك output.xls.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام الطريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الصفوف والأعمدة (بداية من C4، الممثلة بالصف الرابع والعمود الثالث، حيث الصفوف والأعمدة تبدأ من فهرس 0) من ورقة العمل الأولى لملف Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **تقسيم الألواح**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.

### **تطبيق وإزالة تقسيم الألواح**

#### **تقسيم الألواح**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. لتنفيذ عروض متقسمة، استخدم [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) لفئة [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--). لإزالة تقسيم الألواح، استخدم الطريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

بعد تشغيل الكود أعلاه، سيحتوي الملف الذي تم إنشاؤه على عرض مقسم.

#### **إزالة النوافذ**

قم بإزالة أجزاء الانقسام باستخدام الطريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **مواضيع متقدمة**
- [إخفاء عرض القيم الصفرية في صفحة العمل](/cells/ar/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب الصفحة العمل](/cells/ar/nodejs-cpp/set-worksheet-tab-color/)
- [إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود](/cells/ar/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير](/cells/ar/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [إظهار وإخفاء الأوراق العمل وعلامات التبويب](/cells/ar/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [إظهار الصيغ بدلاً من القيم في ورقة العمل](/cells/ar/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدام خيارات فحص الأخطاء](/cells/ar/nodejs-cpp/use-error-checking-options/)

