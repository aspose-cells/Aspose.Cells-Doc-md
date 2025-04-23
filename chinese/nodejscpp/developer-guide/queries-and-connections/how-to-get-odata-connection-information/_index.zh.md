---
title: 如何通过Node.js和C++获取OData连接信息
linktitle: 如何获取OData连接信息
type: docs
weight: 60
url: /zh/nodejs-cpp/how-to-get-odata-connection-information/
description: 学习如何使用Aspose.Cells for Node.js via C++提取Excel文件中的OData连接信息。
---

## **获取OData连接信息**

在某些情况下，开发者需要从Excel文件中提取OData信息。Aspose.Cells for Node.js via C++提供[**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--)属性，可返回Excel文件中的DataMashup信息。这些信息由[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)类表示。[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)类提供[**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--)属性，返回[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)集合。通过[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)，可以访问[**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula)和[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem)。

以下代码片段演示了使用这些类来检索OData信息。

以下代码片段中使用的源文件，请参考附件。

[源文件](96928098.xlsx)

### **示例代码**

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

### **控制台输出**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
