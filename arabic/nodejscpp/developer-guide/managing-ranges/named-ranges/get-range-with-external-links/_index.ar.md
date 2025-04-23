---
title: الحصول على النطاق المرتبط بروابط خارجية باستخدام Node.js عبر C++
linktitle: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 120
url: /ar/nodejs-cpp/get-range-with-external-links/
description: تعلم كيف تحصل على النطاقات مع روابط خارجية باستخدام Aspose.Cells for Node.js via C++. استرجع البيانات من ملفات Excel المختلفة بكفاءة.
---

## **الحصول على نطاق مع روابط خارجية**

في كثير من الأحيان، تصل ملفات Excel إلى البيانات من ملفات Excel أخرى باستخدام روابط خارجية. يوفر Aspose.Cells for Node.js via C++ خيار استرجاع هذه الروابط الخارجية باستخدام طريقة [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-). ترجع طريقة [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). يوفر فئة [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) خاصية [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) التي تعرج عن اسم الملف الخارجي. تعرض فئة [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) الأعضاء التالية.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): عمود النهاية للمنطقة
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): الصف النهائي للمنطقة
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): الحصول على اسم الملف الخارجي إذا كان هذا مرجع خارجي
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): يشير إلى ما إذا كان هذا منطقة
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): يشير إلى ما إذا كان هذا ارتباط خارجي
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): يشير إلى الورقة التي يقع فيها هذا المرجع
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): العمود الابتدائي للمنطقة
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): صف البداية للمنطقة

يوضح رمز النموذج المقدم أدناه استخدام طريقة [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) للحصول على النطاقات ذات الروابط الخارجية.

## **الكود المثالي**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
