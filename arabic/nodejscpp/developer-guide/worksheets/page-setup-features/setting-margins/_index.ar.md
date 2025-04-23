---
title: تعيين الهوامش باستخدام أعضاء فئة {0} في Node.js عبر C++
linktitle: ضبط الهوامش
type: docs
weight: 20
url: /ar/nodejs-cpp/setting-margins/
description: في هذا المقال، ستتعلم كيفية تعيين هوامش ورقة عمل إكسل باستخدام رمز نموذج. كما تتعلم كيفية تعيين الهوامش برمجياً لمركز الصفحة، الرأس، والتذييل باستخدام API الخاص بـ Node.js عبر C++.
keywords: تعيين هامش ورقة العمل في إكسل إلى المركز باستخدام Node.js عبر C++، وتعيين هامش رأس وتذييل ورقة العمل باستخدام Node.js عبر C++
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تماماً خيارات إعداد الصفحة في Microsoft Excel. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة للوظائف للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

{{% /alert %}}

## **ضبط الهوامش**

 توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

 توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) الخاصية [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) التي تُستخدم لتعيين خيارات إعداد الصفحة لورقة العمل. الخاصية [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) كائن من فئة [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) يتيح للمطورين تعيين خيارات تخطيط الصفحة المختلفة لورقة عمل مطبوعة. تقدم فئة [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) خصائص وأساليب متعددة تستخدم لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

تعيين هوامش الصفحة (يسار، يمين، أعلى، أسفل) باستخدام أعضاء فئة [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--). بعض الطرق تستخدم لتحديد هوامش الصفحة مذكورة أدناه:

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **توسيط على الصفحة**

 من الممكن تمركز شيء ما بشكل أفقي وعمودي على الصفحة. لهذا، هناك بعض الأعضاء المفيدة في فئة [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)، [**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--) و [**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **هوامش الرأس والتذييل**

تعيين هوامش الرأس والتذييل مع أعضاء فئة [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) مثل [**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--) و [**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
