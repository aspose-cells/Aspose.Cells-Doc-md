---
title: Aspose.Cells for .NET 22.4 Release Notes
type: docs
weight: 9
url: /sv/net/aspose-cells-for-net-22-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.4](https://www.nuget.org/packages/Aspose.Cells/22.4.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50624|Stöd för att ta bort tomma celler för att spara csv|
|CELLSNET-50747|Lägg till Style.HasBorders för att kontrollera om det finns gränser för det|
|CELLSNET-50627|Få sammanslagna intervall med avseende på kalkylbladscell i Aspose.Cells.GridDesktop|
|CELLSNET-50675|lägg till GridLoadDataFilterOptions för GridDesktop och Worksheet.GetMergeByCell api|
|CELLSNET-50816|Stöd High Contrast Theming i Aspose.Cells.GridDesktop|
|CELLSNET-50751|Stöd PasteType.ValuesAndFormats vid kopiering av intervall.|
|CELLSNET-50620|När du konverterar xls till pdf renderas inte textens tom radstorlek i textrutan korrekt|
|CELLSNET-50684|Problem med att extrahera OLE-bilagor från filen ODS|
|CELLSNET-50712|WordArt-effekter och -former renderas inte korrekt i Excel till PDF-konvertering|
|CELLSNET-50714|XLSB-filen är korrupt när den öppnas och sparas av Aspose.Cells API:er|
|CELLSNET-50778|Vertikala linjer saknas för pivottabellen i utgången PDF|
|CELLSNET-50517|Fel referens i formeln för villkorlig formatering efter infogning/borttagning av rader|
|CELLSNET-50622|Rubrik tom rad/kolumn med anpassad stil exporteras inte till csv|
|CELLSNET-50645|Felaktiga resultat med Workbook.CalculateFormula-metoden|
|CELLSNET-50695|Name.RefersTo/R1C1RefersTo ändras när man refererar till en celladress|
|CELLSNET-50553| Kolumnstil tillämpas inte på hela kolumnen i GridDesktop|
|CELLSNET-50641|Problem med att öppna en lösenordsskyddad fil med tomt lösenord ("") till Aspose.Cells.GridDesktop|
|CELLSNET-50672|lägg till händelsen FailLoadFile|
|CELLSNET-50815| dubbelklicka på redigera cellvärde beteende är inte korrekt|
|CELLSNET-50594|Text döljs bakom inmatningsfält vid konvertering av XLSX till HTML|
|CELLSNET-50665|Pdf/A-1b-validering misslyckades efter inställning av CreatedTime vid konvertering till pdf|
|CELLSNET-50701|Ljusstyrkan och kontrasten för den infogade bilden återställs i Excel till PDF konvertering|
|CELLSNET-50834|Problem med tabellens sammanslagna celler i Excel till HTML konvertering|
|CELLSNET-50595|XLSX till SVG: Skillnader i diagram|
|CELLSNET-50596|Axelenheter ändras inte i utdatafilen XLSX|
|CELLSNET-50740|XLSX till JPG: text flyttad till höger sida på sjökort|
|CELLSNET-50309|Intervall till PNG: utgången inte som förväntat|
|CELLSNET-50610|RecalculateBeforeSave alltid falskt i nyare version|
|CELLSNET-50611|Problem med booleskt värde i Excel till PDF-rendering|
|CELLSNET-50706| Filstorleken minskas många gånger när du sparar med SaveToStream() vid andra gången|
|CELLSNET-50749| DeleteBlankColumns(options)-metoden tar bort kolumner som bara har kommentarer|
|CELLSNET-50759|Formler sparas inte korrekt när en arbetsbok har externa länkar till en arbetsbok som inte har sparats|
|CELLSNET-50776|Smarta markörer bearbetas inte när en generisk lista av typen System.Dynamic.ExpandoObject används som datakälla för ett kapslat objekt|
|CELLSNET-50779| Potentiell dataförlust angående inbäddade objekt vid konvertering XLS -> XLSX -> XLS|
|CELLSNET-50821|Problem med Range.AutoFill - data fylls inte i automatiskt korrekt om intervallområdet skärs|
|CELLSNET-50777|PutValue-metoden kastar System.StackOverflowException i australiskt regionalt format|
|CELLSNET-50275|Undantaget "Objektreferens inte inställt på en instans av ett objekt" vid rendering av ODS till HTML|
|CELLSNET-50713|System.NullReferenceException när en XLSB-fil laddas|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till klassen DefaultStyleSettings.**

Grupp med standardvärden för stilrelaterade egenskaper.

### **Lägger till egenskapen LoadOptions.DefaultStyleSettings.**

Stöd för att ställa in standardvärden för stilrelaterade egenskaper för att initiera en arbetsbok.

### **Lägger till egenskapen TxtSaveOptions.TrimTailingBlankCells.**

Stöd för att ta bort alla tomma celler (upprepade tecken i separator som "~,~,~,~,") i slutet av radposten vid export av csv/tsv.

### **Lägger till Style.HasBorders-egenskapen.**

Stöd för att kontrollera om det finns gränser har satts för stilen.

### **Föråldrade LoadOptions.StandardFont/StandardFontSize egenskaper.**

Använd LoadOptions.DefaultStyleSettings.FontName/FontSize istället.

### **Tar bort föråldrade enum StyleModifyFlag.FontSubscript och FontSuperscript.**

Använd StyleModifyFlag.FontScript istället.

### **Föråldrade Shape.ConnectionPoints-egenskaper.**

Använd metoden GetConnectionPoints() istället.

### **Lägger till metoden Shape.GetConnectionPoints().**

Skaffa anslutningspunkterna.

### **Lägger till egenskaperna Row.IsCollapsed och Column.IsCollapsed.**

Indikerar om raden och kolumnen är komprimerade.

### **Lägger till PasteType.ValuesAndFormats enum.**

Indikerar endast kopieringsvärden och format.

### **Lägger till egenskapen Shape.IsInGroup.**

Anger om formen är grupperad.

### **Lägger till metoden AutoFilter.GetCellArea().**

Hämtar området där det angivna autofiltret gäller.

### **Lägger till metoden Cells.GetRowOriginalHeightPoint().**

Får den ursprungliga radhöjden, i poängenhet.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, sträng destCellName, PivotField baseField).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, int rad, int kolumn, PivotField baseField).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add(PivotTable pivot, string destCellName, int baseFieldIndex).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, int rad, int kolumn, int baseFieldIndex).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till metoden TimelineCollection.Add (pivottabell pivot, sträng destCellName, string baseFieldName).**

Lägg till en ny tidslinje med pivottabell som datakälla.

### **Lägger till DataLabelShapeType.Line enum.**

Representerar linjeformen. Denna typ är inte tillgänglig i Excel, den används bara för vissa specialfiler.
