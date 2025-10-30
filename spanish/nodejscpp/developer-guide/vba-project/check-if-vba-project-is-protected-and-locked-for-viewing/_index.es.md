---
title: Verificar si el proyecto VBA está protegido y bloqueado para visualización con Node.js vía C++
linktitle: Verifique si el Proyecto VBA está Protegido y Bloqueado para Visualización
type: docs
weight: 30
url: /es/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Aprende cómo verificar si un proyecto VBA en un archivo de Excel está protegido y bloqueado para visualización usando Aspose.Cells for Node.js via C++.
---

## Verificar si el proyecto VBA está protegido y bloqueado para visualización en Node.js

Aspose.Cells permite verificar si el proyecto VBA (Visual Basic for Applications) de un archivo de Excel está protegido y bloqueado para visualización. Para ello, la API proporciona la propiedad [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). Si está bloqueado para visualización, entonces la propiedad [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) devuelve **true**.

## **Código de muestra**

El siguiente ejemplo de código carga el [archivo de Excel de ejemplo](43352065.xlsm) y verifica si el proyecto VBA del archivo de Excel está protegido y bloqueado para visualización. También consulta su Salida en Consola para referencia.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Salida de la consola**

Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](43352065.xlsm) proporcionado.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
