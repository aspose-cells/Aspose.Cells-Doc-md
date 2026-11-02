---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells for JavaScript via C++ är ett bibliotek för att arbeta med kalkylbladsfiler. Den här artikeln förklarar hur du anpassar en bild exakt till en enda cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, JavaScript via C++-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, Pictures, EmbeddedImage
type: docs
weight: 80
url: /sv/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att knyta en bild till en enda cell. En flytande bild är en form på kalkylbladets ritlager som ligger ovanpå ett cellintervall, medan en inbäddad bild lagras i själva cellen och automatiskt skalas för att passa cellens visningsyta. Välj den metod som bäst passar dina layoutkrav.
{{% /alert %}}

## **Introduktion**
Att anpassa en bild exakt till en enda cell är ett vanligt krav när du utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, personalkataloger, instrumentpaneler eller lagerlistor. I stället för att sträcka en bild över flera celler eller placera den löst på ett kalkylblad kan du vilja ha en tydligt avgränsad bild som är knuten till cellen och förblir i linje med den cell som bilden tillhör.
Aspose.Cells stöder detta scenario på två komplementerande sätt:
- **Metod 1 – Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess placering med `picture.setPlacement(PlacementType.MoveAndSize)` och justera ankarcellerna med `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` och `picture.setLowerRightColumn()` så att bilden täcker exakt en cell.
- **Metod 2 – Bädda in en bild direkt i en cell.** Använd `cell.setEmbeddedImage(imageBuffer)` för att tilldela cellen en `Buffer` som innehåller bilddata. Bilden skalas automatiskt så att den passar cellens visningsyta och flyttas tillsammans med cellen.
Resten av artikeln går igenom båda metoderna, förklarar relevanta API:er och visar hur du använder dem i kod.

## **Metod 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte tillhör någon enskild cell är den förankrad i ett cellintervall. Bildens ankarceller – dess övre vänstra och nedre högra hörn – bestämmer bildens visuella omfattning på kalkylbladet. Som standard sträcker sig en nytillagd bild över flera celler.
För att få en flytande bild att täcka **exakt en cell** behöver du:
1. Lägg till bilden med `worksheet.getPictures().add(row, column, imageBuffer)`, där `imageBuffer` är en `Buffer` som innehåller bilddata. Detta förankrar den nya bilden i den angivna cellen.
2. Ange de fyra ankervärdena så att bildens gränsrektangel sammanfaller med målcellen.
3. Anropa `picture.setPlacement(PlacementType.MoveAndSize)` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden i en enda cell**
Bildens ankare definieras av fyra åtkomstmetoder för nollbaserade index:
- `picture.getUpperLeftRow()` och `picture.setUpperLeftRow(value)` – radindexet för bildens övre kant.
- `picture.getUpperLeftColumn()` och `picture.setUpperLeftColumn(value)` – kolumnindexet för bildens vänstra kant.
- `picture.getLowerRightRow()` och `picture.setLowerRightRow(value)` – radindexet för bildens nedre kant. Om bildens nedre kant ska ligga vid nederkanten av rad `r` anger du `r + 1`.
- `picture.getLowerRightColumn()` och `picture.setLowerRightColumn(value)` – kolumnindexet för bildens högra kant. Om bildens högra kant ska ligga vid högerkanten av kolumn `c` anger du `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cellen C6 har radindex 5 och kolumnindex 2. Avvikelser på ett i det nedre högra ankaret är den vanligaste orsaken till att en bild verkar sträcka sig in i en angränsande cell.
{{% /alert %}}

### **Styra bildens placeringsbeteende**
`picture.getPlacement()` och `picture.setPlacement(value)` använder enumet `PlacementType` för att styra hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under bilden. Det rekommenderade värdet för en bild i en enda cell är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med den underliggande cellen och bibehåller den exakta passningen.

### **Steg-för-steg-anvisningar**
1. Skapa en ny `Workbook` eller öppna en befintlig.
2. Hämta den `Worksheet` som avses via `workbook.getWorksheets().getAt(0)`.
3. Läs in bildfilen från disken till en `Buffer`, till exempel med Node.js `fs.readFileSync`.
4. Anropa `worksheet.getPictures().add(5, 2, imageBuffer)` för att lägga till en bild förankrad i cell C6. Metoden returnerar indexet för den nya bilden i `Pictures`-samlingen. Använd indexet för att hämta motsvarande `Picture`.
5. Ange de fyra förankringskoordinaterna så att bilden endast täcker cell C6: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` och `picture.setLowerRightColumn(3)`.
6. Anropa `picture.setPlacement(PlacementType.MoveAndSize)` för att hålla bilden anpassad till C6 när kolumnen eller raden ändras.
7. Lägg eventuellt till exempeltext i angränsande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken på disken som en `.xlsx`-fil.
Följande kod visar den fullständiga lösningen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Metod 2: Bädda in en bild direkt i en cell**
Aspose.Cells erbjuder också en enklare mekanism för bilder som är knutna till celler: metoden `cell.setEmbeddedImage(imageBuffer)`. När du tilldelar cellen bilddata med den här metoden binds bilden till själva cellen, som om den vore inbäddat innehåll.

### **Så fungerar inbäddade bilder**
- Bilden lagras som en del av cellens innehåll i stället för att vara en form på ritlagret.
- Bilden skalas automatiskt så att den passar inom cellens återgivna gränser. Inga förankringskoordinater eller placeringsinställningar krävs.
- Cellen förblir en vanlig cell med en egen adress. Den kan refereras i formler, sorteras som en del av en rad och användas i andra åtgärder på cellnivå.
Detta gör `cell.setEmbeddedImage(imageBuffer)` till det mest koncisa alternativet när ditt mål helt enkelt är ”en bild som finns i den här cellen”.

### **Steg-för-steg-anvisningar**
1. Skapa en ny `Workbook` eller öppna en befintlig.
2. Hämta den `Worksheet` som avses via `workbook.getWorksheets().getAt(0)`.
3. Läs in bildfilen från disken till en `Buffer`, till exempel med Node.js `fs.readFileSync`.
4. Hämta en referens till målcellen, antingen via `worksheet.getCells().get("C6")` eller `worksheet.getCells().get(5, 2)`.
5. Anropa `cell.setEmbeddedImage(imageBuffer)` för att tilldela cellen `Buffer`.
6. Justera vid behov målradens höjd och målkolumnens bredd så att den inbäddade bilden syns bättre.
7. Spara arbetsboken på disken som en `.xlsx`-fil.
Följande kod visar den fullständiga lösningen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Hämta målcellen C6
            const cell = worksheet.cells.get("C6");
            // Läs bildfilen in i en byte-array
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Bädda in bilden direkt i cellen
            cell.embeddedImage = imageData;
            // Justera vid behov radhöjd och kolumnbredd så att den inbäddade bilden blir mer synlig
            worksheet.cells.setColumnWidth(2, 30); // Kolumn C (index 2)
            worksheet.cells.setRowHeight(5, 100); // Rad 6 (index 5)
            // Spara den resulterande arbetsboken som en .xlsx-fil
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Välja rätt metod**
Båda metoderna ger en bild som passar inom en enda cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:
- **Använd en flytande bild (metod 1) när:**
  - Du behöver mer detaljerad kontroll över placering, lagerordning eller anpassning i förhållande till andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan markeras, ordnas om eller grupperas tillsammans med andra former.
  - Du kräver bakåtkompatibilitet med äldre kod som redan använder `Pictures`-samlingen via `worksheet.getPictures()`.
  - Du behöver beräkna förankringskoordinater dynamiskt utifrån kalkylbladets layout.
- **Använd en inbäddad bild (metod 2) när:**
  - Du vill infoga en bild i en cell så enkelt som möjligt.
  - Bilden ska flyttas tillsammans med cellen precis som allt annat cellinnehåll.

## Relaterade artiklar
- [Excel-kamera i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/excel-camera/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/)
- [Använd stilar på pivottabeller i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}