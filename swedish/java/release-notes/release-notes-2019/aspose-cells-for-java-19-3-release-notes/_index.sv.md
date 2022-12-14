---
title: Aspose.Cells för Java 19.3 Release Notes
type: docs
weight: 100
url: /sv/java/aspose-cells-for-java-19-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Java 19.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42845|Behåll avgränsare för tomma rader när du exporterar en XLS-fil till CSV|Ny funktion|
|CELLSJAVA-42846|Textextraktionsresultaten skiljer sig från originalet|Förbättring|
|CELLSJAVA-42844|Texten är inte korrekt justerad i PDF-utdata|Insekt|
|CELLSJAVA-42834|Textfärg (svart) ändras till röd i HTML-rendering|Insekt|
|CELLSJAVA-42839|Spridningsdiagram renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42840|Horisontella axeletiketter renderas inte bra för diagram i Excel till PDF-rendering|Insekt|
|CELLSJAVA-42842|2D Bubble diagram renderas inte i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42833|Problem när du bäddar in samma PDF-fil i flera ark i en arbetsbok|Insekt|
|CELLSJAVA-42836|Workbook.hasExernalLinks() returnerar inte sant för DDE-länkar|Insekt|
|CELLSJAVA-42848|Teckensnittsinställning och andra objekt som inte kopierats med Range.copy()-funktionen|Insekt|
|CELLSJAVA-42849|IndexOutOfBoundsException undantag vid konvertering av XLSX till HTML|Undantag|
|CELLSJAVA-42831|Undantag har tagits upp av MS Excel efter att ha applicerat styling på intervall av rubrikceller|Undantag|

## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Ändringar för standardteckensnitt för laddad XLS-mallfil**
äldre versioner stödde vi inte att använda teckensnittet som definierats i temat (avancerad funktion i MS Excel 2007 och senare versioner) enligt regionen när XLS-mallfilerna laddas. På vissa användares krav har vi stött det från v19.3. Om regionen har specificerats i XLS-mallfilen kommer vi att tillämpa teckensnittet som definierats i temat enligt det sparade specificerade regionvärdet. Annars kommer vi att tillämpa typsnittet som definieras i temat enligt applikationsmiljöns regionala inställningar. Detta kommer att göra att standardteckensnittet för arbetsboken (laddat från XLS-mallfil som har specificerat temadata) ändras och sedan påverka andra funktioner, såsom kolumnbredd, formstorlek, renderingseffekt, ... etc.
### **Lägger till metoden Name.GetReferredAreas(bool recalculate).**
Tillhandahåller referenserna som hänvisas till av det definierade namnet som GetRanges(bool recalculate)-metoden. Men de returnerade referenserna representeras av ReferredArea-objekt som ger rikare funktioner inklusive externa länkar.
### **Lägger till egenskapen TxtSaveOptions.KeepSeparatorsForBlankRow**
Anger om separatorer ska matas ut för tom rad. Standardvärdet är falskt vilket betyder att innehållet för den tomma raden kommer att vara tomt.
### **Lägger till enum AutoFitMergedCellsType**
Representerar typen av automatiskt anpassade sammanslagna celler.
### **Föråldrar egenskapen AutoFitterOptions.AutoFitMergedCells och lägger till egenskapen AutoFitterOptions.AutoFitMergedCellsType**
Hämtar och ställer in typen av automatisk passande radhöjd.
### **Lägger till klasser JSONUtility och JsonLayoutOptions**
Den används för att importera json-filer.
### **Lägger till klassen TableToRangeOptions och metoden ListObject.ConvertToRange(TableToRangeOptions options)**
Konverterar tabellen till intervall med alternativ.
