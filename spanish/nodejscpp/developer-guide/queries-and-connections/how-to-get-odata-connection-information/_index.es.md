---
title: Cómo obtener información de conexión OData con Node.js a través de C++
linktitle: Cómo obtener Información de Conexión OData
type: docs
weight: 60
url: /es/nodejs-cpp/how-to-get-odata-connection-information/
description: Aprende cómo extraer información de conexión OData de un archivo Excel usando Aspose.Cells for Node.js via C++.
---

## **Obtener Información de Conexión OData**

Puede haber casos en los que los desarrolladores necesiten extraer información OData del archivo Excel. Aspose.Cells for Node.js via C++ proporciona la propiedad [**Workbook.getDataMashup()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getDataMashup--) que devuelve la información DataMashup presente en el archivo Excel. Esta información está representada por la clase [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup). La clase [**DataMashup**](https://reference.aspose.com/cells/nodejs-cpp/datamashup) ofrece la propiedad [**DataMashup.getPowerQueryFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/datamashup/#getPowerQueryFormulas--) que devuelve la colección [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection). Desde el [**PowerQueryFormulaCollection**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulacollection), puedes acceder a [**PowerQueryFormula**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformula) y [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem).

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información OData.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo de Origen](96928098.xlsx)

### **Código de muestra**

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

### **Salida de la consola**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
