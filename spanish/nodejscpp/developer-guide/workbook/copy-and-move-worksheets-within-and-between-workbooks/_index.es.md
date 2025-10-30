---
title: Copiar y Mover Hojas dentro y entre libros de trabajo con Node.js via C++
linktitle: Copiar y Mover Hojas de Cálculo Dentro y Entre Libros de Excel
type: docs
weight: 80
url: /es/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aprende cómo copiar y mover hojas dentro y entre libros de trabajo usando Aspose.Cells for Node.js via C++. Gestiona la estructura de tu libro de trabajo de manera eficiente.
---

{{% alert color="primary" %}}

A veces, necesitas varias hojas de cálculo con formato y entradas de datos comunes. Por ejemplo, si trabajas con presupuestos trimestrales, es posible que desees crear un libro con hojas que contengan los mismos encabezados de columna, encabezados de fila y fórmulas. Existe una manera de hacerlo: creando una hoja y luego copiándola tres veces.

Aspose.Cells for Node.js via C++ soporta copiar o mover hojas dentro o entre libros de trabajo. Las hojas, incluyendo datos, formatos, tablas, matrices, gráficos, imágenes y otros objetos, se copian con el mayor grado de precisión posible.

{{% /alert %}}

## **Copiar y mover hojas de cálculo**

### **Copiando una Hoja de Cálculo dentro de un Libro**

Los pasos iniciales son los mismos para todos los ejemplos.

1. Crear dos libros con algunos datos en Microsoft Excel. Para este ejemplo, creamos dos nuevos libros en Microsoft Excel e introducimos algunos datos en las hojas de cálculo.

 - FirstWorkbook.xlsx (3 hojas de cálculo).
- SecondWorkbook.xlsx (1 hoja de cálculo).

1. Descargue e instale Aspose.Cells:
   1. [Descarga Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Cree un proyecto:
   1. Inicia tu entorno de desarrollo.
   1. Cree una nueva aplicación de consola.
1. Agregue referencias:
   1. Agrega una referencia a Aspose.Cells al proyecto.
      Por ejemplo, agrega una referencia a ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copia la hoja de cálculo dentro de un libro de trabajo.
   El primer ejemplo copia la primera hoja de cálculo (Copia) dentro de FirstWorkbook.xlsx.

Al ejecutar el código, se copia la hoja llamada Copia dentro de FirstWorkbook.xlsx con el nombre Última Hoja.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Moviendo una Hoja de Cálculo dentro de un Libro de Trabajo**

El siguiente código muestra cómo mover una hoja de cálculo desde una posición a otra en un libro de trabajo. Al ejecutar el código, se mueve la hoja llamada Mover del índice 1 al índice 2 en FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Copiando una hoja de cálculo entre libros**

 Ejecutar el código copia la hoja llamada Copy en SecondWorkbook.xlsx con el nombre Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Moviendo una hoja de cálculo entre libros**

Al ejecutar el código se mueve la hoja llamada Mover de FirstWorkbook.xlsx a SecondWorkbook.xlsx con el nombre Hoja3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
