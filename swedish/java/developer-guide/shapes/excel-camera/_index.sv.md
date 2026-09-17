---
title: Excel-kamera i Aspose.Cells for Java
linktitle: Excel-kamera i Aspose.Cells for Java
description: Lär dig hur du använder Excel-kamera i Aspose.Cells for Java för att skapa en dynamisk bild kopplad till ett cellintervall som uppdateras med källdata och bevarar all källformatering.
keywords: Aspose.Cells, Java, Excel-kamera, dynamisk bild, länkad bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /sv/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-kamera är ett kalkylbladsobjekt som renderar en livebild av ett cellintervall och flyter på ritningslagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdatan ändras och en statisk bild som tar en engångsbild av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## What Is Excel Camera?
Excel-kameran är i princip ett bildobjekt förankrat vid en specifik rad och kolumn på kalkylbladets ritningslager. Till skillnad från en vanlig infogad bild är kameran kopplad till ett källintervall via en A1-formel, till exempel `"A1:F10"`. När en cell i det intervallet ändras uppdateras kamerans bild automatiskt för att återspegla det nya innehållet. Kameran bevarar fullständig formatering av källområdet — kanter, bakgrundsfärger, teckensnitt och talformat — så allt som visas i cellerna visas även i kamerans bild. Detta gör kameran särskilt användbar för dashboards, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två varningar gäller: du måste anropa `updateSelectedValue()` innan du sparar arbetsboken, och filen kommer att exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddad bilddata snarare än en liveomräkning.

## Method 1 — Add a Dynamic Camera Picture
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameraverktyg. Den fungerar genom att lägga till en bild utan initialt bildinnehåll, och sedan tilldela den en `Formula` som refererar till källintervallet. När formeln har tilldelats uppdaterar ett anrop till `updateSelectedValue()` den inbäddade bilddatan så att den är synkroniserad med cellerna den speglar. Kameran implementeras inte via en dedikerad klass — den byggs helt på standardtypen `Picture`.
De viktigaste API:erna är:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — lägger till en bild förankrad vid angiven rad och kolumn. Genom att skicka `null` för parametern `stream` skapas en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.getPictures().get(index)` — indexeringsåtkomst för att hämta en specifik `Picture` från samlingen.
- `Picture.setFormula(String value)` — ställer in A1-referensenen till källintervallet som kameran speglar, till exempel `"A1:F10"`.
- `Picture.updateSelectedValue()` — en void-metod som uppdaterar den inbäddade bilddatan från cellerna som refereras av `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` MÅSTE anropas innan sparning när utdata är HTML eller PDF; annars kommer den exporterade filen inte att innehålla bilddata och kameran visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, länkar den till källintervallet `A1:F10` via `setFormula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellintervall. Istället för att upprätthålla en live-länk renderar du intervallet till bildbytes en gång, paketerar dessa bytes i en `ByteArrayInputStream` och lägger till dem som en vanlig bild. Bildinnehållet är sedan fixerat vid tidpunkten för skapandet och uppdateras inte automatiskt när källcellerna ändras.
De viktigaste API:erna är:
- `Cells.createRange(String address)` — bygger ett `Range`-objekt från en A1-adress, till exempel `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderar intervallet till bildbytes. Genom att skicka `null` används standardrenderingsalternativen; överlagringar finns för finare kontroll över utdata.
- `new ByteArrayInputStream(byte[] buffer)` — paketerar de renderade bildbyten i en `ByteArrayInputStream` som kan matas in i `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — lägger till bilden förankrad vid angiven rad och kolumn, den här gången genom att skicka den `ByteArrayInputStream` som producerades av renderingen.
Följande kod skapar en arbetsbok, bygger en `Range` för `A1:F10`, renderar den till bildbytes via `Range.toImage(null)`, paketerar byten i en `ByteArrayInputStream`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **Dynamisk kamera:** uppdateras vid varje omräkning, stöder HTML- och PDF-export efter `updateSelectedValue()`, och bevarar live-länk-beteendet under hela filens livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fixerad visuell ögonblicksbild inbäddad vid byggtiden snarare än en live-spegel av datan.
Aspose.Cells stöder både en dynamisk, automatiskt uppdaterande kamera byggd på `Picture.Formula` plus `updateSelectedValue()` och en statisk, engångskamera byggd på `Range.toImage` plus en `ByteArrayInputStream`. Välj den dynamiska metoden när din utdata behöver hålla sig synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fixerad visuell ögonblicksbild vid byggtiden.

## Related Articles
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Java](/cells/sv/java/convert-sparkline-to-image-and-html/)
- [Infoga en bild i en cell](/cells/sv/java/inserting-an-image-into-a-cell/)
- [Lägga till filterfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Java](/cells/sv/java/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/java/change-page-field-layout/)

{{< app/cells/assistant language="java" >}}