---  
title: Opciones de configuración de página e impresión con Node.js vía C++  
linktitle: Configuración de página y opciones de impresión  
type: docs  
weight: 60  
url: /es/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
A veces, los desarrolladores necesitan configurar la configuración de página y las opciones de impresión para controlar el proceso de impresión. La configuración de página y las opciones de impresión ofrecen varias opciones y son totalmente compatibles con Aspose.Cells.  

Este artículo muestra cómo crear una aplicación de consola en Node.js vía C++, y aplicar la configuración de página y opciones de impresión a una hoja de trabajo con algunas líneas simples de código usando la API de Aspose.Cells.  
{{% /alert %}}  

## **Trabajar con configuraciones de página y de impresión**  

Para este ejemplo, creamos un libro en Microsoft Excel y usamos Aspose.Cells para establecer la configuración de página y las opciones de impresión.  

### **Usar Aspose.Cells para establecer opciones de configuración de página**  

Primero crea una hoja de cálculo simple en Microsoft Excel. Luego aplica opciones de configuración de página en ella. Ejecutar el código cambia las opciones de configuración de página como se muestra en la captura de pantalla a continuación.  

|**Archivo de salida.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Crea una hoja de cálculo con algunos datos en Microsoft Excel:  
   1. Abra un nuevo libro en Microsoft Excel.  
   1. Agregue algunos datos.  
1. Configure las opciones de la configuración de página:  
   Aplique las opciones de configuración de página al archivo. A continuación se muestra una captura de pantalla de las opciones predeterminadas, antes de que se apliquen las nuevas opciones.  

|**Opciones de configuración de página predeterminadas.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Descargue e instale Aspose.Cells:  
   1. [Descargar](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Instálelo en su equipo de desarrollo.  
      Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.  
1. Cree un proyecto:  
   1. Inicie su entorno de Node.js.  
   1. Cree una nueva aplicación de consola.  
      Este ejemplo mostrará una aplicación de consola de Node.js, pero también puede usar enlaces de C++.  
1. Agregue referencias:  
   1. Este ejemplo utiliza Aspose.Cells, por lo tanto, agregue una referencia a ese componente al proyecto. Por ejemplo:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. Escriba la aplicación que invoque la API:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Configuración de opciones de impresión**  

Las configuraciones de la configuración de página también proporcionan varias opciones de impresión (también llamadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo. Permiten a los usuarios:  

- Seleccionar un área de impresión específica de una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.  

El ejemplo que sigue aplica opciones de impresión al archivo creado en el ejemplo anterior (PageSetup.xls). La captura de pantalla a continuación muestra las opciones de impresión predeterminadas antes de aplicar nuevas opciones.  

|**Documento de entrada**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Ejecutar el código cambia las opciones de impresión.  

|**Archivo de salida**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
