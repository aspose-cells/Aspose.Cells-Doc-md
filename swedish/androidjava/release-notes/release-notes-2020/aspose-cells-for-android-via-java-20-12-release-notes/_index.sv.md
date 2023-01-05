---
title: Aspose.Cells for Android via Java 20.12 Release Notes
type: docs
weight: 8
url: /sv/java/aspose-cells-for-android-via-java-20-12-release-notes/
---
{{% alert color="primary" %}}

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 20.12.

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43322|Egenskapen Shape.getWorksheet() krävs|Ny funktion|
|CELLSJAVA-43367|Stöd beräkning av ISFORMEL-funktionen|
|CELLSJAVA-43191|Tillhandahåll sätt att hantera scenarier när du anger felaktiga teckensnittstyper|Förbättring|
|CELLSJAVA-40913|Pilriktningen har ändrats i den resulterande PDF|Insekt|
|CELLSJAVA-43282|Uppdatera pivot fungerar inte och korrumperar utdatafilen|Insekt|
|CELLSJAVA-43286|Aspose.Cells är i konflikt med HtmlHiddenRowDisplayType.REMOVE-inställningarna|Insekt|
|CELLSJAVA-43302|Problem med att få Cells värde|Insekt|
|CELLSJAVA-43308|HTML för att Excel-konvertering med wrapText-egenskapen|Insekt|
|CELLSJAVA-43318|Cell värdeproblem efter uppdatering av pivottabellen|Insekt|
|CELLSJAVA-43299|Problem med att få Cell-värdet|Insekt|
|CELLSJAVA-43284|Tabellen skrivs inte ut när du använder Aspose.Cells för en viss fysisk skrivare|Insekt|
|CELLSJAVA-43273|Text i förklaringsobjekt klipps ut i utdatabilden|Insekt|
|CELLSJAVA-43274|Skillnad i diagramstapelns konturfärg|Insekt|
|CELLSJAVA-43276|Problem med radbrytning vid konvertering av XLSX till PDF|Insekt|
|CELLSJAVA-43278|Genomstruken i Excel visas inte i filen PDF|Insekt|
|CELLSJAVA-43304|Vissa dataetiketter i diagrammet saknas i utgången PDF|Insekt|
|CELLSJAVA-43311|Diagram X-axeletiketter är vertikala istället för diagonala när de konverteras till bild|Insekt|
|CELLSJAVA-40992|Problem med diagramtextposition när du sparar en Excel-fil igen|Insekt|
|CELLSJAVA-43294|Färgtema för villkorlig formatering fungerar inte korrekt|Insekt|
|CELLSJAVA-43307|Ändra storlek Problem med inbäddat OLE-objekt vid kopiering av kalkylblad|Insekt|
|CELLSJAVA-43319|Problem med att få cellvärde med formel|Insekt|
|CELLSJAVA-43330|Problem efter återlagring av XLSB-fil - skadad fil|Insekt|
|CELLSJAVA-43333|Bilder och textpositionering är felaktig när Excel renderas som HTML|Insekt|
|CELLSJAVA-43321|Problem med autofilter - tomma rader visas|Insekt|
|CELLSJAVA-43335|Dödläge inträffade vid beräkning av formler på arbetsbok|Insekt|
|CELLSJAVA-43313|Sjökortetiketten ändrar sin position när den skrivs ut|Insekt|
|CELLSJAVA-43314|0/100 % rad skrivs inte ut för 100 % cirkeldiagram|Insekt|
|CELLSJAVA-43316| Olika problem vid utskrift av diagram|Insekt|
|CELLSJAVA-40582|Smart art-text renderas inte korrekt till PDF/bild|Insekt|
|CELLSJAVA-41639|Kolumnbredder bevaras inte vid konvertering från formatet "XML Spreadsheet 2003" till formatet XLSX|Insekt|
|CELLSJAVA-43315|Konvertering av XLS till XLSX gör filen korrupt och ger "Shape to Image" fel vid konvertering av utdata XLSX till PDF|Insekt|
|CELLSJAVA-43334|Problem med autofilter på tabell|Insekt|
|CELLSJAVA-43338|Skillnad i utdata vid konvertering av Excel-fil till PDF|
|CELLSJAVA-43346|Utdatafilen är korrupt när fler än 12 fält läggs till i sidfiltren för pivottabellen|
|CELLSJAVA-43351|Bakgrundsfärgen på rubriktabellen är inte rätt vid konvertering till pdf|
|CELLSJAVA-43358|Text saknas vid konvertering av HTML till Excel|
|CELLSJAVA-43341|Extra tomma kolumner vid export av CSV med LightCellsDataProvider|
|CELLSJAVA-43352|Excel-fil konverterad till PDF ger ett problem med stora siffror|
|CELLSJAVA-43339|Bilden är felplacerad när källfilen konverteras till pdf|
|CELLSJAVA-43340|Saknat innehåll i konverteringen XLS till PDF|
|CELLSJAVA-43336| Sjökortsförklaringsposter renderas för långt till vänster|
|CELLSJAVA-43356|Tomma värden/luckor på ett diagram respekteras inte mellan två värden|
|CELLSJAVA-43344|Aktuellt användarnamn visas som författare till den senaste kommentaren|
|CELLSJAVA-43349|Dolda rader underhålls inte från XML till XLS/XLSX konvertering|
|CELLSJAVA-43361|Fel cellfärg vid konvertering av xls till xlsx|
|CELLSJAVA-43366|Egenskapen SetAsTotal uppdateras inte|
|CELLSJAVA-43296|ArrayIndexOutOfBoundsException medan pivottabellen uppdateras|Undantag|
|CELLSJAVA-43298|Aspose.Cells 20.8: Undantag när du sparar till PDF.|Undantag|
|CELLSJAVA-43348|XLSB till PDF konvertering: CellsException: -2147483648|
|CELLSJAVA-43343| Undantag vid export av en fil till PDF som inte har ett valt objekt för en form|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Lägger till ExceptionType.Permission enum**

Representerar ExceptionType.Permission.

### **Lägger till egenskapen ExternalConnection.PowerQueryFormula.**

Hämtar definitionen av kraftfrågeformel.

### **Lägger till metoden FileFormatUtil.VerifyPassword.**

Verifierar om lösenordet är giltigt för filen.

### **Lägger till metoden VbaProject.Copy().**

Kopierar VBA-projekt.

### **Lägger till egenskapen XlsSaveOptions.MatchColor.**

Indikerar om matchande färg om färgen inte finns i paletten när .xls-filen sparas.

### **Tar bort föråldrad Series.Line-egenskap.**

Använd egenskapen Series.Border istället.

### **Tar bort föråldrad CellsHelper.IsProtectedByRMS()-metod**

Använd egenskapen FileFormatUtil.DetectFileFormat().IsProtectedByRMS istället.

### **Tar bort föråldrade metoderna CellsHelper.DetectLoadFormat() och CellsHelper.DetectFileFormat()**

Använd FileFormatUtil.DetectFileFormat() istället.

### **Tar bort föråldrad CellsHelper.FontDir-egenskap.**

Använd FontConfigs.SetFontsFolder(sträng, bool) istället.

### **Tar bort föråldrad CellsHelper.FontDirs-egenskap.**

Använd FontConfigs.SetFontFolders(string[], bool) istället.

### **Tar bort föråldrad CellsHelper.FontFiles-egenskap.**

Använd FontConfigs.SetFontSources(FontSourceBase[]) istället.

### **Lägger till egenskapen CellsHelper.IsCloudPlatform.**

Indikerar om den körs på kundeplattformen.

### **Lägger till egenskapen Shape.Worksheet.**

Hämtar kalkylbladet som innehåller denna form.

### **Lägger till egenskapen SaveOptions.SortExternalNames.**

Anger om externa namn sorteras när .xlsx-filer sparas.

### **Lägger till metoden ListObject.Filter().**

Filtrerar tabellen.

### **Lägger till åsidosättande XmlMapCollection.Clear()-metoden.**

Rensar alla xml-kartor.

### **Lägger till SaveFormat.Docx enum.**

Representerar att spara som .docx-filer.

### **Lägger till ImageType.OfficeCompatibleEmf enum.**

Windows Förbättrad metafil som är mer kompatibel med Office.

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
