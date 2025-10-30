---
title: Formatear celdas con Node.js a través de C++
description: Aprende cómo formatear y estilo en las celdas en Aspose.Cells for Node.js via C++, incluyendo formateo de números, formateo de fechas, estilos de fuente y otras opciones de estilo de celdas. Nuestra guía te ayudará a crear hojas de cálculo atractivas y de aspecto profesional.
keywords: Aspose.Cells for Node.js via C++, formateo de celdas, estilos, formateo de números, formateo de fechas, estilo de fuente, opciones de estilo de celda, hoja de cálculo, crear, aspecto profesional, formatear filas y columnas.
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/nodejs-cpp/cells-formatting/
---

## **Introducción**

{{% alert color="primary" %}}

Aspose.Cells ofrece los métodos [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) y [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) de la clase [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), usados para obtener/establecer el estilo de formato de una celda. Aspose.Cells también proporciona una clase [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{% /alert %}}

## **Cómo dar formato a las celdas usando los métodos GetStyle y SetStyle**

Aplica diferentes tipos de estilos de formato en las celdas para establecer colores de fondo o primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

### **Cómo utilizar los métodos GetStyle y SetStyle**

Si los desarrolladores necesitan aplicar diferentes estilos de formato a distintas celdas, es mejor obtener el [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) de la celda usando el método [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--), especificar los atributos del estilo y luego aplicar el formato usando el método [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-). A continuación se muestra un ejemplo para demostrar este enfoque de aplicar varios formatos en una celda.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Cómo utilizar el objeto Style para dar formato a diferentes celdas**

Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Por favor, sigue los pasos a continuación para usar el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style):

1. Añadir un objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) llamando al método [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)
2. Acceder al objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) recién añadido
3. Establecer las propiedades/atributos deseados del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) para aplicar la configuración de formato deseada
4. Asignar el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configurado a tus celdas deseadas

Este enfoque puede mejorar significativamente la eficiencia de sus aplicaciones y también ahorrar memoria.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Cómo utilizar los estilos predefinidos de Microsoft Excel 2007**

Si necesita aplicar diferentes estilos de formato para Microsoft Excel 2007, aplique estilos usando la API de Aspose.Cells. A continuación se muestra un ejemplo para demostrar este enfoque de aplicar un estilo predefinido en una celda.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Cómo formatear caracteres seleccionados en una celda**

La sección sobre la configuración de fuentes explica cómo formatear texto en las celdas, pero solo explica cómo formatear todo el contenido de la celda. ¿Qué sucede si desea formatear solo caracteres seleccionados?

Aspose.Cells también soporta esta función. Este tema explica cómo usarla de manera efectiva.

### **Cómo formatear caracteres seleccionados**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene la colección [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) proporciona el método [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- **Índice de inicio**, el índice del carácter desde el que comienza la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

El método [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) devuelve una instancia de la clase [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) que permite a los desarrolladores formatear los caracteres de la misma manera que una celda, como se muestra en el ejemplo de código. En el archivo generado, en la celda A1, la palabra 'Visit' estará formateada con la fuente por defecto, pero 'Aspose!' en negrita y en azul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Si estás interesado en formatear una porción del Texto Enriquecido en una celda, considera usar los métodos [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) & [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). El método [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) se usa para acceder a las porciones del texto y luego se pueden hacer modificaciones usando el método [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-), mientras que el método **Get** devuelve un array de objetos [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) que pueden ser manipulados para establecer varias propiedades como nombre de la fuente, color de fuente, negrita, etc., y el método **Set** se puede usar para aplicar los cambios.

{{% /alert %}}

## **Cómo formatear filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato en celdas una por una a menudo lleva más tiempo y no es una buena solución.
Para abordar este problema, Aspose.Cells proporciona una forma simple y rápida discutida en detalle en este artículo.

### **Formato de filas y columnas**

Aspose.Cells proporciona una clase, la [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) ofrece una colección [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--).

### **Cómo dar formato a una fila**

Cada elemento en la colección [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) representa un objeto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row). El objeto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) ofrece el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) que se usa para establecer el formato de fila. Para aplicar el mismo formato en una fila, usa el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Los pasos a continuación muestran cómo usarlo.

1. Añadir un objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) a la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) llamando a su método [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--).
2. Establecer las propiedades del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) para aplicar la configuración de formato.
3. Activar los atributos relevantes en el objeto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).
4. Asignar el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configurado al objeto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Cómo dar formato a una columna**

La colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) también proporciona una colección [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--). Cada elemento en la colección [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) representa un objeto [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column). Similar a un objeto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), el objeto [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) también ofrece el método [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) para formatear una columna.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Temas avanzados**
- [Configuración de alineación](/cells/es/nodejs-cpp/cells-alignment-settings/)
- [Configuración de bordes](/cells/es/nodejs-cpp/cells-border-settings/)
- [Establecer formatos condicionales de archivos de Excel y ODS.](/cells/es/nodejs-cpp/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/nodejs-cpp/excel-themes-and-colors/)
- [Configuración de relleno](/cells/es/nodejs-cpp/cells-fill-settings/)
- [Configuración de fuente](/cells/es/nodejs-cpp/cells-font-settings/)
- [Dar formato a celdas de hoja de cálculo en un libro de trabajo](/cells/es/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas 1904](/cells/es/nodejs-cpp/implement-1904-date-system/)
- [Combinar y descombinar celdas](/cells/es/nodejs-cpp/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/nodejs-cpp/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="nodejs-cpp" >}}
