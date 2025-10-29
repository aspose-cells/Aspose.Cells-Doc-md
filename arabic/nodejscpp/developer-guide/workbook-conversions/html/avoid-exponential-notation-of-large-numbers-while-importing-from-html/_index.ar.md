---  
title: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML  
linktitle: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/  
description: تعرف على كيفية منع تحويل الأرقام الكبيرة إلى صيغة الأُس عند الاستيراد من HTML باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

في بعض الأحيان، يحتوي HTML الخاص بك على أرقام مثل 1234567890123456، وهي أطول من 15 رقمًا، وعند استيراد HTML إلى ملف Excel، تتحول هذه الأرقام إلى صيغة الأُس مثل 1.23457E+15. إذا كنت تريد استيراد الرقم كما هو وعدم تحويله إلى صيغة الأُس، يرجى استخدام خاصية [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) وتعيينها إلى **true** أثناء تحميل HTML.  

{{% /alert %}}  

يوضح الرمز النموذجي التالي كيفية استخدام خاصية [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--). ستقوم API باستيراد الرقم كما هو دون تحويله إلى صيغة الأُس.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";

// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);

// Convert byte array into stream
const stream = byteArray;

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
