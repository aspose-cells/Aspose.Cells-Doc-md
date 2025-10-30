---
title: Sidinställningar och utskriftsalternativ med JavaScript via C++
linktitle: Sidlayout och utskriftsalternativ
type: docs
weight: 60
url: /sv/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
Ibland behöver utvecklare konfigurera sidlayout och utskriftsalternativ för att kontrollera utskriftsprocessen. Sidlayouts- och utskriftsalternativen erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.  

Den här artikeln visar hur man skapar en konsolapplikation i JavaScript via C++, och tillämpar sidinställningar och utskriftsalternativ på ett kalkylblad med några enkla kodrader med Aspose.Cells API.  
{{% /alert %}}  

## **Arbeta med Sid- och Utskriftsalternativ**  

För detta exempel har vi skapat ett arbetsbok i Microsoft Excel och använt Aspose.Cells för att ställa in siduppsättning och utskriftsalternativ.  

### **Användning av Aspose.Cells för att ställa in sidlayoutalternativ**  

Skapa först ett enkelt arbetsblad i Microsoft Excel. Tillämpa sedan sidlayoutalternativ på det. När koden utförs ändras sidlayoutalternativen enligt skärmdumpen nedan.  

|**Utdatafil.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Skapa ett arbetsblad med viss data i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Lägg till viss data.  
1. Ange sidlayoutalternativ:  
   Tillämpa sidlayoutalternativ på filen. Här är en skärmdump av de förvalda alternativen, innan de nya alternativen tillämpas.  

|**Standard sidlayoutalternativ.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Ladda ner och installera Aspose.Cells:  
   1. [Ladda ner](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript via C++.  
   1. Installera det på din utvecklingsdator.  
      Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.  
1. Skapa ett projekt:  
   1. Starta din JavaScript-miljö.  
   1. Skapa en ny konsolapplikation.  
      Det här exemplet visar en JavaScript-konsolapplikation, men du kan också använda C++-bindningar.  
1. Lägg till referenser:  
   1. Detta exempel använder Aspose.Cells så lägg till en referens till den komponenten i projektet. Till exempel:  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. Skriv applikationen som använder API:et:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Inställa utskriftsalternativ**  

Sidlayoutinställningar ger också flera utskriftsalternativ (även kallade bladalternativ) som låter användarna styra hur arksidor skrivs ut. De tillåter användarna att:  

- Välj ett specifikt utskriftsområde av ett kalkylblad.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.  

Exemplet som följer tillämpar utskriftsalternativ på filen skapad i exemplet ovan (PageSetup.xls). Skärmdumpen nedan visar de standardutskriftsalternativen innan nya alternativ tillämpas.  

|**Inmatningsdokument**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Körning av koden ändrar utskriftsalternativen.  

|**Utmatningsfil**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
