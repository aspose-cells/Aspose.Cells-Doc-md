---
title: Aspose.Cells for Java 19.9 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-19-9-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 19.9.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42990|Dolda rader visas när Excel-fil konverteras till HTML när AutoFilter finns|Insekt|
|CELLSJAVA-42997|CalculateFormula() misslyckas med stora formelsträngar|Insekt|
|CELLSJAVA-43000|CalculateFormula() korrumperar Excel-filen|Insekt|
|CELLSJAVA-42987|Formateringsproblem vid konvertering av Excel-fil till PDF|Insekt|
|CELLSJAVA-42986|Text som överlappar efter konvertering av kinesiska XLSX-fil till PDF|Insekt|
|CELLSJAVA-43012|Workbook.setRecalculateOnOpen(false) fungerar inte för nyare Excel-versioner|Insekt|
|CELLSJAVA-42996|Dataetiketter baserade på formler återges inte korrekt i PDF|Insekt|
|CELLSJAVA-42992|Undantag höjdes vid konvertering av XLSM till bild|Undantag|
|CELLSJAVA-42991|Undantaget "Kolumnbredd måste vara mellan 0 och 255" vid konvertering av Excel till PDF i macOS|Undantag|
|CELLSJAVA-43004|Undantag java.lang.NumberFormatException: För inmatningssträng: "0.0" vid konvertering av Excel till HTML|Undantag|
|CELLSJAVA-43010|IllegalArgumentException när deleteBlankColumns() körs|Undantag|

## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Tar bort föråldrad Chart.Rotation-egenskap**
Använd egenskapen Chart.RotationAngle istället.
### **Tar bort föråldrad Chart.IsDataTableShown-egenskap**
Använd egenskapen Chart.ShowDataTable istället.
### **Tar bort föråldrad Chart.IsLegendShown-egenskap**
Använd egenskapen Chart.ShowLegend istället.
### **Tar bort föråldrad Axis.Crosses-egenskap**
Använd egenskapen Axis.Crosses istället.
### **Lägger till egenskaperna OoxmlCompressionType och XlsbSaveOptions.CompressionType, OoxmlSaveOptions.CompressionType.**
Representerar komprimeringstypen för OOXML-filer.
