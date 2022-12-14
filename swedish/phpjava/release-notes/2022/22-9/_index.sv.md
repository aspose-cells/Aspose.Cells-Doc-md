---
title: Aspose.Cells för PHP via Java 22.9 Release Notes
type: docs
weight: 4
url: /sv/php-java/aspose-cells-for-php-via-java-22-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för PHP via Java 22.9](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.9/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44194|Ritningsform renderas inte i Excel till PDF-rendering|
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
|CELLSJAVA-44842|Undantag "java.lang.OutOfMemoryError: Java heap space" vid konvertering av en XLSX-fil till PDF|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

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
