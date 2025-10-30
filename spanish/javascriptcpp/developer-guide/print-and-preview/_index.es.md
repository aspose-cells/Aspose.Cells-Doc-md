---
title: Vista previa del libro de trabajo con JavaScript a través de C++
linktitle: Vista previa del libro 
type: docs
weight: 70
url: /es/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells soporta imprimir y previsualizar archivos de Excel sin necesidad de tener instalado Microsoft Excel usando JavaScript a través de C++.
---

## **Vista previa de impresión**  

Puede haber casos donde archivos de Excel con millones de páginas necesiten convertirse a PDF o imágenes. Procesar estos archivos consumirá mucho tiempo y recursos. En tales casos, la función de vista previa de impresión de Libro y hoja puede ser útil. Antes de convertir estos archivos, el usuario puede verificar el total de páginas y decidir si convertir o no. Este artículo se enfoca en usar las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) para averiguar el total de páginas.  

Aspose.Cells ofrece la función de vista previa de impresión. Para ello, la API proporciona las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/). Para crear la vista previa de todo el libro de trabajo, crea una instancia de la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) pasando los objetos [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) al constructor. La clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) proporciona un método [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) que devuelve el número de páginas en la vista previa generada. Similar a la clase [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/), la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) se usa para generar una vista previa de impresión para una hoja de trabajo específica. Para crear la vista previa de una hoja, crea una instancia de la clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) pasando los objetos [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) al constructor. La clase [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) también proporciona un método [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) que devuelve el número de páginas en la vista previa generada.  

El siguiente fragmento de código demuestra el uso de las clases [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) y [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) usando el [archivo de Excel de ejemplo](94896177.xlsx).  

### **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

A continuación se muestra la salida generada al ejecutar el código anterior.  

### **Salida de la consola**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Temas avanzados**  
- [Configuración de fuentes para la representación de hojas de cálculo](/cells/es/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertir hoja de cálculo a imagen - Eliminar espacios alrededor de los datos](/cells/es/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Conversión de hoja de cálculo a imagen y hoja de cálculo a imagen por página](/cells/es/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Conversión de hoja de cálculo a imagen usando opciones de imagen o impresión](/cells/es/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exportar un rango de celdas en una hoja de cálculo a una imagen](/cells/es/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extraer imágenes de las hojas de cálculo usando opciones de imagen o impresión](/cells/es/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generar miniatura de la hoja de cálculo](/cells/es/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Página en Blanco de Salida cuando no hay Nada que Imprimir](/cells/es/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Configuración de página y opciones de impresión](/cells/es/javascript-cpp/page-setup-and-printing-options/)  
- [Renderizar secuencia de páginas usando las propiedades PageIndex y PageCount de ImageOrPrintOptions](/cells/es/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Renderizar la hoja de cálculo en contexto gráfico](/cells/es/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro](/cells/es/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
