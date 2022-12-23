---
title: Pubblico API Modifiche Aspose.Cells 8.3.0
type: docs
weight: 100
url: /it/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.2.2 alla 8.3.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà WorkbookSettings.AutoRecover aggiunto**
La nuova proprietà AutoRecover è stata aggiunta alla classe WorkbookSettings per consentire agli sviluppatori di impostare l'opzione di Auto-Recovery per i fogli di calcolo nelle loro applicazioni.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Impostazione del ripristino automatico del foglio di calcolo](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) per maggiori informazioni.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Proprietà WorkbookSettings.CrashSave aggiunto**
Alla classe WorkbookSettings è stata aggiunta una proprietà di tipo booleano CrashSave che indica se l'applicazione ha salvato per ultimo il file della cartella di lavoro dopo un arresto anomalo.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Proprietà WorkbookSettings.DataExtractLoad Aggiunta**
La proprietà DataExtractLoad è stata aggiunta alla classe WorkbookSettings per consentire agli sviluppatori di ottenere le informazioni relative all'ultimo ripristino. Se la proprietà DataExtractLoad restituisce true, ciò indica che il ripristino dei dati è stato eseguito sul foglio di calcolo.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Proprietà WorkbookSettings.RepairLoad Aggiunto**
La proprietà RepairLoad indica se il foglio di calcolo è stato riparato nell'ultimo caricamento con l'applicazione Excel.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Proprietà TxtLoadOptions.KeepExactFormat Aggiunta**
La proprietà KeepExactFormat è stata aggiunta alla classe TxtLoadOptions che indica se la formattazione esatta deve essere mantenuta per il valore della cella quando la stringa/testo viene convertita in numeri o DateTime. Questa proprietà è stata aggiunta per corrispondere al comportamento dell'applicazione MS Excel per il caricamento di valori DateTime o numerici dai file CSV. Per simulare il comportamento di MS Excel, imposta la proprietà KeepExactFormat su false, mentre il valore predefinito è true, quindi il valore della cella verrà formattato come la stringa nel file CSV.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Proprietà Shape.Id aggiunta**
La proprietà Id è stata aggiunta alla classe Shape per identificare in modo univoco ogni oggetto forma in un determinato foglio di calcolo. Questa nuova proprietà aiuta anche a identificare gli oggetti del grafico in un foglio di calcolo, come illustrato di seguito.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Metodo PlotArea.SetPositionAuto Aggiunto**
Il metodo SetPositionAuto è stato aggiunto alla classe PlotArea che aiuta a impostare l'area del tracciato del grafico in modalità automatica.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
