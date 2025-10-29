---
title: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML باستخدام Node.js عبر C++
linktitle: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: تعلم كيفية تمكين خصائص CSS المخصصة عند حفظ ملفات Excel بتنسيق HTML باستخدام Aspose.Cells for Node.js via C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك بتنسيق HTML، في الحالة التي توجد فيها تكرارات متعددة لصورة base64 واحدة، مع الخاصية المخصصة، الحاجة إلى حفظ بيانات الصورة مرة واحدة فقط حتى يتحسن أداء HTML الناتج. يرجى استخدام الخاصية [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) وتعيينها **true** أثناء الحفظ إلى HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML**

يوضح رمز المثال التالي استخدام الخاصية [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). تُظهر لقطة الشاشة تأثير هذه الخاصية عندما لا تكون مُعينة على **true**. يرجى تنزيل [ملف Excel النموذجي](50528260.xlsx) المستخدم في هذا الرمز و[ملف HTML الناتج](50528261.zip) الذي تم توليده للمراجعة.



## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
