---
title: Modifiche dell API pubblica in Aspose.Cells 8.3.0
type: docs
weight: 100
url: /it/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.2.2 alla 8.3.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà AutoRecover di WorkbookSettings aggiunta**
La nuova proprietà AutoRecover è stata aggiunta alla classe WorkbookSettings per consentire agli sviluppatori di impostare l'opzione di auto-recovery per i fogli di calcolo nelle loro applicazioni.

{{% alert color="primary" %}} 

Si prega di consultare l'articolo [Impostazione del ripristino automatico del foglio di calcolo] (http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) per ulteriori informazioni.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Proprietà CrashSave di WorkbookSettings aggiunta**
Una proprietà di tipo Boolean CrashSave è stata aggiunta alla classe WorkbookSettings che indica se l'applicazione ha salvato l'ultimo file di lavoro dopo un arresto anomalo.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Proprietà DataExtractLoad di WorkbookSettings aggiunta**
La proprietà DataExtractLoad è stata aggiunta alla classe WorkbookSettings per consentire agli sviluppatori di ottenere informazioni riguardanti l'ultimo recupero. Se la proprietà DataExtractLoad restituisce true, ciò indica che il recupero dei dati è stato eseguito sul foglio di calcolo.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Proprietà RepairLoad di WorkbookSettings aggiunta**
La proprietà RepairLoad indica se il foglio di calcolo è stato riparato nell'ultimo caricamento con l'applicazione Excel.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Proprietà KeepExactFormat di TxtLoadOptions aggiunta**
La proprietà KeepExactFormat è stata aggiunta alla classe TxtLoadOptions e indica se formattazione esatta deve essere mantenuta per il valore della cella quando il testo viene convertito in numeri o DateTime. Questa proprietà è stata aggiunta per corrispondere al comportamento dell'applicazione MS Excel per il caricamento di valori DateTime o numerici da file CSV. Per simulare il comportamento di MS Excel, imposta la proprietà KeepExactFormat su false, mentre il valore predefinito è true in modo che il valore della cella sia formattato come stringa nel file CSV.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Proprietà Id di Shape aggiunta**
La proprietà Id è stata aggiunta alla classe Shape per identificare univocamente ciascun oggetto forma in un determinato foglio di calcolo. Questa nuova proprietà aiuta anche nell'identificare gli oggetti grafico in un foglio di calcolo come dimostrato di seguito.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Metodo SetPositionAuto di PlotArea aggiunto**
Il metodo SetPositionAuto è stato aggiunto alla classe PlotArea che aiuta a impostare l'area del grafico in modalità automatica.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
