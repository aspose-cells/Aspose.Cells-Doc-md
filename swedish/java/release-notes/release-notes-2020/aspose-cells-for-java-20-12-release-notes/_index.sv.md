---
title: Aspose.Cells för Java 20.12 Release Notes
type: docs
weight: 1
url: /sv/java/aspose-cells-for-java-20-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 20.12](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.12/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43367|Stöd beräkning av ISFORMEL-funktionen|
|CELLSJAVA-43338|Skillnad i utdata vid konvertering av Excel-fil till PDF|
|CELLSJAVA-43346|Utdatafilen är korrupt när fler än 12 fält läggs till i sidfiltren för pivottabellen|
|CELLSJAVA-43351|Bakgrundsfärgen på rubriktabellen är inte rätt vid konvertering till pdf|
|CELLSJAVA-43358|Text saknas vid konvertering av HTML till Excel|
|CELLSJAVA-43341|Extra tomma kolumner vid export av CSV med LightCellsDataProvider|
|CELLSJAVA-43352|Excel-fil konverterad till PDF ger ett problem med stora siffror|
|CELLSJAVA-43339|Bilden är felplacerad när källfilen konverteras till pdf|
|CELLSJAVA-43340|Saknat innehåll i XLS till PDF-konvertering|
|CELLSJAVA-43336| Sjökortsförklaringsposter renderas för långt till vänster|
|CELLSJAVA-43356|Tomma värden/luckor på ett diagram respekteras inte mellan två värden|
|CELLSJAVA-43344|Aktuellt användarnamn visas som författare till den senaste kommentaren|
|CELLSJAVA-43349|Dolda rader underhålls inte från XML till XLS/XLSX-konvertering|
|CELLSJAVA-43361|Fel cellfärg vid konvertering av xls till xlsx|
|CELLSJAVA-43366|Egenskapen SetAsTotal uppdateras inte|
|CELLSJAVA-43348|XLSB till PDF-konvertering: CellsException: -2147483648|
|CELLSJAVA-43343| Undantag vid export av en fil till PDF som inte har ett markerat objekt för en form|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till metoden Cell.SetDynamicArrayFormula(string arrayFormula, FormulaParseOptions options, bool calculate).**

Stöder för att ställa in dynamisk arrayformel och spilla in i närliggande celler om möjligt.

### **Lägger till metoden Workbook.RefreshDynamicArrayFormulas(bool calculate).**

Stöder för att uppdatera dynamiska matrisformler och spilla in i angränsande celler enligt aktuella data.

### **Lägger till Cell.Kommentaregenskap.**

Får cellens kommentar.

### **Lägger till egenskapen HtmlSaveOptions.ExportExtraHeadings**

Anger om extra rubriker exporteras när textens längd är längre än maxvisningskolumnen.
Standardvärdet är falskt. Om du vill importera html-filen till Excel, behåll standardvärdet.

### **Lägger till egenskapen HtmlSaveOptions.ExportFormula**

Anger om formeln exporteras när filen sparas till html. Standardvärdet är sant.
Om du vill importera utdata-html till excel, behåll standardvärdet.

### **Lägger till egenskapen HtmlSaveOptions.MergeEmptyTdForcely**

Indikerar om man tvingar samman ett tomt TD-element vid export av fil till html.
Storleken på html-filen kommer att minskas avsevärt efter att värdet ställts in på sant. Standardvärdet är falskt.
Om du vill importera html-filen till Excel eller exportera perfekta rutnätslinjer när du sparar filen till html,
behåll standardvärdet.

### **Lägger till egenskapen LoadOptions.AutoFilter**

Indikerar om data filtreras automatiskt när filerna laddas.
Ibland, även om autofilter är inställt, döljs inte motsvarande rader i filen. Fungerar nu bara för SpreadSheetML-fil.

### **Lägger till WorkbookSettings.Author-egenskap**

Hämtar och ställer in författaren till arbetsboken.

### **Lägger till metoden MultipleFilterCollection.Add().**

Lägger till filtersträng för autofilter.
