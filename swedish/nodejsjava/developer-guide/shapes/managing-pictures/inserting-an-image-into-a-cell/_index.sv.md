---
title: Infoga en bild i en cell
description: Aspose.Cells är ett Node.js via Java-bibliotek för att arbeta med kalkylbladsfiler. Denna artikel förklarar hur man anpassar en bild exakt till en enskild cellstorlek med två olika metoder, placera en flytande bild över cellen, eller bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas för att passa cellens visningsområde. Välj den metod som bäst matchar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att anpassa en bild exakt till en enskild cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, personalregister, instrumentpaneler eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kan du vilja ha en ren, cellbunden bild som håller sig justerad med den cell som äger den.

Aspose.Cells stödjer detta scenario på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` på kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess fästpunktsceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bilddata till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.

Resten av denna artikel går igenom båda metoderna, förklarar de relevanta API:erna och visar hur man använder dem i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte är en del av någon enskild cell, är den förankrad vid ett cellintervall. Bildens fästpunktsceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella utsträckning på kalkylbladet. Som standard sträcker sig en nyligen tillagd bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** behöver du:

1. Lägg till bilden med `worksheet.getPictures().add(int row, int column, InputStream stream)`, vilket förankrar den nya bilden vid den angivna cellen.
2. Ange de fyra fästpunktsegenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` så att bilden flyttas och ändrar storlek med den underliggande cellen när användaren ändrar kolumnbredd eller radhöjd.

### **Förankra bilden till en enskild cell**

Bildens förankring definieras av fyra nollbaserade indexegenskaper:

- `picture.setUpperLeftRow(int)` — radindex för bildens övre kant.
- `picture.setUpperLeftColumn(int)` — kolumnindex för bildens vänstra kant.
- `picture.setLowerRightRow(int)` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna längst ner på rad `r`, ange detta till `r + 1`.
- `picture.setLowerRightColumn(int)` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, ange detta till `c + 1`.

Till exempel, för att anpassa bilden exakt till cell **C6** (radindex `5`, kolumnindex `2`), ange `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` och `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på den nedre högra fästpunkten är den vanligaste källan till bilder som verkar överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteendet**

`Picture.Placement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och ändrar storlek tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Öppna bildfilen från disk till en `InputStream` (till exempel genom att använda `FileInputStream`) så att strömmen stängs korrekt.
4. Anropa `worksheet.getPictures().add(5, 2, stream)` för att lägga till en bild förankrad vid cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra fästpunktkoordinaterna så att bilden endast täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Ange `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` för att hålla bilden justerad med C6 när kolumnen eller raden ändras i storlek.
7. Lägg eventuellt till exempeltext i omgivande celler för att demonstrera att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar den fullständiga metoden.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.EmbeddedImage`. Att tilldela bilddata till denna egenskap bifogar bilden till själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga fästpunktskoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad, eller användas i andra cellnivåoperationer.

Detta gör `Cell.EmbeddedImage` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som finns inuti denna cell".

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Läs bildfilen från disk till en bytearray (till exempel genom att använda `Files.readAllBytes` från `java.nio.file.Files`).
4. Hämta en referens till målcellen — antingen genom `worksheet.getCells().get("C6")` eller `worksheet.getCells().get(5, 2)`.
5. Tilldela bytearrayen till cellens `EmbeddedImage`-egenskap via `cell.setEmbeddedImage(bytes)`.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar den fullständiga metoden.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Hämta målcellen C6
var cell = worksheet.getCells().get("C6");

// Läs bildfilen till en byte-array
var imageData = fs.readFileSync("logo.png");

// Bädda in bilden direkt i cellen
cell.setEmbeddedImage(imageData);

// Justera eventuellt radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.getCells().setColumnWidth(2, 30);   // Kolumn C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Rad 6 (index 5)

// Spara den resulterande arbetsboken som en .xlsx-fil
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Välja rätt metod**

Båda metoderna producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lager eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan fungerar med `PictureCollection`.
  - Du behöver beräkna fästpunktskoordinater dynamiskt baserat på kalkylbladslayouten.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha enklast möjliga infogning av en bild i en cell.
  - Bilden ska följa med cellen som vilket annat cellinnehåll som helst.
  - Du behöver inte manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}