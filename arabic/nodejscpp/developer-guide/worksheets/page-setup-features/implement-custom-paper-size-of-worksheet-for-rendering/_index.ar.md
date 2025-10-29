---  
title: تنفيذ حجم ورق مخصص لورقة العمل للطباعة باستخدام Node.js عبر C++  
linktitle: تنفيذ حجم ورق مخصص لورقة العمل للتقديم  
type: docs  
weight: 70  
url: /ar/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: يشرح هذا المقال كيفية استخدام واجهة برمجة تطبيقات Node.js عبر C++ لضبط حجم ورق مخصص لأوراق العمل المطلوبة عند تصدير ملف Excel إلى صيغة PDF برمجياً.  
keywords: تعيين حجم ورق مخصص عند تصدير Excel إلى PDF باستخدام Node.js عبر C++  
---  

## **سيناريوهات الاستخدام المحتملة**  

لا توجد خيار مباشر لإنشاء أحجام ورق مخصصة في MS Excel، ومع ذلك، يمكنك تعيين حجم ورق مخصص لأوراق العمل الخاصة بك عند تصدير ملف Excel إلى صيغة PDF. يوضح هذا المستند كيفية تعيين حجم ورق مخصص لأوراق العمل باستخدام واجهات Aspose.Cells.  

## **تنفيذ حجم ورق مخصص لورقة العمل للتقديم**  

تسمح Aspose.Cells بتنفيذ حجم ورق مخصص للورقة العمل. يمكنك استخدام طريقة [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) من فئة [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) لتحديد حجم صفحة مخصص. يوضح الكود النموذجي التالي كيفية تحديد حجم ورق مخصص لورقة العمل الأولى في دفتر العمل. يرجى أيضًا مراجعة [الإخراج PDF](45056028.pdf) الذي تم توليده باستخدام الكود التالي للمراجعة.  

## **لقطة شاشة**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
