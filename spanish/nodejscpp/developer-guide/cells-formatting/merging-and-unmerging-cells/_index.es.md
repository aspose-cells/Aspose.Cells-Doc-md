---
title: Combinar y Descombinar Celdas con Node.js a través de C++
linktitle: Fusionar y Desfusionar Celdas
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hojas de cálculo, que soporta combinar y descombinar celdas. Este artículo presentará cómo fusionar y deshacer la fusión de celdas usando la biblioteca Aspose.Cells, con opciones para personalizar el estilo de la celda combinada.
keywords: Aspose.Cells, biblioteca Node.js, hoja de cálculo, fusionar celdas, desfusionar celdas, configuraciones de estilo, estilos personalizados
type: docs
weight: 190
url: /es/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puedes descombinar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango original seleccionado.

{{% /alert %}} 
## **Introducción**
No siempre quieres el mismo número de celdas en cada fila o columna. Por ejemplo, es posible que desees colocar un título en una celda que abarque varias columnas. O, si estás creando una factura, es posible que desees menos columnas para el total. Para hacer una celda a partir de dos o más celdas, combínalas. Microsoft Excel permite a los usuarios seleccionar archivos y combinarlos para estructurar la hoja de cálculo según sus necesidades.

{{% alert color="primary" %}} 

Tenga en cuenta que cuando las celdas están fusionadas, solo se conserva los datos en la celda superior izquierda. Si hay datos en las otras celdas del rango, estos datos se eliminan. El formato, de igual manera, se basa en la celda de referencia, por lo que al fusionar celdas, la configuración de formato de la celda superior izquierda en el rango se aplica a la celda fusionada. Cuando se divide la celda, las nuevas celdas mantienen su configuración de formato original.

{{% /alert %}} 
## **Combina celdas en una hoja de cálculo**
### **Combinar celdas en Microsoft Excel**
Los siguientes pasos describen cómo combinar celdas en la hoja de cálculo utilizando MS Excel.

1. Copie los datos que desea en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea combinar.
1. Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en el icono **Combinar y centrar** en la barra de herramientas **Formato**.

### **Combinar celdas con Aspose.Cells**
La clase Aspose.Cells.Cells tiene algunos métodos útiles para la tarea. Por ejemplo, el método `merge()` fusiona las celdas en una sola dentro de un rango especificado.

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Descombinar (Separar) celdas combinadas**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Seleccione la celda combinada.
   Cuando las celdas se han combinado, **Combinar y centrar** se selecciona en la barra de herramientas **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.

### **Usar Aspose.Cells**
La clase Aspose.Cells.Cells tiene un método llamado `unmerge()` que divide las celdas en su estado original. El método desfusión las celdas usando la referencia de la celda en el rango de celdas fusionadas.

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Temas avanzados**
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
