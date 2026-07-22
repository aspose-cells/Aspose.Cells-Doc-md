---
title: Konvertera sparklinje till bild och HTML i Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells sparklinjer till fristående bilder för cellinbäddning och exporterar sparklinje-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /sv/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklinjer är miniatyrdiagram placerade inuti kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparklinje som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparklinje-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.embedded_image` som används i denna artikel är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklinjer är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparklinje lämnar cellen – till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.to_image` renderar en enskild sparklinje till en ström, och de resulterande bytena kan tilldelas till `Cell.embedded_image` så att bilden lagras inuti en enda cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken – sparklinjer och allt – till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena från början till slut.

## **Arbetsflöde 1 – Rendera sparklinjer till bilder och bädda in dem i celler**

I det här arbetsflödet bygger du ett kalkylblad som innehåller ett litet intervall av källvärden, kopplar tre olika sparklinjegrupper (Line, Column och Stacked/Win-Loss) till det intervallet, renderar varje grupp som en PNG och skriver dessa PNG-byten till intilliggande celler som inbäddade bilder. Det slutliga resultatet är en enda `.xlsx`-fil som innehåller både de levande sparklinjerna och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.sparkline_groups.add(...)`:
   - En `SparklineType.LINE`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.COLUMN`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.STACKED` (win/loss)-grupp förankrad vid `H1`, med dataintervall `A1:E1`.
5. Skapa en `ImageOrPrintOptions`-instans och ställ in dess `image_type` till `ImageType.PNG` så att varje sparklinje renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparklinje med `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, konvertera `ByteArrayOutputStream` till en `byte[]` (eller läs dess `to_byte_array()` till Python `bytes`), och tilldela bytena till `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` respektive `worksheet.cells["H2"].embedded_image`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Skapa en ny arbetsbok och öppna det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fyll i exempeldata i cellerna A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Lägg till en linjesparklinegrupp förankrad vid F1 (kolumn 5, rad 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Lägg till en kolumnsparklinegrupp förankrad vid G1 (kolumn 6, rad 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Lägg till en vinst/förlust (staplad) sparklinegrupp förankrad vid H1 (kolumn 7, rad 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Konfigurera bildalternativ för PNG-utdata
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Konvertera linjesparkline till bild och bädda in den i cell F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Konvertera kolumnsparkline till bild och bädda in den i cell G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Konvertera vinst/förlust-sparkline till bild och bädda in den i cell H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Spara arbetsboken på disk
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

Koden ovan skapar en arbetsbok där varje visuell representation av en sparklinje dupliceras i två former: den levande, nativa sparklinjen förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lever inuti själva filen förblir arbetsboken ett enda självständigt artefakt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparklinjegrupp som en PNG, konvertera `ByteArrayOutputStream` till en `byte[]` (eller använd `to_byte_array()` för att erhålla ett Python `bytes`-objekt), och tilldela arrayen till egenskapen `embedded_image` för målcellen – det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparklinjegrupp är förankrad till en enda cell kan du adressera den via indexeraren `group.sparklines[0]` istället för att räkna upp med en `for`-loop. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparklinje per ankarcell". Att lagra bildbytena via `Cell.embedded_image` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 – Exportera sparklinjekalkylbladet till HTML**

När arbetsboken innehåller levande sparklinjer (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde återanvänder du filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 och konverterar den till ett rent HTML-dokument med en sida.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ställ in dess egenskap `export_active_worksheet_only` till `True` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", html_options)` för att skriva HTML-utdata till disk.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

Koden ovan tar den sparklinje-rika arbetsboken från Arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklinjer bevaras som inline SVG- eller PNG-renderingar inuti den genererade HTML:en, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva Excel installerat. Genom att ställa in `export_active_worksheet_only` till `True` undviker du att av misstag publicera dolda blad eller extra data – endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för att finjustera utdata, såsom `export_hidden_worksheet`, `export_images_as_base64` och `encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsaccessorn `worksheet.sparkline_groups` används för att deklarera typen (Line, Column, Stacked), dataintervallet och ankarcellen för varje sparklinjegrupp. I denna artikel är varje grupp förankrad till en enda cell, så gruppen nås via `worksheet.sparkline_groups[i]`.
- `Sparkline` och indexeraren `group.sparklines[0]` returnerar den enskilda sparklinjen inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparklinje krävs ingen `for`-loop.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparklinjen till en tillhandahållen `OutputStream` (till exempel en `ByteArrayOutputStream`). Metoden returnerar `void`; du läser bytena från strömmen efter anropet.
- `Cell.embedded_image` är en `byte[]`-egenskap som lagrar en bild inuti en enda cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att rundgånga en sparklinje renderad av `to_image` tillbaka till samma arbetsbok.
- `HtmlSaveOptions.export_active_worksheet_only` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` vid generering av en-sidiga rapporter.
- `ImageOrPrintOptions.image_type` finns i namnrymden `com.aspose.cells.drawing` och väljer bildformatet (till exempel `ImageType.PNG`) som används vid rendering med `to_image` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklinjer i Aspose.Cells for Python via Java](/cells/sv/python-java/sparkline/)
- [Infoga en bild i en cell](/cells/sv/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}