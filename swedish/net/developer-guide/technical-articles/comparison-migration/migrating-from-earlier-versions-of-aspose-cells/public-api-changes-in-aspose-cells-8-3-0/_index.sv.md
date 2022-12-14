---
title: Offentliga API-ändringar i Aspose.Cells 8.3.0
type: docs
weight: 100
url: /sv/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.2.2 till 8.3.0 som kan vara av intresse för modul-/applikationsutvecklare.

{{% /alert %}} 
## **Lade till API:er**
### **Property WorkbookSettings.AutoRecover tillagd**
Den nya egenskapen AutoRecover har lagts till i WorkbookSettings-klassen för att göra det möjligt för utvecklare att ställa in alternativet Auto-Recover för kalkylbladen i sina applikationer.

{{% alert color="primary" %}} 

 Vänligen kontrollera artikeln[Ställa in automatisk återställning för kalkylblad](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) för mer information.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Property WorkbookSettings.CrashSave tillagd**
En egenskap av boolesk typ CrashSave har lagts till i klassen WorkbookSettings som anger om programmet senast sparade arbetsboksfilen efter en krasch.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Property WorkbookSettings.DataExtractLoad tillagd**
Egenskapen DataExtractLoad har lagts till i WorkbookSettings-klassen för att utvecklarna ska kunna få information om den senaste återställningen. Om egenskapen DataExtractLoad returnerar true indikerar det att dataåterställningen har utförts på kalkylarket.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Property WorkbookSettings.RepairLoad tillagd**
Egenskapen RepairLoad indikerar om kalkylarket har reparerats vid den senaste laddningen med Excel-applikationen.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Egenskapen TxtLoadOptions.KeepExactFormat har lagts till**
Egenskapen KeepExactFormat har lagts till i klassen TxtLoadOptions som anger om den exakta formateringen ska behållas för cellvärdet när sträng/text konverteras till siffror eller DateTime. Den här egenskapen har lagts till för att matcha beteendet hos MS Excel-applikationen för att ladda DateTime eller numeriska värden från CSV-filer. För att simulera MS Excels beteende, ställ in egenskapen KeepExactFormat på false, medan standardvärdet är sant så att cellvärdet formateras som strängen i CSV-filen.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Property Shape.Id tillagd**
Egenskapen Id har lagts till i Shape-klassen för att unikt identifiera varje formobjekt i ett givet kalkylblad. Den här nya egenskapen hjälper också till att identifiera diagramobjekt i ett kalkylblad som visas nedan.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Metod PlotArea.SetPositionAuto tillagd**
Metoden SetPositionAuto har lagts till i klassen PlotArea som hjälper till att ställa in diagrammets plotområde till automatiskt läge.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
