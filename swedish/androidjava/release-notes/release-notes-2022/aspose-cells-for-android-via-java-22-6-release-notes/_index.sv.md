---
title: Aspose.Cells for Android via Java 22.6 Release Notes
type: docs
weight: 7
url: /sv/java/aspose-cells-for-android-via-java-22-6-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 22.6.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44632|Stöder formatering av hela dataraden i pivottabellen|
|CELLSJAVA-44415|Tusentals getResourceAsAStream-anrop orsakar hög CPU-belastning och minnesförbrukning under rapportgenerering|
|CELLSJAVA-44490|lägg till GridWorkbookSetting för GridWeb|
|CELLSJAVA-44554|Förbättra LightCells-modellen för att ställa in formler|
|CELLSJAVA-44535|implementera fokuscell med vertikal/horisontell rullningslist automatisk rullning till lämplig position|
|CELLSJAVA-44588|Upptäck filformat för stream med lösenord|
|CELLSJAVA-44611|Förbättring för att läsa tomma celler från xlsx-fil|
|CELLSJAVA-44616|Ursprungliga inställningar för villkorlig formatering i destinationsområdet bör tas bort vid kopiering av intervall|
|CELLSJAVA-44658|Stöd BouncyCastle v1.71|
|CELLSJAVA-44455|När du konverterar XLSX-fil till PDF blir datumet i pivottabellen ett serienummer|
|CELLSJAVA-44370|Excel-filen blir korrupt när den öppnas och sparas med Aspose.Cells|
|CELLSJAVA-44381|Problem med villkorsformatering när raden eller kolumnen tas bort|
|CELLSJAVA-44442|Att öppna och spara med Aspose.Cells förstör arbetsboken|
|CELLSJAVA-44356|bildpositionsfråga för utskrift för filen fs.zip i GridWeb|
|CELLSJAVA-44357|problem för visning av ofd.zip i GridWeb|
|CELLSJAVA-44398|GridWeb visningsproblem från kund|
|CELLSJAVA-44464|ytterligare nummer 1, kolumn En bakgrundsfärg är inte samma som i excel för yscl.xls på ark4|
|CELLSJAVA-44466| ytterligare problem 3, setCalculateFormula till false fungerar inte|
|CELLSJAVA-44496|Inkludera rubriktaggen/elementet för tabellen när du laddar html|
|CELLSJAVA-44429|Effekten av Excel-diagram i excel skiljer sig från den i HTML|
|CELLSJAVA-44414| Unicode i JSON kommer att bryta genererad XLSX och CSV|
|CELLSJAVA-44481|Problem med metoden ThreadedComment.setCreatedTime().|
|CELLSJAVA-44483|Sortering fungerar inte efter gruppering av raderna|
|CELLSJAVA-44522|Dubbelt värde till sträng ger tailing noll vilket är felaktigt när man jämför med ms excels resultat|
|CELLSJAVA-44501| sök nästa nummer efter filen duohangduolie.zip|
|CELLSJAVA-44529|implementera sökning efter freezepan|
|CELLSJAVA-44530|undersöka frågan om setactivecell fungerar inte ibland|
|CELLSJAVA-44534|Grafik i utskriftsområdet exporteras inte i Excel till HTML-konvertering|
|CELLSJAVA-44539|Diagrammet flyttas åt höger vid konvertering till html med utskriftsområde|
|CELLSJAVA-44568|Flerradstexter går förlorade förutom den första raden i HTML till XLS-konvertering|
|CELLSJAVA-44512|Diagram saknas vid export av diagram till svg i html|
|CELLSJAVA-44556|Problem med datavisning i datatabellen efter att koordinataxeln är inställd på logaritmisk skala - Excel till HTML/PDF-konvertering|
|CELLSJAVA-44628|Hur man behåller procentformat för vissa pivotrader när man expanderar noddata för en pivotkolumn/-fält|
|CELLSJAVA-44483|Sortering fungerar inte efter gruppering av raderna|
|CELLSJAVA-44609|Långsam kopiering med villkorlig formatering med nyare version|
|CELLSJAVA-44622|När du sorterar stora grupper med flera nycklar, kastar den "java.lang.ArrayIndexOutOfBoundsException"|
|CELLSJAVA-44630|Problem med Smart Markers-funktionen sedan Aspose Cells 22.5|
|CELLSJAVA-44646|Rensa innehåll på kopierade ark kastar NullPointerException|
|CELLSJAVA-44656|Cells.getMaxDataColumn returnerar ett annat (fel) värde i 22.5|
|CELLSJAVA-44650|Excel-dokumentsidan är rörig när den laddas in i Aspose.Cells.GridWeb(Java)|
|CELLSJAVA-44660|Problem med datajustering när du laddar XLS till Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44661|Problem när du laddar et-filen till Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44584|Titeln på axeln i diagrammet roteras i utdatabilden - Konvertering av diagram till bild|
|CELLSJAVA-44615|Grå linje ritad i utdatabilden från XLS-fil|
|CELLSJAVA-44665|Laddar ODS-filen hänger sig|
|CELLSJAVA-44404|Undantag "java.lang.IllegalArgumentException: Ogiltigt kolumnindex" när en XLSX-fil laddas in i GridWeb|
|CELLSJAVA-44651|Felet "Inte ett numeriskt värde" vid konvertering av Excel-ark till HTML/PDF|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Lägger till klassen DefaultStyleSettings.**

Grupp med standardvärden för stilrelaterade egenskaper.

### **Lägger till egenskapen LoadOptions.DefaultStyleSettings.**

Stöd för att ställa in standardvärden för stilrelaterade egenskaper för att initiera en arbetsbok.

### **Lägger till egenskapen TxtSaveOptions.TrimTailingBlankCells.**

Stöd för att ta bort alla tomma celler (upprepade tecken i separator som "~,~,~,~,") i slutet av radposten vid export av csv/tsv.

### **Lägger till Style.HasBorders-egenskapen.**

Stöd för att kontrollera om det finns gränser har satts för stilen.

### **Föråldrade LoadOptions.StandardFont/StandardFontSize egenskaper.**

Använd LoadOptions.DefaultStyleSettings.FontName/FontSize istället.

### **Tar bort föråldrade enum StyleModifyFlag.FontSubscript och FontSuperscript.**

Använd StyleModifyFlag.FontScript istället.

### **Föråldrade Shape.ConnectionPoints-egenskaper.**

Använd metoden GetConnectionPoints() istället.

### **Lägger till metoden Shape.GetConnectionPoints().**

Skaffa anslutningspunkterna.

### **Lägger till egenskaperna Row.IsCollapsed och Column.IsCollapsed.**

Indikerar om raden och kolumnen är komprimerade.

### **Lägger till PasteType.ValuesAndFormats enum.**

Indikerar endast kopieringsvärden och format.

### **Lägger till egenskapen Shape.IsInGroup.**

Anger om formen är grupperad.

### **Lägger till metoden AutoFilter.GetCellArea().**

Hämtar området där det angivna autofiltret gäller.

### **Lägger till metoden Cells.GetRowOriginalHeightPoint().**

Får den ursprungliga radhöjden, i poängenhet.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, sträng destCellName, PivotField baseField).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, int rad, int kolumn, PivotField baseField).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add(PivotTable pivot, string destCellName, int baseFieldIndex).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, int rad, int kolumn, int baseFieldIndex).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, sträng destCellName, string baseFieldName).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till DataLabelShapeType.Line enum.**

Representerar linjeformen. Denna typ är inte tillgänglig i Excel, den används bara för vissa specialfiler.

### **Ändringar för att spara arbetsbok med LightCells**

För att göra formelrelaterade funktioner tillgängliga för LightCells, i gamla versioner behåller vi all formeldata i cellmodell i minnet när vi sparar arbetsbok med LightCells. Detta orsakade missförstånd och missbruk av LightCells för vissa användare. Användaren trodde att cellens formeldata har släppts utanför räckvidden för StartCell(Cell) men faktiskt inte. För de flesta användare som använder LightCells är deras primära oro prestanda (minneskostnad). Få människor kommer att använda formelrelaterade funktioner förutom att ställa in enkel formel till cellen i processen att spara arbetsboken. Så från den här versionen lägger vi till några begränsningar för att ändra cellobjektet inom ramen för metoden StartCell(Cell). Nu är det inte tillåtet att ställa in delade formler, matrisformler för det givna cellobjektet i metoden StartCell(Cell). Om sådan typ av formler behövs, bör användaren ställa in dem innan arbetsboken sparas. Med denna ändring förbättrade vi prestandan för de flesta användare som behöver spara enkla formel för celler till den resulterande kalkylarksfilen med LightCells.

### **Tar bort föråldrad metod Cell.SetAddInFormula()**

Använd WorksheetCollection.RegisterAddInFunction() och Cell.Formula/Cell.SetFormula() istället.

### **Lägger till ExceptionType.FileCorrupted enum**

Representerar typen av undantag där filen är skadad.

### **Lägger till WarningType.Limitation enum**

Representerar varningstypen är begränsningen av Excel.

### **Lägger till metoden ShapeGuideCollection.Add(strängnamn, dubbelvärde).**

Lägger till en formguide.

### **Lägger till klassen CellsDataTableFactory**

Den här klassen tillhandahåller api för att skapa instanser av ICellsDataTable från anpassade objekt för användarens bekvämlighet.

### **Lägger till egenskapen Workbook.CellsDataTableFactory**

Ge användaren CellsDataTableFactory för att skapa en instans av ICellsDataTable från anpassade objekt.

### **Lägger till metoden Cell.GetDependentsInCalculation(bool)**

Enligt nuvarande beräkningskedja, få alla celler vars beräknade resultat beror på denna cell.

### **Lägger till metoden Cell.GetPrecedentsInCalculation()**

Enligt nuvarande beräkningskedja, hämta alla prejudikat (referens till celler i aktuell arbetsbok) som används av denna cells formel när du beräknar den.

### **Föråldrade metoderna Cell.GetLeafs() och Cell.GetLeafs(bool)**

Använd metoden Cell.GetDependentsInCalculation(bool) istället.

### **Lägger till metoden PivotTable.FormatRow(int row, Style style).**

Formatera raddata i det vridbara området.

### **Lägger till egenskapen Shapes.CreateId**

Får skapande id för formen.

### **Lägger till WarningType.InvalidData enum**

Representerar den ogiltiga datatypen.

### **Lägger till överbelastningsmetoden ChartCollection.Add().**

Lägger till ett diagram med datakälla.

### **Lägger till metoden Chart.GetActualSize().**

Hämtar den faktiska storleken på diagrammet i pixelenhet.

### **Föråldrade egenskapen Chart.ActualChartSize**

Använd metoden Chart.GetActualSize() istället.

### **Föråldrade egenskapen PdfSaveOptions.ImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Föråldrade egenskapen ImageOrPrintOptions.ChartImageType**

Diagram och Shape renderas alltid som vektorelement (t.ex. punkt, linje) för renderingskvalitet.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.ImageFormat-egenskap**

Använd egenskapen ImageOrPrintOptions.ImageType istället.

### **Tar bort föråldrad egenskap ImageOrPrintOptions.IsImageFitToPage-egenskapen**

Fastigheten är värdelös.