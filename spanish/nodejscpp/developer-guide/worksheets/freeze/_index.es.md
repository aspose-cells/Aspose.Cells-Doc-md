---  
title: Congelar paneles de hojas de cálculo de Excel con Node.js a través de C++  
linktitle: Congelar paneles  
type: docs  
weight: 190  
url: /es/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: En este artículo, aprenderás cómo congelar paneles de hojas de cálculo de Excel programáticamente usando Aspose.Cells for Node.js via C++.  
keywords: Congelar paneles, congelar ventana.  
---  

## **Introducción**  

En este artículo, aprenderemos Cómo congelar paneles. Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado cuando te desplazas hacia abajo en la hoja de cálculo. Y cada registro contiene muchos datos. Puedes congelar paneles para que puedas ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puedes ver fácilmente los encabezados en las filas superiores o en las primeras columnas. Congelar y descongelar paneles solo cambia la vista de los datos sin modificarlos.  

## **En Excel**  

**![Congelar paneles en Excel](Congelar-paneles.png)**  

1. Si deseas congelar paneles, congelar filas y columnas, primero selecciona una celda (como B2).  
2. Haz clic en Ver > Congelar paneles.  
3. En el menú desplegable, haga clic en Congelar paneles.  
4. Si te desplazas hacia abajo o a la derecha, la primera fila y columna permanecen congeladas.  

**![Paneles congelados](Frozen-Panes.png)**  

Como puedes ver, la primera fila y la columna A están congeladas, la segunda fila es 32 y la segunda columna visible es D.  

Las ventanas congeladas te permiten ver tus datos grandes sin llevar un seguimiento de la fila o etiqueta de columna.  

## **Congelar Paneles con Aspose.Cells for Node.js via C++**  
Es simple congelar paneles con Aspose.Cells for Node.js via C++. Por favor, usa el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) para congelar paneles en la celda seleccionada.  
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.  
2. Congelar paneles con el método Worksheet.freezePanes().  
3. Guarda el archivo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).  

