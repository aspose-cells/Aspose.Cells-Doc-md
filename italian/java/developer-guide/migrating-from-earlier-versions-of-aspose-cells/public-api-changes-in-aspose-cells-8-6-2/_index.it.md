---
title: Modifiche alle API pubbliche in Aspose.Cells 8.6.2
type: docs
weight: 220
url: /it/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.6.1 alla 8.6.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il richiamo con Smart Markers**
Questo rilascio dell'API Aspose.Cells for Java ha esposto il campo WorkbookDesigner.CallBack e l'interfaccia ISmartMarkerCallBack che insieme consentono di ricevere le notifiche sul riferimento della cella e/o smart marker in elaborazione. Il seguente codice mostra l'utilizzo dell'interfaccia ISmartMarkerCallBack per definire una nuova classe che gestisce il richiamo per il metodo WorkbookDesigner.process. 

**Java**

{{< highlight csharp >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

Il resto del processo include il caricamento del foglio di calcolo del designer contenente gli Smart Markers con WorkbookDesigner o la creazione di uno da zero e il suo utilizzo impostando la sorgente dati. Tuttavia, per abilitare le notifiche, è necessario impostare la proprietà WorkbookDesigner.CallBack prima di chiamare il metodo WorkbookDesigner.process come mostrato di seguito.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Metodo Chart.toPdf Aggiunto**
Aspose.Cells for Java 8.6.2 ha esposto il metodo Chart.toPdf che può essere utilizzato per renderizzare direttamente la forma del grafico nel formato PDF. Il metodo accetta attualmente un parametro di tipo String come percorso del file per memorizzare il file risultante su disco.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Aggiunto il metodo Workbook.removeUnusedStyles**
Aspose.Cells for Java 8.6.2 ha esposto il metodo Workbook.removeUnusedStyles che può essere utilizzato per rimuovere tutti gli oggetti di stile inutilizzati dalla raccolta degli stili. 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Aggiunta la proprietà Cells.Style**
La proprietà Cells.Style può essere utilizzata per accedere allo stile per il foglio di lavoro che rappresenta lo stile predefinito.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Eventi aggiunti per GridWeb**
Aspose.Cells.GridWeb per Java 8.6.2 ha esposto i seguenti due nuovi eventi.

1. AjaxCallFinished: Si attiva quando l'aggiornamento AJAX del controllo è terminato. (EnableAJAX dovrebbe essere impostato su true).
1. CellModifiedOnAjax: Viene attivato quando la cella viene modificata in una chiamata AJAX.
{{< app/cells/assistant language="java" >}}
