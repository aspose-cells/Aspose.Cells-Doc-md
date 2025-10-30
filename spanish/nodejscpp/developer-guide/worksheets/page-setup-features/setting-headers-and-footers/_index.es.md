---
title: Configuración de encabezados y pies de página con Node.js a través de C++
linktitle: Configuración de encabezados y pies de página
type: docs
weight: 30
url: /es/nodejs-cpp/setting-headers-and-footers/
description: Este artículo explica cómo insertar programáticamente una imagen en el encabezado y pie de página de las hojas de cálculo de Excel usando Aspose.Cells for Node.js via C++. 
keywords: Insertar imagen en encabezado pie de página de Excel Node.js vía C++, establecer comandos de script de encabezado pie de página en Excel Node.js vía C++
---

{{% alert color="primary" %}}

Los encabezados y pies de página son las líneas de texto que se muestran debajo del margen superior o encima del margen inferior, respectivamente. También es posible agregar encabezados y pies de página a las hojas de cálculo. Los encabezados y pies de página pueden utilizarse para mostrar información útil como el número de página, el nombre del autor, el nombre del tema o la fecha y hora. Los encabezados y pies de página se gestionan mediante la configuración del diseño de página.

{{% /alert %}}

## **Configuración de encabezados y pies de página**

Aspose.Cells for Node.js via C++ permite agregar encabezados y pies de página a las hojas de cálculo en tiempo de ejecución, pero recomendamos configurar encabezados y pies de página manualmente en un archivo pre-diseñado para imprimir. Puedes usar Microsoft Excel como una herramienta GUI para establecer encabezados y pies de página y ahorrar esfuerzo y tiempo de desarrollo. Aspose.Cells puede importar el archivo y guardar las configuraciones.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona llamadas de API especiales y comandos de script para formatear encabezados y pies de página.

### **Comandos de Script**

Los comandos de script son comandos especiales que le permiten configurar el formato de los encabezados y pies de página.

|**Comandos de Script**|**Descripción**|
| :- | :- |
|&P|Número de página actual|
|&G|Una imagen|
|&N|El número total de páginas|
|&D|La fecha actual|
|&T|La hora actual|
|&A|Nombre de la hoja de cálculo|
|&F|El nombre del archivo sin su ruta|
|&&Texto|Muestra &Texto. Por ejemplo: &&WO será mostrado como &WO|
|&"\<FontName>"|Representa un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representa el nombre de la fuente con estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de la fuente. Por ejemplo: “&14abc”. Sin embargo, si este comando va seguido de un número normal a imprimir en el encabezado, esto debe separarse con un carácter de espacio del tamaño de la fuente. Por ejemplo: “&14 123”.|

### **Establecer Encabezados y Pies de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) proporciona dos métodos, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) y [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), utilizados para agregar un encabezado y pie de página a una hoja de cálculo. Estos métodos solo toman dos parámetros:

- **Sección** – la sección donde se debe colocar el encabezado o pie de página. Hay tres secciones: izquierda, centro y derecha, representadas respectivamente por 0, 1 y 2.
- **Script** – el script a utilizar para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Insertar una Imagen en un Encabezado o Pie de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) tiene dos métodos adicionales, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) y [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), utilizados para agregar imágenes en el encabezado y pie de página. Estos métodos toman los siguientes parámetros:

- **Sección** – la sección de encabezado o pie de página donde se colocará la imagen. Hay tres secciones, izquierda, centro y derecha, representadas por los valores 0, 1 y 2 respectivamente.
- **Arreglo de bytes** – los datos gráficos (los datos binarios deben escribirse en el búfer de un arreglo de bytes).

Después de ejecutar el código a continuación y abrir el archivo, verificar el encabezado de la hoja de trabajo mediante:

1. En el menú **Archivo**, seleccionar **Configurar Página**. Se mostrará un cuadro de diálogo.
1. Seleccionar la pestaña **Encabezado/Pie de página**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
