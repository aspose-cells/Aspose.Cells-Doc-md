---
title: Offentliga API ändringar i Aspose.Cells 8.3.0
type: docs
weight: 100
url: /sv/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.2.2 till 8.3.0 som kan vara av intresse för modul/tillämpningsutvecklare.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till WorkbookSettings.AutoRecover Egenskap**
Den nya egenskapen AutoRecover har lagts till WorkbookSettings-klassen för att möjliggöra för utvecklare att ställa in alternativet för automatisk återställning för kalkylbladen i deras applikationer.

{{% alert color="primary" %}} 

Kontrollera artikeln [Ställa in kalkylbladets automatiska återställning](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) för mer information.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Lade till WorkbookSettings.CrashSave Egenskap**
En boolesk typ egenskap CrashSave har lagts till WorkbookSettings-klassen som indikerar om programmet senast sparade arbetsbokfilen efter en krasch.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Lade till WorkbookSettings.DataExtractLoad Egenskap**
Egenskapen DataExtractLoad har lagts till WorkbookSettings-klassen för att tillåta utvecklare att få information om den senaste återställningen. Om egenskapen DataExtractLoad returnerar sant så indikerar det att dataåterställningen har utförts på kalkylarket.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Lade till WorkbookSettings.RepairLoad Egenskap**
Egenskapen RepairLoad indikerar om kalkylarket har reparerats vid senaste laddningen med Excel-applikationen.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Tillagd TxtLoadOptions.KeepExactFormat Egenskap**
Egenskapen KeepExactFormat har lagts till i TxtLoadOptions-klassen som indikerar om exakt formatering ska behållas för cellvärdet när sträng/text konverteras till nummer eller datum. Denna egenskap har lagts till för att matcha beteendet hos MS Excel-applikationen för att ladda in datum eller numeriska värden från CSV-filer. För att simulera MS Excels beteende, sätt KeepExactFormat-egenskapen till falskt, medan standardvärdet är sant så att cellvärdet formateras som strängen i CSV-filen.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Tillagd Shape.Id Egenskap**
Egenskapen Id har lagts till i Shape-klassen för att unikt identifiera varje formobjekt i ett givet kalkylblad. Denna nya egenskap hjälper också till att identifiera diagramobjekt i ett kalkylblad, som demonstrerats nedan.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Tillagd PlotArea.SetPositionAuto Metod**
Metoden SetPositionAuto har lagts till i PlotArea-klassen som hjälper till att ställa in diagrammets område till automatläge.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
