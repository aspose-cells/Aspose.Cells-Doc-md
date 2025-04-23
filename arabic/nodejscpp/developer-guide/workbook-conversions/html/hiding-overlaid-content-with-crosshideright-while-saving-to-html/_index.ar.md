---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML باستخدام Node.js عبر C++
linktitle: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML، يمكنك تحديد أنواع تقاطع مختلفة لسلاسل الخلايا. بشكل افتراضي، يولد Aspose.Cells HTML وفقًا لـ Microsoft Excel، ولكنه عند تغيير نوع التقاطع إلى [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)، فإنه يخفي جميع النصوص على الجانب الأيمن من الخلية التي تتراكب أو تتداخل مع نص الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمِّل الكود النموذجي التالي [ملف إكسل النموذجي](64716894.xlsx) ويحفظه إلى [ملف HTML الإخراجي](64716893.zip) بعد ضبط [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) كـ [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). يشرح لقطة الشاشة كيف يؤثر [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) على ملف HTML الناتج من الوضع الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
