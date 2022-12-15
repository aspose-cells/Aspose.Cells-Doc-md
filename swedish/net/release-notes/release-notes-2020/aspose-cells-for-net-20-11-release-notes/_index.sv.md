---
title: Aspose.Cells for .NET 20.11 Release Notes
type: docs
weight: 2
url: /sv/net/aspose-cells-for-net-20-11-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.11](https://www.nuget.org/packages/Aspose.Cells/20.11.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47706|Stöd för språkberoende formateringsmönster "aaaa" för år i regionen Spanien|Förbättringar|
|CELLSNET-47641|Varning höjdes när 29 ark lades till och XLS-filen öppnades i MS Excel|Prestanda|
|CELLSNET-46716|Text klipptes ut vid rendering av PDF|Buggar|
|CELLSNET-47618|En bild blir helvit och en del textkorruption i andra bilder/former|Buggar|
|CELLSNET-47635| Slicer på olika bord genererar skadad fil|Buggar|
|CELLSNET-47642|XLSB-filen är skadad efter att ha laddats och sparats|Buggar|
|CELLSNET-47660|Diagramfält som innehåller datum har olika format i PDF-format|Buggar|
|CELLSNET-47661|Aspose.Cells genererar ogiltig HTML-uppmärkning för ett visst kalkylblad för ett särskilt Cells-dokument|Buggar|
|CELLSNET-47680|Pivottabeller uppdaterades inte|Buggar|
|CELLSNET-47659|Problem med att hitta celler med specifika stilar|Buggar|
|CELLSNET-47679|Skillnad i beräkning av Aspose.Cells och Excel|Buggar|
|CELLSNET-47666|Arbetsbok kan inte visas i SharePoint|Buggar|
|CELLSNET-47698|Skift i logotypposition medan du konverterar XLS-fil till PDF|Buggar|
|CELLSNET-47651|Export av polardiagram till pdf är skev|Buggar|
|CELLSNET-47662|Fel data Etiketter visas vid konvertering av Excel-diagram till bild|Buggar|
|CELLSNET-47667|Staplar saknas i stapeldiagram i utdatabilden|Buggar|
|CELLSNET-47697|Vissa Y-axelvärden går utanför diagrammet i den utgående PDF-filen|Buggar|
|CELLSNET-43579|WortArt-textens krökning ändras vid konvertering från Excel till PDF|Buggar|
|CELLSNET-47675|Innehållet i XLS-filen ändras efter att ha laddats och sparats|Buggar|
|CELLSNET-47704|Anpassade egenskaper försvann efter att ha redigerat/sparat en lösenordsskyddad (krypterad) XLS-fil|Buggar|
|CELLSNET-47708|Sorteringsordningen fungerade inte korrekt med dynamiska formler (smarta markörer)|Buggar|
|CELLSNET-47682|Undantag vid laddning av viss Htm|Undantag|
|CELLSNET-47683|Undantag vid laddning av viss Htm|Undantag|
|CELLSNET-47684|Undantag vid laddning av viss Htm|Undantag|
|CELLSNET-47689|Undantag vid konvertering av XLSB till PNG och HTML|Undantag|
|CELLSNET-47701|Det gick inte att skapa en kopia av XLTX-arbetsboken|Undantag|
|CELLSNET-47628|Att radera tomma rader från celler orsakar ArgumentOutOfRangeException|Undantag|
|CELLSNET-47629|Att anropa cellvärden efter att ha tagit bort tomma rader och kolumner orsakar ArgumentException|Undantag|
|CELLSNET-47700|CalculateFormula kastar InvalidCastException|Undantag|
|CELLSNET-47703|Undantag uppstod vid anrop av Workbook.CalculateFormula()|Undantag|
|CELLSNET-47669|Ogiltigt kolumnindex ArgumentException kastas när det första kalkylbladet konverteras till HTML|Undantag|
|CELLSNET-47677|DataBar.ToImage höjning undantag om raden är dold.|Undantag|
|CELLSNET-47686|Kan inte konvertera XLSB till XLSX|Undantag|
|CELLSNET-47687|Kan inte ladda Ods|Undantag|
|CELLSNET-47694|Undantag när dokument XLSX-fil öppnas|Undantag|
|CELLSNET-47695|Ogiltigt cellnamn efter DeleteRange|Undantag|
|CELLSNET-47699|Undantag när ODS-filen är öppen|Undantag|
|CELLSNET-47702| Undantag inträffade när de krypterade "Microsoft Excel 5.0/95 Workbook"-filerna laddades|Undantag|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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

### **Lägger till metoden XmlMapCollection.Clear().**

Rensar alla xml-kartor.

### **Lägger till SaveFormat.Docx enum.**

Representerar att spara som .docx-filer.

### **Lägger till ImageType.OfficeCompatibleEmf enum.**

Windows Förbättrad metafil som är mer kompatibel med Office.

