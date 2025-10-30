---
title: Implementación de rangos no secuenciales con Node.js a través de C++
linktitle: Implementando rangos no secuenciales
type: docs
weight: 700
url: /es/nodejs-cpp/implementing-non-sequential-ranges/
description: Aprende cómo crear rangos no secuenciales con nombres usando Aspose.Cells for Node.js via C++. Utiliza de manera efectiva rangos de celdas no adyacentes.
---

{{% alert color="primary" %}} 

Normalmente, los rangos con nombre son rectangulares con celdas continuas y adyacentes entre sí. Pero a veces, puedes necesitar usar un rango de celdas no secuencial en el que las celdas no están adyacentes. Aspose.Cells for Node.js via C++ admite crear un rango con nombre con celdas no adyacentes.

{{% /alert %}} 

El código de muestra a continuación muestra cómo crear un rango con nombre no secuencial con Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a Name for non sequenced range
const index = workbook.getWorksheets().getNames().add("NonSequencedRange");

const name = workbook.getWorksheets().getNames().get(index);

// Creating a non sequence range of cells
name.setRefersTo("=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

// Save the workbook
workbook.save(path.join(dataDir, "Output.out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
