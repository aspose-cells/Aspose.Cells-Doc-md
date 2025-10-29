---
title: تصدير بيانات XML المرتبطة بخريطة XML داخل دفتر العمل عبر node.js باستخدام C++
linktitle: تصدير بيانات XML المرتبطة بخريطة XML داخل دفتر العمل
type: docs
weight: 20
url: /ar/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: تعلم كيفية تصدير بيانات XML المرتبطة بخريطات XML داخل دفتر عملك باستخدام Aspose.Cells for Node.js via C++. 
---

## **تصدير البيانات XML المرتبطة بخريطة XML داخل الكتيب**

يرجى استخدام طريقة [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) لتصدير بيانات XML المرتبطة بخريطات XML داخل مصنفك. يوضح الكود النموذجي التالي تصدير بيانات XML لجميع خرائط XML من المصنف واحدة تلو الأخرى. يرجى مراجعة [ملف إكسل النموذجي](5115497.xlsx) المستخدم في هذا الكود و[بيانات XML المصدرة من أول خريطة XML](5472487.xml).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
