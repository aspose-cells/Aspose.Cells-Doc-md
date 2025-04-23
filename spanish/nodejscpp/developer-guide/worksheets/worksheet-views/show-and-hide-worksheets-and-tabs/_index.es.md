---  
title: Mostrar y ocultar hojas de trabajo y pestañas con Node.js vía C++  
linktitle: Mostrar y Ocultar Hojas de Cálculo y Pestañas  
type: docs  
weight: 10  
url: /es/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Este artículo proporciona código de ejemplo para usar la API de Node.js o la Biblioteca de Node.js para mostrar y ocultar programáticamente una hoja de trabajo de Excel. Además, cómo mostrar y ocultar pestañas del libro de trabajo de Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells permite al usuario mostrar y ocultar elementos de un libro de trabajo, incluidas las hojas de cálculo y las pestañas.  
{{% /alert %}}  

## **Mostrar y ocultar una hoja de cálculo**  

Un archivo de Excel puede tener una o más hojas de cálculo. Siempre que creamos un archivo de Excel, agregamos hojas de cálculo al archivo de Excel en el que trabajamos. Cada hoja de cálculo en un archivo de Excel es independiente de las demás hojas de cálculo al tener sus propios datos, configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de cálculo y mostrar otras en el archivo de Excel por su propio interés. Entonces, **Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de cálculo en sus archivos de Excel.  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de trabajo en el archivo Excel.  

Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ofrece una amplia variedad de propiedades y métodos para gestionar hojas de trabajo. Para controlar la visibilidad de una hoja de trabajo, use la propiedad [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.  

### **Hacer visible una hoja de cálculo**  

Haz visible una hoja de trabajo configurando la propiedad [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a **true**.  

### **Ocultar una hoja de trabajo**  

Oculta una hoja de trabajo configurando la propiedad [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) a **false**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Mostrar y Ocultar Pestañas**  

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:  

- Pestañas de hojas.  
- Botones de desplazamiento de pestañas.  

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.  

Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de hojas y los botones de desplazamiento en archivos de Excel.  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) ofrece una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar la propiedad [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) es una propiedad Booleana, lo que significa que solo puede almacenar un valor de **true** o **false**.  

### **Hacer pestañas visibles**  

Haz visibles las pestañas con la propiedad [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) configurada a **true**.  

### **Ocultar pestañas**  

Oculta las pestañas en un archivo de Excel configurando la propiedad [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) a **false**.  

A continuación, se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls. Después de la ejecución del código, verás que las pestañas del libro están ocultas.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Controlando el Ancho de la Barra de Pestañas**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

