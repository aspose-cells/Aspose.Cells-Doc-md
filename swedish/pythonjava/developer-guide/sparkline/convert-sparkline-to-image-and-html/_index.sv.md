---
title: Konvertera sparklinje till bild och HTML i Aspose.Cells for Python via Java
linktitle: Konvertera sparklinje till bild och HTML i Aspose.Cells for Python via Java
description: Lär dig hur du med Aspose.Cells renderar sparklinjer till fristående bilder för inbäddning i celler och exporterar kalkylblad med sparklinjer till HTML med hjälp av HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparklinje, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, rendera sparklinje, konvertera sparklinje till bild, exportera sparklinje till HTML
type: docs
weight: 120
url: /sv/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklinjer är miniatyrdiagram som placeras i kalkylbladsceller. Med Aspose.Cells kan du extrahera varje sparklinje som en fristående bild, för inbäddning i en annan cell eller i en extern rapport, och även exportera hela kalkylbladet med sparklinjer till HTML för visning i webbläsare. Egenskapen `Cell.embedded_image` som används i den här artikeln är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**
Sparklinjer är ett kompakt sätt att visualisera trender direkt i kalkylbladet. Excel-användare ser dem direkt i cellerna, men i många verkliga användningsscenarier måste en sparklinje lämna cellen – till exempel för att bäddas in i en annan cell som en statisk bild, bifogas ett automatiskt e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.
Aspose.Cells stöder båda dessa åtgärder. Metoden `Sparkline.to_image` renderar en enskild sparklinje till en ström. Resultatet i form av byte kan sedan tilldelas `Cell.embedded_image`, så att bilden lagras i en enda cell i arbetsboken. Dessutom kan `HtmlSaveOptions` användas för att konvertera hela arbetsboken – inklusive sparklinjerna – till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena från början till slut.

## **Arbetsflöde 1 — Rendera sparklinjer till bilder och bädda in dem i celler**
I det här arbetsflödet skapar du ett kalkylblad med ett litet intervall med källvärden, kopplar tre olika sparklinjegrupper (Line, Column och Stacked/Win-Loss) till intervallet, renderar varje grupp till en PNG-bild och lagrar resultatet som en inbäddad bild i en intilliggande cell. Slutresultatet är en enda `.xlsx`-fil som innehåller både sparklinjerna och deras motsvarande statiska bilder.

### **Steg-för-steg-instruktioner**
1. Ange en arbetskatalog och se till att den finns på disken.
2. Skapa en ny `Workbook` och hämta en referens till den första `Worksheet`-instansen.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden, till exempel daglig försäljning eller temperaturmätningar.
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.sparkline_groups.add(...)`:
   - En `SparklineType.LINE`-grupp med `F1` som förankringscell och `A1:E1` som dataintervall.
   - En `SparklineType.COLUMN`-grupp med `G1` som förankringscell och `A1:E1` som dataintervall.
   - En `SparklineType.STACKED`-grupp (win/loss) med `H1` som förankringscell och `A1:E1` som dataintervall.
5. Skapa en `ImageOrPrintOptions`-instans och ange `image_type` till `ImageType.PNG`, så att varje sparklinje renderas som en transparent PNG-bild.
6. Spara arbetsboken som `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
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
lineArea.StartColumn = 5
lineArea.EndColumn = 5
lineArea.StartRow = 0
lineArea.EndRow = 0
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
# Lägg till en kolumnsparklinegrupp förankrad vid G1 (kolumn 6, rad 0)
columnArea = CellArea()
columnArea.StartColumn = 6
columnArea.EndColumn = 6
columnArea.StartRow = 0
columnArea.EndRow = 0
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
# Lägg till en Win/Loss (stapel) sparklinegrupp förankrad vid H1 (kolumn 7, rad 0)
stackedArea = CellArea()
stackedArea.StartColumn = 7
stackedArea.EndColumn = 7
stackedArea.StartRow = 0
stackedArea.EndRow = 0
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
# Konfigurera bildalternativ för PNG-utdata
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.PNG)
# Konvertera linjesparklinen till bild och bädda in den i cell F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())
# Konvertera kolumnsparklinen till bild och bädda in den i cell G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())
# Konvertera Win/Loss-sparklinen till bild och bädda in den i cell H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())
# Spara arbetsboken till disk
workbook.save("output_with_sparklines.xlsx")
jpype.shutdownJVM()
```

Koden ovan skapar en arbetsbok där varje visuell representation av en sparklinje finns i två former: själva sparklinjen, förankrad i rad 1, och en statisk PNG-bild som har bäddats in direkt i en intilliggande cell i rad 2. Eftersom bilderna finns i själva filen kan arbetsboken skickas via e-post eller arkiveras som en enda självständig fil, utan att referenserna till de inbäddade bilderna bryts. Rendera varje sparklinjegrupp till en PNG-bild, konvertera `ByteArrayOutputStream` till en `byte[]` eller använd `to_byte_array()` för att få ett objekt av typen Python `bytes`, och tilldela arrayen till målcellens `embedded_image`-egenskap. Den här tilldelningen gör att bilden lagras som en del av cellens innehåll.

{{% alert color="primary" %}}
Eftersom varje sparklinjegrupp är förankrad i en enda cell kan du referera till den via indexeraren `group.sparklines[0]` i stället för att iterera med en `for`-loop. Detta håller renderingskoden kort och följer det typiska mönstret med en sparklinje per förankringscell. Att lagra bilddata via `Cell.embedded_image` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera kalkylbladet med sparklinjer till HTML**
Om arbetsboken innehåller sparklinjer och eventuellt deras motsvarande inbäddade bilder kan hela kalkylbladet publiceras på webben genom att det sparas som HTML. Klassen `HtmlSaveOptions` ger kontroll över de inställningar som behövs för att styra exporten. I det här arbetsflödet återanvänder du filen `output_with_sparklines.xlsx` som skapades i arbetsflöde 1 och konverterar den till ett renodrat HTML-dokument med en enda sida.

### **Steg-för-steg-instruktioner**
1. Se till att filen `output_with_sparklines.xlsx` som skapades i arbetsflöde 1 finns i arbetskatalogen på disken.
2. Läs in filen i en ny `Workbook`-instans.
3. Skapa en `HtmlSaveOptions`-instans och ange `export_active_worksheet_only` till `True`, så att HTML-filen endast innehåller det aktiva kalkylbladet och inte hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", html_options)` för att skriva HTML-filen till disk.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, HtmlSaveOptions
workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)
jpype.shutdownJVM()
```

Koden ovan tar arbetsboken med sparklinjer från arbetsflöde 1 och omvandlar den till en portabel HTML-fil. Sparklinjer bevaras som inbäddade SVG- eller PNG-bilder i den genererade HTML-filen, beroende på exportläge, så att slutanvändare kan se trenderna i alla moderna webbläsare utan att behöva installera Excel. Genom att ange `export_active_worksheet_only` till `True` undviker du att oavsiktligt publicera dolda kalkylblad eller hjälpdata – endast det kalkylblad som användaren för närvarande ser exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` har ytterligare egenskaper som du kan använda för att finjustera resultatet, till exempel `export_hidden_worksheet`, `export_images_as_base64` och `encoding`. Justera dem efter behov för den avsedda distributionsmiljön.
{{% /alert %}}

## **API-sammanfattning**
Arbetsflödena ovan bygger på ett litet antal Aspose.Cells-API:er som används tillsammans.
- `SparklineGroup` och åtkomsten till samlingen `worksheet.sparkline_groups` används för att ange typen (Line, Column, Stacked), dataintervallet och förankringscellen för varje sparklinjegrupp. I den här artikeln är varje grupp förankrad i en enda cell och nås därför via `worksheet.sparkline_groups[i]`.
- `Sparkline` och indexeraren `group.sparklines[0]` returnerar den enskilda sparklinjen i en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparklinje behövs ingen `for`-loop.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparklinjen till den angivna `OutputStream`, till exempel en `ByteArrayOutputStream`. Metoden returnerar `void`; du läser byte från strömmen efter anropet.
- `HtmlSaveOptions.export_active_worksheet_only` (datatypen `bool`) begränsar HTML-exporten till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när ensidiga rapporter genereras.
- `ImageOrPrintOptions.image_type` finns i namespace `com.aspose.cells.drawing` och väljer bildformatet, till exempel `ImageType.PNG`, som används vid rendering med `to_image` och vid utskrift av kalkylblad till bilder.
- [Sparklinjer i Aspose.Cells for Python via Java](/cells/sv/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}