---
title: Infoga en bild i en cell
description: Aspose.Cells for Python via Java är ett bibliotek för att arbeta med kalkylarksfiler. Den här artikeln förklarar hur man passar in en bild exakt i en enda cellstorlek med hjälp av två olika metoder, antingen placera en flytande bild över cellen, eller bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylark, infoga bild, bädda in bild, bild i cell, passa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att associera en bild med en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas till cellens visningsområde. Välj den metod som bäst motsvarar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att passa in en bild exakt i en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, dashboards eller inventarielistor. I stället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kan du vilja ha en ren, cellbunden bild som håller sig justerad med den cell som äger den.

Aspose.Cells stöder detta scenario på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` på kalkylbladet, ange dess `setPlacement` till `MOVE_AND_SIZE`, och justera dess ankarceller (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `setEmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.

Resten av den här artikeln går igenom båda metoderna, förklarar de relevanta API:erna och visar hur de används i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte är en del av någon enskild cell, är den förankrad till ett cellintervall. Bildens ankarceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella utsträckning på kalkylbladet. Som standard sträcker sig en nyligen tillagd bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** måste du:

1. Lägga till bilden med `Worksheet.getPictures().add(int row, int column, InputStream stream)`, vilket förankrar den nya bilden till den angivna cellen.
2. Ange de fyra ankaregenskaper så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Sätt `Picture.setPlacement` till `PlacementType.MOVE_AND_SIZE` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enskild cell**

Bildens ankare definieras av fyra nollbaserade indexegenskaper:

- `setUpperLeftRow` — radindex för bildens övre kant.
- `setUpperLeftColumn` — kolumnindex för bildens vänstra kant.
- `setLowerRightRow` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna i botten av rad `r`, sätt detta till `r + 1`.
- `setLowerRightColumn` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, sätt detta till `c + 1`.

Till exempel, för att passa in bilden exakt i cell **C6** (radindex `5`, kolumnindex `2`), sätt `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` och `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på det nedre högra ankaret är den vanligaste källan till bilder som ser ut att överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteendet**

`getPlacement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MOVE_AND_SIZE`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell, vilket bevarar den exakta passningen.

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Öppna bildfilen från disk till en `InputStream` (vanligtvis en `FileInputStream`) så att strömmen stängs ordentligt.
4. Anropa `worksheet.getPictures().add(5, 2, stream)` för att lägga till en bild förankrad till cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra ankar-koordinaterna så att bilden bara täcker cell C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Sätt `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` för att hålla bilden justerad med C6 när kolumnen eller raden ändras i storlek.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.setEmbeddedImage`. Att tilldela bildbytes till den här egenskapen fäster bilden till själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga ankar-koordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad, eller användas i andra cellnivåoperationer.

Detta gör `Cell.setEmbeddedImage` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som lever inuti den här cellen".

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Läs bildfilen från disk till en `byte[]`-array (till exempel genom att använda ett `Files.readAllBytes`-anrop från `java.nio.file.Files`).
4. Hämta en referens till målcellen — antingen via `worksheet.getCells().get("C6")` eller `worksheet.getCells().get(5, 2)`.
5. Tilldela byte-arrayen till cellens `setEmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# porterad kod här
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Hämta målcellen C6
cell = worksheet.getCells().get("C6")

# Läs bildfilen till en byte-array
imageData = open("logo.png", "rb").read()

# Bädda in bilden direkt i cellen
cell.setEmbeddedImage(imageData)

# Valfritt: justera radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.getCells().setColumnWidth(2, 30)   # Kolumn C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Rad 6 (index 5)

# Spara den resulterande arbetsboken som en .xlsx-fil
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Välja rätt metod**

Båda metoderna producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagring eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan markeras, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan arbetar med `PictureCollection`.
  - Du behöver beräkna ankar-koordinater dynamiskt baserat på kalkylbladets layout.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha det enklaste möjliga införandet av en bild i en cell.
  - Bilden ska följa med cellen som allt annat cellinnehåll.
  - Du inte behöver manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}