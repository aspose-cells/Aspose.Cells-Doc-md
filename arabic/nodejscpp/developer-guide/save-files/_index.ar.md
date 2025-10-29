---
title: طرق مختلفة لحفظ الملفات باستخدام Node.js عبر C++
linktitle: حفظ الملفات
type: docs
weight: 40
url: /ar/nodejs-cpp/different-ways-to-save-files/
description: يمكن لـ Aspose.Cells for Node.js via C++ حفظ الملفات بصيغ مختلفة بما في ذلك PDF و HTML و DOCX و PPTX و JSON و MHTML.
keywords: Aspose.Cells يحفظ Excel كـ PDF و HTML و JSON و CSV و TXT و XML و DOCX و PPTX و MHT و MHTML والمزيد باستخدام Node.js عبر C++.
---

{{% alert color="primary" %}}

‏تجعل Aspose.Cells من الممكن إنشاء الملفات وحفظها. يشرح هذا المقال الطرق المختلفة التي يمكن بها حفظ الملفات.

{{% /alert %}}

## **طرق مختلفة لحفظ الملفات**

توفر Aspose.Cells [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) الذي يمثل ملف Microsoft Excel ويقدم الخصائص والطرق اللازمة للعمل مع ملفات Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) الطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) المستخدمة لحفظ ملفات Excel. تحتوي الطريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) على العديد من التحميلات المفرطة التي تُستخدم لحفظ الملفات بطرق مختلفة.

يتم تحديد تنسيق الملف الذي يتم حفظ الملف به بواسطة التعداد [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)

|**أنواع تنسيق الملفات**|**الوصف**|
| :- | :- |
|CSV|يمثل ملف CSV|
|Excel97To2003| يمثل ملف Excel 97-2003|
||Xlsx| يمثل ملف Excel 2007 XLSX|
||Xlsm| يمثل ملف Excel 2007 XLSM|
||Xltx| يمثل قالب Excel 2007 XLTX|
||Xltm| يمثل ملف Excel 2007 الممكن للتشغيل الآلي XLTM|
|Xlsb| يمثل ملف XLSB بتنسيق Excel 2007 الثنائي
|SpreadsheetML| يمثل ملف XML لجدول بيانات
|TSV|يمثل ملف قيم مفصولة بعلامة التبويب|
|TabDelimited|يمثل ملف نصي بقيم مفصولة بواسطة علامة التبويب|
|ODS|يمثل ملف ODS|
|Html| يمثل ملف HTML
|MHtml| يمثل ملف MHTML
|Pdf| يمثل ملف PDF
|XPS| يمثل مستند XPS
|TIFF| يمثل ملف TIFF

## **كيفية حفظ الملف بتنسيقات مختلفة**

لحفظ الملفات في موقع تخزين، حدد اسم الملف (بالشامل مع مسار التخزين) والتنسيق المطلوب للملف (من تعداد [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)) عند استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) في كائن [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **كيفية حفظ الكتاب الدراسي إلى صيغة PDF**
صيغة المستندات المحمولة (PDF) هي نوع من المستندات التي أنشأتها Adobe في التسعينيات. كان الهدف من هذا التنسيق تقديم معيار لعرض المستندات والمواد المرجعية الأخرى بشكل مستقل عن تطبيقات البرمجيات والأجهزة، بالإضافة إلى نظام التشغيل. يمتلك تنسيق ملف PDF القدرة الكاملة على احتواء معلومات مثل النصوص والصور والروابط التشعبية وحقول النموذج media الغني والتوقيعات الرقمية والمرفقات والبيانات الوصفية والخصائص الجغرافية والميزات ثلاثية الأبعاد الموجودة فيه والتي يمكن أن تصبح جزءًا من المستند المصدر.

يوضح الكود التالي كيفية حفظ دفتر العمل كملف PDF باستخدام Aspose.Cells:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **كيفية حفظ الكتاب الدراسي إلى تنسيق نصي أو CSV**

في بعض الأحيان ، تريد تحويل أو حفظ دفتر عمل بعدة ورقات عمل إلى تنسيق نصي. بالنسبة لتنسيقات النص (مثل TXT، TabDelim، CSV، إلخ) ، يحفظ كل من Microsoft Excel وAspose.Cells افتراضيًا محتويات الورقة العمل النشطة فقط.

يشرح المثال التالي كيفية حفظ دفتر عمل كامل بصيغة نصية. قم بتحميل دفتر العمل المصدر الذي يمكن أن يكون أي ملف جدول بيانات من Microsoft Excel أو OpenOffice (مثل XLS و XLSX و XLSM و XLSB و ODS وغيرها) مع أي عدد من أوراق العمل.

عند تنفيذ الكود ، يتم تحويل بيانات كافة الأوراق في دفتر العمل إلى تنسيق TXT.

يمكنك تعديل نفس المثال لحفظ ملفك بصيغة CSV. بشكل افتراضي، [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) هو فاصلة، لذا لا تحدد فاصلًا إذا كنت تحفظ بصيغة CSV. يرجى ملاحظة: إذا كنت تستخدم النسخة التقييمية وحتى إذا تم تعيين خاصية [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) إلى true، فإن البرنامج سيسمح فقط بتصدير ورقة عمل واحدة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **كيفية حفظ ملف إلى ملفات نصية مع فاصل مخصص**

تحتوي ملفات النص على بيانات جداول بيانات دون تنسيق. الملف هو نوع ملف نصي عادي يمكن أن يحتوي على بعض الفواصل المخصصة بين بياناته.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **كيفية حفظ ملف إلى تيار**

لحفظ الملفات إلى تيار، أنشئ كائن *MemoryStream* أو *FileStream* واحفظ الملف إلى ذلك التيار باستخدام استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) من الكائن [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). حدد تنسيق الملف المطلوب باستخدام تعداد [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) عند استدعاء طريقة [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **كيفية حفظ ملف إكسل إلى ملفات Html و Mht**
يمكن لـ Aspose.Cells حفظ ملف Excel ببساطة كملف HTML و MHTML و JSON و CSV والملفات الأخرى التي يمكن تحميلها بواسطة Aspose.Cells كمصادر ملفات .html و .mht.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **كيفية حفظ ملف إكسل إلى OpenOffice (ODS, SXC, FODS, OTS)**
يمكننا حفظ الملفات بصيغة OpenOffice: ODS و SXC و FODS و OTS وغيرها.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **كيفية حفظ ملف إكسل إلى JSON أو XML**

JSON (JavaScript Object Notation) هو تنسيق ملف مفتوح المعايير لمشاركة البيانات التي تستخدم النص القابل للقراءة من قبل الإنسان لتخزين ونقل البيانات. يتم تخزين ملفات JSON باستخدام الامتداد .json. يتطلب JSON تنسيقًا أقل وهو بديل جيد لـ XML. يتم استخلاص JSON من JavaScript ولكنه تنسيق بيانات مستقل عن اللغة. تدعم العديد من لغات البرمجة الحديثة مولد وتجزئة JSON. application/json هو نوع الوسائط المستخدم لـ JSON.

تدعم Aspose.Cells حفظ الملفات في JSON أو XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **مواضيع متقدمة**
- [ضبط مستوى ضغط الورقة العمل](/cells/ar/nodejs-cpp/adjust-workbook-compression-level/)
- [حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم](/cells/ar/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [حفظ الملف في كائن الاستجابة](/cells/ar/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
