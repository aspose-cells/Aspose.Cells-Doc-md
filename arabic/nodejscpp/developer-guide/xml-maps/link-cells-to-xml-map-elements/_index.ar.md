---
title: ربط الخلايا بعناصر خريطة XML باستخدام node.js عبر C++
linktitle: ربط الخلايا بعناصر خريطة XML
type: docs
weight: 50
url: /ar/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك ربط خلاياك بعناصر خريطة XML باستخدام Aspose.Cells for Node.js via C++. يرجى استخدام طريقة [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) لهذا الغرض.

## **ربط الخلايا بعناصر خريطة XML**

يقوم الكود العيني التالي بتحميل [ملف إكسل المصدري](5115471.xlsx) الذي يحتوي على خريطة XML ومن ثم يربط الخلايا A1، B2، C3، D4، E5، و F6 بعناصر خريطة XML FIELD1، FIELD2، FIELD4، FIELD5، FIELD7، و FIELD8 على التوالي ومن ثم يحفظ سجل العمل في [ملف إكسل المخرجات](5115467.xlsx).

إذا قمت بفتح [ملف إكسل المخرجات](5115467.xlsx) ونقرت على زر المطور > مصدر، سترى الخلايا مرتبطة بعناصر خريطة XML وسيتم إظهارها أيضًا من قبل Microsoft Excel كما هو موضح في هذه الصورة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
