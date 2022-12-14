---
title: Aspose.Cells för .NET 22.12 Release Notes
type: docs
weight: 1
url: /sv/net/aspose-cells-for-net-22-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 22.12](https://www.nuget.org/packages/Aspose.Cells/22.12.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42315|Stöd för crtx-filer - tillämpa anpassade diagrammallar|
|CELLSNET-47895|Bilder förvrängs i Excel till PDF/HTML-rendering|
|CELLSNET-47946|Bildrotationseffekten visas inte korrekt i pdf/html|
|CELLSNET-47947|Den rektangulära boxrotationseffekten i grafikgruppen visas inte korrekt i pdf/html|
|CELLSNET-52126|Vissa former ändras efter konvertering av Excel-fil till PDF|
|CELLSNET-52197|Rutorna ändrades vid konvertering av XLSX-dokument till PDF|
|CELLSNET-52330|Ritningsformer renderade inte bra i HTML|
|CELLSNET-50042| Det definierade namnet ändras efter att ha sparats på nytt|
|CELLSNET-52270|YEARFRAC Funktionen är inte korrekt beräknad|
|CELLSNET-52305|MMULT med OFFSET beräknas inte korrekt|
|CELLSNET-52307|Bruten länkformel returnerar 0 istället för #REF!|
|CELLSNET-52325| Workbook.CalculateFormula hänger sig under vissa omständigheter|
|CELLSNET-52387|Cell referenser till tabeller resulterar i #REF-fel efter borttagning av kolumner|
|CELLSNET-52290|Sjökortsaxeln fångas inte korrekt|
|CELLSNET-52301|XLSX-diagram till bild: Anpassade kombinationsdiagramstaplar felaktigt återgivna|
|CELLSNET-52336|Histogramdiagram renderas inte korrekt i XLSX till HTML/PDF-konvertering|
|CELLSNET-52292|Text visas på fel sida i utdata-PDF - Excel till PDF-konvertering|
|CELLSNET-52367|AutofitRows resulterar i klippt text i PDF-konverteringsutdata|
|CELLSNET-52242|Förälder-barn-hierarkin är felaktig när Excel konverteras till JSON och vice versa|
|CELLSNET-52281|Json header kan inte ignoreras|
|CELLSNET-52289|Talformatet går förlorat vid konvertering av html till excel|
|CELLSNET-52298|Alternativet AutoSort är aktiverat för pivotfältet när XLSX sparas igen|
|CELLSNET-52299| HasRevisions-attributet är felaktigt efter att ha sparat en arbetsbok|
|CELLSNET-52332|Siffror visas som '#' eller vetenskapligt nummer vid konvertering till html|
|CELLSNET-52338| Utdata-HTML är icke-deterministisk|
|CELLSNET-52344|Hyperlänkar saknas i HTML till JSON-konvertering|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

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
