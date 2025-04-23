---  
title: Fyllningsinställningar
linktitle: Fyllningsinställningar  
description: Lär dig hur man skräddarsyr fyllningsinställningar, bakgrund och cellstil med Aspose.Cells biblioteket för Node.js via C++.  
keywords: Aspose.Cells, Celler, Fyllningsinställningar, Bakgrund, Stil, Node.js via C++  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/cells-fill-settings/  
---  

## **Färger och bakgrundsmönster**  

Microsoft Excel kan ställa in förgrund (omridning) och bakgrundsfärger (fyllning) för celler och bakgrundsmönster.  

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här avsnittet lär vi oss att använda dessa funktioner med hjälp av Aspose.Cells.  

### **Inställning av färger och bakgrundsmönster**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen ger en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.  

 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) har [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) och [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metoder som används för att hämta och sätta ett cells formatering. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-klassen tillhandahåller egenskaper för att ställa in förgrunds- och bakgrundsfärger för cellerna. Aspose.Cells erbjuder en [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)-uppräkning som innehåller en uppsättning fördefinierade typer av bakgrundsmönster, listade nedan.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Viktigt att veta**  

{{% alert color="primary" %}}  

- För att sätta en cells förgrunds- eller bakgrundsfärg, använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) eller [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-) metod. Båda metoderna träder i kraft endast om [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) egenskap är konfigurerad.  
- [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-)-metoden sätter cellens skuggfärg.  
  [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-)-metoden specificerar typen av bakgrundsmönster som används för förgrunds- eller bakgrundsfärgen. Aspose.Cells tillhandahåller en uppräkning, [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.  
- Om du väljer värdet *BackgroundType.None* från [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)-uppräkningen, tillämpas ingen förgrundsfärg.  
  Likaså tillämpas inte bakgrundsfärgen om du väljer värdena *BackgroundType.None* eller *BackgroundType.Solid*.  
- Vid hämtning av cellens skugg-/fyllfärg, om [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) är *BackgroundType.None*, kommer [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) att returnera *Color.Empty*.  

{{% /alert %}}  

### **Tillämpning av gradientfylleffekter**  

För att tillämpa dina önskade gradientfyllningseffekter på cellen, använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-)-metod därefter.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Färger och Palett**  

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.  

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan också anpassade färger. Innan du använder en anpassad färg, lägg till den först i paletten.  

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.  

### **Lägga till Anpassade Färger i Paletten**  

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:  

- Anpassad färg, den anpassade färgen som ska läggas till.  
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.  

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.  

{{% /alert %}}  

