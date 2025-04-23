---
title: Node.js経由でC++を使ってOData接続情報を取得する方法
linktitle: OData接続情報を取得する方法
type: docs
weight: 60
url: /ja/nodejs-cpp/how-to-get-odata-connection-information/
description: ExcelファイルからOData接続情報を抽出する方法を学びます。Aspose.Cells for Node.js via C++ を使用します。
---

## **OData接続情報を取得**

開発者がExcelファイルからOData情報を抽出する必要がある場合があります。Aspose.Cells for Node.js via C++は、Excelファイル内のDataMashup情報を返す[**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--)プロパティを提供します。この情報は[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)クラスによって表されます。[**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup)クラスは、[**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--)プロパティを提供し、[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)コレクションを返します。[**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection)から、[**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula)や[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem)へアクセスできます。

次のコードスニペットは、これらのクラスを使用してOData情報を取得する方法を示しています。

以下のコードスニペットで使用されるソースファイルは参照用に添付されています。

[ソースファイル](96928098.xlsx)

### **サンプルコード**

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

### **コンソール出力**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
