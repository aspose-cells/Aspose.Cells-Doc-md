---  
title: إنشاء دفتر عمل مشترك مع Aspose.Cells for Node.js via C++  
linktitle: إنشاء دفتر عمل مشترك باستخدام Aspose.Cells  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: تعلّم كيفية إنشاء دفتر عمل مشترك باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يسمح Microsoft Excel بمشاركة دفتر العمل كما هو موضح في لقطة الشاشة التالية. عند مشاركة دفتر العمل، يمكن لأكثر من مستخدم تحريره على الشبكة. Aspose.Cells for Node.js via C++ يمكّنك من إنشاء دفتر عمل مشترك باستخدام الخاصية [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **إنشاء دفتر عمل مشترك باستخدام Aspose.Cells**  

يخلق الكود النموذجي التالي دفتر عمل مشترك عن طريق تعيين الخاصية [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) كـ **true**. عندما تفتح ملف Excel المخرج ([ملف الإخراج](55541786.xlsx)) في Microsoft Excel، سترى **مشترك** مع اسم دفتر العمل كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **الكود المثالي**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
