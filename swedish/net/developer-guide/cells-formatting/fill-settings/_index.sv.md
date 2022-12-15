---
title: Fyll i inställningar
type: docs
weight: 50
url: /sv/net/cells-fill-settings/
---
## **Färger och bakgrundsmönster**

Microsoft Excel kan ställa in förgrunds- (kontur) och bakgrunds- (fyll)färger för celler och bakgrundsmönster.

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här ämnet lär vi oss att använda dessa funktioner med Aspose.Cells.

### **Ställa in färger och bakgrundsmönster**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 De[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) har[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) och[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metoder som används för att hämta och ställa in en cells formatering. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)klass tillhandahåller egenskaper för att ställa in förgrunds- och bakgrundsfärgerna för cellerna. Aspose.Cells tillhandahåller en[**Bakgrundstyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)uppräkning som innehåller en uppsättning fördefinierade typer av bakgrundsmönster som ges nedan.

|**Bakgrundsmönster**|**Beskrivning**|
|:- |:- |
|Diagonal Crosshatch|Representerar diagonalt rutmönster|
|Diagonal Stripe|Representerar diagonalt randmönster|
|Grå6|Representerar 6,25 % grått mönster|
|Grå12|Representerar 12,5 % grått mönster|
|Grå25|Representerar 25 % grått mönster|
|Grå50|Representerar 50 % grått mönster|
|Grå75|Representerar 75 % grått mönster|
|Horisontell Stripe|Representerar horisontellt randmönster|
|Ingen|Representerar ingen bakgrund|
|ReverseDiagonalStripe|Representerar omvänt diagonalt randmönster|
|Fast|Representerar ett fast mönster|
|ThickDiagonal Crosshatch|Representerar ett tjockt diagonalt kryssmönster|
|ThinDiagonal Crosshatch|Representerar ett tunt diagonalt streckmönster|
|ThinDiagonalStripe|Representerar ett tunt diagonalt randmönster|
|ThinHorizontal Crosshatch|Representerar ett tunt horisontellt streckmönster|
|ThinHorizontal Stripe|Representerar ett tunt horisontellt randmönster|
|ThinReverseDiagonalStripe|Representerar ett tunt omvänt diagonalt randmönster|
|ThinVerticalStripe|Representerar ett tunt vertikalt randmönster|
|VerticalStripe|Representerar vertikalt randmönster|

I exemplet nedan är förgrundsfärgen för A1-cellen inställd men A2 är konfigurerad att ha både förgrunds- och bakgrundsfärger med ett vertikalt randmönster.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

-  För att ställa in en cells förgrunds- eller bakgrundsfärg, använd[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**Förgrundsfärg**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) eller[**Bakgrundsfärg**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) egenskaper. Båda egenskaperna träder i kraft endast om[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**Mönster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)egenskapen är konfigurerad.
-  De[**Förgrundsfärg**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)egenskapen anger cellens nyansfärg.
 De[**Mönster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)egenskapen anger typen av bakgrundsmönster som används för förgrunden eller bakgrundsfärgen. Aspose.Cells tillhandahåller en uppräkning,[**Bakgrundstyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
-  Om du väljer*BackgroundType.None* värde från[**Bakgrundstyp**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)uppräkning tillämpas inte förgrundsfärgen.
 På samma sätt tillämpas inte bakgrundsfärgen om du väljer*BackgroundType.None* eller*BackgroundType.Solid* värden.
-  Vid hämtning av cellens skuggnings-/fyllningsfärg, om[**Stil.mönster**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) är*BackgroundType.None*, [**Style.Förgrundsfärg**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) kommer tillbaka*Färg.Tom*.

{{% /alert %}}

### **Använda Gradient Fill Effects**

 För att applicera önskade gradientfyllningseffekter på cellen, använd[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)metod i enlighet därmed.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Färger och palett**

En palett är antalet tillgängliga färger för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa ett konsekvent utseende. Varje Microsoft Excel-fil (97-2003) har en palett med 56 färger som kan appliceras på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i ett diagram.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten först.

Det här ämnet diskuterar hur man lägger till anpassade färger till paletten.

### **Lägga till anpassade färger till paletten**

Aspose.Cells stöder Microsoft Excels 56 färgpalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass ger en[**Ändra palett**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Custom Color, den anpassade färgen som ska läggas till.
- Index, indexet för färgen i paletten som den anpassade färgen kommer att ersätta. Bör vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) till paletten innan den appliceras på ett teckensnitt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg till paletten ändras paletten och alla element i filen som formaterats med föregående färg ändras. Så var mycket försiktig när du ändrar paletten. Dessutom är detta endast begränsningen i XLS (Excel 97 - 2003) filformat eftersom det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}
