---
title: تغيير خصائص المقسم باستخدام Node.js عبر C++
linktitle: تغيير خصائص المنقي
type: docs
weight: 70
url: /ar/nodejs-cpp/change-slicer-properties/
---

## **سيناريوهات الاستخدام المحتملة**

قد تكون هناك حالات تريد فيها تغيير خصائص المقسم مثل الموضع أو ارتفاع الصف. يوفر لك Aspose.Cells for Node.js via C++ خيار تحديث هذه الخصائص.

## **تغيير خصائص المنقي**

يرجى الاطلاع على الكود العيني التالي. يحمل [ملف Excel العيني](sampleCreateSlicerToExcelTable.xlsx) الذي يحتوي على جدول. ينشئ بعد ذلك المنقي بناءً على العمود الأول ويقوم بتغيير خصائصه مثل ارتفاع الصف، العرض، القابلية للطباعة، العنوان، وما إلى ذلك. يحفظ المصنف كـ [ملف الإخراج لتغيير خصائص المنقي](outputChangeSlicerProperties.xlsx).

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
