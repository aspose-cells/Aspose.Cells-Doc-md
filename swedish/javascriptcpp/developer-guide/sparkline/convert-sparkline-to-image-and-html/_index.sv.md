---
title: Konvertera sparkline till bild och HTML i Aspose.Cells for JavaScript via C++
linktitle: Konvertera sparkline till bild och HTML i Aspose.Cells for JavaScript via C++
description: Lär dig hur du renderar sparklines i Aspose.Cells till fristående bilder för inbäddning i celler och exporterar kalkylblad med sparklines till HTML med hjälp av HtmlSaveOptions.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, sparkline, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är minidiagram som placeras i kalkylbladets celler. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller i en extern rapport) och även exportera hela kalkylbladet med sparklines till HTML för distribution i webbläsare. Egenskapen `cell.embeddedImage` som används i den här artikeln är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**
Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Excel-användare ser dem på plats, men många verkliga användningsfall kräver att en sparkline lämnar cellen – till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.
Aspose.Cells stöder båda dessa operationer. Metoden `sparkline.toImage` renderar en enskild sparkline till en `Buffer`, och de resulterande bytena kan tilldelas `cell.embeddedImage`, så att bilden lagras i en enda cell i arbetsboken. Med `HtmlSaveOptions` kan du dessutom konvertera hela arbetsboken – inklusive sparklines – till en självständig HTML-fil. Den här artikeln beskriver båda arbetsflödena steg för steg.

## **Arbetsflöde 1 – Rendera sparklines till bilder och bädda in dem i celler**
I det här arbetsflödet skapar du ett kalkylblad som innehåller ett litet intervall med källvärden, kopplar tre olika sparklinegrupper (`SparklineType.Line`, `SparklineType.Column` och `SparklineType.Stacked`/vinst-förlust) till intervallet, renderar varje grupp som en PNG-bild och skriver PNG-bytena till intilliggande celler som inbäddade bilder. Slutresultatet är en enda `.xlsx`-fil som innehåller både de aktiva sparklines och deras renderade bildversioner.

### **Instruktioner steg för steg**
1. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
2. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturmätningar).
3. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.getSparklineGroups().add(...)`:
   - En `SparklineType.Line`-grupp med `F1` som ankarcell och dataintervallet `A1:E1`.
   - En `SparklineType.Column`-grupp med `G1` som ankarcell och dataintervallet `A1:E1`.
   - En `SparklineType.Stacked`-grupp (vinst/förlust) med `H1` som ankarcell och dataintervallet `A1:E1`.
4. Skapa en `ImageOrPrintOptions`-instans och ange egenskapen `imageType` till `ImageType.Png`, så att varje sparkline renderas som en PNG-bild.
5. Spara arbetsboken som `output_with_sparklines.xlsx`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Skapa en ny arbetsbok och kom åt till det första kalkylbladet
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Fyll i exempeldata i cellerna A1:E1
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // Lägg till en grupp med linjesparklines förankrad vid F1 (kolumn 5, rad 0)
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // Lägg till en grupp med kolumnsparklines förankrad vid G1 (kolumn 6, rad 0)
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // Lägg till en grupp med vinst/förlustsparklines (staplad) förankrad vid H1 (kolumn 7, rad 0)
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // Konfigurera bildalternativ för PNG-utdata
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Konvertera linjesparklinen till en bild och bädda in den i cell F2
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Konvertera kolumnsparklinen till en bild och bädda in den i cell G2
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Konvertera vinst/förlustsparklinen till en bild och bädda in den i cell H2
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // Spara arbetsboken till disk
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Den kod ovan skapar en arbetsbok där varje visuell representation av en sparkline finns i två former: den aktiva sparkline som återges i kalkylbladet och som är förankrad på rad 1, samt en statisk PNG-bild som är inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna finns i själva filen är arbetsboken en enda sammanhållen fil som kan skickas via e-post eller arkiveras utan att de inbäddade bildreferenserna bryts.

{{% alert color="primary" %}}
Eftersom varje sparklinegrupp är förankrad i en enda cell kan du referera till den med indexeraren `group.getSparklines()[0]` i stället för att iterera över samlingen. Detta håller renderingskoden kort och följer det vanliga mönstret ”en sparkline per ankarcell”. För att lagra bildbytena via `cell.embeddedImage` krävs Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 – Exportera kalkylbladet med sparklines till HTML**
När arbetsboken innehåller aktiva sparklines (och eventuellt inbäddade bildversioner) kan hela kalkylbladet publiceras på webben genom att sparas som HTML. Klassen `HtmlSaveOptions` exponerar de inställningar som behövs för att styra exporten. I det här arbetsflödet återanvänder du filen `output_with_sparklines.xlsx` från arbetsflöde 1 och konverterar den till ett enkelt ensidigt HTML-dokument.

### **Instruktioner steg för steg**
1. Kontrollera att filen `output_with_sparklines.xlsx` från arbetsflöde 1 finns på disk i arbetskatalogen.
2. Läs in filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ange egenskapen `exportActiveWorksheetOnly` till `true`, så att den resulterande HTML-filen bara innehåller det aktiva kalkylbladet i stället för hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

Den kod ovan tar arbetsboken med sparklines från arbetsflöde 1 och omvandlar den till en portabel HTML-fil. Sparklinegrupperna renderas som bilder direkt i den genererade HTML-tabellen, så att slutanvändare kan se trenderna i alla moderna webbläsare utan att behöva installera Excel. Genom att ange `exportActiveWorksheetOnly` till `true` undviker du att oavsiktligt publicera dolda kalkylblad eller hjälpdata – endast det kalkylblad som är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för att finjustera utdata, till exempel `exportHiddenWorksheet`, `exportImagesAsBase64` och `encoding`. Anpassa dem efter behov för din målmiljö.
{{% /alert %}}

## **API-översikt**
De arbetsflöden ovan bygger på ett litet antal API:er i Aspose.Cells som fungerar tillsammans.
- `SparklineGroup` och åtkomstmetoden `worksheet.getSparklineGroups()` används för att ange typen (`Line`, `Column`, `Stacked`), dataintervallet och ankarcellen för varje sparklinegrupp. I den här artikeln är varje grupp förankrad i en enda cell, så gruppen nås via `worksheet.getSparklineGroups()[i]`.
- `Sparkline` och indexeraren `group.getSparklines()[0]` returnerar den enskilda sparkline som finns i en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen iterationsloop.
- `sparkline.toImage(imageOrPrintOptions)` är renderingsmetoden som returnerar en bild av sparklinen i form av en `Buffer`. De returnerade bytena kan tilldelas direkt till `cell.embeddedImage`.
- `HtmlSaveOptions.exportActiveWorksheetOnly` (ett booleskt värde) begränsar HTML-exporten till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna i `HtmlSaveOptions` när ensidiga rapporter genereras.
- `ImageOrPrintOptions.imageType` väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `toImage` och vid utskrift av kalkylblad till bilder.

{{< app/cells/assistant language="javascript-cpp" >}}