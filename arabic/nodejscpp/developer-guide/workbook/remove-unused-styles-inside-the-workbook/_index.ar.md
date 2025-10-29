---  
title: إزالة الأنماط غير المستخدمة داخل دفتر العمل باستخدام Node.js عبر C++  
linktitle: إزالة الأنماط الغير مستخدمة في دفتر العمل  
type: docs  
weight: 340  
url: /ar/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: تعلّم كيفية إزالة الأنماط غير المستخدمة من دفتر العمل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
تستهلك الأنماط غير المستخدمة في ملفات Excel مساحة وتسبب أيضًا مشاكل في الأداء أثناء التحويل إلى تنسيقات مختلفة مثل PDF و HTML وغيرها. يوفر Aspose.Cells خاصية [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) لإزالة جميع الأنماط غير المستخدمة داخل دفتر العمل.  
{{% /alert %}}  

يوضح الكود التالي طريقة استخدام [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). يقوم الكود بتحميل ملف Excel النموذجي ([ملف القالب](5115520.xlsx)) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم يُدعى **AsposeStyle**؛ سيتم حذف هذا النمط وجميع الأنماط غير المستخدمة الأخرى بعد تشغيل الكود.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
