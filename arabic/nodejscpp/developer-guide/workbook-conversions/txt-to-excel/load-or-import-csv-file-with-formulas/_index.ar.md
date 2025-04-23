---  
title: تحميل أو استيراد ملف CSV يحتوي على صيغ باستخدام Node.js  
linktitle: تحميل أو استيراد ملف CSV مع الصيغ  
type: docs  
weight: 350  
url: /ar/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: تعلّم كيفية تحميل واستيراد ملفات CSV التي تحتوي على صيغ باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

يحتوي ملف CSV في الغالب على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك، أحيانًا تحتوي ملفات CSV على صيغ. يجب تحميل مثل هذه الملفات بضبط [خيارات تحميل النص](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) على **true**. بمجرد ضبط هذه الخاصية على **true**، لن تتعامل Aspose.Cells مع الصيغ كنص بسيط، بل ستعاملها كصيغ، وسيقوم محرك حساب الصيغ في Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}}  

يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV مع الصيغ. يمكنك استخدام أي ملف CSV. لأغراض التوضيح، نستخدم [ملف CSV البسيط](5115034.csv) الذي يحتوي على بيانات مثل هذه. كما ترى فإنه يحتوي على صيغة.

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

يتم أولاً تحميل ملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيراً، يتم حفظ مصنف العمل بصيغة XLSX. يبدو ملف XLSX الناتج هكذا. كما ترى، الخلية C3 و F4 تحتويان على صيغ ونتيجتهما 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


