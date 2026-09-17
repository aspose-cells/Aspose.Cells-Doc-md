---
title: Excel-kamera i Aspose.Cells for Python via .NET
linktitle: Excel-kamera i Aspose.Cells for Python via .NET
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for Python via .NET för att skapa en dynamisk bild kopplad till ett cellområde som uppdateras med källdata och bevarar all källformatering.
keywords: Aspose.Cells, Python, Excel-kamera, dynamisk bild, länkad bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /sv/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som renderar en levande bild av ett cellområde och flyter på ritlagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdata ändras och en statisk bild som tar en engångsögonblicksbild av ett område. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## Vad är Excel-kamera?
Excel-kameran är i princip ett bildobjekt förankrat i en specifik rad och kolumn på kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är kameran kopplad till ett källområde via en A1-formel som t.ex. `"A1:F10"`. När en cell i det området ändras uppdateras kamerans bild automatiskt för att återspegla det nya innehållet. Kameran bevarar all formatering i källområdet — kanter, bakgrundsfärger, teckensnitt och talformat — så allt som är synligt i cellerna visas också i kamerans bild. Detta gör kameran särskilt användbar för dashboards, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två förbehåll gäller: du måste anropa `update_selected_value()` innan du sparar arbetsboken, och filen exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddade bilddata snarare än en levande omräkning.

## Metod 1 — Lägg till en dynamisk kamerabild
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameraverktyg. Den fungerar genom att lägga till en bild utan ursprungligt bildinnehåll och sedan tilldela den en `formula` som refererar till källområdet. När formeln har tilldelats uppdaterar ett anrop till `update_selected_value()` den inbäddade bilddatan så att den är synkroniserad med cellerna den speglar. Kameran implementeras inte via en dedikerad klass — den är helt uppbyggd på standardtypen `Picture`.
De viktigaste API:erna är:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — lägger till en bild förankrad vid angiven rad och kolumn. Om du skickar `None` för parametern `stream` skapas en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.pictures[index]` — indexeringsåtkomst för att hämta en specifik `Picture` från samlingen.
- `picture.formula` — en strängegenskap (get/set) som håller A1-referensen till källområdet som kameran speglar, t.ex. `"A1:F10"`.
- `picture.update_selected_value()` — en void-metod som uppdaterar den inbäddade bilddatan från cellerna som refereras av `formula`.

{{% alert color="primary" %}}
`update_selected_value()` MÅSTE anropas innan du sparar när utdata är HTML eller PDF, annars kommer den exporterade filen inte att innehålla bilddatan och kameran visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, kopplar den till källområdet `A1:F10` via egenskapen `formula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10, uppdatera sedan
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metod 2 — Lägg till en statisk kamerabild
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellområde. Istället för att upprätthålla en levande länk renderar du området till bildbyte en gång, packar in dessa byte i en `BytesIO` och lägger till dem som en vanlig bild. Bildinnehållet är då fast vid skapandetillfället och uppdateras inte automatiskt när källcellerna ändras.
De viktigaste API:erna är:
- `Cells.create_range(string address)` — bygger ett `Range`-objekt från en A1-adress som t.ex. `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — renderar området till bildbyte. Om du skickar `None` används standardrenderingsalternativen; överlagringar finns för finare kontroll över utdata.
- `BytesIO(byte[] buffer)` — packar in de renderade bildbyten i en `BytesIO` som kan matas in i `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — lägger till bilden förankrad vid angiven rad och kolumn, den här gången med den `BytesIO` som skapats av renderingen.
Följande kod skapar en arbetsbok, bygger en `Range` för `A1:F10`, renderar den till bildbyte via `Range.to_image(null)`, packar in byten i en `BytesIO`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Statisk kamera: bygg Range, rendera till bytes, wrappar i BytesIO, lägg till som bild
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Välja mellan dynamisk och statisk
- **Dynamisk kamera:** uppdateras vid varje omräkning, stöder HTML- och PDF-export efter `update_selected_value()`, och bevarar levande länkbeteende under filens hela livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fast visuell ögonblicksbild inbäddad vid byggtiden snarare än en levande spegel av data.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande kamera byggd på `picture.formula` plus `update_selected_value()` och en statisk engångskamera byggd på `Range.to_image` plus en `BytesIO`. Välj den dynamiska metoden när din utdata behöver hållas synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fast visuell ögonblicksbild vid byggtiden.

{{< app/cells/assistant language="python-net" >}}