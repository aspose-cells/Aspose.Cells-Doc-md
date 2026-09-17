---
title: Excel Camera i Aspose.Cells for .NET
description: Lär dig hur du använder Excel Camera i Aspose.Cells for .NET för att skapa en dynamisk bild kopplad till ett cellintervall som uppdateras med källdatan och bevarar all källformatering.
linktitle: Excel Camera
keywords: Aspose.Cells, .NET, Excel Camera, dynamisk bild, länkad bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /sv/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera är ett kalkylbladsobjekt som renderar en livebild av ett cellintervall och ligger på ritlagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som automatiskt uppdateras när källdatan ändras och en statisk bild som tar en engångssnapshot av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## Vad är Excel Camera?
Excel Camera är i grunden ett bildobjekt som är förankrat i en specifik rad och kolumn på kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är Camera kopplad till ett källintervall via en A1-formel som t.ex. `"A1:F10"`. Närhelst en cell i det intervallet ändras uppdateras Cameras bild automatiskt för att återspegla det nya innehållet. Camera bevarar fullständig formatering av källområdet — ramar, bakgrundsfärger, typsnitt och talformat — så allt som syns i cellerna visas också i Cameras bild. Detta gör Camera särskilt användbar för dashboards, sammanfattningar, sidopanel och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två förbehåll gäller, du måste anropa `UpdateSelectedValue()` innan du sparar arbetsboken och filen kommer att exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddade bilddata snarare än en liveomräkning.

## Metod 1 — Lägg till en dynamisk kamerabild
Den dynamiska Camera är den vanligaste metoden och ligger närmast Excels inbyggda Camera-verktyg. Den fungerar genom att lägga till en bild utan initialt bildinnehåll och sedan tilldela den en `Formula` som refererar till källintervallet. När formeln har tilldelats uppdaterar ett anrop till `UpdateSelectedValue()` de inbäddade bilddata så att de är synkroniserade med cellerna de speglar. Camera implementeras inte via en dedikerad klass —den byggs helt på standardtypen `Picture`.
De viktigaste API:erna är:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — lägger till en bild förankrad vid den givna raden och kolumnen. Om du skickar `null` för parametern `stream` skapas en tom bild som fungerar som platshållare för en dynamisk Camera. Metoden returnerar indexet för den nya bilden.
- `worksheet.Pictures[index]` — indexeraråtkomst för att hämta en specifik `Picture` från samlingen.
- `Picture.Formula` — en strängegenskap (get/set) som håller A1-referensen till källintervallet som Camera speglar, t.ex. `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — en void-metod som uppdaterar de inbäddade bilddata från cellerna som refereras av `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` MÅSTE anropas innan sparning när utdata är HTML eller PDF, annars kommer den exporterade filen inte att innehålla bilddata och Camera kommer att visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, länkar den till källintervallet `A1:F10` via egenskapen `Formula`, uppdaterar de inbäddade bilddata och sparar arbetsboken.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10, uppdatera sedan
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Metod 2 — Lägg till en statisk kamerabild
Den statiska Camera är i grunden en engångsrenderad förhandsvisning av ett cellintervall. Istället för att bibehålla en levande länk renderar du intervallet till bildbytes en gång, paketerar dessa bytes i en `MemoryStream` och lägger till dem som en vanlig bild. Bildinnehållet är då fixerat vid skapandetillfället och uppdateras inte automatiskt när källcellerna ändras.
De viktigaste API:erna är:
- `Cells.CreateRange(string address)` — bygger ett `Range`-objekt från en A1-adress som t.ex. `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — renderar intervallet till bildbytes. Om du skickar `null` används standardrenderingsalternativen; det finns överlagringar för finare kontroll över utdata.
- `new MemoryStream(byte[] buffer)` — paketerar de renderade bildbytes i en `MemoryStream` som kan matas in i `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — lägger till bilden förankrad vid den givna raden och kolumnen, denna gång genom att skicka den `MemoryStream` som skapades av renderingen.
Följande kod skapar en arbetsbok, bygger en `Range` för `A1:F10`, renderar den till bildbytes via `Range.ToImage(null)`, paketerar byten i en `MemoryStream`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Statisk kamera: bygg Range, rendera till bytes, wrappa i MemoryStream, lägg till som bild
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Välja mellan dynamisk och statisk
- **Dynamisk Camera:** uppdateras vid varje omräkning, stöder HTML- och PDF-export efter `UpdateSelectedValue()` och bevarar levande länk-beteendet under filens livstid.
- **Statisk Camera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fixerad visuell snapshot inbäddad vid byggtillfället snarare än en levande spegel av datan.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande Camera byggd på `Picture.Formula` plus `UpdateSelectedValue()` och en statisk, engångs-Camera byggd på `Range.ToImage` plus en `MemoryStream`. Välj den dynamiska metoden när din utdata behöver hålla sig synkroniserad med källcellerna och välj den statiska metoden när du bara behöver en fixerad visuell snapshot vid byggtillfället.

## Relaterade artiklar
- [Konvertera sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}