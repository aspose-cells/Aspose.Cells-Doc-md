---  
title: Vista previa del libro con Node.js a través de C++  
linktitle: Vista previa del libro 
type: docs  
weight: 70  
url: /es/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells soporta impresión y vista previa de archivos de Excel sin necesidad de tener instalada Microsoft Excel usando Node.js a través de C++.  
---  

## **Vista previa de impresión**  

Puede haber casos donde archivos de Excel con millones de páginas necesiten convertirse a PDF o imágenes. Procesar estos archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión de Libro y hoja puede ser útil. Antes de convertir estos archivos, el usuario puede verificar el total de páginas y decidir si convertir o no. Este artículo se enfoca en usar las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) para averiguar el total de páginas.  

Aspose.Cells ofrece la función de vista previa de impresión. Para ello, la API proporciona las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/). Para crear la vista previa de todo el libro de trabajo, crea una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) pasando los objetos [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) proporciona un método [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) que devuelve el número de páginas en la vista previa generada. Similar a la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) se usa para generar una vista previa de impresión para una hoja de trabajo específica. Para crear la vista previa de una hoja, crea una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) pasando los objetos [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) también proporciona un método [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) que devuelve el número de páginas en la vista previa generada.  

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) usando el [archivo de Excel de ejemplo](94896177.xlsx).  

### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

A continuación se muestra la salida generada al ejecutar el código anterior.  

### **Salida de la consola**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Temas avanzados**  
- [Configuración de fuentes para la representación de hojas de cálculo](/cells/es/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertir hoja de cálculo a imagen - Eliminar espacios alrededor de los datos](/cells/es/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Conversión de hoja de cálculo a imagen usando opciones de imagen o impresión](/cells/es/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exportar un rango de celdas en una hoja de cálculo a una imagen](/cells/es/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extraer imágenes de las hojas de cálculo usando opciones de imagen o impresión](/cells/es/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generar miniatura de la hoja de cálculo](/cells/es/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Página en Blanco de Salida cuando no hay Nada que Imprimir](/cells/es/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Configuración de página y opciones de impresión](/cells/es/nodejs-cpp/page-setup-and-printing-options/)  
- [Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions](/cells/es/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Renderizar la hoja de cálculo en contexto gráfico](/cells/es/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro](/cells/es/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

{{< app/cells/assistant language="nodejs-cpp" >}}
