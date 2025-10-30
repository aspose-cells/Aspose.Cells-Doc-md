---  
title: Insertar imágenes y formas en archivos de Excel con Node.js mediante C++  
linktitle: Formas  
type: docs  
weight: 140  
url: /es/nodejs-cpp/insert-shapes/  
description: Gestionar imágenes, objetos OLE y formas en archivos de Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A veces necesitas insertar algunas formas necesarias en la hoja de cálculo. Es posible que necesites insertar la misma forma en diferentes posiciones de la hoja. O que necesites insertar en lote formas en la hoja.  
¡No te preocupes! [Aspose.Cells](https://products.aspose.com/cells/) soporta todas estas operaciones.  
{{% /alert %}}  

Las formas en Excel se dividen principalmente en los siguientes tipos:  
- **Imágenes**  
- **OleObjects**  
- **Líneas**  
- **Rectángulos**  
- **Formas Básicas**  
- **Flechas en Bloque**  
- **Formas de Ecuaciones**  
- **Diagramas de Flujo**  
- **Estrellas y Banderas**  
- **Llamadas**  

Este documento guía seleccionará una o dos formas de cada tipo para hacer muestras. A través de estos ejemplos, aprenderá cómo usar [Aspose.Cells](https://products.aspose.com/cells/) para insertar la forma especificada en la hoja de cálculo.  

## **Agregar imágenes en la hoja de cálculo de Excel usando Node.js**  

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:  
Simplemente llama al método [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) de la colección [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). El método [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) toma los siguientes parámetros:  

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

## **Insertar objetos OLE en la hoja de cálculo de Excel usando Node.js**  

Aspose.Cells soporta agregar, extraer y manipular objetos OLE en hojas de cálculo. Por esta razón, Aspose.Cells tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:  

- La propiedad [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) especifica los datos de la imagen (ícono) de tipo arreglo de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.  
- La propiedad [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) especifica los datos del objeto en forma de un arreglo de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.  

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Insertar una línea en la hoja de cálculo de Excel usando Node.js**  

La forma de la línea pertenece a la categoría **líneas**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Selecciona la celda donde deseas insertar la línea  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la línea de 'Formas usadas recientemente' o 'Líneas'  

![](line.png)  

***Usando Aspose.Cells***  

Puedes utilizar el siguiente método para insertar una línea en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una línea en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](line2.png)  

## **Insertar una flecha de línea en la hoja de cálculo de Excel usando Node.js**  

La forma de la flecha de línea pertenece a la categoría **Líneas**. Es un caso especial de línea.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Seleccione la celda donde desea insertar la flecha de línea  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la flecha de línea de 'Formas usadas recientemente' o 'Líneas'  

![](line_arrow1.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar una flecha de línea en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una flecha de línea en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](line_arrow2.png)  

## **Insertar un rectángulo en la hoja de cálculo de Excel usando Node.js**  

La forma del rectángulo pertenece a la categoría **Rectángulos**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Selecciona la celda donde deseas insertar el rectángulo  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el rectángulo de 'Formas usadas recientemente' o 'Rectángulos'  

![](rectangle.png)  

***Usando Aspose.Cells***  

Puedes utilizar el siguiente método para insertar un rectángulo en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
El método devuelve un objeto [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un rectángulo en una hoja de cálculo.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](rectangle2.png)  

## **Insertar un Cubo en la hoja de cálculo de Excel usando Node.js**  

La forma del cubo pertenece a la categoría **Formas Básicas**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Selecciona la celda donde deseas insertar el cubo  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el Cubo en **Formas Básicas**  

![](cube.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un cubo en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un cubo en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](cube2.png)  

## **Insertar una flecha de cuadro de llamada en la hoja de cálculo de Excel usando Node.js**  

La forma de la flecha de cuadro de llamada pertenece a la categoría **Flechas de Bloques**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Seleccione la celda donde desea insertar la flecha de cuadro de referencia  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la flecha de cuadro de llamada en **Flechas de Bloques**  

![](callout_quad_arrow.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar una flecha de cuadro de referencia en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una flecha de cuadro de llamada en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](callout_quad_arrow2.png)  

## **Insertar un signo de multiplicación en la hoja de cálculo de Excel usando Node.js**  

La forma del signo de multiplicación pertenece a la categoría **Formas de Ecuación**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Seleccione la celda donde desea insertar el signo de multiplicación  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el signo de multiplicación en **Formas de Ecuación**  

![](multiplication_sign.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un signo de multiplicación en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un signo de multiplicación en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](multiplication_sign2.png)  

## **Insertar un multidocumento en la hoja de cálculo de Excel usando Node.js**  

La forma del multidocumento pertenece a la categoría **Diagramas de Flujo**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Seleccione la celda donde desea insertar el multidocumento  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona el multidocumento en **Diagramas de Flujo**  

![](multidocument.png)  

***Usando Aspose.Cells***  

Puedes usar el siguiente método para insertar un multidocumento en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar un multidocumento en una hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](multidocument2.png)  

## **Insertar una estrella de cinco puntas en la hoja de cálculo de Excel usando Node.js**  

La forma de la estrella de cinco puntas pertenece a la categoría **Estrellas y Banderas**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Selecciona la celda donde desees insertar la estrella de cinco puntas  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la estrella de cinco puntas en **Estrellas y Banderas**  

![](star_5_points.png)  

***Usando Aspose.Cells***  

Puedes usar el siguiente método para insertar una estrella de cinco puntas en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una estrella de cinco puntas en una hoja de cálculo.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](star_5_points2.png)  

## **Insertar una nube de burbuja de pensamiento en la hoja de cálculo de Excel usando Node.js**  

La forma de la nube de burbuja de pensamiento pertenece a la categoría **Comentarios**.  

***En Microsoft Excel (por ejemplo, 2007):***  

- Seleccione la celda donde desea insertar el globo de pensamiento  
- Haga clic en el menú Insertar y luego en Formas.  
- Luego, selecciona la nube de burbuja de pensamiento en **Comentarios**  

![](thought_bubble_cloud.png)  

***Usando Aspose.Cells***  

Puede utilizar el siguiente método para insertar un globo de pensamiento en la hoja de cálculo.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
El método devuelve un objeto [Forma](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

El siguiente ejemplo muestra cómo insertar una nube de burbujas en un globo de pensamiento en una hoja de cálculo.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Ejecute el código anterior, obtendrá los siguientes resultados:  

![](thought_bubble_cloud2.png)  

## **Temas avanzados**  
- [Cambiar los valores de ajuste de la forma](/cells/es/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Copiar formas entre hojas de cálculo](/cells/es/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Datos en Forma No Primitiva](/cells/es/nodejs-cpp/data-in-non-primitive-shape/)  
- [Encontrar la Posición Absoluta de la Forma dentro de la Hoja de Trabajo](/cells/es/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Obtener Puntos de Conexión de la Forma](/cells/es/nodejs-cpp/get-connection-points-from-shape/)  
- [Gestionar Controles](/cells/es/nodejs-cpp/managing-controls/)  
- [Agregar Iconos a la Hoja de Trabajo](/cells/es/nodejs-cpp/insert-svg-to-excel/)  
- [Gestionar Objetos OLE](/cells/es/nodejs-cpp/managing-ole-objects/)  
- [Gestionar Imágenes](/cells/es/nodejs-cpp/managing-pictures/)  
- [Gestionar SmartArt](/cells/es/nodejs-cpp/managing-smartart/)  
- [Gestionar Cuadro de Texto](/cells/es/nodejs-cpp/managing-textbox-of-excel/)  
- [Agregar WordArt como Marca de Agua a la Hoja de Trabajo](/cells/es/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Actualizar Valores de Formas Vinculadas](/cells/es/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo](/cells/es/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Gestionar Opciones de la Forma](/cells/es/nodejs-cpp/managing-shape-options/)  
- [Gestionar Opciones de Texto de la Forma](/cells/es/nodejs-cpp/managing-shape-text-options/)  
- [Extensiones Web - Complementos de Office](/cells/es/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
