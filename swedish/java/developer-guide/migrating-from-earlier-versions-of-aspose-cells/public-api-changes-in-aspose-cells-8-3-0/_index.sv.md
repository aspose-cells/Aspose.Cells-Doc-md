---
title: Offentliga API ändringar i Aspose.Cells 8.3.0
type: docs
weight: 110
url: /sv/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.2.2 till 8.3.0 som kan vara av intresse för modul/tillämpningsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till WorkbookSettings.AutoRecover Egenskap**
Getter/setter har lagts till egenskapen AutoRecover till WorkbookSettings-klassen för att låta utvecklare få/sätta alternativet Auto-Recovery för kalkylblad i deras applikationer. 

{{% alert color="primary" %}} 

Se artikeln [Ställa in Auto Recovery för Kalkylblad](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) för mer information.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Lade till WorkbookSettings.CrashSave Egenskap**
Getter/setter har lagts till egenskapen CrashSave till WorkbookSettings-klassen. Egenskapen av typen Boolean indikerar om applikationen senast sparade kalkylbladsfilen efter en krasch.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Lade till WorkbookSettings.DataExtractLoad Egenskap**
Getter/setter har lagts till egenskapen DataExtractLoad till WorkbookSettings-klassen för att låta utvecklare få/sätta informationen om senaste återställningen. Om egenskapen DataExtractLoad returnerar true indikerar det att dataskrädderiet har utförts på kalkylbladsfilen.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Lade till WorkbookSettings.RepairLoad Egenskap**
Getter/setter har lagts till egenskapen RepairLoad till WorkbookSettings-klassen. Egenskapen av typen Boolean indikerar om kalkylbladet har lagats vid den senaste laddningssessionen med Excel-applikationen.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Tillagd TxtLoadOptions.KeepExactFormat Egenskap**
Egenskapen KeepExactFormat har lagts till i TxtLoadOptions-klassen som indikerar om exakt formatering ska behållas för cellvärdet när sträng/text konverteras till nummer eller datum. Denna egenskap har lagts till för att matcha beteendet hos MS Excel-applikationen för att ladda in datum eller numeriska värden från CSV-filer. För att simulera MS Excels beteende, sätt KeepExactFormat-egenskapen till falskt, medan standardvärdet är sant så att cellvärdet formateras som strängen i CSV-filen.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Tillagd Shape.Id Egenskap**
v8.3.0 har lagt till getter/setter för egenskapen Shape.Id för att unikt identifiera varje formobjekt i ett givet kalkylblad. Denna nya egenskap hjälper också till att unikt identifiera Diagramobjekt i ett kalkylblad som demonstreras nedan.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Tillagd PlotArea.setPositionAuto Metod**
Metoden setPositionAuto har lagts till PlotArea-klassen som hjälper till att ställa in diagrammets plottområde till automatiskt läge.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
