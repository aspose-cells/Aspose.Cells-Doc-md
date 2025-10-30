---
title: Anteprima del foglio di lavoro con JavaScript tramite C++
linktitle: Anteprima del workbook 
type: docs
weight: 70
url: /it/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells supporta la stampa e l anteprima dei file Excel senza l installazione di Microsoft Excel usando JavaScript tramite C++.
---

## **Anteprima di stampa**  

Potrebbero esserci casi in cui file Excel con milioni di pagine devono essere convertiti in PDF o immagini. L'elaborazione di tali file richiederà molto tempo e risorse. In questi casi, la funzione di anteprima di stampa del Workbook e del Worksheet potrebbe essere utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e decidere se convertire o meno il file. Questo articolo si concentra sull'uso delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) per scoprire il numero totale di pagine.  

Aspose.Cells fornisce la funzione di anteprima di stampa. A tal fine, l'API fornisce le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/). Per creare l'anteprima di stampa dell'intero workbook, crea un'istanza della classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) passando gli oggetti [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) al costruttore. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) fornisce un metodo [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) che restituisce il numero di pagine nell'anteprima generata. Come la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) viene usata per generare un'anteprima di stampa di un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, crea un'istanza della classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) passando gli oggetti [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) al costruttore. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) fornisce anche un metodo [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) che restituisce il numero di pagine dell'anteprima generata.  

Il seguente frammento di codice dimostra l'uso di entrambe le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) usando il [file excel di esempio](94896177.xlsx).  

### **Codice di Esempio**  

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

Quello che segue è l'output generato eseguendo il codice sopra.  

### **Output della console**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Argomenti avanzati**  
- [Configurare i font per la resa dei fogli di calcolo](/cells/it/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convertire il foglio di lavoro in un'immagine - Rimuovere gli spazi vuoti intorno ai dati](/cells/it/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Convertire il foglio di lavoro in un'immagine e Foglio di lavoro in un'immagine per pagina](/cells/it/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Convertire il foglio di lavoro in un'immagine utilizzando le opzioni ImageOrPrint](/cells/it/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Esportare un intervallo di celle in un foglio di lavoro in un'immagine](/cells/it/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Estrarre immagini dai fogli di lavoro utilizzando ImageOrPrintOptions](/cells/it/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generare l'anteprima del foglio di lavoro](/cells/it/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Output Pagina Bianca quando non c'è Nulla da Stampare](/cells/it/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Impostazioni di layout pagina e stampa](/cells/it/javascript-cpp/page-setup-and-printing-options/)  
- [Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Renderizzare il foglio di lavoro al contesto grafico](/cells/it/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Specificare un insieme individuale o privato di caratteri per la rappresentazione del foglio di lavoro](/cells/it/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
