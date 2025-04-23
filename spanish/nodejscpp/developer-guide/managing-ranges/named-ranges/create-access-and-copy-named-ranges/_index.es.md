---  
title: Crear y copiar rangos nombrados con Node.js a través de C++  
linktitle: Crear y copiar rangos con nombre  
type: docs  
weight: 200  
url: /es/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Aprende cómo crear, acceder y copiar rangos nombrados en Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Introducción**  

Normalmente, las etiquetas de columnas y filas se usan para referirse a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **nombre** puede referirse a una cadena de caracteres que representa una celda, rango de celdas, fórmula o valor constante. Asignar un nombre a un rango significa que ese rango de celdas puede ser referido por su nombre. Usa nombres fáciles de entender, como Productos, para referirte a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas pueden usarse en fórmulas que hacen referencia a datos en la misma hoja; si quieres representar un rango en otra hoja, puedes usar un nombre. *Los rangos nombrados son algunas de las funciones más poderosas de Microsoft Excel, especialmente cuando se usan como rango de origen para controles de listas, tablas dinámicas, gráficos, etc.*  

## **Trabajar con Rangos con Nombre Usando Microsoft Excel**  

### **Crear Rangos con Nombre**  

Los siguientes pasos describen cómo nombrar una celda o rango de celdas usando **MS Excel**. Este método se aplica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** y **2002**.  

1. Selecciona la celda o rango de celdas que deseas nombrar.  
2. Haz clic en la **Caja de nombres** al extremo izquierdo de la barra de fórmulas.  
3. Escribe el nombre para las celdas.  
4. Presiona ENTER.  

{{% alert color="primary" %}}  
No puedes nombrar una celda mientras estás cambiando el contenido de la celda.  
{{% /alert %}}  

## **Trabajar con Rangos con Nombre Usando Aspose.Cells**  

Aquí, usamos la API de Aspose.Cells para realizar la tarea.  
Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite el acceso a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

### **Crear Rango con Nombre**  

Es posible crear un rango con nombre llamando al método sobrecargado [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Una versión típica del método [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) toma los siguientes parámetros:  

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.  
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.  

Cuando se llama al método [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-), devuelve el rango recién creado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Utilice este objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) para configurar el rango con nombre. Por ejemplo, establezca el nombre del rango utilizando la propiedad [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--). El siguiente ejemplo muestra cómo crear un rango con nombre de celdas que se extiende sobre B4:G14.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Ingresar Datos en las Celdas en el Rango Nombrado**  

Puede insertar datos en las celdas individuales de un rango siguiendo el patrón  

- **JavaScript**: Rango[fila,columna]  

Supongamos que tienes un rango de celdas que abarca de A1 a C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].  

Utiliza las siguientes propiedades para identificar las celdas en el rango:  

- firstRow devuelve el índice de la primera fila en el rango nombrado.  
- firstColumn devuelve el índice de la primera columna en el rango nombrado.  
- rowCount devuelve el número total de filas en el rango nombrado.  
- columnCount devuelve el número total de columnas en el rango con nombre.  

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **Identificar Celdas en el Rango con Nombre**  

Puedes insertar datos en las celdas individuales de un rango siguiendo el patrón:  

- **JavaScript**: Rango[fila,columna]  

Si tienes un rango con nombre que abarca de A1 a C4. La matriz hace 4 * 3 = 12 celdas. Las celdas de rango individuales están dispuestas secuencialmente: Rango[0,0], Rango[0,1], Rango[0,2], Rango[1,0], Rango[1,1], Rango[1,2], Rango[2,0], Rango[2,1], Rango[2,2], Rango[3,0], Rango[3,1], Rango[3,2].  

Utiliza las siguientes propiedades para identificar las celdas en el rango:  

- firstRow devuelve el índice de la primera fila en el rango nombrado.  
- firstColumn devuelve el índice de la primera columna en el rango nombrado.  
- rowCount devuelve el número total de filas en el rango nombrado.  
- columnCount devuelve el número total de columnas en el rango con nombre.  

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **Acceder a rangos con nombres**  

#### **Acceder a un Rango Nombrado Específico**  

Llame al método [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) de la colección [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) para obtener un rango por el nombre especificado. Un método [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) típico toma el nombre del rango con nombre y devuelve el rango con nombre especificado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). El siguiente ejemplo muestra cómo acceder a un rango especificado por su nombre.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Acceder a todos los rangos con nombres en una hoja de cálculo**  

Llame al método [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) de la colección [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) para obtener todos los rangos con nombre en una hoja de cálculo. El método [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) devuelve una matriz de todos los rangos con nombre en la colección [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).  

El siguiente ejemplo muestra cómo acceder a todos los rangos nombrados en un libro de trabajo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **Copiar rangos con nombres**  

Aspose.Cells proporciona el método [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) para copiar un rango de celdas con formato en otro rango.  

El siguiente ejemplo muestra cómo copiar un rango de celdas fuente en otro rango con nombre.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

