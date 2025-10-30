---
title: Visa arbetsbok med JavaScript via C++
linktitle: Förhandsgranska arbetsbok 
type: docs
weight: 70
url: /sv/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells stöder utskrift och förhandsgranskning av Excel filer utan Microsoft Excel installation med hjälp av JavaScript via C++.
---

## **Förhandsgranska utskrift**  

Det kan finnas fall där Excel-filer med miljontals sidor måste konverteras till PDF eller bilder. Behandling av sådana filer tar mycket tid och resurser. I sådana fall kan funtionen för arbetsboks- och bladutsiktsförhandsgranskning vara användbar. Innan konvertering kan användaren kontrollera det totala sidantalet och bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda klasserna [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) för att ta reda på det totala antalet sidor.  

Aspose.Cells tillhandahåller utskriftsförhandsgranskning. För detta använder API:et [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) klasser. För att skapa en förhandsgranskning av hela arbetsboken, skapa en instans av [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) klassen genom att passera [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) objekt till konstruktorn. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) klassen tillhandahåller en [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) metod som returnerar antalet sidor i den genererade förhandsgranskningen. Liknande [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) klassen, används [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) klassen för att generera en utskriftsförhandsgranskning för ett specifikt blad. För att skapa utskriftsförhandsgranskning av ett blad, skapa en instans av [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) klassen genom att passera [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) objekt till konstruktorn. [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) klassen tillhandahåller också en [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) metod som returnerar antalet sidor i den genererade förhandsgranskningen.  

Följande kodexempel demonstrerar användningen av både [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) klasser genom att använda [provläsnings Excel-fil](94896177.xlsx).  

### **Exempelkod**  

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

Följande är utdatan som genereras genom att köra ovanstående kod.  

### **Konsoloutput**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Fortsatta ämnen**  
- [Konfigurera typsnitt för att rendera kalkylblad](/cells/sv/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Konvertera arbetsblad till bild - Ta bort mellanrum runt data](/cells/sv/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Konvertera arbetsblad till bild med hjälp av ImageOrPrint Options](/cells/sv/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exportera område av celler i en arbetsbok till bild](/cells/sv/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extrahera bilder från arbetsblad med hjälp av ImageOrPrintOptions](/cells/sv/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generera miniatyrbild av arbetsbladet](/cells/sv/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Utdata tom sida när det inte finns något att skriva ut](/cells/sv/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Sidlayout- och utskriftsalternativ](/cells/sv/javascript-cpp/page-setup-and-printing-options/)  
- [Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions](/cells/sv/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Rendera kalkylblad till grafiskt sammanhang](/cells/sv/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation](/cells/sv/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
