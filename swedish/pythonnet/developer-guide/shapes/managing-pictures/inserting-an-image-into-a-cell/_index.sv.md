---
title: Infoga en bild i en cell
description: Aspose.Cells är ett Python-bibliotek för att arbeta med kalkylarksfiler. Den här artikeln förklarar hur man anpassar en bild exakt till en enda cellstorlek med två olika metoder, placera en flytande bild över cellen, eller bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Python-bibliotek, kalkylark, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att associera en bild med en enda cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas till cellens visningsområde. Välj den metod som bäst matchar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att anpassa en bild exakt till en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, dashboards eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kan du vilja ha en ren, cellbunden bild som håller sig justerad med cellen som äger den.

Aspose.Cells stöder detta scenario på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `placement` till `MOVE_AND_SIZE`, och justera dess förankringsceller (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bildbyten till cellens `embedded_image`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.

Resten av den här artikeln går igenom båda metoderna, förklarar de relevanta API:erna och visar hur man använder dem i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte är en del av någon enskild cell är den förankrad vid ett cellintervall. Bildens förankringsceller — dess övre vänstra och nedre högra hörn — avgör dess visuella omfattning på kalkylbladet. Som standard spänner en nybildad bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** måste du:

1. Lägga till bilden med `Worksheet.pictures.add(row, column, stream)`, vilket förankrar den nya bilden vid den angivna cellen.
2. Ställa in de fyra förankringsegenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ställa in `Picture.placement` till `PlacementType.MOVE_AND_SIZE` så att bilden flyttas och ändras storlek tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enda cell**

Bildens förankring definieras av fyra nollbaserade indexegenskaper:

- `Picture.upper_left_row` — radindex för bildens övre kant.
- `Picture.upper_left_column` — kolumnindex för bildens vänstra kant.
- `Picture.lower_right_row` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna längst ner i rad `r`, ange detta till `r + 1`.
- `Picture.lower_right_column` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, ange detta till `c + 1`.

Till exempel, för att anpassa bilden exakt till cell **C6** (radindex `5`, kolumnindex `2`), ange `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6` och `lower_right_column = 3`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Avvikelser med ett i den nedre högra förankringen är den vanligaste källan till bilder som ser ut att överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteendet**

`Picture.placement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MOVE_AND_SIZE`, vilket gör att bilden flyttas och ändras storlek tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Öppna bildfilen från disk till en filström (eller ett `BytesIO`-objekt) med hjälp av ett `with`-block så att strömmen kasseras korrekt.
4. Anropa `worksheet.pictures.add(5, 2, stream)` för att lägga till en bild förankrad vid cell C6. Spara den returnerade `Picture`-referensen.
5. Ställ in de fyra förankringskoordinaterna så att bilden endast täcker cell C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Ställ in `picture.placement = PlacementType.MOVE_AND_SIZE` för att hålla bilden justerad med C6 när kolumnen eller raden ändras.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE

workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.embedded_image`. Att tilldela bildbyten till denna egenskap bifogar bilden till själva cellen, som om den vore infogat innehåll.

### **Hur inbäddade bilder fungerar**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga förankringskoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad eller användas i andra cellnivåoperationer.

Detta gör `Cell.embedded_image` till det mest kortfattade alternativet när ditt mål helt enkelt är "en bild som finns inuti denna cell".

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Läs bildfilen från disk till ett `bytes`-objekt (till exempel genom att öppna filen i binärt läge och anropa `.read()`).
4. Hämta en referens till målcellen — antingen via `worksheet.cells["C6"]` eller `worksheet.cells[5, 2]`.
5. Tilldela byteobjektet till cellens `embedded_image`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Hämta målcellen C6
cell = worksheet.cells["C6"]

# Läs bildfilen till en byte-array
with open("logo.png", "rb") as f:
    imageData = f.read()

# Bädda in bilden direkt i cellen
cell.embedded_image = imageData

# Valfritt: justera radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.cells.set_column_width(2, 30)   # Kolumn C (index 2)
worksheet.cells.set_row_height(5, 100)     # Rad 6 (index 5)

# Spara den resulterande arbetsboken som en .xlsx-fil
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Välja rätt metod**

Båda metoderna ger en bild som passar inuti en enda cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagervisning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan arbetar med `pictures`-samlingar.
  - Du behöver beräkna förankringskoordinater dynamiskt baserat på kalkylbladets layout.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som vilket annat cellinnehåll som helst.
  - Du behöver inte manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}

## **Relaterade artiklar**

- [Hur man infogar bild i cell](/cells/sv/python-net/how-to-place-image-to-cell/)
- [Lägg till bildhyperlänkar](/cells/sv/python-net/add-image-hyperlinks/)
- [Ladda en webbild från en URL till ett Excel-kalkylblad](/cells/sv/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulera position, storlek och designer-diagram](/cells/sv/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}