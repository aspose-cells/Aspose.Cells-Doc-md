---
title: Offentliga API-ändringar i Aspose.Cells 8.3.0
type: docs
weight: 110
url: /sv/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.2.2 till 8.3.0 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Lade till API:er**
### **Property WorkbookSettings.AutoRecover tillagd**
Getter/setter för egenskapen AutoRecover har lagts till i WorkbookSettings-klassen för att göra det möjligt för utvecklare att få/ställa in alternativet Auto-Recover för kalkylbladen i sina applikationer.

{{% alert color="primary" %}} 

 Vänligen kontrollera artikeln[Ställa in automatisk återställning för kalkylblad](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) för mer information.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Property WorkbookSettings.CrashSave tillagd**
Getter/setter för egenskapen CrashSave har lagts till i klassen WorkbookSettings. Egenskapen boolesk typ anger om programmet senast sparade arbetsboksfilen efter en krasch.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Property WorkbookSettings.DataExtractLoad tillagd**
Getter/setter för egenskapen DataExtractLoad har lagts till i WorkbookSettings-klassen för att utvecklarna ska kunna hämta/ställa in informationen om den senaste återställningen. Om egenskapen DataExtractLoad returnerar true indikerar det att dataåterställningen har utförts på arbetsboksfilen.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Property WorkbookSettings.RepairLoad tillagd**
Getter/setter för egenskapen RepairLoad har lagts till i klassen WorkbookSettings. Egenskapen boolesk typ indikerar om kalkylarket har reparerats under den senaste laddningssessionen med Excel-applikationen.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Egenskapen TxtLoadOptions.KeepExactFormat har lagts till**
Egenskapen KeepExactFormat har lagts till i klassen TxtLoadOptions som anger om den exakta formateringen ska behållas för cellvärdet när sträng/text konverteras till siffror eller DateTime. Den här egenskapen har lagts till för att matcha beteendet hos MS Excel-applikationen för att ladda DateTime eller numeriska värden från CSV-filer. För att simulera MS Excels beteende, ställ in egenskapen KeepExactFormat på false, medan standardvärdet är sant så att cellvärdet formateras som strängen i CSV-filen.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Property Shape.Id tillagd**
V8.3.0 har lagt till getter/setter för egenskapen Shape.Id för att unikt identifiera varje formobjekt i ett givet kalkylblad. Den här nya egenskapen hjälper också till att unikt identifiera diagramobjekt i ett kalkylblad som visas nedan.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection diagram = book.getWorksheets().get(0).getCharts();

 for(int index = 0; index<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Metod PlotArea.setPositionAuto tillagd**
Metoden setPositionAuto har lagts till i klassen PlotArea som hjälper till att ställa in diagrammets plotområde till automatiskt läge.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
