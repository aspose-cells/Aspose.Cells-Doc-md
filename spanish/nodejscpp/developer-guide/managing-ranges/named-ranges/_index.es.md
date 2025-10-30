---
title: Crear libros y hojas de cálculo con rangos con nombre en Node.js vía C++
linktitle: Rango con nombre
type: docs
weight: 40
url: /es/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aprende a crear rangos con nombres de alcance en el libro y en la hoja usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de cálculo.

- Los rangos con nombre con ámbito de libro de trabajo se pueden acceder desde cualquier hoja de cálculo dentro de ese libro de trabajo simplemente utilizando su nombre.
- Los rangos con nombre de ámbito de hoja de cálculo se acceden con la referencia de la hoja de cálculo particular en la que se creó.

Aspose.Cells for Node.js via C++ proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombres de alcance en el libro y en la hoja. Al crear un rango con nombre de alcance en la hoja, se debe usar la referencia de la hoja en el rango con nombre para especificarlo como un rango con nombre de alcance en la hoja.

{{% /alert %}} 
## **Agregar un Rango con Nombre de Alcance de Libro**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Agregar un Rango con Nombre de Alcance de Hoja de Cálculo**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Temas avanzados**
- [Crear y Copiar Rangos con Nombre de Acceso](/cells/es/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Formato y Modificación de Rangos con Nombre](/cells/es/nodejs-cpp/format-and-modify-named-ranges/)
- [Obtener Rango con Vínculos Externos](/cells/es/nodejs-cpp/get-range-with-external-links/)
- [Implementación de Rangos No Secuenciales](/cells/es/nodejs-cpp/implementing-non-sequential-ranges/)


{{< app/cells/assistant language="nodejs-cpp" >}}
