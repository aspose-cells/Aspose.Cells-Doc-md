---
title: كيفية الحصول على معلومات اتصال OData باستخدام Node.js عبر C++
linktitle: كيفية الحصول على معلومات اتصال OData
type: docs
weight: 60
url: /ar/nodejs-cpp/how-to-get-odata-connection-information/
description: تعلم كيفية استخراج معلومات اتصال OData من ملف Excel باستخدام Aspose.Cells for Node.js via C++.
---

## **الحصول على معلومات اتصال OData**

قد تكون هناك حالات يحتاج فيها المطورون إلى استخراج معلومات OData من ملف Excel. يوفر Aspose.Cells for Node.js via C++ خاصية [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) التي تُرجع معلومات DataMashup الموجودة في ملف Excel. تُعبّر هذه المعلومات عن طريق فئة [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup). توفر فئة [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) الخاصية [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) التي تُرجع مجموعة [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection). من خلال [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)، يمكنك الوصول إلى [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) و[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).

توضح مقتطفات الشفرة التالية استخدام هذه الفئات لاسترداد معلومات OData.

الملف المصدر المستخدم في مقطع الكود التالي مرفق للرجوع إليه.

[الملف المصدر](96928098.xlsx)

### **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ODataSample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const PQFcoll = workbook.getDataMashup().getPowerQueryFormulas();

for (let i = 0; i < PQFcoll.getCount(); i++) {
const PQF = PQFcoll.get(i);
console.log("Connection Name: " + PQF.getName());
const PQFIcoll = PQF.getPowerQueryFormulaItems();

for (let j = 0; j < PQFIcoll.getCount(); j++) {
const PQFI = PQFIcoll.get(j);
console.log("Name: " + PQFI.getName());
console.log("Value: " + PQFI.getValue());
}
}
```

### **مخرجات الوحدة**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
