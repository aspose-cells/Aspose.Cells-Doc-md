---
title: Fyllningsinställningar
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in fyllningsinställningarna för celler, vilket gör att användare kan anpassa bakgrunden och stilen för celler. Den här artikeln kommer att introducera hur man använder Aspose.Cells biblioteket för att ställa in fyllningsinställningar för celler.
keywords: Aspose.Cells, Celler, Fyllningsinställningar, Bakgrund, Stil
type: docs
weight: 50
url: /sv/net/cells-fill-settings/
---

## **Färger och bakgrundsmönster**

Microsoft Excel kan ställa in förgrund (omridning) och bakgrundsfärger (fyllning) för celler och bakgrundsmönster.

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här avsnittet lär vi oss att använda dessa funktioner med hjälp av Aspose.Cells.

### **Inställning av färger och bakgrundsmönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innefattar en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

The [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) har [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) och [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metoder som används för att hämta och sätta en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) tillhandahåller egenskaper för att ange förgrund och bakgrundsfärger för cellerna. Aspose.Cells tillhandahåller en [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) uppräkning som innehåller en uppsättning fördefinierade typer av bakgrundsmönster som ges nedan.

|**Bakgrundsmönster**|**Beskrivning**|
| :- | :- |
|DiagonalCrosshatch|Representerar diagonalt kryssmönster|
|DiagonalStripe|Representerar diagonalt rutmönster|
|Gray6|Representerar 6,25% grått mönster|
|Gray12|Representerar 12,5% grått mönster|
|Gray25|Representerar 25% grått mönster|
|Gray50|Representerar 50% grått mönster|
|Gray75|Representerar 75% grått mönster|
|HorizontalStripe|Representerar horisontellt rutmönster|
|None|Representerar ingen bakgrund|
|ReverseDiagonalStripe|Representerar omvänd diagonalt rutmönster|
|Solid|Representerar enfärgat mönster|
|ThickDiagonalCrosshatch|Representerar tjockt diagonalt kryssmönster|
|ThinDiagonalCrosshatch|Representerar tunt diagonalt kryssmönster|
|ThinDiagonalStripe|Representerar tunt diagonalt rutmönster|
|ThinHorizontalCrosshatch|Representerar tunt horisontellt kryssmönster|
|ThinHorizontalStripe|Representerar tunt horisontellt rutmönster|
|ThinReverseDiagonalStripe|Representerar tunt omvänt diagonalt rutmönster|
|ThinVerticalStripe|Representerar tunt vertikalt rutmönster|
|VerticalStripe|Representerar vertikalt rutmönster|

I exemplet nedan är förgrundsfärgen för cellen A1 inställd men A2 är konfigurerad för att ha både förgrund och bakgrundsfärger med ett bakgrundsmönster med vertikal rand.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

- För att ange en cells förgrund eller bakgrundsfärg, använd [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) eller [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) egenskaper. Båda egenskaperna kommer att ha effekt endast om [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) egenskap är konfigurerad.
- Egenskapen [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) sätter cellens skuggfärg.
  Egenskapen [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) anger typen av bakgrundsmönster som används för förgrund eller bakgrundsfärg. Aspose.Cells tillhandahåller en uppräkning, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
- Om du väljer värdet *BackgroundType.None* från [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) uppräkningen, tillämpas inte förgrundsfärgen.
  Likaså tillämpas inte bakgrundsfärgen om du väljer värdena *BackgroundType.None* eller *BackgroundType.Solid*.
- Vid hämtning av cellens skugg-/fyllfärg, om [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) är *BackgroundType.None*, kommer [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) att returnera *Color.Empty*.

{{% /alert %}}

### **Tillämpning av gradientfylleffekter**

För att applicera önskade gradientfylleffekter på cellen, använd [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) metod enligt behov.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan också anpassade färger. Innan du använder en anpassad färg, lägg till den först i paletten.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

### **Lägga till Anpassade Färger i Paletten**

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) tillhandahåller en [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
