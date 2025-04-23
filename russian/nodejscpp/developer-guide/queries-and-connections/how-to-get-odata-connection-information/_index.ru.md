---
title: Как получить информацию об OData соединениях с помощью Node.js через C++
linktitle: Как получить информацию о подключении OData
type: docs
weight: 60
url: /ru/nodejs-cpp/how-to-get-odata-connection-information/
description: Узнайте, как извлечь информацию о соединении OData из файла Excel с помощью Aspose.Cells for Node.js via C++.
---

## **Получение информации о подключении OData**

Могут возникнуть ситуации, когда разработчикам необходимо извлечь информацию OData из файла Excel. Aspose.Cells for Node.js via C++ предоставляет свойство [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--), которое возвращает информацию DataMashup, содержащуюся в файле Excel. Эта информация представлена классом [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup). Класс [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) обеспечивает свойство [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--), возвращающее коллекцию [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection). Из [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) можно получить доступ к [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) и [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).

В следующем фрагменте кода демонстрируется использование этих классов для извлечения информации OData.

Исходный файл, использованный в следующем фрагменте кода, прикреплен для вашего ознакомления.

[Исходный файл](96928098.xlsx)

### **Образец кода**

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

### **Вывод в консоль**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
