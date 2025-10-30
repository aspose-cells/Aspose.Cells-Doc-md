---  
title: Gestión de Imágenes con Node.js a través de C++  
linktitle: Gestión de imágenes  
type: docs  
weight: 10  
url: /es/nodejs-cpp/managing-pictures/  
description: Aprende cómo agregar y posicionar imágenes en hojas de cálculo utilizando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells permite a los desarrolladores agregar imágenes a las hojas de cálculo en tiempo de ejecución. Además, la posición de estas imágenes se puede controlar en tiempo de ejecución, lo cual se discute con más detalle en las siguientes secciones.

Este artículo explica cómo agregar imágenes y cómo insertar una imagen que muestra el contenido de ciertas celdas.

## **Añadir imágenes**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:  
Simplemente llama al método [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) de la colección [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). El método [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) toma los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Posicionamiento de imágenes**

Hay dos formas posibles de controlar el posicionamiento de las imágenes usando Aspose.Cells:

- Posicionamiento proporcional: define una posición proporcional a la altura y ancho de la fila.
- Posicionamiento absoluto: define la posición exacta en la página donde se insertará la imagen, por ejemplo, 40 píxeles a la izquierda y 20 píxeles por debajo del borde de la celda.

### **Posicionamiento proporcional**

Los desarrolladores pueden posicionar las imágenes proporcionalmente a la altura de la fila y el ancho de la columna usando las propiedades [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) y [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) del objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Se puede obtener un objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) del conjunto [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) pasando su índice de imagen. Este ejemplo coloca una imagen en la celda F6.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Posicionamiento absoluto**

Los desarrolladores también pueden posicionar las imágenes absolutamente usando las propiedades [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) y [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) del objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Este ejemplo coloca una imagen en la celda F6, a 60 píxeles desde la izquierda y 10 píxeles desde la parte superior de la celda.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Insertar una imagen basada en referencia de celda**

Aspose.Cells te permite mostrar el contenido de una celda de la hoja de cálculo en una forma de imagen. Puedes vincular la imagen a la celda que contiene los datos que deseas mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios que realices en los datos de esa celda o rango de celdas aparecerán automáticamente en el objeto gráfico.

Agrega una imagen a la hoja de cálculo llamando al método [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) del conjunto [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Especifica el rango de celdas usando el atributo [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) del objeto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Temas avanzados**
- [Agregar Iconos Condicionales Establecidos con el Texto de la Celda](/cells/es/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insertar una imagen vinculada desde una dirección web](/cells/es/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Insertar una imagen basada en la referencia de la celda](/cells/es/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Cargar una imagen web desde una URL en una hoja de cálculo de Excel](/cells/es/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
