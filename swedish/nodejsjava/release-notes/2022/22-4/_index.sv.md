---
title: Aspose.Cells for Node.js via Java 22.4 Release Notes
type: docs
weight: 9
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-22-4-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 22.4](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-22.4/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44415|Tusentals getResourceAsAStream-anrop orsakar hög CPU-belastning och minnesförbrukning under rapportgenerering|
|CELLSJAVA-44490|lägg till GridWorkbookSetting för GridWeb|
|CELLSJAVA-44455|När du konverterar filen XLSX till PDF blir datumet i pivottabellen ett serienummer|
|CELLSJAVA-44370|Excel-filen blir korrupt när den öppnas och sparas med Aspose.Cells|
|CELLSJAVA-44381|Problem med villkorsformatering när raden eller kolumnen tas bort|
|CELLSJAVA-44442|Att öppna och spara med Aspose.Cells förstör arbetsboken|
|CELLSJAVA-44356|bildpositionsfråga för utskrift för filen fs.zip i GridWeb|
|CELLSJAVA-44357|problem för visning av ofd.zip i GridWeb|
|CELLSJAVA-44398|GridWeb visningsproblem från kund|
|CELLSJAVA-44464|ytterligare nummer 1, kolumn En bakgrundsfärg är inte samma som i excel för yscl.xls på ark4|
|CELLSJAVA-44466| ytterligare problem 3, setCalculateFormula till false fungerar inte|
|CELLSJAVA-44496|Inkludera rubriktaggen/elementet för tabellen när du laddar html|
|CELLSJAVA-44429|Effekten av Excel-diagram i excel skiljer sig från den i HTML|
|CELLSJAVA-44414| Unicode i JSON kommer att bryta genererade XLSX och CSV|
|CELLSJAVA-44404|Undantag "java.lang.IllegalArgumentException: Ogiltigt kolumnindex" vid inläsning av en XLSX-fil i GridWeb|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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
