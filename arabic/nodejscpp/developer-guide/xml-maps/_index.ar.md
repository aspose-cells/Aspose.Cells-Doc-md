---
title: استيراد XML إلى دفتر عمل إكسل باستخدام Node.js عبر C++
linktitle: خرائط XML
type: docs
weight: 210
url: /ar/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: استيراد البيانات من ملفات XML إلى إكسل باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells إمكانية استيراد خريطة XML داخل ملف العمل باستخدام طريقة [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). يمكنك استيراد خريطة XML باستخدام Microsoft Excel وفقًا للخطوات التالية:

- حدد علامة **المطور**
- انقر فوق **استيراد** في القسم XML واتبع الخطوات المطلوبة.

ستحتاج إلى تقديم بياناتك XML لإكمال الاستيراد. إليك [بيانات XML عينية](5115037.txt) يمكنك استخدامها للفحص.

{{% /alert %}}

## **استيراد خريطة XML باستخدام Microsoft Excel**

تُظهر اللقطة الشاشة التالية كيفية استيراد خريطة XML باستخدام Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **استيراد خريطة XML باستخدام Aspose.Cells for Node.js via C++**

يُظهر الكود العينة التالي كيفية استخدام الـ [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). يُولّد ملف الإكسل [الناتج](5115036.xlsx) كما هو موضح في هذه اللقطة الشاشة.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **مواضيع متقدمة**
- [أضف خريطة XML داخل دفتر العمل باستخدام طريقة XmlMapCollection.add()](/cells/ar/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [تصدير البيانات XML المرتبطة بخريطة XML داخل الكتيب](/cells/ar/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [العثور على اسم عنصر الجذر في خريطة XML](/cells/ar/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [ربط الخلايا بعناصر خريطة XML](/cells/ar/nodejs-cpp/link-cells-to-xml-map-elements/)

