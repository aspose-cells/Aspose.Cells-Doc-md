---
title: Aspose.Cells för Java 8.9.0 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-8-9-0-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41901 | Staplar rör sig uppåt i utdata-PDF-filen| Förbättring|
|CELLSJAVA-41909 | Det fungerar inte att ange anpassade decimaler och gruppseparatorer för arbetsbok| Insekt|
|CELLSJAVA-41895 | Resultatet av formelberäkningen skiljer sig från den inbyggda Excel-beräkningen| Insekt|
|CELLSJAVA-41917 | Kryssrutor renderas inte korrekt när du använder metoden SheetRender.toImage().| Insekt|
|CELLSJAVA-41903 | Teckenorienteringen är annorlunda vid rendering till PDF| Insekt|
|CELLSJAVA-41896 | Vissa tecken saknas eller har inte klistrats in direkt i Excel till PDF-konvertering| Insekt|
|CELLSJAVA-41740 | Vissa av DataBar-bilderna är tomma| Insekt|
|CELLSJAVA-41769 | Staplarna i diagrammet är inte korrekt justerade med celler i PDF| Insekt|
|CELLSJAVA-41905 | Feljusterade staplar efter rendering av kalkylark till EMF| Insekt|
|CELLSJAVA-41894 |Teckenutrymmesproblem vid rendering av kalkylark till PDF| Insekt|
|CELLSJAVA-41893 | Bakgrundsbilden är förvrängd eller suddig i den utgående PDF-filen| Insekt|
|CELLSJAVA-41892 | Bakgrundsbilden sträcks ut i PDF-filen| Insekt|
|CELLSJAVA-41916 | Trasiga externa formelreferenser när du använder Cells.copyColumns| Insekt|
|CELLSJAVA-41915 | Skadad XLSX-fil efter textersättning| Insekt|
|CELLSJAVA-41912 | Problem med removeFormula på ett kalkylblad som hänvisar till Named Ranges| Insekt|
|CELLSJAVA-41899 | Kan inte upptäcka XLSX-laddningsformat med FileFormatUtil.detectFileFormat| Insekt|
|CELLSJAVA-41328 | Förlust av textblock i frenchCommonWords.xlsx| Insekt|
|CELLSJAVA-40307 | Problem med textspillningskontroll| Insekt|
|CELLSJAVA-41919 | CellsException: 2"="Stra?e zu breit",", vid Workbook ctor| Undantag|
|CELLSJAVA-41914 | java.lang.ArrayIndexOutOfBoundsException: 4 när teckensnittet för cellen hämtas| Undantag|
|CELLSJAVA-41920 | StringIndexOutOfBoundsException: Strängindex utanför intervallet: 7, vid export av diagram till bild| Undantag|
|CELLSJAVA-41913 | Undantag: "IllegalArgumentException: length" vid laddning av en Excel-fil (XLS).| Undantag|
|CELLSJAVA-41911 | Undantag: "Fel i Cell: ... -Ogiltig formel" när en Excel-fil laddas via Aspose.Cells API:er| Undantag|
|CELLSJAVA-41906 |Arbetsbokskonstruktorn kastar undantag: "java.lang.NumberFormatException: tom sträng"| Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen HtmlSaveOptions.DefaultFontName**
Anger standardteckensnittsnamnet vid export av HTML, standardteckensnittet kommer att användas när stiltypsnittet inte finns. Om den här egenskapen är null kommer Aspose.Cells att använda universellt teckensnitt som har samma familj som det ursprungliga teckensnittet, standardvärdet är null.
### **Lägger till egenskapen PivotTable.IsExcel2003Compatible**
Anger om pivottabellen är kompatibel med Excel2003 vid uppdatering av pivottabell. Om sant måste en sträng vara mindre än eller lika med 255 tecken, så om strängen är större än 255 tecken kommer den att trunkeras. Om det är falskt kommer en sträng inte att ha den ovannämnda begränsningen. Standardvärdet är sant.
### **Lägger till egenskapen ImageOrPrintOptions.DefaultFont**
När tecken i Excel är unicode och inte ska ställas in med korrekt typsnitt i cellstil, kan de visas som block i PDF och bild.
Ställ in standardteckensnittet som MingLiu eller MS Gothic för att visa dessa tecken. Om den här egenskapen inte är inställd kommer Aspose.Cells att använda systemets standardteckensnitt för att visa dessa unicode-tecken.
### **Lägger till GetVersion-metoden i GridWeb.**
Hämta releaseversionen.

{{% alert color="primary" %}} 

Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.9.0 också i denna Aspose.Cells för Java v8.9.0.

{{% /alert %}}
