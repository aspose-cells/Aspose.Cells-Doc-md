---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells for Python via Java är ett bibliotek för arbete med kalkylbladsfiler. Den här artikeln förklarar hur du anpassar en bild exakt till en enskild cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form i kalkylbladets ritlager som visuellt ligger ovanpå ett cellintervall, medan en inbäddad bild lagras i själva cellen och automatiskt skalas för att passa cellens visningsområde. Välj det tillvägagångssätt som bäst passar dina layoutkrav.
{{% /alert %}}

## **Introduktion**
Att anpassa en bild exakt till en enskild cell är ett vanligt krav när man utformar kalkylblad som används som visuella rapporter, produktkataloger, personalkataloger, instrumentpaneler eller inventarielistor. I stället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en tydligt avgränsad bild som hålls justerad i förhållande till den cell den är knuten till.
Aspose.Cells stöder det här scenariot på två kompletterande sätt:
- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange `setPlacement` som `MOVE_AND_SIZE` och justera förankringscellerna (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bilddata i form av en bytearray till cellens `setEmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.
Resten av den här artikeln går igenom båda metoderna, beskriver de relevanta API:erna och visar hur de används i kod.

## **Metod 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som finns i kalkylbladets ritlager. Även om bilden inte är en del av någon enskild cell är den förankrad i ett cellintervall. Bildens förankringsceller – dess övre vänstra och nedre högra hörn – bestämmer bildens visuella utsträckning på kalkylbladet. Som standard sträcker sig en nyligen tillagd bild över flera celler.
För att en flytande bild ska täcka **exakt en cell** måste du:
1. Lägg till bilden med `Worksheet.getPictures().add(int row, int column, InputStream stream)`, vilket förankrar den nya bilden vid den angivna cellen.
2. Ange de fyra förankringsegenskaperna så att bildens avgränsningsrektangel sammanfaller med målcellen.
3. Ange `Picture.setPlacement` som `PlacementType.MOVE_AND_SIZE` så att bilden flyttas och storleksanpassas tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enskild cell**
Bildens förankring definieras av fyra egenskaper med nollbaserade index:
- `setUpperLeftRow` — radindexet för bildens övre kant.
- `setUpperLeftColumn` — kolumnindexet för bildens vänstra kant.
- `setLowerRightRow` — radindexet för bildens nedre kant. För att bildens nedre kant ska ligga vid underkanten av rad `r` ska värdet anges som `r + 1`.
- `setLowerRightColumn` — kolumnindexet för bildens högra kant. För att bildens högra kant ska ligga vid högra kanten av kolumn `c` ska värdet anges som `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel i det nedre högra ankaret är den vanligaste orsaken till bilder som ser ut att överlappa en intilliggande cell.

### **Styra placeringsbeteendet**
`getPlacement` är en uppräkning av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på den underliggande raden eller kolumnen. Det rekommenderade värdet för en bild i en enda cell är `PlacementType.MOVE_AND_SIZE`, vilket innebär att bilden flyttas och storleksanpassas tillsammans med den underliggande cellen så att den exakta anpassningen bibehålls.

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig arbetsbok).
2. Hämta målkalkylbladet `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Öppna bildfilen från disken som en `InputStream` (vanligtvis en `FileInputStream`) så att strömmen stängs korrekt.
4. Anropa `worksheet.getPictures().add(5, 2, stream)` för att lägga till en bild förankrad vid cell C6. Spara den returnerade `Picture`-referensen.
5. Ange de fyra förankringskoordinaterna så att bilden endast täcker cell C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Ange `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` för att hålla bilden justerad i förhållande till C6 när kolumnbredden eller radhöjden ändras.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken på disken som en `.xlsx`-fil.
Följande kod visar hela tillvägagångssättet.

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
Aspose.Cells tillhandahåller även en enklare mekanism för cellbundna bilder: egenskapen `Cell.setEmbeddedImage`. Att tilldela bilddata i form av en bytearray till den här egenskapen kopplar bilden till själva cellen, som om den vore inlineinnehåll.

### **Så här fungerar inbäddade bilder**
- Bilden lagras som en del av cellinnehållet och inte som en form i ritlagret.
- Bilden skalas automatiskt för att passa inom cellens renderade yta. Inga förankringskoordinater eller placeringsinställningar krävs.
- Cellen är fortfarande en riktig cell med en riktig adress. Den kan refereras i formler, sorteras som en del av en rad och användas i andra åtgärder på cellnivå.
Detta gör `Cell.setEmbeddedImage` till det mest koncisa alternativet när målet helt enkelt är ”en bild som finns inuti den här cellen”.

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig arbetsbok).
2. Hämta målkalkylbladet `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Läs in bildfilen från disken till en `byte[]`-array (till exempel med ett anrop till `Files.readAllBytes` i `java.nio.file.Files`).
4. Hämta målcellen – antingen via `worksheet.getCells().get("C6")` eller `worksheet.getCells().get(5, 2)`.
5. Tilldela bytearrayen till cellens `setEmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden för målraden och kolumnbredden för målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken på disken som en `.xlsx`-fil.
Följande kod visar hela tillvägagångssättet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Välja rätt metod**
Båda metoderna skapar en bild som anpassas till en enskild cell, men de skiljer sig åt när det gäller hur bilden lagras och beter sig:
- **Använd en flytande bild (Metod 1) när:**
  - Du behöver mer detaljerad kontroll över placering, lagerhantering eller justering i förhållande till andra ritobjekt.
  - Du vill att bilden ska fungera som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver bakåtkompatibilitet med kod som redan fungerar med `PictureCollection`.
  - Du behöver beräkna förankringskoordinater dynamiskt utifrån kalkylbladets layout.
- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill kunna infoga en bild i en cell så enkelt som möjligt.
  - Bilden ska följa med cellen som allt annat cellinnehåll.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}