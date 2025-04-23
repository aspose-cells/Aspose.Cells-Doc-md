---
title: ابحث عن اسم العنصر الجذر لخريطة XML باستخدام node.js عبر C++
linktitle: العثور على اسم العنصر الجذري لخريطة XML
type: docs
weight: 30
url: /ar/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: تعلم كيف تجد اسم العنصر الجذر لخريطة XML في Excel باستخدام Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك العثور على *اسم العنصر الجذر لخريطة XML* باستخدام Aspose.Cells for Node.js via C++ مع خاصية [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). يُظهر لقطة الشاشة التالية اسم العنصر الجذر لخريطة XML في Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **الكود المثالي**

تحميل الكود النموذجي التالي لملف Excel التجريبي الخاص بك والوصول إلى خريطة XML الأولى وطباعة خاصية [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). يُرجى مراجعة مخرجات وحدة التحكم للكود النموذجي أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **مخرجات الوحدة**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
