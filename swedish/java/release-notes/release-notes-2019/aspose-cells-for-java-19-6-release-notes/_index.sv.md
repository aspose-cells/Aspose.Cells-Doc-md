---
title: Aspose.Cells for Java 19.6 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 19.6.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42914|Stora villkorliga format orsakar OOM-undantag|Förbättring|
|CELLSJAVA-42916|Dataformatproblem efter Workbook.save()|Förbättring|
|CELLSJAVA-42930|Excel95 laddningsfel|Förbättring|
|CELLSJAVA-42927|Den sparade filen öppnas långsamt i Excel efter att kolumner tagits bort|Förbättring|
|CELLSJAVA-42932|Villkorligt formateringsfel med metoden Style.getDisplayStyle|Insekt|
|CELLSJAVA-42928|Vissa rader återspeglas inte i XLSX till PDF-konvertering|Insekt|
|CELLSJAVA-42904|Rubrikbilden verkar förstöra filen|Insekt|
|CELLSJAVA-42907|Filter förlorat efter att arbetsboken sparats|Insekt|
|CELLSJAVA-42915|Filter ändras efter att ett ark lagts till i arbetsboken|Insekt|
|CELLSJAVA-42918|Konverterad fils diagram tillplattat (XLS till XLSX konvertering)|Insekt|
|CELLSJAVA-42938|Laddar XLSX-filen stoppar programmet|Insekt|
|CELLSJAVA-42859|CellsException för att ladda namn från ODS-fil|Undantag|
|CELLSJAVA-42908|Undantag vid anrop av Name.getRefersTo()|Undantag|
|CELLSJAVA-42926|IllegalStateException vid inläsning av arbetsbok|Undantag|

## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
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
