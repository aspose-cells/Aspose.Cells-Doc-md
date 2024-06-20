---
title: Modifiche dell API pubblica in Aspose.Cells 8.3.0
type: docs
weight: 110
url: /it/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.2.2 alla 8.3.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà AutoRecover di WorkbookSettings aggiunta**
Il getter/setter per la proprietà AutoRecover è stato aggiunto alla classe WorkbookSettings per consentire ai programmatori di ottenere/impostare l'opzione di auto-recupero per i fogli di calcolo delle loro applicazioni. 

{{% alert color="primary" %}} 

Si prega di controllare l'articolo [Impostazione Recupero Automatico Fogli di Calcolo](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) per ulteriori informazioni.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Proprietà CrashSave di WorkbookSettings aggiunta**
Il getter/setter per la proprietà CrashSave è stato aggiunto alla classe WorkbookSettings. La proprietà di tipo Boolean indica se l'applicazione ha salvato l'ultimo file di lavoro dopo un arresto anomalo.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Proprietà DataExtractLoad di WorkbookSettings aggiunta**
Il getter/setter per la proprietà DataExtractLoad è stato aggiunto alla classe WorkbookSettings per consentire agli sviluppatori di ottenere/impostare le informazioni relative all'ultimo recupero. Se la proprietà DataExtractLoad restituisce true, indica che il recupero dei dati è stato eseguito sul file di lavoro.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Proprietà RepairLoad di WorkbookSettings aggiunta**
Il getter/setter per la proprietà RepairLoad è stato aggiunto alla classe WorkbookSettings. La proprietà di tipo Boolean indica se il foglio di calcolo è stato riparato nell'ultima sessione di caricamento con l'applicazione Excel.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Proprietà KeepExactFormat di TxtLoadOptions aggiunta**
La proprietà KeepExactFormat è stata aggiunta alla classe TxtLoadOptions e indica se formattazione esatta deve essere mantenuta per il valore della cella quando il testo viene convertito in numeri o DateTime. Questa proprietà è stata aggiunta per corrispondere al comportamento dell'applicazione MS Excel per il caricamento di valori DateTime o numerici da file CSV. Per simulare il comportamento di MS Excel, imposta la proprietà KeepExactFormat su false, mentre il valore predefinito è true in modo che il valore della cella sia formattato come stringa nel file CSV.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Proprietà Id di Shape aggiunta**
La v8.3.0 ha aggiunto il getter/setter per la proprietà Shape.Id per identificare univocamente ciascun oggetto forma in un determinato foglio di calcolo. Questa nuova proprietà aiuta anche a identificare in modo univoco gli oggetti Chart in un foglio di calcolo come dimostrato di seguito.

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

### **Aggiunto il metodo PlotArea.setPositionAuto**
Il metodo setPositionAuto è stato aggiunto alla classe PlotArea che aiuta a impostare l'area di tracciamento del grafico in modalità automatica.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
