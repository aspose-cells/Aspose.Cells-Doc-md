---
title: Aspose.Cells for Java 21.4 Release Notes
type: docs
weight: 9
url: /sv/java/aspose-cells-for-java-21-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 21.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.4/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43396|Konvertering av Excel-ark till textfil tar bort enstaka citat från början|
|CELLSJAVA-43386|Sortering fungerar inte när data innehåller icke-alfanumeriska tecken|
|CELLSJAVA-43403|Textplacering flyttades till vänster när du sparade som HTML|
|CELLSJAVA-43421|Escape- och radbrytningstecken renderade inte korrekt vid konvertering av HTML till Excel|
|CELLSJAVA-43427|Villkorsformat med datafält Visa värden i HTML-export|
|CELLSJAVA-43428| Bokföringsformat kombinerat med 6-punktsfont förvränger siffror i HTML|
|CELLSJAVA-43429|Text med vertikal textjustering försvinner i HTML|
|CELLSJAVA-43407|Excel-formler hoppas över/ändras efter att filen har sparats|
|CELLSJAVA-43419| Anpassat nummerformat visas inte korrekt i PDF|
|CELLSJAVA-43374|Diagrametiketter upprepas när de bifogade Excel-filerna konverterades till PDF|
|CELLSJAVA-43409| Oväntade dataetiketter dök upp i utdatabilden för diagram|
|CELLSJAVA-43411|Teckensnittsersättningsvarningar fungerar inte i diagram till bildkonvertering|
|CELLSJAVA-43414|Xls till pdf-konverteringsproblem|
|CELLSJAVA-43425|Sidhuvud-sidfot är inte tillgänglig på första sidan när den exporteras till Excel|
|CELLSJAVA-43432|Diagraminnehåll matchade inte när ett XLS-filformat sparades på nytt|
|CELLSJAVA-43433|Den refererade bilden renderas inte i PDF|
|CELLSJAVA-43434|SmartMarkers dynamiska formel har fel expanderande cellstil|
|CELLSJAVA-43435| Smart Markers dynamisk formel infogar celler enligt vänster expanderad kolumn men inte enligt kolumnerna i formeln|
|CELLSJAVA-43417|Undantag höjdes när XLSX öppnades från stor fil|
|CELLSJAVA-43431|java.lang.NullPointerException höjdes när Cells.deleteColumn() anropades med den senaste versionen 21.3 medan den fungerar med 21.2|
|CELLSJAVA-43437|IndexOutOfBoundsUndantag för att klicka på andra arksidor i utvärderingsläge|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till StartAccessCache()/CloseAccessCache()-metoder för arbetsbok och arbetsblad.**

Ge användarna möjlighet att komma åt data i batch-läge med bättre prestanda.

### **Lägger till egenskaperna TxtSaveOptions.ExportQuotePrefix och TxtLoadOptions.TreatQuotePrefixAsValue.**

Ge användarna möjligheten att bestämma hur de ska göra med det ledande citatet av cellens värde vid export/import av CSV/TSV-filer.

### **Lägger till metoderna GlobalizationSettings.GetCollationKey(string,bool) och Compare(string,string,bool).**

Ge användarna möjlighet att åsidosätta standardreglerna för strängjämförelse. För vissa lokaler eller strängvärden kan standardregeln för strängjämförelse inte vara den förväntade (resultatet av vissa funktioner, såsom formelberäkning, sortering, etc., skiljer sig från vad som borde finnas i ms excel). Om så är fallet kan användaren åsidosätta dessa metoder med den förväntade regeln (till exempel kan användaren använda implementeringen av icu-biblioteket).

### **Lägger till enum ImageType.WebP.**

Representerar Weppy-bilden.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

För att kontrollera om ikonen uppdateras automatiskt.

### **Lägger till egenskapen WorkbookDesigner.LineByLine.**

Indikerar om bearbetning av smarta markörer rad för rad.

### **Lägger till egenskapen HtmlSaveOptions.ExportCellCoordinate.**

Anger om excel-koordinater för icke-tomma celler exporteras när filen sparas till html. Standardvärdet är false.Om du vill importera utdata-html till Excel, behåll standardvärdet.

### **Lägger till egenskapen AutoFitterOptions.DefaultEditLanguage.**

Hämtar eller ställer in standardspråk för redigering.
