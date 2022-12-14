---
title: Aspose.Cells för Android via Java 19.6 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-android-via-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Android via Java 19.6.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42914|Stora villkorliga format orsakar OOM-undantag|Förbättring|
|CELLSJAVA-42916|Dataformatproblem efter Workbook.save()|Förbättring|
|CELLSJAVA-42930|Excel95 laddningsfel|Förbättring|
|CELLSJAVA-42927|Sparad fil öppnas långsamt i Excel efter att kolumner tagits bort|Förbättring|
|CELLSJAVA-42857|Fel värde visas för former i den exporterade PDF-filen|Insekt|
|CELLSJAVA-42890|Bilden är ogenomskinlig och inte transparent efter konvertering - Excel till HTML-rendering|Insekt|
|CELLSJAVA-42893|Diagram saknas i Excel till HTML-rendering|Insekt|
|CELLSJAVA-42899|Excel till HTML problem|Insekt|
|CELLSJAVA-42903|Excel till HTML-renderingsproblem på CentOS|Insekt|
|CELLSJAVA-42882|Det gick inte att extrahera data från en MS Excel 95 XLS-fil|Insekt|
|CELLSJAVA-42887|Beräkningsskillnad mellan MS Excel och Aspose.Cells|Insekt|
|CELLSJAVA-42891|XIRR-funktionen ger ett numeriskt fel om något nollvärde finns i området|Insekt|
|CELLSJAVA-42909|Problem med funktionen DATUMVÄRDE|Insekt|
|CELLSJAVA-42910|Problem med VLOOKUP-funktionen när ett tecken finns i strängen|Insekt|
|CELLSJAVA-42911|Problem när du använder TEXT-funktionen för datum|Insekt|
|CELLSJAVA-42896|Konvertering till PDF vänder telefonnummer|Insekt|
|CELLSJAVA-42900|Konvertering till PDF ändrar textordning|Insekt|
|CELLSJAVA-42932|Villkorligt formateringsfel med metoden Style.getDisplayStyle|Insekt|
|CELLSJAVA-42928|Vissa rader återspeglas inte i XLSX till PDF-konvertering|Insekt|
|CELLSJAVA-42904|Rubrikbilden verkar förstöra filen|Insekt|
|CELLSJAVA-42907|Filter förlorat efter att arbetsboken sparats|Insekt|
|CELLSJAVA-42915|Filter ändras efter att ett ark lagts till i arbetsboken|Insekt|
|CELLSJAVA-42918|Konverterad fils diagram tillplattat (XLS till XLSX konvertering)|Insekt|
|CELLSJAVA-42938|Laddar XLSX-filen stoppar programmet|Insekt|
|CELLSJAVA-42881|Undantag "java.lang.IllegalStateException: Ogiltig kodning: null " när en MS Excel 5.0/95 XLS-fil laddas|Undantag|
|CELLSJAVA-42884|Undantag "java.lang.ArrayIndexOutOfBoundsException" när en MS Excel 5.0/95 XLS-fil laddas|Undantag|
|CELLSJAVA-42859|CellsException för att ladda namn från ODS-fil|Undantag|
|CELLSJAVA-42908|Undantag vid anrop av Name.getRefersTo()|Undantag|
|CELLSJAVA-42926|IllegalStateException vid inläsning av arbetsbok|Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Android via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till StreamProviderOptions konstruktor**
Nya StreamProviderOptions.
### **Lägger till FileFormatType.GraphChart enum**
Representerar den inbäddade diagramfilen.
### **Lägger till egenskaper för ImportTableOptions.CheckMergedCells**
Anger om sammanslagna celler kontrolleras vid import av data.
### **Lägger till ODSCellFieldCollection, ODSCellField-klasser och ODSCellFieldType enum**
Representerar cellfältet för ODS.
### **Lägger till Cells.ODSCellFields-egenskaper**
Hämtar listan över cellfält för ODS.
### **Lägger till ODSPageBackground-klass och PageSetup.ODSPageBackground-egenskap**
Representerar bakgrunden till ODS.
### **Lägger till enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS och SaveFormat.SXC**
Representerar filformatstyperna .FODS och .SXC.
### **Lägger till enum WarningType.UnsupportedFileFormat**
Representerar filformat som inte stöds för varningstyper.
### **Lägger till enum ODSGeneratorType**
Representerar generatortypen av ods.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Anger om OOXML-fil bäddas in som OleObject.
### **Lägger till Row.CopySettings(Aspose.Cells.Row,System.Boolean)**
Kopiera inställningar för rad, som stil, höjd, synlighet, ... etc.
