---
title: Verificar si el proyecto VBA en un libro de trabajo está firmado con Node.js vía C++
linktitle: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 70
url: /es/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aprende cómo verificar si un proyecto VBA en un libro de trabajo está firmado usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Puedes verificar si tu proyecto VBA está firmado o no utilizando Microsoft Excel a través del menú **Herramientas > Firmas Digitales...**. Del mismo modo, puedes verificarlo programáticamente utilizando la propiedad [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) de Aspose.Cells.

{{% /alert %}}

## **Verificar si el proyecto VBA en un libro de trabajo está firmado en Node.js**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado usando la propiedad [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--). La propiedad devolverá **true** si el proyecto está firmado, de lo contrario devolverá **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
