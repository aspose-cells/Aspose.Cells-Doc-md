---
title: Aspose.Cells för Android via Java 22.9 Release Notes
type: docs
weight: 4
url: /sv/java/aspose-cells-for-android-via-java-22-9-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Android via Java 22.9.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44721|Stöd sortering av PivotField via beräknat fält|
|CELLSJAVA-44811|Stöd för att ange ark som ska matas ut vid export till pdf/xps|
|CELLSJAVA-44194|Ritningsform renderas inte i Excel till PDF-rendering|
|CELLSJAVA-44733|Undersök regler för ms excel för att visa cellens ram när intilliggande kolumn är dold: cellens ram har inte synkroniserats|
|CELLSJAVA-44777|Exportera formler endast till html beroende på alternativet HtmlSaveOptions.Exportformula|
|CELLSJAVA-44791|Förbättra analys av HTML-sträng till cell|
|CELLSJAVA-44695| Dålig konvertering till PDF från XLS med Line Callout till vänster på arket|
|CELLSJAVA-44700|Pivottabellberäknade fält uppdateras inte vid uppdatering av datakälla|
|CELLSJAVA-44705|Cell.getDependents() kastar undantag eller kan inte tillhandahålla alla anhöriga|
|CELLSJAVA-44717|Problem med kantstil (linje).|
|CELLSJAVA-44707| gränslinjen visas inte|
|CELLSJAVA-44670| Problem med formler i utdata HTML - Excel till HTML konvertering|
|CELLSJAVA-44202|Vid export till HTML är förklaringen i diagrammet inte densamma som MS Excel|
|CELLSJAVA-44591|Textrotation av etiketter stämmer inte överens med Excel i diagrammets utdatabild|
|CELLSJAVA-44655|Det går inte att visa trädkarta med negativt värde vilket gör att körningen fortsätter att köras|
|CELLSJAVA-44686|Titeltexten för diagram (2016) är felaktig när Title.IsAutoText är sant|
|CELLSJAVA-44689|Regression: Språkfråga för vattenfallsdiagramlegend|
|CELLSJAVA-44687|Diagramproblem vid kombination av filer|
|CELLSJAVA-44736|Bordsstilen förloras vid kopiering av ark|
|CELLSJAVA-44740|Inställning av datum före 1581 till en cell genererade felaktig datumsträng|
|CELLSJAVA-44758|Kopiera kalkylblad över arbetsböcker, cellformatet är onormalt|
|CELLSJAVA-44796|Aspose.Cells formelberäkningsmotor producerar ?#N/A? värden för vissa celler|
|CELLSJAVA-44798|Bug för formatering 0,9999999999999999 med anpassat "#" för JDK8 eller senare versioner|
|CELLSJAVA-44773|Data förstörs när du öppnar ett Excel-dokument med dolda kolumner i GridWeb (Java)|
|CELLSJAVA-44781|undersök problemet med radändring av storlek när du ändrar storlek till mycket liten höjd|
|CELLSJAVA-44787|Nedre kant som tappades vid sista raden i arbetsboken|
|CELLSJAVA-44761|Överdriven minnesanvändning vid konvertering av Excel-fil till HTML|
|CELLSJAVA-44801|Excel till PDF-konvertering med Aspose.Cells för Java v22.7 orsakar förvrängda tecken|
|CELLSJAVA-44741|Radbrytningen är inte rätt i utgången xlsx efter att ha satt html-strängen i cellen|
|CELLSJAVA-44776|Utformning av tabellrubrikrad förlorade vid kopiering av ark|
|CELLSJAVA-44789|Problem med teckensträngsersättning av textruta placerad i Excel-kalkylblad|
|CELLSJAVA-44792| Oändligt sparande arbetsbok till HTML-format (2892)|
|CELLSJAVA-44864|Samtidig laddning av arbetsböcker ger falska "Filen är skadad"-fel|
|CELLSJAVA-44327|Kanter och färre linjer visas i svartvita pajskivor i diagram till bildrendering|
|CELLSJAVA-44591|Textrotation av etiketter stämmer inte överens med Excel i diagrammets utdatabild|
|CELLSJAVA-44775|Diagrametiketter överlappade i diagram till bildrendering|
|CELLSJAVA-44860|visningen av celltext är inte samma som i excel i vissa sammanslagna områden|
|CELLSJAVA-44832|Flera sidor matas ut istället för en sida som i Excel vid konvertering till pdf|
|CELLSJAVA-44812|Det går inte att minska plotytan för diagrammet|
|CELLSJAVA-44831|MS Word visar ett felmeddelande "Word hittade oläsbart innehåll i..." när den konverterade DOCX-filen från XLSX-filen öppnas av Aspose.Cells för Java|
|CELLSJAVA-44833|Textfärg tillämpas inte på olika ord eller delar av innehållet i den utgående Excel-filen när du använder metoden Cell.setHtmlString()|
|CELLSJAVA-44852| Ramen är felaktig när den statiska Excel-filen konverteras till HTML|
|CELLSJAVA-44856| Excel till HTML-konvertering - Sparkline (minidiagram) visas/renderas inte|
|CELLSJAVA-44859|Vissa HTML-formateringar fungerar inte för kalkylbladsceller i en befintlig Excel-fil|
|CELLSJAVA-44725| Undantag "java.util.zip.ZipException: ogiltig poststorlek (förväntade 0 men fick 1053 byte)" vid konvertering av XLSX till PDF|
|CELLSJAVA-44763|Undantag "java.lang.IllegalArgumentException: kan inte analysera argumentnummer: 1:X8" när Excel-filen laddas med "org.apache.commons.io.input.AutoCloseInputStream"|
|CELLSJAVA-44774|Fel vid lagring som PDF - Undersökning krävs|
|CELLSJAVA-44842|Undantag "java.lang.OutOfMemoryError: Java heap space" vid konvertering av en XLSX-fil till PDF|


## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Android via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till metoden Cells.GetDependentsInCalculation(int,int,bool)**

Hämtar alla celler vars beräknade resultat beror på cellen som anges av rad och kolumn enligt aktuell beräkningskedja. För cellen som är tom och inte har instansierats i nuvarande cellmodell, kan användaren använda denna metod istället för Cell.GetDependentsInCalculation(bool) eftersom den senare måste instansiera cellobjektet till den aktuella cellmodellen först.

### **Ändrar cellens vänster/höger kant för Cell.GetStyle() när den intilliggande kolumnen är dold**

gamla versioner, om den intilliggande kolumnen är dold för en cell, kommer denna cells Vänster/Höger-kant inte att kontrolleras med den intilliggande cellen, så den returnerade gränsen kan skilja sig från vad som visas i ms excels dialogruta när den här cellens kant ställs in. Från 22.7 gör vi att den returnerade gränsen alltid är det faktiska värdet (vilket bör överensstämma med gränsen för dess intilliggande cell) för cellen för Cell.GetStyle(). Om användaren behöver det som visas för cellen i ms excel (när den intilliggande kolumnen är dold, kan den visade gränsen vara den av nästa synliga kolumn), kan användaren prova Cell.GetDisplayStyle().

### **Lägg till egenskaperna Range.Top, Range.Left, Range.Height och Range.Width.**

Hämtar intervallets position och storlek i poängenhet.

### **Ta bort klassen PowerQueryFormulaCollction och lägg till klassen PowerQueryFormulaCollection.**

Det är ett stavfel i den gamla klassen.

### **Lägg till egenskaperna HtmlSaveOptions.ExportPageFooters och HtmlSaveOptions.ExportPageHeaders.**

Anger om sidhuvuden och sidfötter exporteras när du sparar som en enda html-fil.

### **Lägger till egenskapen HtmlSaveOptions.ShowAllSheets.**

Anger om alla ark visas när du sparar som en enda html-fil.

### **Föråldrar egenskapen HtmlSaveOptions.ExportHeadings och lägger till egenskapen HtmlSaveOptions.ExportRowColumnHeadings.**

Använd HtmlSaveOptions.ExportRowColumnHeadings istället.

### **Föråldrade Chart.ToImage(string, ImageFormat) och lägg till Chart.ToImage(string, ImageType)**

Använd Chart.ToImage(string, ImageType) istället.

### **Lägg till metoden FontSettingCollection.Replace().**

Byt ut formens text.

### **Lägg till egenskapen ShapeTextAlignment.NumberOfColumns.**

Hämtar och ställer in antalet kolumner i formens text.

### **Lägg till egenskapen HtmlSaveOptions.ExportCommentsType.**

Hämtar och ställer in typen av exportkommentarer till html.

### **Lägg till basklassen PagineradeSaveOptions för PdfSaveOptions och XpsSaveOptions.**

Representerar alternativen för paginering.

### **Lägg till klass SheetSet.**

Beskriver en uppsättning ark.

### **Lägg till egendomen PaginatedSaveOptions.SheetSet.**

Hämtar eller ställer in arken att rendera.

### **Lägg till egenskapen ImageOrPrintOptions.SheetSet.**

Hämtar eller ställer in arken att rendera.

### **Lägg till egenskapen GridWeb.IgnoreStyleWithNoData.**

Hämtar eller ställer in om GridWeb ignorerar att visa rader eller kolumner som inte innehåller cellvärden men som fortfarande är formaterade

### **Föråldrad ImageOrPrintOptions.SaveFormat-egenskap.**

För Tiff/Svg, använd ImageType; För Xps, använd Workbook.Save(sträng, SaveOptions) med XpsSaveOptions.

### **Föråldrad konstruktor XpsSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn XpsSaveOptions() istället.

### **Föråldrad konstruktor SvgSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn SvgSaveOptions() istället.

### **Ta bort konstruktorn PdfSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Använd konstruktorn PdfSaveOptions() istället.

### **Lägger till metoderna Cell.SetTableFormula(...).**

Stöd för att ställa in formler för cellintervall för att skapa datatabeller med två variabler och datatabeller med en variabel.

### **Lägger till Cell.SetDynamicArrayFormula(string arrayFormula, FormulaParseOptions options, object[][] values, bool calculateRange, bool calculateValue, CalculationOptions copts) metod**

Stöd för att ställa in dynamisk matrisformel med anpassade alternativ för beräkning, speciellt när det finns funktioner som behöver användarens anpassade motor för beräkning i formeln.

### **Lägger till Workbook.RefreshDynamicArrayFormulas(bool calculate, CalculationOptions copts) metod**

Stöd för att uppdatera dynamiska matrisformler med anpassade alternativ för beräkning, särskilt när det finns funktioner som behöver användarens anpassade motor för beräkningsfunktioner i de dynamiska matrisformlerna.

### **Lägger till egenskapen ChartFrame.TextOptions.**

Representerar teckensnittsalternativen för diagrammets text.

### **Lägger till egenskapen ExportRangeToJsonOptions.ExportEmptyCells.**

Anger om null exporteras om cellerna är tomma.

### **Lägg till NumbersLoadOptions-konstruktorn.**

Representerar alternativen för laddningsnummer.

### **Lägger till enum LoadNumbersTableType.**

Representerar typen av laddning av flera tabeller i ett kalkylblad med Mac .numbers.

### **Lägger till egenskapen ProtectedRange.IsProtectedWithPassword.**

Indikerar om området är skyddat med lösenord.

### **Lägger till egenskaper för ImportTableOptions.ExportCaptionAsFieldName**

Anger om bildtext exporteras som fältnamn vid import av datatabell.

### **Lägger till egenskapen TextOptions.LanguageCode.**

Hämtar och ställer in språkkoden för teckensnittet.

### **Lägger till enum PresetThemeGradientType.**

Representerar den förinställda tematoningstypen.

### **Lägger till metoden GradientFill.SetPresetThemeGradient().**

Ställer in den förinställda tematoningstypen.

### **Lägger till åsidosättande Style.SetBorder()-metoder.**

Ställer in gränserna med olika typer av färg.

### **Lägger till metoderna Range.SetOutlineBorder() och Range.SetOutlineBorders()**

Ställer in gränserna för intervallet med olika typer av färg.