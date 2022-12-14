---
title: Aspose.Cells för Android via Java 22.12 Release Notes
type: docs
weight: 1
url: /sv/java/aspose-cells-for-android-via-java-22-12-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för Android via Java 22.12.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44890|stöd importfil med openpassword för GridWeb|
|CELLSJAVA-43645|Attributet "3-D-format" för rektangeln renderas inte korrekt|
|CELLSJAVA-44936|Ställ in diagrambild (PNG) DPI-inställningar|
|CELLSJAVA-44937|Ställ in diagrambild (JPG) DPI-inställningar|
|CELLSJAVA-44998|Dubbla citattecken som orsakar inline stil misslyckades i HTML|
|CELLSJAVA-44884| Listnummer är felaktiga efter konvertering av XLSX till HTML eller PDF|
|CELLSJAVA-44883|Arbetsboken som innehåller pivottabellen skadas efter bearbetning av pivottabellen i den|
|CELLSJAVA-44879|Det formaterade resultatet för GridWeb skilde sig från Cell.DisplayStringValue|
|CELLSJAVA-44327|Kanter och färre linjer visas i svartvita pajskivor i diagram till bildrendering|
|CELLSJAVA-44853|Data om x-axelns vinkel är inte samma som Excel i diagram till bild-rendering|
|CELLSJAVA-44854|Data på y-axelsteget är inte samma som Excel i diagram-till-bild-rendering|
|CELLSJAVA-44904|Problem vid rendering av Excel-diagram till JPG-konvertering|
|CELLSJAVA-44850|När du importerar en XLT-fil, visas inte texten helt med de senaste demos med senaste Aspose.Cells.GridWeb-versionen med senaste resursfiler|
|CELLSJAVA-44857|När du använder versionen Aspose.Cells.GridWeb för Java v22.8 med de senaste resursfilerna för att öppna ett Excel-dokument, skiljer sig effekten av cellerna från originaldokumentet|
|CELLSJAVA-44903|SVG-återgivningen fungerar inte som förväntat|
|CELLSJAVA-44909| När flera rader är fetstilade verkar det svämma över till de andra raderna i onödan|
|CELLSJAVA-44888|"+" och "-" försvann efter konvertering - Excel till HTML-rendering|
|CELLSJAVA-44775|Diagrametiketter överlappade i diagram till bildrendering|
|CELLSJAVA-44882|Tabell-till-bild-rendering - En av etiketterna finns inuti munkdiagrammet|
|CELLSJAVA-44943|XLSX till PDF: Diagrametiketter renderade inte korrekt|
|CELLSJAVA-44928|XLS till PDF: Otillräcklig data för en bild|
|CELLSJAVA-44910|Konvertera Excel till HTML resulterar i tusentals liknande små bilder|
|CELLSJAVA-44944|Ändra storlek på tabeller ändra formateringen av celler|
|CELLSJAVA-44948| Bilder kan inte visas i arket när HTML konverteras till Excel|
|CELLSJAVA-44970|Optimera skuggeffekten|
|CELLSJAVA-44967|Diagram getDataLabels().getText() som returnerar ett annat värde i v22.6.0 och senare versioner|
|CELLSJAVA-44969|Konvertera Excel till HTML, dataetiketterna visar fel|
|CELLSJAVA-44949|Transparensen ändrades när Excel-intervall infogades som bild med annat format i PowerPoint-bilden|
|CELLSJAVA-44985|Excel till HTML-konvertering - grafförklaringen visas inte och plotområdet är trunkerat|
|CELLSJAVA-44952|Problem med DataBar.toImage-metoden angående bredd|
|CELLSJAVA-44986|De importerade bilderna är inte justerade i en linje när bilderna är i Div|
|CELLSJAVA-44987|Vissa bilder täcks av andra när html laddas|
|CELLSJAVA-44988|Text roteras inte när html laddas|
|CELLSJAVA-44989|Teckensnittsinställningar i div går förlorade när html laddas|
|CELLSJAVA-44997|Data och formatering förlorade i HTML till Excel-konvertering|
|CELLSJAVA-44999| Aspose.Cells Anpassade globaliseringsinställningar fungerar inte för större delen av pivottabellen|
|CELLSJAVA-44898|Att läsa från GZIPInputStream ger ibland falskt "Filen är skadad" fel i 22.7 och nyare versioner|
|CELLSJAVA-44881|Undantag "java.lang.ArrayIndexOutOfBoundsException: 15070" vid inläsning av en XLS-fil|
|CELLSJAVA-44908|Undantag "java.lang.OutOfMemoryError: Java heap space" vid laddning av stora XLSB-filer|
|CELLSJAVA-44929|Regression: "java.lang.NullPointerException" på Workbook.calculateFormula()|
|CELLSJAVA-44927|Undantag "java.lang.IndexOutOfBoundsException: Index: 5, Storlek: 5" vid konvertering av Excel-fil till HTML|
|CELLSJAVA-44939|Fel "java.lang.StringIndexOutOfBoundsException: Strängindex utanför intervallet: 0" vid försök att läsa en Excel-fil|


## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för Android via Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Ändrade gränsen för att flytta celler ut från arket för att infoga rader**

I gamla versioner, om det finns celler som har formateringsinställningar men som inte har något värde? och som kommer att flyttas ut från arket, är infogning inte tillåten. Från 22.10 är infogning tillåten för en sådan typ av situation och sådant beteende är samma sak med ms excel nu.

### **Lägger till klassen DataModelConnection**

Anger en datamodellanslutning.

### **Lägger till metoder för Chart.ChangeTemplate(byte[]).**

Ändra diagramtyp med förinställd mallfil.

### **Lägger till ChartCollection.Add(byte[] data, sträng dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Lägger till diagram med förinställd mallfil.

### **Lägger till egenskapen Cell.IsDynamicArrayFormula**

Anger om cellens formel är dynamisk matrisformel (sant) eller äldre matrisformel (falsk).

### **Föråldrade egendomen SparklineGroup.SparklineCollection och lägger till egendomen SparklineGroup.Sparklines**

Använd egenskapen SparklineGroup.Sparklines istället.

### **Föråldrade egendomen Worksheet.SparklineGroupCollection och lägger till egenskapen Worksheet.SparklineGroups**

Använd egenskapen Worksheet.SparklineGroups istället.

### **Lägger till enum JsonExportHyperlinkType**

Representerar typen av exporterande hyperlänk till json-filer.

### **Lägger till JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) och föråldrar metoden ExportRangeToJson(Range, ExportRangeToJsonOptions)**

Använd JsonUtility.ExportRangeToJson(Range, JsonSaveOptions) istället.

### **Lägger till egenskapen PivotTable.DataFieldHeaderName**

Hämtar och ställer in namnet på värdeområdets fälthuvud i pivottabellen.

### **Lägger till åsidosättande Range.SetStyle(Style,System.Boolean) metod**

Skriv bara över formatering som är uttryckligen inställd när flaggan är inställd

### **Lägger till egenskapen PivotField.NonAutoSortDefault**

Anger om en sorteringsoperation som kommer att tillämpas på detta pivotfält är en autosorteringsoperation eller en enkel datasortering.

### **Lägger till metoden GlobalizationSettings.GetDataFieldHeaderNameOfPivotTable()**

Hämtar det lokala namnet på värdeområdesfälthuvudet i pivottabellen.

### **Lägger till egenskapen Chart.PlotVisibleCellsOnly och föråldrar egenskapen Chart.PlotVisibleCells.**

Använd egenskapen Chart.PlotVisibleCellsOnly istället.

### **Lägger till egenskapen JsonSaveOptions.ExportEmptyCells.**

Anger om tomma celler exporteras som null.

### **Lägger till egenskapen JsonSaveOptions.ExportHyperlinkType.**

Representerar typen av exporterande hyperlänk till json.

### **Lägger till egenskapen JsonSaveOptions.ExportNestedStructure.**

Exporterad som Json-struktur för överordnad och underordnad hierarki.

### **Lägger till egenskapen JsonSaveOptions.SkipEmptyRows.**

Anger om tomma rader hoppar över.

### **Tar bort föråldrad SheetRender.GetPageSize(System.Int32) metod**

Använd SheetRender.GetPageSizeInch(System.Int32) istället.

### **Tar bort föråldrad WorkbookRender.GetPageSize(System.Int32) metod**

Använd WorkbookRender.GetPageSizeInch(System.Int32) istället.

### **Tar bort föråldrade AutoShapeType.TextWave3 och AutoShapeType.TextWave4 enum**

Använd UseAutoShape.TextDoubleWave1 och UseAutoShape.TextDoubleWave2 istället.

