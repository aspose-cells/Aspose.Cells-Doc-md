---
title: Excel-kamera i Aspose.Cells for Node.js via Java
linktitle: Excel-kamera i Aspose.Cells for Node.js via Java
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for Node.js via Java för att skapa en dynamisk bild kopplad till ett cellintervall som uppdateras med källdata och bevarar all källformatering.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel-kamera, dynamisk bild, länkad bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /sv/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som visar en livebild av ett cellintervall och flyter på ritlagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdatan ändras och en statisk bild som tar en engångsögonblicksbild av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## Vad är Excel-kamera?
Excel-kameran är i princip ett bildobjekt förankrat vid en specifik rad och kolumn på kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är kameran kopplad till ett källintervall via en A1-formel som t.ex. `"A1:F10"`. Närhelst en cell inom det intervallet ändras uppdateras kamerans bild automatiskt för att återspegla det nya innehållet. Kameran bevarar hela formateringen av källområdet — kanter, bakgrundsfärger, typsnitt och talformat — så allt som är synligt i cellerna visas också i kamerans bild. Detta gör kameran särskilt användbar för instrumentpaneler, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två förbehåll gäller: du måste anropa `updateSelectedValue()` innan du sparar arbetsboken, och filen kommer att exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddad bilddata snarare än en live-omberäkning.

## Metod 1 — Lägg till en dynamisk kamerabild
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameratool. Den fungerar genom att lägga till en bild utan initialt bildinnehåll och sedan tilldela den en `Formula` som refererar till källintervallet. När formeln är tilldelad uppdaterar ett anrop till `updateSelectedValue()` den inbäddade bilddatan så att den är synkroniserad med cellerna den speglar. Kameran implementeras inte via en dedikerad klass — den är helt byggd på standardtypen `Picture`.
De centrala API:erna är:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — lägger till en bild förankrad vid den angivna raden och kolumnen. Att skicka `null` för parametern `stream` skapar en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.getPictures().get(index)` — indexeringsåtkomst för att hämta en specifik `Picture` från samlingen.
- `Picture.Formula` — en strängegenskap (`getFormula()`/`setFormula()`) som håller A1-referensen till källintervallet som kameran speglar, t.ex. `"A1:F10"`.
- `Picture.updateSelectedValue()` — en void-metod som uppdaterar den inbäddade bilddatan från cellerna som refereras av `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` MÅSTE anropas innan du sparar när utdata är HTML eller PDF; annars kommer den exporterade filen inte att innehålla bilddata och kameran kommer att visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, länkar den till källintervallet `A1:F10` via egenskapen `Formula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10, uppdatera sedan
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Metod 2 — Lägg till en statisk kamerabild
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellintervall. Istället för att upprätthålla en live-länk renderar du intervallet till bildbytes en gång, paketerar dessa bytes i en `ByteArrayInputStream` och lägger till dem som en vanlig bild. Bildinnehållet är då fast vid skapandetillfället och uppdateras inte automatiskt när källceller ändras.
De centrala API:erna är:
- `Cells.createRange(String address)` — bygger ett `Range`-objekt från en A1-adress, t.ex. `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderar intervallet till bildbytes. Att skicka `null` använder standardrenderingsalternativen; överlagringar finns för finare kontroll över utdata.
- `new ByteArrayInputStream(byte[] buffer)` — paketerar de renderade bildbytes i en `ByteArrayInputStream` som kan matas in i `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — lägger till bilden förankrad vid den angivna raden och kolumnen, denna gång med `ByteArrayInputStream` som producerats av renderingen.
Följande kod skapar en arbetsbok, bygger en `Range` för `A1:F10`, renderar den till bildbytes via `range.toImage(null)`, paketerar bytes i en `ByteArrayInputStream`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statisk kamera: bygg Range, rendera till bytes, wrappa i ByteArrayInputStream, lägg till som bild
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Välja mellan dynamisk och statisk
- **Dynamisk kamera:** uppdateras vid varje omberäkning, stöder HTML- och PDF-export efter `updateSelectedValue()` och bevarar live-länkens beteende under filens livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fast visuell ögonblicksbild inbäddad vid byggtillfället snarare än en live-spegel av datan.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande kamera byggd på `Picture.Formula` plus `updateSelectedValue()` och en statisk, engångskamera byggd på `Range.toImage` plus en `ByteArrayInputStream`. Välj den dynamiska metoden när din utdata behöver hålla sig synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fast visuell ögonblicksbild vid byggtillfället.

{{< app/cells/assistant language="nodejs-java" >}}