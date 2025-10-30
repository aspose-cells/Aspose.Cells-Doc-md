---
title: Node.js ve C++ kullanarak OData Bağlantı Bilgisi Nasıl Alınır
linktitle: OData Bağlantı Bilgilerini Nasıl Alınır
type: docs
weight: 60
url: /tr/nodejs-cpp/how-to-get-odata-connection-information/
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel dosyasından OData bağlantı bilgisi nasıl çıkarılır öğrenin.
---

## **OData Bağlantı Bilgilerini Alın**

Bazı durumlarda, geliştiricilerin Excel dosyasından OData bilgisini çıkarması gerekebilir. Aspose.Cells for Node.js via C++, Excel dosyasında bulunan DataMashup bilgisini döndüren [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) özelliği sağlar. Bu bilgi [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) sınıfı ile temsil edilir. [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) sınıfı, [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) özelliği sayesinde [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) koleksiyonunu döndürür. [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) öğesinden [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) ve [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) erişebilirsiniz.

Aşağıdaki kod parçası, bu sınıfları kullanarak OData bilgisini almayı göstermektedir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosyası](96928098.xlsx)

### **Örnek Kod**

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

### **Konsol Çıktısı**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
