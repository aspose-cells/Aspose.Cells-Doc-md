---
title: Aspose.Cells for .NET 20.9 Release Notes
type: docs
weight: 8
url: /sv/net/aspose-cells-for-net-20-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.9](https://www.nuget.org/packages/Aspose.Cells/20.9.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47567|Stöd Hämta/ställ in egenskaperna för skivformen|Ny funktion|
|CELLSNET-47549|Klient-api för att lägga till/ta bort kommentarer för GridWeb|Ny funktion|
|CELLSNET-47555|Diagram tillåter inte att #N/A behandlas som tomma celler när du sparar som PDF|Förbättring|
|CELLSNET-47579|Kaiti-teckensnittet är inte korrekt renderat|Förbättring|
|CELLSNET-47154|Frågetabeller laddas inte från ODS-fil|Förbättring|
|CELLSNET-47556|Förbättring för frysning och delning av arbetsblad|Förbättring|
|CELLSNET-47570|Makron bör tas bort när du kombinerar/kopierar arbetsböcker|Förbättring|
|CELLSNET-47543|Problem med smarta markörer med villkorlig formatering|Insekt|
|CELLSNET-47561|Valuta med anpassat format visas utanför cellen i HTML|Insekt|
|CELLSNET-47562|Sparar tomt ark med exporterade rutnätsinställningar till HTML|Insekt|
|CELLSNET-47569|Pivottabellen visas inte korrekt efter konvertering av XLSX till PDF|Insekt|
|CELLSNET-47475|CalculateFormula() beräknar annorlunda än MS Excel|Insekt|
|CELLSNET-47531|Formler som innehåller namn som inte finns visas som `WorkbookName`!Namn|Insekt|
|CELLSNET-47545|Anpassat negativt nummer renderas felaktigt till PDF|Insekt|
|CELLSNET-47548|Problem med att importera textfil med dubbla citattecken|Insekt|
|CELLSNET-47558|Anpassade negativa tal (med användning av regionen Schweiz) renderade felaktigt till PDF|Insekt|
|CELLSNET-47075|Behöver synkronisera rullning av två rutnät precis som excels SyncScrollingSideBySide.|Insekt|
|CELLSNET-47559|Det går inte att markera celler med piltangenterna på tangentbordet när arket är skrivskyddat|Insekt|
|CELLSNET-47360|Transparenta markörpunkter i diagrammet i Excel-filen blir förvrängda i den utgående PDF-filen|Insekt|
|CELLSNET-47565|Förgrundssidfotsbild blir bakgrund|Insekt|
|CELLSNET-46502|XLSX till TIFF-konvertering resulterar i en svart låda|Insekt|
|CELLSNET-46821|Konverterar kalkylblad till TIFF - Bilden är mörk|Insekt|
|CELLSNET-47458|Formförvrängning efter konvertering till PDF-fil|Insekt|
|CELLSNET-47551|X-axeln är inte korrekt vid konvertering av Excel-diagram till PDF|Insekt|
|CELLSNET-47546| Ta bort tomma rader/kolumner skadar Excel-dokument|Insekt|
|CELLSNET-47552|Fel PowerQueryFormula.FormulaDefinition|Insekt|
|CELLSNET-47573|Det går inte att skapa önskad formatering med shift|Insekt|
|CELLSNET-47574|XLS till HTML producerar tom fil|Insekt|
|CELLSNET-47581|MaxColumn är inställd på kolumn XFD efter anrop av InsertCutCells()|Insekt|
|CELLSNET-47586|Arbetsbok med vattenfallsdiagram kan inte öppnas med Excel 2016 efter kopiering|Insekt|
|CELLSNET-47547|Undantaget höjs när man lägger till skivare för bordet|Undantag|
|CELLSNET-47553|Undantag när en XLS-fil sparas till XLSX|Undantag|
|CELLSNET-47563|Undantag "Filen är skadad" när ett XLS-filformat laddas|Undantag|
|CELLSNET-47580|ArgumentOutOfRangeException vid konvertering av excel|Undantag|
|CELLSNET-47592|Undantag vid konvertering av viss XLSX till XLS|Undantag|
|CELLSNET-47557|Vissa egenskaper saknas vid kombination av arbetsböcker|Regression|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen AbstractCalculationEngine.ProcessBuiltInFunctions**

För prestanda och användarens bekvämlighetsskäl lade vi till den här egenskapen och gjorde dess standardvärde som**falsk** så att användaren kan koncentrera sig på de funktioner som inte har stöds av den inbyggda motorn. Om användarens befintliga implementering av**AbstractCalculation Engine** ändrat vissa inbyggda funktioners beräkning, bör användaren åsidosätta denna egenskap för att göra den som**Sann** från**20.9**.

### **Lägger till egenskapen TxtLoadOptions.HasTextQualifier**

Anger om det finns textkvalificerare för cellvärden i mallfilen.

### **Lägger till egenskapen TxtLoadOptions.TextQualifier**

Anger textkvalificeraren för cellvärden i mallfilen.

### **Lägger till egenskapen HtmlSaveOptions.ImageScalable**

 Indikerar om skalbar enhet ska användas för att beskriva bildens bredd. Standardvärdet för fastigheten är**Sann**.

### **Lägger till egenskapen Slicer.AlternativeText**

Hämtar eller ställer in den beskrivande (alternativa) textsträngen för Slicer-objektet.

### **Lägger till egenskapen Slicer.ColumnWidthPixel**

Hämtar eller ställer in bredden i pixelenhet för varje kolumn i utsnittet.

### **Lägger till Slicer.HeightPixel-egenskapen**

Hämtar eller ställer in höjden på det angivna utsnittet i pixlar.

### **Lägger till egenskapen Slicer.IsLocked**

Indikerar om skärformen är låst.

### **Lägger till egenskapen Slicer.IsPrintable**

Indikerar om skivobjektet är utskrivbart.

### **Lägger till egenskapen Slicer.LeftPixel**

Hämtar eller ställer in den horisontella förskjutningen av skivformen från dess vänstra kolumn, i pixlar.

### **Lägger till egenskapen Slicer.LockedAspectRatio**

Indikerar om låsning av bildförhållande.

### **Lägger till egenskapen Slicer.Placement**

Representerar hur ritobjektet är fäst vid cellerna under det. Egenskapen styr placeringen av ett objekt på ett kalkylblad.

### **Lägger till egenskapen Slicer.RowHeightPixel**

Returnerar eller ställer in höjden, i pixlar, för varje rad i det angivna utsnittet.

### **Lägger till egenskapen Slicer.Title**

Anger titeln på det aktuella Slicer-objektet.

### **Lägger till egenskapen Slicer.TopPixel**

Hämtar eller ställer in den vertikala förskjutningen av skivformen från den översta raden, i pixlar.

### **Lägger till egenskapen Slicer.WidthPixel**

Hämtar eller ställer in bredden på det angivna utsnittet, i pixlar.

### **Lägger till Worksheet.PaneState-egenskapen och PaneStateType-enum.**

Representerar tillståndet för rutan i kalkylbladet.

### **Lägger till egenskapen OdsLoadOptions.RefreshPivotTables.**

Anger om pivottabellen uppdateras när .ods-filer laddas.

### **Lägger till egenskapen FilterColumn.IsDropdownVisible.**

Indikerar om AutoFilter-knappen för denna kolumn är synlig.

### **Föråldrad Filter.Visibledropdown-egenskap.**

Använd FilterColumn.IsDropdownVisible istället.

### **Lägger till CopyOptions.KeepMacros-egenskapen.**

Indikerar om macorerna behålls i målarbetsboken. Det fungerar bara när den ursprungliga arbetsboken inte innehåller makron.

### **Lägger till överbelastning Workbook.Copy (Arbetsbok, CopyOptions) metod.**

Kopierar arbetsbok med alternativ.

### **Lägger till WarningType.InvalidAutoFilterRange enum.**

Representerar varningstypen att intervallet inte kunde autofiltreras.

### **Lägger till egenskapen Chart.DisplayNaAsBlank.**

Indikerar om #N/A visas som tomt värde.

### **Lägger till CrossType.Minimum enum.**

Representerar axelkorset vid minimivärdet.

### **Lägger till egenskapen XlsbSaveOptions.ExportAllColumnIndex.**

Anger om kolumnindex för alla celler exporteras.
