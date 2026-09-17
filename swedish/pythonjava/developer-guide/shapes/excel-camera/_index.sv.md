---
title: Excel-kamera i Aspose.Cells for Python via Java
linktitle: Excel-kamera i Aspose.Cells for Python via Java
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for Python via Java för att skapa en dynamisk bild länkad till ett cellområde som uppdateras med källdata och bevarar all källformatering.
keywords: Aspose.Cells, Python via Java, Excel-kamera, dynamisk bild, länkad bild, Picture.formula, updateSelectedValue, createRange, toImage, byte[] array
type: docs
weight: 90
url: /sv/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som återger en levande bild av ett cellområde och flyter på ritlagret som en vanlig bild. Aspose.Cells for Python via Java stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdata ändras och en statisk bild som tar en engångsbild av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## Vad är Excel-kamera?
Excel-kameran är i princip ett bildobjekt förankrat vid en specifik rad och kolumn på kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är kameran länkad till ett källintervall via en A1-formel som t.ex. `"A1:F10"`. Närhelst någon cell inom det intervallet ändras uppdateras kamerans bild automatiskt för att återspegla det nya innehållet. Kameran bevarar fullständig formatering av källområdet — kanter, bakgrundsfärger, teckensnitt och talformat — så allt som är synligt i cellerna visas också i kamerans bild. Detta gör kameran särskilt användbar för instrumentpaneler, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två förbehåll gäller, du måste anropa `updateSelectedValue()` innan arbetsboken sparas, och filen kommer att exporteras till HTML eller PDF, eftersom dessa format förlitar sig på den inbäddade bilddatan snarare än en live-omberäkning.

## Metod 1 — Lägg till en dynamisk kamerabild
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameraverktyg. Den fungerar genom att lägga till en bild utan initialt bildinnehåll och sedan tilldela den en formel som refererar till källintervallet. När formeln har tilldelats uppdaterar anropet till `updateSelectedValue()` den inbäddade bilddatan så att den är synkroniserad med cellerna den speglar. Kameran implementeras inte via en dedikerad klass — den byggs helt på standardtypen `Picture`.
De viktigaste API:erna är:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — lägger till en bild förankrad vid den angivna raden och kolumnen. Att skicka `None` för parametern `stream` skapar en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.getPictures().get(index)` — accessmetod för att hämta en specifik `Picture` från samlingen.
- `Picture.getFormula()` / `Picture.setFormula()` — hämta/ange A1-referensen till källintervallet som kameran speglar, t.ex. `"A1:F10"`.
- `Picture.updateSelectedValue()` — en void-metod som uppdaterar den inbäddade bilddatan från cellerna som refereras av formeln.

{{% alert color="primary" %}}
`updateSelectedValue()` MÅSTE anropas innan arbetsboken sparas när utdata är HTML eller PDF; annars kommer den exporterade filen inte att innehålla bilddata och kameran visas tom i den renderade utdatan.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, länkar den till källintervallet `A1:F10` via metoden `setFormula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10, uppdatera sedan
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metod 2 — Lägg till en statisk kamerabild
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellintervall. Istället för att underhålla en levande länk renderar du intervallet till bildbytes en gång, omsluter dessa bytes i en `byte[]`-array och lägger till dem som en vanlig bild. Bildinnehållet är sedan fixerat vid skapandetillfället och uppdateras inte automatiskt när källcellerna ändras.
De viktigaste API:erna är:
- `Cells.createRange(String address)` — bygger ett `Range`-objekt från en A1-adress som t.ex. `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderar intervallet till bildbytes. Att skicka `None` använder standardrenderingsalternativen; överlagringar finns för finare kontroll över utdata.
- `byte[] array(byte[] buffer)` — omsluter de renderade bildbyten i en `byte[] array` som kan matas in i `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — lägger till bilden förankrad vid den angivna raden och kolumnen, denna gång genom att skicka den `byte[] array` som produceras av renderingen.
Följande kod skapar en arbetsbok, bygger ett `Range` för `A1:F10`, renderar det till bildbytes via `Range.toImage(None)`, omsluter byten i en `byte[]`-array, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Statisk kamera: bygg Range, rendera till bytes, svep in i ByteArrayInputStream, lägg till som bild
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Välja mellan dynamisk och statisk
- **Dynamisk kamera:** uppdateras vid varje omberäkning, stöder HTML- och PDF-export efter `updateSelectedValue()`, och bevarar levande-länk-beteendet under filens livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fixerad visuell ögonblicksbild inbäddad vid byggtiden snarare än en levande spegling av datat.
Aspose.Cells for Python via Java stöder både en dynamisk, automatiskt uppdaterande kamera byggd på `setFormula` plus `updateSelectedValue()` och en statisk, engångskamera byggd på `toImage` plus en `byte[] array`. Välj den dynamiska metoden när din utdata behöver hålla sig synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fixerad visuell ögonblicksbild vid byggtiden.

{{< app/cells/assistant language="python" >}}