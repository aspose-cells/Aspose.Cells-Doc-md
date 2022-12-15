---
title: Aspose.Cells for Node.js via Java 22.8 Release Notes
type: docs
weight: 5
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-22-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 22.8](https://releases.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.8/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44811|Stöd för att ange ark som ska matas ut vid export till pdf/xps|
|CELLSJAVA-44777|Exportera formler endast till html beroende på alternativet HtmlSaveOptions.Exportformula|
|CELLSJAVA-44791|Förbättra analys av HTML-sträng till cell|
|CELLSJAVA-44740|Inställning av datum före 1581 till en cell genererade felaktig datumsträng|
|CELLSJAVA-44758|Kopiera kalkylblad över arbetsböcker, cellformatet är onormalt|
|CELLSJAVA-44796|Aspose.Cells formelberäkningsmotor producerar ?#N/A? värden för vissa celler|
|CELLSJAVA-44798|Bug för formatering 0,9999999999999999 med anpassat "#" för JDK8 eller senare versioner|
|CELLSJAVA-44773|Data är förstörda när du öppnar ett Excel-dokument med dolda kolumner i GridWeb (Java)|
|CELLSJAVA-44781|undersök problemet med radändring av storlek när du ändrar storlek till mycket liten höjd|
|CELLSJAVA-44787|Nedre kant som tappades vid sista raden i arbetsboken|
|CELLSJAVA-44761|Överdriven minnesanvändning vid konvertering av Excel-fil till HTML|
|CELLSJAVA-44801|Excel till PDF-konvertering med Aspose.Cells for Java v22.7 orsakar förvrängda tecken|
|CELLSJAVA-44741|Radbrytningen är inte rätt i utgången xlsx efter att ha satt html-strängen i cellen|
|CELLSJAVA-44776|Utformning av tabellrubrikrad förlorade vid kopiering av ark|
|CELLSJAVA-44789|Problem med teckensträngsersättning av textruta placerad i Excel-kalkylblad|
|CELLSJAVA-44792| Oändligt sparande arbetsbok till HTML-format (2892)|
|CELLSJAVA-44763|Undantag "java.lang.IllegalArgumentException: kan inte analysera argumentnummer: 1:X8" när Excel-filen laddas med "org.apache.commons.io.input.AutoCloseInputStream"|
|CELLSJAVA-44774|Fel vid lagring som PDF - Undersökning krävs|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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
