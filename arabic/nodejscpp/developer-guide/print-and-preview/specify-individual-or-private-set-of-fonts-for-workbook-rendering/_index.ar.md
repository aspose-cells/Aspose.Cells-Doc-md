---  
title: تحديد مجموعة خطوط فردية أو خاصة لعرض دفتر العمل باستخدام Node.js عبر C++  
linktitle: تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: تعلم كيفية تحديد مجموعات خطوط فردية أو خاصة لعرض دفتر العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

 بشكل عام، تقوم بتحديد دليل الخطوط أو قائمة الخطوط لجميع دفاتر العمل، لكن أحيانًا، يتعين عليك تحديد مجموعة خطوط فردية أو خاصة لدفاتر العمل الخاصة بك. يوفر Aspose.Cells for Node.js via C++ فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) التي يمكن استخدامها لتحديد مجموعة الخطوط الفردية أو الخاصة لدفتر العمل الخاص بك.  

## **تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر**  

يحمّل المثال التالي ملف Excel النموذجي (67338268.xlsx) باستخدام مجموعة خطوط فردية أو خاصة محددة باستخدام فئة [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). يرجى الاطلاع على الخط (67338271.zip) المستخدم داخل الكود وكذلك ملف PDF الناتج (67338269.pdf). يُظهر لقطة الشاشة التالية كيف يبدو ملف PDF الناتج إذا تم العثور على الخط بنجاح.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

