---
title: Aspose.Cells för Android via Java 18.9 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-android-via-java-18-9-release-notes/
---
{{% alert color="primary" %}}

Den här sidan innehåller utgåvor för Aspose.Cells för Android via Java 18.9.

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42680|Inaktivera Pivot Table Ribbon|Ny funktion|
|CELLSJAVA-42568|Skydda arbetsbok och kalkylblad i ODS-fil|Ny funktion|
|CELLSJAVA-42668|Stöd flera värden när du använder klassstil (länkad till: CELLSJAVA-42635)|Förbättring|
|CELLSJAVA-42627|Det går inte att extrahera Smart Art-bilder korrekt - Konvertering från form till bild (CELLSJAVA-42619)|Förbättring|
|CELLSJAVA-42677|Avbrottsproblem med att spara XLSX-filprocessen|Förbättring|
|CELLSJAVA-42687|Hyperlänken fungerar inte när den refereras från ett annat ark|Förbättring|
|CELLSJAVA-42672|PDF-dokumentet är för stort|Insekt|
|CELLSJAVA-42671|Hyperlänkproblem vid visning av utdata Excel-fil i MS Excel japansk version|Insekt|
|CELLSJAVA-42667|Får '#NUM!' för en cell med IRR-funktion|Insekt|
|CELLSJAVA-42658|Arbetsböcker med XL4-makron (XLSM) blir korrupta efter lagring|Insekt|
|CELLSJAVA-42656|AlternativText returnerar värdet på kommentaren Text|Insekt|
|CELLSJAVA-42635|HTML till XLS - CSS-stil ignoreras|Insekt|
|CELLSJAVA-41176|Felaktig justering vid rendering av kalkylark till PDF-format|Insekt|
|CELLSJAVA-42676|Tabelldata flyttades till fel rad och kolumn vid konvertering från HTML till MS Excel-filformat|Insekt|
|CELLSJAVA-41670|Diagrammets bildposition är fel i Chrome och FireFox vid konvertering till HTML|Insekt|
|CELLSJAVA-41245|Slicer-kontroll återges inte när Excel-fil konverteras till HTML-filformat|Insekt|
|CELLSJAVA-42684|Vertikal linje i mitten av diagrammet ritas inte korrekt i den renderade bilden|Insekt|
|CELLSJAVA-42682|Gradientfärg för negativa bubblor tillämpas inte i PDF-utdata|Insekt|
|CELLSJAVA-42681|Sjökortskategorins titel visas inte korrekt i bilden|Insekt|
|CELLSJAVA-42695|Fel kantstil returnerades för sammanslagen cell|Insekt|
|CELLSJAVA-42694|Läs vattenstämpel från Excel-fil|Insekt|
|CELLSJAVA-42686|Fastighetskommentaren innehåller onödig text|Insekt|
|CELLSJAVA-42685|Egendomen "revisionsnummer" har inte markerats korrekt|Insekt|
|CELLSJAVA-41485|Makron i ODS-filen behålls inte i det genererade ODS-filformatet|Insekt|
|CELLSJAVA-42715|Formler hämtas inte på samma sätt som i Excel-fil|Insekt|
|CELLSJAVA-42711|Diagram i PDF genereras inte från Excel-mallen|Insekt|
|CELLSJAVA-42710|Duplicera förklaringsobjekttext i diagrammet i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42706|PDF-utdata visar inte diagrametikett|Insekt|
|CELLSJAVA-42700|Vattenfallsdiagrammet återges inte korrekt efter att ha ändrat sjökortsdata|Insekt|
|CELLSJAVA-42717|Cells.deleteRow fungerar felaktigt|Insekt|
|CELLSJAVA-42716|Fel värde hämtat för kantstil|Insekt|
|CELLSJAVA-42709|Fel nedre kantstil returnerades för sammanslagen cell|Insekt|
|CELLSJAVA-42705|Excel ger upp ett fel när filen laddas efter inställning av autofiltret|Insekt|
|CELLSJAVA-42703|Diagrammet renderades inte vid konvertering av ODS till PDF|Insekt|
|CELLSJAVA-42702|Grå ramar visas efter att ha läst cellformat i kalkylbladet|Insekt|
|CELLSJAVA-42699|PasteType.VALUES_OCH_NUMBER_FORMATS fungerar inte bra|Insekt|
|CELLSJAVA-42646|Undantag: "FormulaBuild Unknown formula token0" på Name.getRefersTo()|Undantag|
|CELLSJAVA-42707|Chart.calculate-metoden orsakar OutOfMemoryError|Undantag|
|CELLSJAVA-42673|Undantag "java.lang.NumberFormatException" när en Excel-fil laddas|Undantag|
|CELLSJAVA-42669|Undantag "java.lang.NullPointerException" vid beräkning av formler i arbetsboken|Undantag|
|CELLSJAVA-42663|Chart.calculate() kastar IndexOutOfBoundsException|Undantag|
|CELLSJAVA-42655|Undantag: "Ogiltig kodning: null" när en XLS-fil laddas - II|Undantag|
|CELLSJAVA-42675|NumberFormatException höjdes när HTML-filen laddades in i arbetsboken|Undantag|
|CELLSJAVA-42689|NullPointerException undantag uppstod när CalculateFormula anropades|Undantag|
|CELLSJAVA-42678|Undantag vid rendering av kalkylblad till PNG-filformat|Undantag|
|CELLSJAVA-42411|Fel i Cell: E22-Ogiltig formel - undantag vid öppning av MS Excel-fil|Undantag|
|CELLSJAVA-42691|NegativeArraySizeException vid konvertering av XLSX till HTML|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Android via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till enum StyleFlag.Alignments**

Representerar alla inställningar för justering.

### **Lägger till egenskaperna WorkbookSettings.MaxRow och WorkbookSettings.MaxColumn**

Hämtar det maximala rad- och kolumnindexet för arbetsboken.

### **Lägger till egenskapen WriteProtection.Author**

Får och ställer in författaren till skrivskyddet.

### **Lägger till egenskapen PdfSecurityOptions.AccessibilityExtractContent**

Tillstånd att kopiera eller extrahera innehåll (till stöd för tillgänglighet för funktionshindrade användare eller för andra ändamål).

### **Lägger till klassen SubtotalSetting**

Representerar inställningen för delsumman.

### **Lägger till metoden Cells.RetrieveSubtotalSetting(CellArea)**

Hämtar inställningen för delsumma.

### **Lägger till överbelastningsmetoden Range.ExportDataTable(Aspose.Cells.ExportTableOptions).**

Stöder alternativ för export av intervall.

### **Lägger till egenskapen WebQueryConnection.IsSameSetting och tar bort egenskapen WebQueryConnection.IsFirstRow**

Använd egenskapen WebQueryConnection.IsSameSetting istället.

### **Lägger till egenskapen WebQueryConnection.IsXmlSourceData och tar bort egenskapen WebQueryConnection.IsSourceData**

Använd egenskapen WebQueryConnection.IsXmlSourceData istället.

### **Lägger till egenskapen Shape.IsEquation**

Anger om formen innehåller ekvation.

### **Lägger till överbelastningsmetoden Cells.CopyColumns(Int32,Int32,PasteOptions) och Cells.CopyRows(Int32,Int32,PasteOptions)**

Stöder inklistringsalternativ när du kopierar rader och kolumner.

### **Lägger till egenskapen Axis.IsAutoTickLabelSpacing**

Indikerar om avståndet mellan bocketiketter är automatiskt.

### **Lägger till metoderna CellsHelper.CreateSafeSheetName(strängnamnProposal)/CreateSafeSheetName(strängnamnProposal, char replaceChar)**

Metoder för användarens bekvämlighet för att skapa ett giltigt arknamn.

### **Lägger till Row.FirstDataCell**

Får den första icke-tomma cellen i raden.

### **Lägger till MapChartLabelLayout enum**

Representerar etikettlayouttypen för kartdiagrammet.

### **Lägger till MapChartProjectionType enum**

Representerar projektionstypen för kartdiagrammet.

### **Lägger till MapChartRegionType enum**

Representerar regiontypen för kartdiagrammet.

### **Lägger till QuartileCalculationType enum**

Representerar diagrammets kvartilberäkningstyp.

### **Lägger till egenskapen Series.LayoutProperties och klassen SeriesLayoutProperties**

Representerar layoutegenskaperna för serien.

### **Lägger till egenskapen TickLabels.IsAutomaticRotation**

Indikerar om rotationen av bocketiketterna är automatisk.

### **Lägger till FilterOperatorType.BeginsWith, Contains, EndsWith och NotContains enum**

Representerar textfilteroperatortypen.

### **Lägger till metoden Cell.GetDisplayStyle(bool).**

Hämtar visningsstilen för cellen.

### **Lägger till metoden GlobalizationSettings.GetStandardHeaderFooterFontStyleName(string localFontStyleName)**

Får standardnamn på engelska typsnittsstilen (vanlig, fet, kursiv) för sidhuvud/sidfot enligt det givna språkets teckensnittsnamn.

### **Lägger till PdfCustomPropertiesExport enum**

Anger hur CustomDocumentPropertyCollection exporteras till PDF-fil.

### **Lägger till egenskapen PdfSaveOptions.CustomPropertiesExport**

Hämtar eller ställer in ett värde som bestämmer hur CustomDocumentPropertyCollection exporteras till PDF-fil. Standardvärdet är None.

### **Lägger till klass XmlDataBinding**

Representerar Xml-databindningsinformation.

### **Lägger till egenskapen ListObject.XmlMap**

Får en XmlMap som används för den här listan.

### **Lägger till egenskapen XmlDataBinding.Url**

Hämtar käll-url för denna databindning.

### **Lägger till egenskapen XmlMap.DataBinding**

Får en XmlDataBinding av denna karta.

{{% alert color="primary" %}}

Eftersom kodbasen för Aspose.Cells för Android via Java matchar koden för relevanta .NET- och Java-versioner, ingår de flesta ändringar, förbättringar och korrigeringar i Aspose.Cells för .NET v18.7, Aspose.Cells för .NET v18.8 , Aspose.Cells för .NET v18.9, Aspose.Cells för Java v18.7, Aspose.Cells för Java v18.8 och Aspose.Cells för Java v18.9 ingår också i denna Aspose.Cells för Android via Java v18.

{{% /alert %}}
