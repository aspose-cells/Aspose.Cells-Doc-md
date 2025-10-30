---
title: Congelar la(s) fila(s) superior(es) de la hoja de Excel con Node.js a través de C++
linktitle: Congelar Filas
type: docs
weight: 190
url: /es/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: En este artículo, aprenderás a congelar programáticamente las filas superiores de las hojas de Excel usando la biblioteca con API C++.
keywords: Congelar filas superiores, congelar fila superior en Node.js a través de C++.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar fila(s) superior(es). Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado al desplazarte hacia abajo en la hoja. Puedes congelar la(s) fila(s) superior(es) para que puedas ver esa porción congelada incluso cuando el resto de los datos se desplazan. Puedes ver fácilmente los encabezados en las filas superiores.

## **Congelar Filas en Excel**

**![Congelar fila(s) superior(es) en Excel](Freeze-Rows.png)**

1. Si deseas congelar la(s) fila(s) superior(es), primero selecciona la fila debajo de la fila que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar fila superior.
4. Si te desplazas hacia abajo, la primera fila siempre estará en la vista superior.

**![Fila congelada](Frozen-Row.png)**

Como puedes ver, la primera fila está congelada; la primera fila siempre permanece en la parte superior de la vista cuando te desplazas hacia abajo.

Congelar filas te permite ver tus datos grandes sin necesidad de mantener visible la etiqueta de la fila.

## **Congelar filas con Aspose.Cells for Node.js via C++**
Es simple bloquear fila(s) con Aspose.Cells for Node.js via C++. 
Por favor, usa el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) para bloquear fila(s) en la fila seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Bloquear la primera fila con el método Worksheet.freezePanes().
3. Guarda el archivo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Adjunto [archivo de Excel de muestra](../Freeze.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
