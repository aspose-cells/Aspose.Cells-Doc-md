---
title: Aspose.Cells för .NET 22.9 Release Notes
type: docs
weight: 4
url: /sv/net/aspose-cells-for-net-22-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 22.9](https://www.nuget.org/packages/Aspose.Cells/22.9.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-51935|Stöd för diskret gruppdata för xls-fil|
|CELLSNET-51925|Stöd förinställda övertoningsinställningar för övertoningsfyllning|
|CELLSNET-51740|Stöd för att ställa in tabellformel för datatabellen|
|CELLSNET-51853|Stöd för att konvertera ozm till lbm för CONVERT-funktionen|
|CELLSNET-51931|Förbättra igenkänningen av användarens input för Style.Custom till inbyggd|
|CELLSNET-51709|Stöd flera tabeller i ett kalkylblad med .Numbers|
|CELLSNET-51810|Stöd för att exportera tomma celler som null till Json|
|CELLSNET-51811|Förbättra funktionen att upptäcka om den första raden är en rubrikrad|
|CELLSNET-51910|Stöd för att applicera konturgränser med ThemeColor till Range|
|CELLSNET-51928|Stöd läs- och skrivskyddad räckvidd med SHA-512-algoritmen för xlsb|
|CELLSNET-51743|Vissa symboler ändrades efter konvertering av Excel-fil till PDF|
|CELLSNET-51747|mm blir "??" i pdf|
|CELLSNET-50960|Återsparad XLSM-fil (som innehåller en pivottabell) blev skadad|
|CELLSNET-51506|Externa anslutningar är skadade i den genererade filen|
|CELLSNET-51735|Fel text fet stil vid konvertering av Excel-pivottabell till PDF|
|CELLSNET-51761|När XLS-fil med pivottabell konverteras till XLSM raderades dataanslutningsdetaljerna|
|CELLSNET-51899|XLS till XLSM-konvertering - MS Excel kunde inte öppna XLSM-utdatafilen|
|CELLSNET-51716| Dynamisk matrisformel fyller inte ut spillda celler|
|CELLSNET-51753|Vissa formler är inte beräknade för att uppdatera data över arken vid ändring av urval|
|CELLSNET-51800|Värden från XLSX är felaktiga i den utgående PDF-filen|
|CELLSNET-51801|Omräkning av en arbetsbok går långsamt efter beräkning med beräkningskedja|
|CELLSNET-51897|HLOOKUP-värdet är felaktigt|
|CELLSNET-51187|Vertikala prickade linjer felinriktade med etiketter på axeln i diagrammet till SVG-rendering|
|CELLSNET-51734|System.Security.Cryptography.Pkcs 6.0.1-beroende kräver .NET Core 3.1|
|CELLSNET-51912|När du konverterar Excel till PDF visar den resulterande PDF-filen inte axeln korrekt|
|CELLSNET-51744|Gridweb fortsätter att hoppa tillbaka|
|CELLSNET-51608|Numret är dolt bakom röd/grön cirkel vid export av Excel till HTML på docker (Azure cloud kubernetes)|
|CELLSNET-51864|Problem med att beräkna "PageSetup.Zoom" med HorizontalPageBreaks|
|CELLSNET-51938|XLSX till PDF: Teckenavståndet är fel|
|CELLSNET-51226|Lägg till identifierarattribut för diagram/grupp i Excel Workbook|
|CELLSNET-51461|Onödiga ramar läggs till för data i Excel till DOCX-konvertering|
|CELLSNET-51736| Cell gränser försvann i den resulterande PDF-filen|
|CELLSNET-51738|Ogiltig post för en cell orsakade att genererad fil är skadad|
|CELLSNET-51760|Worksheet.AutoFitColumns fungerar inte korrekt|
|CELLSNET-51770|Merged Cells fungerar inte bra när du sparar som PowerPoint-fil|
|CELLSNET-51771|Efter att celler har slagits samman går vissa data förlorade i den genererade PowerPoint-filen|
|CELLSNET-51772|Anslutningsinformationen ändras när XLS-fil konverteras till XLSM|
|CELLSNET-51778|Att konvertera en XLS-fil till XLSM tar bort några tecken i slutet av länken i namngivna intervall|
|CELLSNET-51785| DOCX >> Html-tabell >> Excel-ark konverterar inte korrekt|
|CELLSNET-51825|AutoFit fungerade annorlunda i v22.1.0 och v22.8.0|
|CELLSNET-51829|XLS till XLSM filkonvertering orsakade att vissa anpassade egenskaper gick förlorade|
|CELLSNET-51830|Indatadokumentström kasseras i förtid efter att du skapat arbetsbok för en viss fil|
|CELLSNET-51865|XLS-kalkylbladet har inga data medan du kan se fyllda rader i Excel|
|CELLSNET-51880|XLSB till XLSM-konvertering - XLSM-utdatafilen är skadad|
|CELLSNET-51898|XLS till XLSM-konvertering - XLSM-utdatafilen är skadad|
|CELLSNET-51921|Det går inte att använda en kopierad stil utan att ställa in dess flaggor till explicit eller använda en flagga|
|CELLSNET-51922|Cell-skyddet går förlorat efter att ha öppnat och sparat XLSX-filen igen|
|CELLSNET-51923|DataTable Column Caption-egenskapen respekteras och återges inte i utdata Excel vid import av data|
|CELLSNET-51924|Felaktig språkinställning i diagramtextelement|
|CELLSNET-51944|Namnet på inbyggda stilar ändras inte automatiskt beroende på region|
|CELLSNET-51848|Beräkning av arbetsbok ger Stackoverflow-undantag|
|CELLSNET-51965|Undantag vid import av en XLSX-fil med redovisningsformatering till Aspose.Cells.GridDesktop|
|CELLSNET-51961|Undantag "Index var utanför intervallet" vid rendering av en ODS till PDF|
|CELLSNET-51863|System.StackOverflowException i CollectionBase.Exists|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

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
