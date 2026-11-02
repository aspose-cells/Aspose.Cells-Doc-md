---
title: Excel-kamera i Aspose.Cells for JavaScript via C++
linktitle: Excel-kamera i Aspose.Cells for JavaScript via C++
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for JavaScript via C++ för att skapa en dynamisk bild som är länkad till ett cellintervall, uppdateras när källdatan ändras och bevarar källans fullständiga formatering.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel-kamera, dynamisk bild, länkad bild, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /sv/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som renderar en levande bild av ett cellintervall och flyter i ritlagret på samma sätt som en vanlig bild. Aspose.Cells stöder två skapningslägen: en dynamisk bild som uppdateras automatiskt när källdatan ändras och en statisk bild som representerar ett intervall som en ögonblicksbild. Den här artikeln går igenom båda metoderna så att du kan välja den metod som passar din layout.

## Vad är Excel-kameran?
Excel-kameran är i praktiken ett bildobjekt som är förankrat vid en bestämd rad och kolumn i kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är kameran länkad till ett källintervall genom en formel i A1-format, till exempel `"A1:F10"`. När någon cell i intervallet ändras uppdateras kamerans bild automatiskt så att den visar det nya innehållet. Kameran bevarar källområdets fullständiga formatering – ramar, bakgrundsfärger, teckensnitt och talformat – så att allt som syns i cellerna också syns i kamerans bild. Det gör kameran särskilt användbar för instrumentpaneler, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett område på en annan plats i kalkylbladet, utan att behöva rulla eller upprepa data. Två förbehåll gäller: du måste anropa `updateSelectedValue()` innan du sparar arbetsboken, och filen måste exporteras till HTML eller PDF, eftersom dessa format använder inbäddad bilddata i stället för resultatet av en omräkning i realtid.

## Metod 1 – Lägg till en dynamisk kamerabild
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kamerverktyg. Den fungerar genom att lägga till en bild utan bildinnehåll från början och sedan tilldela bilden egenskapen `formula` med en referens till källintervallet. När formeln har angetts uppdaterar `updateSelectedValue()` den inbäddade bilddatan så att den är synkroniserad med de celler som kameran speglar. Kameran implementeras inte med en dedikerad klass – den byggs helt och hållet utifrån standardtypen `Picture`.
De viktigaste API:erna är:
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` – lägger till en bild som förankras vid den angivna raden och kolumnen. När du skickar `null` som bildparameter skapas en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.getPictures().get(index)` – hämtar en specifik `Picture` från samlingen.
- `picture.formula` – en egenskap av strängtyp som innehåller A1-referensen till det källintervall som kameran speglar, till exempel `"A1:F10"`.
- `picture.updateSelectedValue()` – en metod utan returvärde som uppdaterar den inbäddade bilddatan från de celler som `formula` refererar till.

{{% alert color="primary" %}}
`updateSelectedValue()` MÅSTE anropas innan arbetsboken sparas om utdata exporteras till HTML eller PDF; annars innehåller den exporterade filen ingen bilddata och kameran visas tom i det renderade resultatet.
Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 och kolumn 6, länkar den till källintervallet `A1:F10` via egenskapen `formula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10 och uppdatera sedan
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Metod 2 – Lägg till en statisk kamerabild
Den statiska kameran är i praktiken en förhandsvisning av ett cellintervall som renderas en gång. I stället för att underhålla en levande länk renderar du intervallet till bilddata i byteformat en gång, skapar en `Buffer` med bytena och lägger till den som en vanlig bild. Bildinnehållet är därefter låst vid tidpunkten för skapandet och uppdateras inte automatiskt när källcellerna ändras.
De viktigaste API:erna är:
- `cells.createRange(address)` – bygger ett `Range`-objekt från en adress i A1-format, till exempel `"A1:F10"`.
- `range.toImage(options)` – renderar intervallet till bilddata i byteformat. Att skicka `null` använder standardalternativen för rendering; det finns även överlastade metoder för mer detaljerad kontroll av utdata.
- `Buffer.from(imageBytes)` – skapar en `Buffer` som innehåller de renderade bildbytena och som kan skickas till `worksheet.getPictures().add`.
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` – lägger till bilden som är förankrad vid den angivna raden och kolumnen, denna gång med den `Buffer` som skapades vid renderingen.
Följande kod skapar en arbetsbok, bygger ett `Range` för `A1:F10`, renderar det till bilddata i byteformat med `range.toImage(null)`, skapar en `Buffer` med bytena, lägger till bilden förankrad vid rad 10 och kolumn 6 och sparar arbetsboken.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // Statisk kamera: skapa Range, rendera till byte, packa in i MemoryStream och lägg till som bild
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Välja mellan dynamisk och statisk kamera
- **Dynamisk kamera:** uppdateras vid varje omräkning, stöder export till HTML och PDF efter `updateSelectedValue()` och behåller den levande länken under hela filens livslängd.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill bädda in en fast visuell ögonblicksbild vid byggtiden i stället för en levande spegel av data.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande kamera som byggs med `picture.formula` plus `updateSelectedValue()` och en statisk engångskamera som byggs med `range.toImage` plus en `Buffer`. Välj den dynamiska metoden när resultatet måste vara synkroniserat med källcellerna, och välj den statiska metoden när du endast behöver en fast visuell ögonblicksbild vid byggtiden.

## Relaterade artiklar
- [Konvertera sparklinje till bild och HTML i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/)
- [Använd stilar på pivottabeller i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}