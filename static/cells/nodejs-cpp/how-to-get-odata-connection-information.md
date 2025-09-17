##How to get OData Connection Information with Node.js via C++
Learn how to extract OData connection information from an Excel file using Aspose.Cells for Node.js via C++.
## **Get OData Connection Information**
There might be cases where developers need to extract OData information from the Excel file. Aspose.Cells for Node.js via C++ provides the [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) property which returns the DataMashup information present in the Excel file. This information is represented by the [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) class. The [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) class provides the [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) property that returns the [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection) collection. From the [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection), you can get access to [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) and [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).
The following code snippet demonstrates the use of these classes to retrieve the OData information.
The Source file used in the following code snippet is attached for your reference.
[Source File](96928098.xlsx)
### **Sample Code**
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
### **Console Output**
Connection Name: Orders
Name: Source
Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])
Name: Orders_table
Value: Source{[Name="Orders",Signature="table"]}[Data]
