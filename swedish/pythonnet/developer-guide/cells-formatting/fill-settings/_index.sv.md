---
title: Fyllningsinställningar
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler. Det stöder att ställa in fyllningsinställningar för celler, vilket gör att användare kan anpassa bakgrund och stil för celler. Denna artikel introducerar hur man använder Aspose.Cells för Python via .NET biblioteket för att ställa in cellfyllnadsinställningar.
keywords: Aspose.Cells för Python via .NET, Celler, Fyllningsinställningar, Bakgrund, Stil
type: docs
weight: 50
url: /sv/python-net/cells-fill-settings/
---

## **Färger och bakgrundsmönster**

Microsoft Excel kan ställa in förgrund (omridning) och bakgrundsfärger (fyllning) för celler och bakgrundsmönster.

 Aspose.Cells för Python via .NET stöder också dessa funktioner på ett flexibelt sätt. I detta ämne lär vi oss att använda dessa funktioner med Aspose.Cells.

### **Inställning av färger och bakgrundsmönster**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) har metoderna [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) och [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) som används för att få och sätta formateringen av en cell. Klassen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) tillhandahåller egenskaper för att sätta cellernas förgrunds- och bakgrundsfärger. Aspose.Cells för Python via .NET tillhandahåller en [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)-uppräkning som innehåller ett urval av fördefinierade bakgrundsmönster som listas nedan.

|**Bakgrundsmönster**|**Beskrivning**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Representerar diagonal korshatch-mönster|
|DIAGONAL_STRIPE|Representerar diagonal randmönster|
|GRAY6|Representerar grått mönster med 6,25 %|
|GRAY12|Representerar grått mönster med 12,5 %|
|GRAY25|Representerar grått mönster med 25 %|
|GRAY50|Representerar grått mönster med 50 %|
|GRAY75|Representerar grått mönster med 75 %|
|HORIZONTAL_STRIPE|Representerar horisontell randmönster|
|NONE|Representerar ingen bakgrund|
|REVERSE_DIAGONAL_STRIPE|Representerar omvänd diagonalt randmönster|
|SOLID|Representerar solidt mönster|
|THICK_DIAGONAL_CROSSHATCH|Representerar tjockt diagonalt korshatch-mönster|
|THIN_DIAGONAL_CROSSHATCH|Representerar tunt diagonalt korshatch-mönster|
|THIN_DIAGONAL_STRIPE|Representerar tunt diagonalt randmönster|
|THIN_HORIZONTAL_CROSSHATCH|Representerar tunt horisontellt korshatch-mönster|
|THIN_HORIZONTAL_STRIPE|Representerar tunt horisontellt randmönster|
|THIN_REVERSE_DIAGONAL_STRIPE|Representerar tunt omvänt diagonalt randmönster|
|THIN_VERTICAL_STRIPE|Representerar tunt vertikalt randmönster|
|VERTICAL_STRIPE|Representerar vertikalt randmönster|

I exemplet nedan är förgrundsfärgen för cellen A1 inställd men A2 är konfigurerad för att ha både förgrund och bakgrundsfärger med ett bakgrundsmönster med vertikal rand.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

- För att ange en cells förgrund eller bakgrundsfärg, använd [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) eller [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) egenskaper. Båda egenskaperna kommer att ha effekt endast om [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) egenskap är konfigurerad.
- Egenskapen [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) sätter cellens skuggfärg.
  Egenskapen [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) specificerar vilken typ av bakgrundsmönster som används för förgrunds- eller bakgrundsfärgen. Aspose.Cells för Python via .NET innehåller en uppräkning, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
- Om du väljer värdet *BackgroundType.None* från [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) uppräkningen, tillämpas inte förgrundsfärgen.
  Likaså tillämpas inte bakgrundsfärgen om du väljer värdena *BackgroundType.None* eller *BackgroundType.Solid*.
- Vid hämtning av cellens skugg-/fyllfärg, om [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) är *BackgroundType.None*, kommer [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) att returnera *Color.Empty*.

{{% /alert %}}

### **Tillämpning av gradientfylleffekter**

För att applicera önskade gradientfylleffekter på cellen, använd [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) metod enligt behov.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells för Python via .NET är det inte bara möjligt att använda paletteens befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten först.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

### **Lägga till Anpassade Färger i Paletten**

Aspose.Cells för Python via .NET stöder Microsoft Excels 56 färgpalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen till paletten.

Aspose.Cells för Python via .NET tillhandahåller en klass, {0}, som representerar en Microsoft Excel-fil. Klassen {1} innehåller en {2} samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen {3}. Klassen {4} tillhandahåller en {5} samling. Varje objekt i {6} samlingen representerar ett objekt av klassen {7}.

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}

