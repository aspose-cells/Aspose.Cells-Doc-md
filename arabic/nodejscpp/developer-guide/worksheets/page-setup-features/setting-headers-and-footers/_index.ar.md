---
title: تعيين رؤوس وتذييلات مع Node.js عبر C++
linktitle: ضبط رؤوس وأسافل
type: docs
weight: 30
url: /ar/nodejs-cpp/setting-headers-and-footers/
description: يوضح هذا المقال كيفية إدراج صورة برمجياً في رأس وتذييل أوراق عمل إكسل باستخدام Aspose.Cells for Node.js via C++. 
keywords: إدراج صورة في رأس وتذييل إكسل باستخدام Node.js عبر C++، تعيين أوامر سكريبت الرأس والتذييل في إكسل باستخدام Node.js عبر C++
---

{{% alert color="primary" %}}

رؤوس وأسافل هي سطور النص المعروضة أسفل هامش الأعلى أو أعلى الهامش على التوالي. يمكن إضافة رؤوس وأسافل إلى الأوراق العمل أيضًا. يمكن استخدام رؤوس وأسافل لعرض معلومات مفيدة مثل رقم الصفحة أو اسم المؤلف أو اسم الموضوع أو التاريخ والوقت. يتم إدارة الرؤوس والأسافل باستخدام إعدادات تخطيط الصفحة.

{{% /alert %}}

## **ضبط رؤساء الصفحات وتذايلها**

 يسمح لك Aspose.Cells for Node.js via C++ بإضافة رؤوس وتذييلات إلى أوراق العمل في وقت التشغيل ولكن نوصي بضبط الرؤوس والتذييلات يدويًا في ملف مُجهز للطباعة. يمكنك استخدام Microsoft Excel كأداة بواجهة المستخدم لضبط الرؤوس والتذييلات لتوفير الجهد ووقت التطوير. يمكن لـ Aspose.Cells استيراد الملف وحفظ الإعدادات.

لإضافة رؤوس وتذييلات بناءً على النموذج، يوفر Aspose.Cells استدعاءات API خاصة وأوامر سكريبت لتنسيق الرؤوس والتذييلات.

### **أوامر السكريبت**

أوامر السكريبت هي أوامر خاصة تسمح لك بتعيين تنسيقات الرأس والتذييل.

| **أوامر السكريبت** | **الوصف** |
| :- | :- |
|&P| - رقم الصفحة الحالية
|&G| - صورة
|&N| - مجموع عدد الصفحات
|&D| - التاريخ الحالي
|&T| - الوقت الحالي
|&A| - اسم ورقة العمل
|&F| - اسم الملف بدون مساره
|&&Text|يعرض &Text. على سبيل المثال: &&WO سيتم عرضه كـ &WO|
|&"\<FontName>"| - يمثل اسم الخط. على سبيل المثال: &"Arial"
|&"\<FontName>, \<FontStyle>"| - يمثل اسم الخط بالنمط. مثال: &"Arial,Bold"
|&\<FontSize>| - يمثل حجم الخط. على سبيل المثال: “&14abc”. ولكن، إذا تبعت هذه الأمر برقم عادي يتم طباعته في الرأس، يجب أن يتم فصله بحرف مسافة عن حجم الخط. على سبيل المثال: “&14 123”.

### **تعيين رؤوس وتذييلات**

 توفر فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) طريقتين، [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) و [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-)، لإضافة رأس وتذييل إلى ورقة عمل. تأخذ هذه الطرق وسيطين فقط:

- **القسم** – القسم الذي يجب وضع الرأس أو التذيل فيه. هناك ثلاثة أقسام: اليسار، الوسط، واليمين، يُمثلون بالترتيب 0، 1، و2.
- **السكريبت** – السكريبت الذي يجب استخدامه للرأس أو التذيل. يتضمن هذا السكريبت أوامر سكريبت لتنسيق الرؤوس أو التذيلات.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **إدراج صورة في رأس أو تذيل**

 تحتوي فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) على طريقتين إضافيتين، [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) و [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-)، لإضافة الصور إلى الرأس والتذييل. تأخذ هذه الطرق المعلمات:

- **القسم** – القسم الخطوط العليا أو السفلية حيث سيتم وضع الصورة. هناك ثلاثة أقسام، اليمين، الوسط واليسار، يُمثلها القيم 0، 1 و 2 على التوالي.
- **مصفوفة بايت** – البيانات الرسومية (يجب كتابة البيانات الثنائية في مخزن مصفوفة بايت).

بعد تنفيذ الكود أدناه وفتح الملف، تحقق من رأس الصفحة في ورقة العمل عن طريق:

1. في قائمة **ملف**, حدد **إعداد الصفحة**. سيتم عرض مربع حواري.
1. حدد علامة التبويب **رأس / تذييل**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
