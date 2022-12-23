---
title: Aspose.Cells for Java 20.9 Release Notes
type: docs
weight: 7
url: /sv/java/aspose-cells-for-java-20-9-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.9](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.9/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-40792|Pivottabellen skapas inte för ODS-filen|Ny funktion|
|CELLSJAVA-43263|SmartMarker-problem när en cell är inställd på fyllningsfärg och villkorlig formatering|Insekt|
|CELLSJAVA-43269|Kan inte få värde från pivotark|Insekt|
|CELLSJAVA-43272|Bilden krymper efter inställning av skalbar bredd|Insekt|
|CELLSJAVA-43280|Filterproblem efter uppdateringen av pivottabellen|Insekt|
|CELLSJAVA-43281|Uppdatera pivottabellproblem|Insekt|
|CELLSJAVA-43285|Statiska filter går förlorade efter uppdatering av pivottabellen|Insekt|
|CELLSJAVA-43288|Resultatet XLSB filen är korrupt när filen sparas till XLSB|Insekt|
|CELLSJAVA-43289|Filterproblem efter uppdatering av pivottabellen|Insekt|
|CELLSJAVA-43293|Problem med filteralternativ efter PivotTable.refreshData()|Insekt|
|CELLSJAVA-43279|Värden hämtas inte korrekt med getStringValue()|Insekt|
|CELLSJAVA-43291|Rutnätsinnehåll är inte synligt|Insekt|
|CELLSJAVA-43037|Teckensnittsproblem vid konvertering av PDF|Insekt|
|CELLSJAVA-43249|Utskriftsproblem när du använder fysiska skrivare, XPS och PDF skrivare|Insekt|
|CELLSJAVA-43254|Teckensnittsskillnad vid konvertering av kalkylblad till bild|Insekt|
|CELLSJAVA-43266|Java-versionen stöder inte inläsning av teckensnitt från den aktuella användarens teckensnittsmapp som standard|Insekt|
|CELLSJAVA-43268|Excel till TIFF rendering - några av värdena ersätts med " #" tecken|Insekt|
|CELLSJAVA-43275|Aspose.Cell for Java 20.8 com.aspose.cells.CellsException: Fel för ZipFile|Insekt|
|CELLSJAVA-43277|Problem med höjd breddförhållande|Insekt|
|CELLSJAVA-43245|Kombinationsdiagrammet visas inte korrekt efter konvertering av Excel-fil till PDF|Insekt|
|CELLSJAVA-43276|Problem med radbrytning vid konvertering av XLSX till PDF|Insekt|
|CELLSJAVA-43261|SmartMarker: när du använder group:merge med Number Format Percentage är det expanderande resultatet fel|Insekt|
|CELLSJAVA-43265|Kan inte ladda XLSX-filen|Insekt|
|CELLSJAVA-43270|Duplicering av innehåll (inbäddat Word) vid kopiering av arbetsblad|Insekt|
|CELLSJAVA-43271|WaterFall Chart bevarar inte SetAsTotal Property|Insekt|
|CELLSJAVA-43287|Att lägga till autofilter förstör arbetsboken|Insekt|
|CELLSJAVA-43290|Bearbetning returneras inte när XML Spreadsheet 2003-fil sparas i MS Excel-arbetsboksformat|Insekt|
|CELLSJAVA-43267|Undantag "java.lang.NullPointerException" vid beräkning av pivottabell i arket|Undantag|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen AbstractCalculationEngine.ProcessBuiltInFunctions**

 För prestanda och användarens bekvämlighetsskäl lägger vi till den här egenskapen och gör dess standardvärde som falskt så att användaren kan koncentrera sig på de funktioner som inte har stöds av den inbyggda motorn. Om användarens befintliga implementering av AbstractCalculationEngine ändrade vissa inbyggda funktioners beräkning, bör användaren åsidosätta denna egenskap för att göra den till**Sann** från**20.9**.

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

Anger om makron behålls i målarbetsboken. Det fungerar bara när den ursprungliga arbetsboken inte innehåller makron.

### **Lägger till överbelastning Workbook.Copy (Arbetsbok, CopyOptions) metod.**

Kopierar arbetsbok med alternativ.

### **Lägger till WarningType.InvalidAutoFilterRange enum.**

Representerar varningstypen att intervallet inte kunde filtreras automatiskt.

### **Lägger till egenskapen Chart.DisplayNaAsBlank.**

Indikerar om #N/A visas som tomt värde.

### **Lägger till CrossType.Minimum enum.**

Representerar axelkorset vid minimivärdet.

### **Lägger till egenskapen XlsbSaveOptions.ExportAllColumnIndex.**

Anger om export kolumnindex för alla celler när XLSB-filer sparas.
