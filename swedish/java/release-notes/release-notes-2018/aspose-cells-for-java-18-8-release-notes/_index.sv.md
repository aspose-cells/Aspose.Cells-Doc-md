---
title: Aspose.Cells for Java 18.8 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-java-18-8-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.8.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42680|Inaktivera Pivot Table Ribbon|Ny funktion|
|CELLSJAVA-42568|Skydda arbetsbok och kalkylblad i filen ODS|Ny funktion|
|CELLSJAVA-42677|Avbrottsproblem med att spara XLSX-filprocessen|Förbättring|
|CELLSJAVA-42687|Hyperlänken fungerar inte när den refereras från ett annat ark|Förbättring|
|CELLSJAVA-41176|Felaktig justering vid rendering av kalkylark till PDF-format|Insekt|
|CELLSJAVA-42676|Tabelldata flyttades till fel rad och kolumn vid konvertering från HTML till MS Excel-filformat|Insekt|
|CELLSJAVA-41670|Diagrammets bildposition är fel i Chrome och FireFox vid konvertering till HTML|Insekt|
|CELLSJAVA-41245|Slicer-kontroll renderas inte när Excel-fil konverteras till filformatet HTML|Insekt|
|CELLSJAVA-42684|Vertikal linje i mitten av diagrammet ritas inte korrekt i den renderade bilden|Insekt|
|CELLSJAVA-42682|Gradientfärg för negativa bubblor gäller inte i PDF-utgången|Insekt|
|CELLSJAVA-42681|Sjökortskategorins titel visas inte korrekt i bilden|Insekt|
|CELLSJAVA-42695|Fel kantstil returnerades för sammanslagen cell|Insekt|
|CELLSJAVA-42694|Läs vattenstämpel från Excel-fil|Insekt|
|CELLSJAVA-42686|Fastighetskommentaren innehåller onödig text|Insekt|
|CELLSJAVA-42685|Egendomen "revisionsnummer" har inte markerats korrekt|Insekt|
|CELLSJAVA-41485|Makron i ODS-filen behålls inte i det genererade ODS-filformatet|Insekt|
|CELLSJAVA-42691|NegativeArraySizeException vid konvertering av XLSX till HTML|Undantag|
|CELLSJAVA-42675|NumberFormatException uppstod när filen HTML laddades in i arbetsboken|Undantag|
|CELLSJAVA-42689|NullPointerException undantag uppstod när CalculateFormula anropades|Undantag|
|CELLSJAVA-42678|Undantag vid rendering av kalkylblad till filformatet PNG|Undantag|
|CELLSJAVA-42411|Fel i Cell: E22-Ogiltig formel - undantag vid öppning av MS Excel-fil|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
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
### **Lägger till överbelastning Cells.CopyColumns(Int32,Int32,PasteOptions) och Cels.CopyRows(Int32,Int32,PasteOptions) metod**
Stöder inklistringsalternativ när du kopierar rader och kolumner.
### **Lägger till egenskapen Axis.IsAutoTickLabelSpacing**
Indikerar om avståndet mellan bocketiketter är automatiskt.
