---
title: Aspose.Cells for .NET 20.12 Release Notes
type: docs
weight: 1
url: /sv/net/aspose-cells-for-net-20-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.12](https://www.nuget.org/packages/Aspose.Cells/20.12.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47309|IFS-formler lindas med lockiga hängslen efter att ha sparats med ASPOSE|Ny funktion|
|CELLSNET-47710|Stöd formel med Sheet() funktion|Ny funktion|
|CELLSNET-47672|Minska utdatastorleken vid konvertering till HTML|Förbättring|
|CELLSNET-47674|Visa ytterligare kolumner när texten överlappar nästa celler|Förbättring|
|CELLSNET-47749|Ta bort ods makro i Workbook.RemoveMacro|Förbättring|
|CELLSNET-47759|Stöd h1-tagg när du ställer in Cell.HtmlString|Förbättring|
|CELLSNET-47771|Nytt kalkylblad saknas mc:Ignorable="x14ac xr xr2 xr3"|Förbättring|
|CELLSNET-47758| Konverteringskomplex XLSM till HTML tar mycket tid|Prestanda|
|CELLSNET-47578|Ogiltig uppmärkning med oöppnad avslutande SPAN-tagg produceras vid konvertering av Cells dokument till HTML|Insekt|
|CELLSNET-47776|DirectoryNotFoundException när du försöker öppna HTML|Insekt|
|CELLSNET-47643|Några extra kolumner i den nya utdata i Excel till HTML-rendering|Insekt|
|CELLSNET-47688|Vissa TD:er kommer att orsaka teckensnittsfel för Wingdings-teckensnitt i HTML till PDF rendering|Insekt|
|CELLSNET-47690|Konvertering av HTML till Xlsx respekterar inte formateringen av HTML-tabellen|Insekt|
|CELLSNET-47718|Bilderna är felaktigt justerade vid import av fil till html|Insekt|
|CELLSNET-47729|Bilder överlappar texten när du importerar html till Excel|Insekt|
|CELLSNET-47746|Okodade citattecken i värden för HTML attribut|Insekt|
|CELLSNET-47747|Skillnader vid konvertering av Excel till HTML|Insekt|
|CELLSNET-47763|Seriens värde är inte korrekt efter uppdatering av pivotdata.|Insekt|
|CELLSNET-47731|Felaktigt resultat för körning av PPMT-formel|Insekt|
|CELLSNET-47734|Om du infogar kolumn och ändrar formel raderas andra formler|Insekt|
|CELLSNET-47738|autofilter fungerar inte som excel|Insekt|
|CELLSNET-47764|Antal konverterade till vetenskapligt under konvertering från XLSX till CSV|Insekt|
|CELLSNET-47740| Text klipps (första raden visas inte) med anpassat teckensnitt när rader anpassas automatiskt|Insekt|
|CELLSNET-47753|Ram runt ikonen vid konvertering av Excel till PDF|Insekt|
|CELLSNETCORE-88|SetFontFolders fungerar inte korrekt med dataserieetiketter|Insekt|
|CELLSNET-47739|Förklaring visar namnet på serien istället för etiketttexten|Insekt|
|CELLSNET-47713|Problem med att kopiera ark när "dold namndefinition" finns i Excel-fil|Insekt|
|CELLSNET-47733|Olika beteende mellan version 20.3 och 20.11|Insekt|
|CELLSNET-47752|Ole Objektetikett inte hämtad i Excel-ark|Insekt|
|CELLSNET-47761|Filen är skadad efter att ha rensat diagramtiteln.|Insekt|
|CELLSNETCORE-89|Om du tar bort tomma kolumner tas kommentarerna i kolumnerna efter den borttagna kolumnen bort|Insekt|
|CELLSNET-47732|RefreshPivotData kastar undantag|Undantag|
|CELLSNET-47745|Undantag uppstod vid import av exempelfiler|Undantag|
|CELLSNET-47711|Undantag vid öppning av filen ODS|Undantag|
|CELLSNET-47712|Undantag görs när man försöker ladda bifogat dokument|Undantag|
|CELLSNET-47715|Kan inte ladda Xltx-fil|Undantag|
|CELLSNET-47735|Undantag vid öppning XLSB|Undantag|
|CELLSNET-47741|Kolumnindexet ska inte finnas inom det pivotbara rapportundantaget när DeleteBlankColumns anropas|Undantag|
|CELLSNET-47750|Kan inte öppna XLSX|Undantag|
|CELLSNET-47751|Kan inte konvertera XLSX till XLSM|Undantag|
|CELLSNET-47773|ArgumentOutOfRangeException vid konvertering av kalkylblad till bild|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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

