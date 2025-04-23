---
title: حماية أوراق العمل باستخدام Node.js عبر C++
linktitle: حماية الأوراق العمل
type: docs
weight: 10
url: /ar/nodejs-cpp/protecting-worksheets/
description: تعرف على كيفة حماية أوراق العمل في Excel باستخدام Aspose.Cells for Node.js via C++، بما في ذلك حماية الصفوف والأعمدة وخلايا معينة.
---


{{% alert color="primary" %}}

عندما يتم حماية ورقة العمل، يتم تقييد الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال، لا يمكنهم إدخال بيانات، أو إدراج، أو حذف صفوف أو أعمدة، إلخ.

{{% /alert %}}

## **حماية الأوراق العمل**

### **مقدمة**

خيارات الحماية العامة في Microsoft Excel هي:

- المحتويات
- الكائنات
- السيناريوهات

لاتخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فإنها تختلف عن تشفير الملف. بشكل عام ، يعتبر حماية ورقة العمل مناسبة لأغراض العرض. فهي تمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **حماية ورقة العمل**

توفر Aspose.Cells فصل [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) الذي يمثل ملف Excel من Microsoft. يحتوي فصل [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فصل [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

يوفر فصل [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) الطريقة [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) التي تُستخدم لتطبيق الحماية على ورقة العمل. يقبل الأسلوب [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) المعلمات التالية:

- نوع الحماية، نوع الحماية المطبقة على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة تعداد [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype).
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور السابقة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بكلمة مرور بالفعل ، فقط قم بتمرير قيمة فارغة.

تحتوي تعداد [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) على أنواع الحماية المعرفة مسبقًا التالية:

|**أنواع الحماية**|**الوصف**|
| :- | :- |
|All| لا يمكن للمستخدم تعديل أي شيء على هذه الورقة العمل|
|Contents| لا يمكن للمستخدم إدخال بيانات في هذه الورقة العمل|
|Objects| لا يمكن للمستخدم تعديل أجسام الرسم|
|Scenarios| لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|Structure| لا يمكن للمستخدم تعديل الهيكل|
|Windows| تم تطبيق الحماية على النوافذ|
|None| لا يوجد تطبيق للحماية|

المثال أدناه يوضح كيفية حماية ورقة عمل بكلمة مرور.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

بعد استخدام الكود أعلاه لحماية الورقة العمل، يمكنك التحقق من الحماية على الورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى الورقة العمل، ستظهر لك نافذة التالي:

|**تحذير الذي يظهر عندما لا يستطيع المستخدم تعديل الورقة العمل**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

للعمل على الورقة العمل، قم بإلغاء حمايتها عن طريق تحديد **Protection**، ثم **Unprotect Sheet** من عنصر القائمة **Tools**.

بعد اختيار عنصر القائمة Unprotect Sheet، ستفتح نافذة تطالبك بإدخال كلمة المرور حتى تتمكن من العمل على الورقة العمل كما هو موضح أدناه:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **حماية خلايا قليلة في الورقة العمل باستخدام Microsoft Excel**

قد تكون هناك سيناريوهات معينة حيث تحتاج إلى قفل بعض الخلايا فقط في ورقة العمل. إذا كنت تريد قفل خلايا معينة في ورقة العمل، عليك إلغاء قفل جميع الخلايا الأخرى في ورقة العمل. جميع الخلايا في ورقة العمل مهيأة بالفعل للقفل؛ يمكنك التحقق من ذلك بفتح أي ملف Excel في MS Excel والنقر على **Format | Cells...** لعرض مربع حوار **Format Cells** ثم النقر على علامة التبويب **Protection** ورؤية مربع اختيار "Locked" المحدد افتراضيًا.

تشير النقاط التالية إلى كيفية قفل بعض الخلايا باستخدام MS Excel. تنطبق هذه الطريقة على Microsoft Office Excel 97، 2000، 2002، 2003، والإصدارات الأحدث.

1. حدد الورقة العمل بأكملها بالنقر على زر **Select All** (المستطيل الرمادي مباشرة فوق رقم الصف للصف 1 وعند اليسار من حرف العمود A).
2. انقر على **Cells** في قائمة **Format**، ثم انتقل إلى علامة التبويب **Protection**، وقم بإلغاء تحديد مربع **Locked**.
   يفتح هذا جميع الخلايا على ورقة العمل خلاف ذلك.
   إذا كانت الأمر **Cells** غير متاح، فقد يكون بعض أجزاء الورقة العمل مقفلة بالفعل. في القائمة **Tools**، قم بتوجيه المؤشر إلى **Protection**، ثم انقر على **Unprotect Sheet**.
3. حدد فقط الخلايا التي تريد قفلها وكرر الخطوة 2، ولكن هذه المرة حدد خانة الاختيار **مقفلة**.
4. في قائمة **الأدوات**، اشاره إلى **ال protection**، انقر على **Protect Sheet** ثم انقر على **موافق**.
5. في مربع الحوار **حماية الورقة**، لديك خيار تحديد كلمة مرور وتحديد العناصر التي تريد أن يتمكن المستخدمون من تغييرها.

### **حماية بعض الخلايا في ورقة العمل باستخدام Aspose.Cells**

في هذه الطريقة، نستخدم واجهة برمجة التطبيقات Aspose.Cells فقط لأداء المهمة.

مثال: يعرض المثال التالي كيفية حماية بعض الخلايا في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل 3 خلايا (A1، B1، C1) فيها. وأخيرًا، يحمي ورقة العمل. يحتوي كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) إلى true أو false وتطبيق طريقة *Column/Row.applyStyle()* لقفل أو فتح قفل الصف أو العمود بالسمات التي ترغب بها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **حماية صف في ورقة العمل**

يسمح لك Aspose.Cells بقفل أي صف بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) من فئة [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row) لتطبيق [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على صف معين في ورقة العمل. تستقبل هذه الطريقة وسيطين: كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) و [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) الذي يحتوي على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية صف في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل الصف الأول فيها. وأخيرًا، يحمي ورقة العمل. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) إلى true أو false لقفل أو فتح قفل الصف أو العمود باستخدام الكائن [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **حماية عمود في ورقة العمل**

يسمح لك Aspose.Cells بقفل أي عمود بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-) من فئة [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column) لتطبيق [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على عمود معين في ورقة العمل. تستقبل هذه الطريقة وسيطين: كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) و [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) الذي يحتوي على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية عمود في ورقة العمل. يفتح جميع الخلايا في ورقة العمل أولاً ثم يقفل العمود الأول فيها. وأخيرًا، يحمي ورقة العمل. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) على خاصية بوليانية، [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). يمكنك تعيين الخاصية [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) إلى true أو false لقفل أو فتح قفل الصف أو العمود باستخدام الكائن [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **السماح للمستخدمين بتعديل المدى**

يُظهر المثال التالي كيفية السماح للمستخدمين بتعديل مدى محدد في ورقة العمل الخاصة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
