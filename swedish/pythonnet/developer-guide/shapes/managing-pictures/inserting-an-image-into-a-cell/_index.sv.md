---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells är ett Python-bibliotek för att arbeta med kalkylbladsfiler. Den här artikeln förklarar hur man anpassar en bild exakt till en enda cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Python-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att koppla en bild till en enda cell. En flytande bild är en form på kalkylbladets ritningslager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas för att passa cellens visningsområde. Välj det tillvägagångssätt som bäst passar dina layoutkrav.

## **Introduktion**
Att anpassa en bild exakt till en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, personalkataloger, instrumentpaneler eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig justerad med cellen som äger den.
Aspose.Cells stöder det här scenariot på två kompletterande sätt:
- **Tillvägagångssätt 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ställ in dess `placement` till `MOVE_AND_SIZE` och justera dess ankarceller (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) så att bilden täcker exakt en cell.
- **Tillvägagångssätt 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `embedded_image`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.
Resten av den här artikeln går igenom båda tillvägagångssätten, förklarar de relevanta API:erna och visar hur de används i kod.

## **Tillvägagångssätt 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritningslager. Även om den inte är en del av någon enskild cell är den förankrad i ett cellintervall. Bildens ankarceller — dess övre vänstra och nedre högra hörn — avgör dess visuella omfattning på kalkylbladet. Som standard sträcker sig en nyligen tillagd bild över flera celler.
För att få en flytande bild att täcka **exakt en cell** behöver du:
1. Lägg till bilden med hjälp av `Worksheet.pictures.add(row, column, stream)`, vilket förankrar den nya bilden i den givna cellen.
2. Ställ in de fyra ankaregenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ställ in `Picture.placement` till `PlacementType.MOVE_AND_SIZE` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enda cell**
Bildens ankare definieras av fyra nollbaserade indexegenskaper:
- `Picture.upper_left_row` — radindexet för bildens övre kant.
- `Picture.upper_left_column` — kolumnindexet för bildens vänstra kant.
- `Picture.lower_right_row` — radindexet för bildens nedre kant. För att bildens nedre kant ska hamna längst ner på rad `r`, ställ in detta på `r + 1`.
- `Picture.lower_right_column` — kolumnindexet för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, ställ in detta på `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på det nedre högra ankaret är den vanligaste orsaken till att bilder verkar överlappa in i en intilliggande cell.

### **Styra placeringsbeteendet**
`Picture.placement` är en uppräkning av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellbild är `PlacementType.MOVE_AND_SIZE`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell och bevarar den exakta passningen.

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Öppna bildfilen från disk till en filström (eller ett `BytesIO`-objekt) med hjälp av ett `with`-block så att strömmen kasseras korrekt.
4. Anropa `worksheet.pictures.add(5, 2, stream)` för att lägga till en bild förankrad i cell C6. Fånga den returnerade `Picture`-referensen.
5. Ställ in de fyra ankarpositionerna så att bilden bara täcker cell C6: `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Ställ in `picture.placement = PlacementType.MOVE_AND_SIZE` för att hålla bilden justerad med C6 när kolumnen eller raden ändras i storlek.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att bara cell C6 innehåller bilden.
8. Spara arbetsboken på disk som en `.xlsx`-fil.
Följande kod demonstrerar det fullständiga tillvägagångssättet.

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

## **Tillvägagångssätt 2: Bädda in en bild direkt i en cell**
Aspose.Cells erbjuder också en enklare mekanism för cellbundna bilder: egenskapen `Cell.embedded_image`. Genom att tilldela bildbytes till den här egenskapen bifogas bilden till själva cellen, som om den vore inline-innehåll.

### **Så här fungerar inbäddade bilder**
- Bilden lagras som en del av cellinnehållet snarare än som en form på ritningslagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga ankarpositioner eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad eller användas i andra operationer på cellnivå.
Detta gör `Cell.embedded_image` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som lever inuti den här cellen".

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Läs bildfilen från disk till ett `bytes`-objekt (till exempel genom att öppna filen i binärt läge och anropa `.read()`).
4. Hämta en referens till målcellen — antingen via `worksheet.cells["C6"]` eller `worksheet.cells[5, 2]`.
5. Tilldela bytes-objektet till cellens `embedded_image`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och kolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken på disk som en `.xlsx`-fil.
Följande kod demonstrerar det fullständiga tillvägagångssättet.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Välja rätt tillvägagångssätt**
Båda tillvägagångssätten producerar en bild som passar inuti en enda cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:
- **Använd en flytande bild (Tillvägagångssätt 1) när:**
  - Du behöver finare kontroll över placering, lagerordning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver bakåtkompatibilitet med kod som redan arbetar med `pictures`-samlingar.
  - Du behöver beräkna ankarpositioner dynamiskt baserat på kalkylbladets layout.
- **Använd en inbäddad bild (Tillvägagångssätt 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som annat cellinnehåll.
  - Du inte behöver manipulera bilden som en form.
{{% /alert %}}

{{% /alert %}}

## Relaterade artiklar
- [Excel Camera i Aspose.Cells for Python via .NET](/cells/sv/python-net/excel-camera/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for Python via .NET](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Python via .NET](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/python-net/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Python via .NET](/cells/sv/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}