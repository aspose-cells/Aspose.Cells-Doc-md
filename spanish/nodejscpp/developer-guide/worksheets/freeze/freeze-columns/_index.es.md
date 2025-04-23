---  
title: Congelar la(s) primera(s) columna(s) de la hoja de Excel con Node.js a través de C++  
linktitle: Congelar Columnas  
type: docs  
weight: 190  
url: /es/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Aprende cómo congelar programáticamente las columnas de la izquierda en las hojas de Excel usando Aspose.Cells for Node.js via C++.  
keywords: Congelar columnas de la izquierda, Congelar primeras columnas, Bloquear la(s) columna(s)  
---  

## **Introducción**  

En este artículo, aprenderemos cómo congelar la(s) columna(s) de la izquierda. Cuando tienes una gran cantidad de datos en una fila, puedes no poder ver las columnas de la izquierda al desplazarte horizontalmente por la hoja. Puedes congelar y bloquear la(s) primera(s) columna(s) para que puedas ver esa porción congelada incluso cuando se desplazan los demás datos. Puedes ver fácilmente los encabezados en las columnas de la izquierda.  

## **Congelar Columnas en Excel**  

**![Congelar columnas izquierdas en Excel](freeze-columns.png)**  

1. Si deseas congelar la(s) columna(s) izquierda(s), primero selecciona la columna debajo de la columna que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar Primera columna.
4. Si te desplazas hacia abajo, la primera columna estará siempre en la vista izquierda.

**![Columna congelada](frozen-columns.png)**  

Como puedes ver, la primera columna está congelada y siempre está bloqueada en la parte superior de la vista cuando te desplazas horizontalmente.

Congelar columnas te permite ver tus datos largos sin preocuparte por mantener visible la primera columna.

## **Congelar columnas con Aspose.Cells for Node.js via C++**  
Es sencillo congelar la(s) primera(s) columna(s) con Aspose.Cells for Node.js via C++.  
Utiliza el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) para congelar columna(s) en la columna seleccionada.  
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera columna con el método Worksheet.freezePanes().
3. Guarda el archivo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).  

