---  
title: تحويل ملف إكسل إلى تنسيق PDF متوافق مع PDF/A 1a باستخدام Node.js عبر C++  
linktitle: تحويل ملف إكسل إلى تنسيق PDF متوافق مع PDF/A 1a  
type: docs  
weight: 130  
url: /ar/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: تعلم كيفية تحويل ملفات Excel إلى ملفات PDF متوافقة مع معيار PDF/A باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

PDF/A هو نوع فريد من PDF مصمم للحفاظ طويل الأمد على المستندات. PDF/A هو إصدار موحد من معيار ISO لتنسيق المستندات المحمولة (PDF) والذي يتضمن جميع الخطوط المستخدمة في المستند داخل ملف PDF. يختلف PDF/A عن PDF بعدم السماح بميزات مثل ربط الخطوط (بخلاف تضمين الخطوط) والتشفير. يتيح لك Aspose.Cells for Node.js via C++ حفظ ملفات Excel كملفات PDF متوافقة مع PDF/A (يشمل PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، و PDF/A-3u). يوضح هذا الموضوع كيفية حفظ مصنف Excel على أنه ملف PDF متوافق مع PDF/A (PDF/A-1a).  

## **تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a**  

يمكن للمطورين استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) لضبط سمات مختلفة للتحويل. ضبط خصائص مختلفة من فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لملف PDF الناتج. الخاصية الأهم هي [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF / A متوافقة.  

يشرح الكود النموذجي التالي كيفية تحويل ملف Excel إلى صيغة PDF متوافقة مع PDF/A-1a. يرجى الاطلاع على [ملف PDF الناتج](outputCompliancePdfA1a.pdf) والصورة الملتقطة للشاشة لمزيد من المعلومات.  

## **لقطة شاشة**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
