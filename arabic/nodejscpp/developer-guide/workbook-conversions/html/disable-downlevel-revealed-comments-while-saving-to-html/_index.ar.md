---
title: تعطيل التعليقات المكشوفة من المستوى الأدنى عند الحفظ إلى HTML باستخدام Node.js عبر C++
linktitle: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: تعلم كيفية تعطيل التعليقات المكشوفة من المستوى الأدنى عند حفظ ملف Excel إلى HTML باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel إلى HTML، تكشف Aspose.Cells عن التعليقات الشرطية من المستوى الأدنى. هذه التعليقات الشرطية ذات صلة في الغالب بالإصدارات القديمة من Internet Explorer وغير ذات صلة بالمتصفحات الحديثة. يمكنك الاطلاع على التفاصيل عبر الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

يتيح لك Aspose.Cells for Node.js via C++ إلغاء ظهور هذه التعليقات المكشوفة من المستوى الأدنى عن طريق تعيين الخاصية [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) إلى **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

يعرض مثال الكود التالي استخدام الخاصية [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). تُظهر لقطة الشاشة تأثير هذه الخاصية عندما لا تكون معدلة إلى true. يرجى تحميل ملف Excel النموذجي المستخدم في هذا الكود وملف HTML الناتج عنه للمرجعة.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
