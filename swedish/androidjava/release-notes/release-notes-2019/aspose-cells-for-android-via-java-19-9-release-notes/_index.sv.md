---
title: Aspose.Cells for Android via Java 19.9 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-android-via-java-19-9-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 19.9.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSANDROID-92|Support Product.Family licens|Ny funktion|
|CELLSJAVA-42949|Stöder Aspose.Cells ECDSA- och RSA-algoritmer|Ny funktion|
|CELLSJAVA-42979|Få totalt sidantal innan du konverterar till pdf/bild|Ny funktion|
|CELLSJAVA-42967|Infoga SVG-filen i kalkylbladet|Ny funktion|
|CELLSJAVA-42969|Support Java 12 i Aspose.Cells for Java|Förbättring|
|CELLSJAVA-42977|Hög CPU- och minnesförbrukning under konvertering av Excel till PDF|Förbättring|
|CELLSJAVA-42861|Det gick inte att hämta formens alternativa text i ODS-filformat|Insekt|
|CELLSJAVA-42929|Graftiteländringar vid konvertering av XLSX till PDF|Insekt|
|CELLSJAVA-42933|Grafikens färg ändras när Excel-filen konverteras till PDF|Insekt|
|CELLSJAVA-42946|Fel rendering av staplade stapeldiagram med serier till PDF|Insekt|
|CELLSJAVA-42942|Sidor som skrivs ut på kalkylbladsnivå och inte på arbetsboksnivå|Insekt|
|CELLSJAVA-42952|Fel indrag från toppen av cellen i vissa ord|Insekt|
|CELLSJAVA-42902|Vattenfallsdiagramsstil kopieras inte korrekt när arbetsboken kopieras|Insekt|
|CELLSJAVA-42939|Varning väckt av Excel om vi bara kallar Workbook.getVbaProject() för en arbetsbok|Insekt|
|CELLSJAVA-42940|Säkerhetsvarning efter borttagning av alla VBA-modulskript|Insekt|
|CELLSJAVA-42955|Att öppna VBAProject förstör arbetsboken|Insekt|
|CELLSJAVA-42902|Vattenfallsdiagramsstil kopieras inte korrekt när arbetsboken kopieras|Insekt|
|CELLSJAVA-42944|Fel vid konvertering av XLSX till HTML|Insekt|
|CELLSJAVA-42966|Uppdatering av pivottabell och pivotdiagram skadar Excel-filen|Insekt|
|CELLSJAVA-42975|Skillnader i HTML-konvertering|Insekt|
|CELLSJAVA-42971|# N/A visas i den renderade PDF-filen
|Insekt|
|CELLSJAVA-42970|Oönskad utökad gränslinje i Excel till PDF-rendering|Insekt|
|CELLSJAVA-42976|Bildpositionen matchar inte när Excel-fil renderas till PDF|Insekt|
|CELLSJAVA-42961|Tabellegenskaper kopierades inte korrekt när data kopierades med copyColumns|Insekt|
|CELLSJAVA-42980|Transparent bild ändras till ogenomskinlig under bildkopiering|Insekt|
|CELLSJAVA-42990|Dolda rader visas när Excel-fil konverteras till HTML när AutoFilter finns|Insekt|
|CELLSJAVA-42997|CalculateFormula() misslyckas med stora formelsträngar|Insekt|
|CELLSJAVA-43000|CalculateFormula() korrumperar Excel-filen|Insekt|
|CELLSJAVA-42987|Formateringsproblem vid konvertering av Excel-fil till PDF|Insekt|
|CELLSJAVA-42986|Text som överlappar efter konvertering av kinesisk XLSX-fil till PDF|Insekt|
|CELLSJAVA-43012|Workbook.setRecalculateOnOpen(false) fungerar inte för nyare Excel-versioner|Insekt|
|CELLSJAVA-42996|Dataetiketter baserade på formler återges inte korrekt i PDF|Insekt|
|CELLSJAVA-42945|Spara som HTML kastar undantag om ExportImagesAsBase64 är inställt|Undantag|
|CELLSJAVA-42953|NullPointerException vid konvertering av XLS-filer till HTML|Undantag|
|CELLSJAVA-42951|java.lang.NullPointerException slängt av comment.setHtmlNote()|Undantag|
|CELLSJAVA-42954|Undantag höjdes när du laddade och sparade XLSX|Undantag|
|CELLSJAVA-42957|Ogiltigt FontUnderlineType-värde visas när XLSX sparas|Undantag|
|CELLSJAVA-42992|Undantag höjdes vid konvertering av XLSM till bild|Undantag|
|CELLSJAVA-42991|Undantaget "Kolumnbredd måste vara mellan 0 och 255" vid konvertering av Excel till PDF i macOS|Undantag|
|CELLSJAVA-43004|Undantag java.lang.NumberFormatException: För inmatningssträng: "0.0" vid konvertering av Excel till HTML|Undantag|
|CELLSJAVA-43010|IllegalArgumentException när deleteBlankColumns() körs|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.
### **Uppgraderar det refererade BouncyCastle-biblioteket till 1.60**
Det använda BouncyCastle-biblioteket i releasearkivet har uppgraderats till version 1.60.
### **Föråldrar HTMLLoadOptions-klassen och lägger till HtmlLoadOptions-klassen**
Använd klassen HtmlLoadOptions istället.
### **Föråldrar klassen ODSLoadOptions och lägger till klassen OdsLoadOptions**
Använd klassen OdsLoadOptions istället.
### **Föråldrar JSONUtility-klassen och lägger till JsonUtility-klassen**
Använd klassen JsonUtility istället.
### **Lägger till gränssnitt IPageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.
### **Lägger till klass PageSavingArgs**
Info för en process för att spara sidan.
### **Lägger till klass PageStartSavingArgs**
Info för en sida startar sparningsprocessen.
### **Lägger till klass PageEndSavingArgs**
Info för en sida avslutar sparprocessen.
### **Lägger till klass SheetPrintingPreview**
Representerar förhandsvisningen av kalkylbladsutskrift.
### **Lägger till klass WorkbookPrintingPreview**
Representerar förhandsvisningen av arbetsbokens utskrift.
### **Lägger till egenskapen QueryTable.ExternalConnection.**
Får anslutningen av frågetabellen.
### **Lägger till Hyperlink.LinkType-egenskapen och enum TargetModeType.**
Representerar länktypen för hyperlänken.
### **Tar bort föråldrad Chart.Rotation-egenskap.**
Använd egenskapen Chart.RotationAngle istället.
### **Tar bort föråldrad Chart.IsDataTableShownproperty.**
Använd Chart.ShowDataTableproperty istället.
### **Tar bort föråldrad Chart.IsLegendShown-egenskap.**
Använd egenskapen Chart.ShowLegend istället.
### **Tar bort föråldrad Axis.Crosses-egenskap.**
Använd egenskapen Axis.Crosses istället.
### **Lägger till egenskaperna OoxmlCompressionType och XlsbSaveOptions.CompressionType, OoxmlSaveOptions.CompressionType.**
Representerar komprimeringstypen för OOXML-filer.
