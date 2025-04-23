---
title: Vistas de hoja de trabajo con Node.js a través de C++
linktitle: Vistas de Hoja de Cálculo
type: docs
weight: 40
url: /es/nodejs-cpp/worksheet-views/
description: Este artículo describirá cómo usar Node.js y la API de Node.js para interactuar con la vista previa de salto de página de un libro de Excel y hojas de trabajo. Trabajar con paneles divididos, paneles congelados y factor de zoom también.
---

## **Vista previa de salto de página**

Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

La vista normal es la vista predeterminada de una hoja de trabajo. La vista previa de salto de página es una vista de edición que muestra una hoja de trabajo como será al imprimir. La vista previa de salto de página muestra qué datos irán en cada página, para que puedas ajustar el área de impresión y los saltos de página. Usando Aspose.Cells for Node.js via C++, los desarrolladores pueden habilitar modos de vista normal o vista previa de salto de página.

### **Controlando Modos de Vista**

Aspose.Cells provee una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para habilitar los modos de vista normal o vista previa de salto de página, use la propiedad [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o un valor **false**.

#### **Habilitar Vista Normal**

Establezca una hoja de cálculo en vista normal configurando la propiedad [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) en **false**.

#### **Habilitar vista previa de salto de página**

Establezca cualquier hoja de cálculo en vista previa de salto de página configurando la propiedad [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) en **true**. Al hacerlo, cambia la hoja de cálculo de la vista normal a la vista previa de salto de página.

A continuación se muestra un ejemplo completo que demuestra cómo usar la propiedad [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). La vista se cambia a vista previa de salto de página para la primera hoja de cálculo configurando la propiedad [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) en **true**. El archivo modificado se guarda como output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Factor de zoom**

### **Usar Microsoft Excel**

Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

### **Aspose.Cells y el factor de zoom**

Aspose.Cells permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo.
Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice la propiedad [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) de la clase [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--). El factor de zoom se establece asignando un valor numérico (entero) a la propiedad [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) .

A continuación se presenta un ejemplo completo que demuestra cómo usar la propiedad [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) para establecer el nivel de zoom de la primera hoja de un archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). El factor de zoom de la primera hoja de cálculo se establece en 75 y el archivo modificado se guarda como output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Congelar paneles**

### **Usar Microsoft Excel**

Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.

### **Aspose.Cells y fijar paneles**

Aspose.Cells permite a los desarrolladores aplicar bloquear paneles a las hojas de cálculo en tiempo de ejecución.

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece una amplia gama de propiedades y métodos para gestionar hojas de trabajo. Para configurar paneles congelados, llama al método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) de la clase Hoja de trabajo. El método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

El archivo book1.xls se abre llamando al constructor de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) mientras se instancia y se congelan algunas filas y columnas en la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

A continuación se muestra un ejemplo completo que muestra cómo utilizar el método [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) para congelar filas y columnas (a partir de C4, representado por la cuarta fila y tercera columna, donde las filas y columnas empiezan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **División de paneles**

Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.

### **Aplicación y eliminación de divisiones de paneles**

#### **División de paneles**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) ofrece una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para implementar vistas divididas, use el [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Para eliminar los paneles divididos, use el método [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Después de ejecutar el código anterior, el archivo generado tendrá una vista dividida.

#### **Eliminación de paneles**

Eliminar paneles divididos utilizando el método [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Temas avanzados**
- [Ocultar la visualización de los valores cero en la hoja de cálculo](/cells/es/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de cálculo](/cells/es/nodejs-cpp/set-worksheet-tab-color/)
- [Mostrar y ocultar la cuadrícula y las cabeceras de filas y columnas](/cells/es/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Mostrar y ocultar filas, columnas y barras de desplazamiento](/cells/es/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostrar y ocultar hojas de cálculo y pestañas](/cells/es/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Mostrar fórmulas en lugar de valores en una hoja de cálculo](/cells/es/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Utilizar opciones de verificación de errores](/cells/es/nodejs-cpp/use-error-checking-options/)

