---
title: Aspose.Cells för Java 21.1 Release Notes
type: docs
weight: 12
url: /sv/java/aspose-cells-for-java-21-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 21.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.1/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43375|Kontrollera Excel VBA-lösenord|
|CELLSJAVA-43371|XLSX till PDF-konvertering hänger sig|
|CELLSJAVA-43353|Olika diagram på excel till pdf|
|CELLSJAVA-43377|Bildplaceringsproblem vid konvertering av Excel till HTML|
|CELLSJAVA-43381|DAYS funktionsberäkningsfel|
|CELLSJAVA-43342|Kombinationsdiagram kan inte visas korrekt i excel till pdf|
|CELLSJAVA-43354|Procentandelar visades inte i de små histogrammen|
|CELLSJAVA-40264|Fel med formulärkontroller eller ActiveX-kontroller när du sparar som EXCEL_97_TO_2003|
|CELLSJAVA-43372|Skadad fil skapades vid konvertering av ODS till XLSX|
|CELLSJAVA-43378|Visa som tomt ändras från sant till falskt efter kloning av arbetsboken|
|CELLSJAVA-43379|Undantag uppstod när arbetsboken sparades som HTML|
|CELLSJAVA-43376|Undantag "java.lang.ClassCastException: Överflöde i int till byte-konvertering. int värde: 144" vid inläsning av en XLSX-fil|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Föråldrad PdfSaveOptions(SaveFormat) konstruktor.**

Använd PdfSaveOptions()-konstruktorn istället.

### **Föråldrad XlsbSaveOptions(SaveFormat) konstruktor.**

Använd XlsbSaveOptions()-konstruktorn istället.

### **Föråldrad XlsSaveOptions(SaveFormat) konstruktor.**

Använd XlsSaveOptions()-konstruktorn istället.

### **Föråldrad SpreadsheetML2003SaveOptions(SaveFormat) konstruktor.**

Använd SpreadsheetML2003SaveOptions()-konstruktorn istället.

### **Lägger till metoden Chart.GetChartDataRange().**

Hämtar dataintervallskällan för diagrammet.

### **Lägger till metoden Chart.SwitchRowColumn().**

Byter rad/kolumn för diagrammets dataintervallskälla.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

Ställer in inbäddat objekt.

### **Lägger till metoden VbaProject.ValidatePassword().**

Validerar lösenordet för VBA-projektet.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColor och Series.MarkerBackgroundColor, lägger till egenskapen Marker.BackgroundColor.**

Använder Marker.BackgroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColor och Series.MarkerForegroundColor , lägger till egenskapen Marker.ForegroundColor.**

Använder Marker.ForegroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColorSetType och Series.MarkerBackgroundColorSetType , lägger till egenskapen Marker.BackgroundColorSetType.**

Använder Marker.BackgroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColorSetType och Series.MarkerForegroundColorSetType , lägger till egenskapen Marker.ForegroundColorSetType.**

Använder Marker.ForegroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerSize och Series.MarkerSize.**

Använder Marker.MarkerSize istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerStyle och Series.MarkerStyle.**

Använder Marker.MarkerStyle istället.
