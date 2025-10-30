---  
title: Mostrar y ocultar filas, columnas y barras de desplazamiento con Node.js vía C++  
linktitle: Mostrar y ocultar filas, columnas y barras de desplazamiento  
type: docs  
weight: 20  
url: /es/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Este artículo demuestra cómo mostrar u ocultar programáticamente filas y columnas de la hoja de Excel usando Node.js vía C++. Controle la visibilidad de las barras de desplazamiento y oculte múltiples filas y columnas de manera eficiente.  
---  

{{% alert color="primary" %}}  
Aspose.Cells proporciona formas de controlar la visibilidad de filas, columnas y barras de desplazamiento de una hoja de cálculo.  
{{% /alert %}}  

## **Mostrar y ocultar filas y columnas**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) que representa todas las celdas en la hoja de trabajo. La colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) ofrece varios métodos para gestionar filas o columnas en una hoja de trabajo. Algunos de estos se discuten a continuación.  

### **Mostrar filas y columnas**  

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) y [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) respectivamente. Ambos métodos requieren dos parámetros:  

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.  
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Al hacer visible una columna oculta, si necesita restaurarla a su ancho previamente asignado o a su ancho original, por favor desoculte la columna con un ancho negativo. Por ejemplo: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Ocultar filas y columnas**  

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) y [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.  
{{% /alert %}}  

### **Ocultar múltiples filas y columnas**  

Los desarrolladores pueden ocultar varias filas o columnas a la vez llamando a los métodos [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) y [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) de la colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) respectivamente. Ambos métodos toman el índice de fila o columna inicial y el número de filas o columnas que deben ocultarse como parámetros.  

```javascript
const fs = require('fs');
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Mostrar y ocultar barras de desplazamiento**  

Las barras de desplazamiento se utilizan para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:  

- Barras de desplazamiento verticales  
- Barras de desplazamiento horizontales  

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de cálculo. Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en los archivos de Excel.  

### **Controlar la visibilidad de las barras de desplazamiento**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, use las propiedades [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) y [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) y [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) son propiedades booleanas, lo que significa que solo pueden almacenar valores **verdadero** o **falso**.  

#### **Hacer visibles las Barras de Desplazamiento**  

Hacer visibles las barras de desplazamiento estableciendo en **verdadero** las propiedades [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) o [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

#### **Ocultar Barras de Desplazamiento**  

Ocultar barras de desplazamiento estableciendo en **falso** las propiedades [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) o [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

**Código de Ejemplo**  

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
