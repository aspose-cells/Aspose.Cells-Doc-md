---
title: قراءة ملف CSV بعدة ترميزات باستخدام Node.js عبر C++
linktitle: قراءة ملف CSV بترميزات متعددة
type: docs
weight: 200
url: /ar/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: تعلّم كيفية قراءة ملفات CSV ذات الترميزات المتعددة باستخدام Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

أحيانًا، يحتوي ملف CSV الخاص بك على ترميزات متعددة (Unicode، ANSI، UTF8، UTF7، وغيرها). تتيح لك Aspose.Cells تحميل مثل هذه الملفات وتحويلها إلى تنسيقات أخرى، مثل PDF أو XLSX.

{{% /alert %}}

توفر Aspose.Cells الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--)، والتي تحتاج إلى ضبطها على **true** لتحميل ملف CSV الخاص بك مع ترميزات متعددة بشكل صحيح.

يوضح اللقطة الشاشية التالية ملف CSV عينة يحتوي على سطرين. السطر الأول بترميز **ANSI** والسطر الثاني بترميز **Unicode**.

|**ملف الإدخال**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV أعلاه دون ضبط الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) على **true**. كما ترى، لم يتم تحويل النص Unicode بشكل صحيح.

|**ملف الإخراج 1: لم يتم اتخاذ إجراءات للتعامل مع الترميز المتعدد**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

تظهر الصورة التالية ملف XLSX الذي تم تحويله من ملف CSV السابق بعد ضبط الخاصية [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) على **true**. كما ترى، النص الداخلي Unicode الآن تم تحويله بشكل صحيح.

|**ملف الإخراج 2: تم تعيين IsMultiEncoded على true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

أدناه الكود النموذجي الذي يحول ملف CSV أعلاه إلى صيغة XLSX بشكل صحيح.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## مقالات ذات صلة

- [فتح ملفات CSV](/cells/ar/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="nodejs-cpp" >}}
