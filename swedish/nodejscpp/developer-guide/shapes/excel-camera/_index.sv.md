---
title: Excel-kamera i Aspose.Cells for Node.js via C++
linktitle: Excel-kamera i Aspose.Cells for Node.js via C++
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for Node.js via C++ för att skapa en dynamisk bild som är länkad till ett cellintervall och som uppdateras med källdata samt bevarar all källformatering.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel-kamera, dynamisk bild, länkad bild, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /sv/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som renderar en livebild av ett cellintervall och flyter på ritningslagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdatan ändras och en statisk bild som tar en engångsögonblicksbild av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## Vad är Excel-kamera?
Excel-kameran är i princip ett bildobjekt förankrat vid en specifik rad och kolumn på kalkylbladets ritningslager. Till skillnad från en vanlig infogad bild är kameran länkad till ett källintervall via en A1-stilformel som till exempel `"A1:F10"`. När en cell i intervallet ändras uppdateras kamerans bild automatiskt för att återge det nya innehållet. Kameran bevarar all formatering av källområdet — kantlinjer, bakgrundsfärger, teckensnitt och talformat — så allt som är synligt i cellerna visas också i kamerans bild. Detta gör kameran särskilt användbar för instrumentpaneler, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att scrolla eller upprepa data. Två förbehåll gäller: du måste anropa `updateSelectedValue()` innan arbetsboken sparas, och filen exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddade bilddata snarare än på en liveomräkning.

## Metod 1 — Lägg till en dynamisk kamerabild
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameraverktyg. Den fungerar genom att lägga till en bild utan initialt bildinnehåll och sedan tilldela den en `Formula` som refererar till källintervallet. När formeln har tilldelats uppdaterar ett anrop till `updateSelectedValue()` de inbäddade bilddata så att de är synkroniserade med cellerna de speglar. Kameran implementeras inte via en dedikerad klass — den byggs helt på standardtypen `Picture`.
De viktigaste API:erna är:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — lägger till en bild förankrad vid den givna raden och kolumnen. Att skicka `null` för parametern `stream` skapar en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `pictures.get(index)` — hämtar en specifik `Picture` från samlingen via index.
- `Picture.formula` — en strängegenskap (get/set) som håller A1-stilreferensen till källintervallet som kameran speglar, till exempel `"A1:F10"`.
- `Picture.updateSelectedValue()` — en void-metod som uppdaterar de inbäddade bilddata från cellerna som refereras av `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` MÅSTE anropas innan sparning när utdata är HTML eller PDF; annars kommer den exporterade filen inte att innehålla bilddata och kameran visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, länkar den till källintervallet `A1:F10` via egenskapen `Formula`, uppdaterar de inbäddade bilddata och sparar arbetsboken.

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
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Metod 2 — Lägg till en statisk kamerabild
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellintervall. Istället för att upprätthålla en live-länk renderar du intervallet till bildbytes en gång, lindar in dessa bytes i en `Buffer` och lägger till dem som en vanlig bild. Bildinnehållet är sedan fast vid skapandetillfället och uppdateras inte automatiskt när källceller ändras.
De viktigaste API:erna är:
- `Cells.createRange(address)` — bygger ett `Range`-objekt från en A1-stiladress som till exempel `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderar intervallet till bildbytes. Att skicka `null` använder standardrenderingsalternativen; överlagringar finns för finare kontroll över utdata.
- `new Buffer(byte[] buffer)` — lindar in de renderade bildbyten i en `Buffer` som kan matas in i `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — lägger till bilden förankrad vid den givna raden och kolumnen, denna gång med `Buffer` som skapats av renderingen.
Följande kod skapar en arbetsbok, bygger en `Range` för `A1:F10`, renderar den till bildbytes via `range.toImage(null)`, lindar in byten i en `Buffer`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Statisk kamera: bygg intervall, rendera till bytes, paketera i MemoryStream, lägg till som bild
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Välja mellan dynamisk och statisk
- **Dynamisk kamera:** uppdateras vid varje omräkning, stöder HTML- och PDF-export efter `updateSelectedValue()` och bevarar live-länksbeteendet under filens livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fast visuell ögonblicksbild inbäddad vid byggtiden snarare än en live-spegling av datan.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande kamera byggd på `Picture.formula` plus `updateSelectedValue()` och en statisk engångskamera byggd på `Range.toImage` plus en `Buffer`. Välj den dynamiska metoden när din utdata behöver hållas synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fast visuell ögonblicksbild vid byggtiden.

{{< app/cells/assistant language="nodejs-cpp" >}}