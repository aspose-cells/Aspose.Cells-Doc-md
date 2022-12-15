---
title: Aspose.Cells for Node.js via Java 21.9 Release Notes
type: docs
weight: 4
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-21-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 21.9](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.9/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43639|Skapandedatum och tid och ändringsdatum kan inte extraheras|
|CELLSJAVA-43622|XLSX till PDF: Form till bild-fel|
|CELLSJAVA-43756| Bildförvrängning under Excel till HTML|
|CELLSJAVA-43309|Detaljer ändrade på Excel till HTML-konvertering|
|CELLSJAVA-43578|Formateringsproblem vid konvertering av Excel till HTML|
|CELLSJAVA-43579|Problem med textjustering under konvertering av Excel till HTML|
|CELLSJAVA-43630|Hyperlänkfunktionens hyperlänk är ogiltig när Excel konverteras till HTML|
|CELLSJAVA-43635|Vid export av html är längden på datafältet kortare än i excel|
|CELLSJAVA-43709|Återsparad XLSM-fil orsakar filkorruption popup när den öppnas av ms excel|
|CELLSJAVA-43758|Problem med utvärdering av matrisformel|
|CELLSJAVA-43680|Datafältsproblem med villkorlig formatering i den genererade pdf-filen|
|CELLSJAVA-43689|Att ställa in den villkorliga formateringen till cell och använda DataBar.toImage resulterar i tom bild|
|CELLSJAVA-43723|Teckensnittet i cellen visas inte helt när Excel-filen konverteras till PDF|
|CELLSJAVA-43724|Kan inte konvertera komplex HTML till CSV|
|CELLSJAVA-43728| Textorienteringen ändrades medan Excel till PDF-konvertering|
|CELLSJAVA-43752|Excel till HTML-rendering - problem med villkorlig formatering för att dölja gränser|
|CELLSJAVA-43792|Teckensnittet är felaktigt när du ställer in HtmlLoadOptions för HTML till Excel-konvertering|
|CELLSJAVA-43571| DataLabels trunkeringsproblem vid konvertering av XLSX till PDF|
|CELLSJAVA-43587|Etiketter för munkdiagram är felplacerade|
|CELLSJAVA-43620|Vertikala axelvärden och punktetiketter renderas inte korrekt när Excel-fil (innehåller vattenfallsdiagram) renderas till HTML|
|CELLSJAVA-43621|Funktionen RANDBETWEEN (botten, överst) värderesultat skiljer sig från Excel-resultat|
|CELLSJAVA-41710|Felaktig rendering av HTML efter konvertering från XLSX|
|CELLSJAVA-43422|HTML till Excel-konvertering - "mso-ignore: padding" i CSS har ingen effekt|
|CELLSJAVA-43606|Bakgrundstextformateringen ändrades när filer slogs samman|
|CELLSJAVA-43769|MSO Excel (XLS) dokument kan inte laddas|
|CELLSJAVA-43631|Undantag "java.lang.NullPointerException" vid laddning av XLSM-fil|
|CELLSJAVA-43655|ArrayIndexOutOfBoundsException med getStringValue|
|CELLSJAVA-43788|Undantaget höjdes vid inställning av värde för sjökortsserier|
|CELLSJAVA-43632| Undantag "Invalid FontUnderlineType string val" när en XLSX-fil laddas|
|CELLSJAVA-43633|Undantag "Invalid MsoLineDashStyle string val" när en XLSX-fil laddas|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen AutoFitterOptions.FormatStrategy.**

Hämtar och ställer in den formaterade strategin för automatisk anpassning.

### **Lägger till egenskapen MsoFormatPicture.Transparency.**

Returnerar eller ställer in graden av transparens för området som ett värde från 0,0 (opak) till 1,0 (ren).

### **Lägger till överbelastade PivotTableCollection.Remove()-metoder.**

Tar bort den angivna pivottabellen och kontrollerar om celldata behålls .

### **Lägger till egenskapen ImageOrPrintOptions.IsOptimized.**

 Indikerar om utgångselementen optimeras. Standardvärdet är falskt. För närvarande är endast kantlinjerna optimerade när den här egenskapen är inställd på sann.

