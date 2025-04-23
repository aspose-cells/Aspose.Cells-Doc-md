---  
title: تحميل دفتر العمل مع حجم ورق الطابعة المحدد عبر Node.js و C++  
linktitle: تحميل الدفتر بحجم ورقة الطابعة المحدد  
type: docs  
weight: 430  
url: /ar/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: تعلم كيفية ضبط حجم ورق الطابعة أثناء تحميل دفتر العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
يمكنك تحديد حجم ورق الطابعة الخاص بك أثناء تحميل دفتر العمل الخاص بك باستخدام الطريقة [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). يُرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورق هو نفس إعداد طابعة الافتراضي في جهازك.  
{{% /alert %}}  

توضح الكود النموذجي التالي استخدام طريقة [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). يتم أولًا إنشاء دفتر عمل، ثم حفظه في تيار الذاكرة بصيغة XLSX، ثم يتم تحميله بحجم ورق A5 ويحفظ في صيغة PDF، ثم يتم تحميله مرة أخرى بحجم ورق A3 ويحفظ مجددًا بصيغة PDF. إذا فتحت ملفات PDF الناتجة وتحققت من حجم الورق، سترى أن أحدهما A5 والآخر A3. يرجى تنزيل ملف PDF الناتج بـ A5 ([A5 output PDF](5115234.pdf)) وملف PDF الناتج بـ A3 ([A3 output PDF](5115233.pdf)) المولدين من قبل الكود للاطلاع.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

