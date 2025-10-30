---
title: Obtener rango con enlaces externos usando Node.js vía C++
linktitle: Obtener rango con enlaces externos
type: docs
weight: 120
url: /es/nodejs-cpp/get-range-with-external-links/
description: Aprende cómo obtener rangos con enlaces externos usando Aspose.Cells for Node.js via C++. Recupera datos de diferentes archivos de Excel de manera eficiente.
---

## **Obtener Rango con Vínculos Externos**

Muchas veces los archivos de Excel acceden a datos desde otros archivos de Excel mediante enlaces externos. Aspose.Cells for Node.js via C++ ofrece la opción de recuperar estos enlaces externos usando el método [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-). El método [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) devuelve un arreglo de tipo [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). La clase [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) proporciona una propiedad [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) que devuelve el nombre del archivo externo. La clase [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) expone los siguientes miembros.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): La columna final del área
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): La fila final del área
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Obtener el nombre del archivo externo si esta es una referencia externa
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Indica si esto es un área
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Indica si esto es un enlace externo
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Indica en qué hoja está esta referencia
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): La columna inicial del área
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): La fila inicial del área

El código de ejemplo a continuación demuestra el uso del método [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) para obtener Rangos con enlaces externos.

## **Código de muestra**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
