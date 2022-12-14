---
title: Aspose.Cells för PHP via Java 22.12 Release Notes
type: docs
weight: 1
url: /sv/php-java/aspose-cells-for-php-via-java-22-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för PHP via Java 22.12](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.12/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43645|Attributet "3-D-format" för rektangeln renderas inte korrekt|
|CELLSJAVA-44936|Ställ in diagrambild (PNG) DPI-inställningar|
|CELLSJAVA-44937|Ställ in diagrambild (JPG) DPI-inställningar|
|CELLSJAVA-44998|Dubbla citattecken som orsakar inline stil misslyckades i HTML|
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

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

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