---
title: Pubblico API Modifiche Aspose.Cells 8.3.0
type: docs
weight: 110
url: /it/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.2.2 alla 8.3.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà WorkbookSettings.AutoRecover aggiunto**
Il getter/setter per la proprietà AutoRecover è stato aggiunto alla classe WorkbookSettings per consentire agli sviluppatori di ottenere/impostare l'opzione di ripristino automatico per i fogli di calcolo nelle loro applicazioni.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo[Impostazione del ripristino automatico del foglio di calcolo](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) per maggiori informazioni.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Proprietà WorkbookSettings.CrashSave aggiunto**
Il getter/setter per la proprietà CrashSave è stato aggiunto alla classe WorkbookSettings. La proprietà Boolean type indica se l'applicazione ha salvato per ultimo il file della cartella di lavoro dopo un arresto anomalo.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Proprietà WorkbookSettings.DataExtractLoad Aggiunta**
I getter/setter per la proprietà DataExtractLoad sono stati aggiunti alla classe WorkbookSettings per consentire agli sviluppatori di ottenere/impostare le informazioni relative all'ultimo ripristino. Se la proprietà DataExtractLoad restituisce true, ciò indica che il ripristino dei dati è stato eseguito sul file della cartella di lavoro.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Proprietà WorkbookSettings.RepairLoad Aggiunto**
getter/setter per la proprietà RepairLoad sono stati aggiunti alla classe WorkbookSettings. La proprietà di tipo booleano indica se il foglio di calcolo è stato riparato nell'ultima sessione di caricamento con l'applicazione Excel.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Proprietà TxtLoadOptions.KeepExactFormat Aggiunta**
La proprietà KeepExactFormat è stata aggiunta alla classe TxtLoadOptions che indica se la formattazione esatta deve essere mantenuta per il valore della cella quando la stringa/testo viene convertita in numeri o DateTime. Questa proprietà è stata aggiunta per corrispondere al comportamento dell'applicazione MS Excel per il caricamento di valori DateTime o numerici dai file CSV. Per simulare il comportamento di MS Excel, imposta la proprietà KeepExactFormat su false, mentre il valore predefinito è true, quindi il valore della cella verrà formattato come la stringa nel file CSV.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Proprietà Shape.Id aggiunta**
La v8.3.0 ha aggiunto il getter/setter per la proprietà Shape.Id al fine di identificare in modo univoco ogni oggetto forma in un dato foglio di calcolo. Questa nuova proprietà aiuta anche a identificare in modo univoco gli oggetti del grafico in un foglio di calcolo, come illustrato di seguito.

**Java**

{{< highlight "csharp" >}}

 Libro della cartella di lavoro = new Cartella di lavoro("sample.xlsx");

Grafici ChartCollection = book.getWorksheets().get(0).getCharts();

 for(int indice = 0; indice<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Metodo PlotArea.setPositionAuto Aggiunto**
Il metodo setPositionAuto è stato aggiunto alla classe PlotArea che aiuta a impostare l'area del tracciato del grafico in modalità automatica.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
