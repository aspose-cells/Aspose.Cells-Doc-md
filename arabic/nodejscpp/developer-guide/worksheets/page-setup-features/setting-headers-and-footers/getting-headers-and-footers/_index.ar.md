---
title: الحصول على رؤوس وتذييلات مع Node.js عبر C++
linktitle: الحصول على رؤوس أو تذييلات
type: docs
weight: 30
url: /ar/nodejs-cpp/get-headers-or-footers/
description: توضح هذه المقالة كيفية الحصول على رؤوس وتذييلات من ملفات Excel أو OpenOffice برمجيًا باستخدام API أو مكتبة Node.js عبر C++.
---

{{% alert color="primary" %}}

يتم عرض الرؤوس والتذييلات فقط في عرض تخطيط الصفحة ومعاينة الطباعة وعلى الصفحات المطبوعة. 

يمكنك أيضًا استخدام مربع حوار إعداد الصفحة إذا كنت ترغب في عرض الرؤوس أو التذييلات لأكثر من ورقة عمل في نفس الوقت. 

بالنسبة لأنواع الورق الأخرى، مثل ورقات الرسومات أو الرسوم البيانية، يمكنك إدراج رؤوس وتذييلات فقط عن طريق مربع حوار إعداد الصفحة.

{{% /alert %}}

## **الحصول على رؤوس وتذييلات في برنامج إكسل**
1. انقر على ورقة العمل حيث ترغب في عرض أو تغيير الرؤوس أو التذييلات.
2. على علامة التبويب عرض، في مجموعة عروض دفتر العمل، انقر فوق تخطيط الصفحة.
   يعرض إكسل ورقة العمل في وضع تخطيط الصفحة.
3. لعرض أو تحرير رأس أو تذييل، انقر على مربع النص للرأس أو التذييل في اليسار، وسط، أو اليمين في الجزء العلوي أو السفلي من صفحة الورقة (تحت رأس، أو فوق تذييل).


## **الحصول على رؤوس وتذييلات باستخدام Aspose.Cells for Node.js via C++**
باستخدام طرق [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) و [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-)، يمكن لمطوري Node.js ببساطة الحصول على رؤوس أو تذييلات من الملف.

1. إنشاء دفتر عمل لفتح الملف.
2. الحصول على ورقة العمل التي تريد الحصول على رؤوس أو تذييلات منها.
3. الحصول على الرأس أو التذييل مع معرف قسم محدد.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **تحليل رؤوس وتذييلات إلى قائمة الأوامر**
يمكن أن تحتوي نصوص الرأس أو التذييل على أوامر خاصة، على سبيل المثال، عنصر نائب لرقم الصفحة، التاريخ الحالي، أو سمات تنسيق النص.

تمثل الأوامر الخاصة بواسطة حرف واحد مع علامة واصلة في المقدمة ("&")

يتم بناء سلاسل الرأس والتذييل باستخدام قواعد ABNF. وليس من السهل فهمها بدون عارض.

يقدم Aspose.Cells for Node.js via C++ [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) طريقة لتحليل رؤوس وتذييلات كقائمة أوامر.

الرموز التالية توضح كيفية تحليل الرأس أو التذييل كقائمة أوامر ومعالجة الأوامر:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
