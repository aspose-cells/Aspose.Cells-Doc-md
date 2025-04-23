---
title: Crear y gestionar tablas de archivos de Microsoft Excel con Node.js a través de C++
linktitle: Tablas
type: docs
weight: 150
url: /es/nodejs-cpp/create-and-format-table/
description: Insertar, redimensionar, editar, eliminar y formatear tablas de archivos de Excel usando Aspose.Cells for Node.js via C++.
---

## **Crear Tabla**

Una de las ventajas de las hojas de cálculo es que te permiten crear diferentes tipos de listas, por ejemplo, listas de teléfonos, listas de tareas, listas de transacciones, activos o pasivos. Varios usuarios pueden colaborar para usar, crear y mantener varias listas.

Aspose.Cells soporta la creación y gestión de listas.

### **Ventajas de un Objeto de Lista**

Existen varias ventajas cuando conviertes una lista de datos en un Objeto de Lista real

- Se incluyen automáticamente nuevas filas y columnas.
- Se puede agregar fácilmente una fila total en la parte inferior de tu lista para mostrar SUMA, PROMEDIO, CONTAR, etc.
- Las columnas agregadas a la derecha se incorporan automáticamente en el Objeto de Lista.
- Los gráficos basados en filas y columnas se expandirán automáticamente.
- Los rangos nombrados asignados a filas y columnas se expandirán automáticamente.
- La lista está protegida contra la eliminación accidental de filas y columnas.

### **Creación de un Objeto de Lista utilizando Microsoft Excel**

- Seleccionar el rango de datos para crear un objeto Lista
- Esto muestra el cuadro de diálogo Crear Lista.
- Implementar el objeto Lista para los datos y especificar la fila total (Seleccionar **Datos**, luego **Lista**, seguido de **Fila Total**).

### **Uso de la API de Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección de [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona un amplio rango de propiedades y métodos para gestionar una hoja de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) en una hoja, usa la propiedad de colección [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) es, en realidad, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), que además proporciona el método [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) para agregar un objeto Lista y especificar un rango de celdas para la lista.

De acuerdo con el rango de celdas especificado, el objeto Lista es creado por Aspose.Cells. Usa atributos (por ejemplo, [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--), etc.) de la clase [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) para controlar la lista.

En el ejemplo que se muestra a continuación, hemos creado la misma [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) usando la API de Aspose.Cells como la que creamos usando Microsoft Excel en la sección anterior.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Formato de una Tabla**

Para gestionar y analizar un grupo de datos relacionados, es posible convertir un rango de celdas en un objeto de lista (también conocido como una tabla de Excel). Una tabla es una serie de filas y columnas que contienen datos relacionados administrados de forma independiente de los datos en otras filas y columnas. Por defecto, cada columna en la tabla tiene activada la filtración en la fila de encabezado para que puedas filtrar o ordenar tus datos de objeto de lista rápidamente. Puedes agregar una fila total (una fila especial en una lista que proporciona una selección de funciones de agregación útiles para trabajar con datos numéricos) al objeto de lista que ofrece una lista desplegable de funciones de agregación para cada celda de fila total. Aspose.Cells proporciona opciones para crear y gestionar listas (o tablas).

### **Formateando un Objeto de Lista**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección de [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona un amplio rango de propiedades y métodos para gestionar hojas de cálculo. Para crear un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) en una hoja, usa la propiedad de colección [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Cada [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) es, en realidad, un objeto de la clase [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), que además proporciona el método [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) para agregar un objeto Lista y especificar el rango de celdas que debe abarcar. De acuerdo con el rango de celdas especificado, se crea un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) en la hoja de cálculo por Aspose.Cells. Usa atributos (por ejemplo, [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) de la clase [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) para formatear la tabla según tus requisitos.

El ejemplo a continuación añade datos de ejemplo a una hoja, añade un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) y aplica estilos predeterminados. Los estilos [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) son compatibles con Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Temas avanzados**
- [Convertir Tabla a ODS](/cells/es/nodejs-cpp/convert-table-to-ods/)
- [Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos](/cells/es/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta](/cells/es/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Establecer el Comentario de la Tabla o Objeto de Lista dentro de la Hoja de Cálculo](/cells/es/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablas y Rangos](/cells/es/nodejs-cpp/tables-and-ranges/)

