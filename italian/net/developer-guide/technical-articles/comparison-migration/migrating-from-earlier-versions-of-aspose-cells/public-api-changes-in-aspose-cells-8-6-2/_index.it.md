---
title: Modifiche alle API pubbliche in Aspose.Cells 8.6.2
type: docs
weight: 210
url: /it/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.6.1 alla 8.6.2 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per il richiamo con Smart Markers**
Questa versione di Aspose.Cells for .NET API ha esposto la proprietà WorkbookDesigner.CallBack e l'interfaccia ISmartMarkerCallBack che insieme permettono di [ottenere le notifiche sul riferimento della cella e/o smart marker in fase di elaborazione](/cells/it/net/getting-notifications-while-merging-data-with-smart-markers/). Il seguente codice dimostra l'uso dell'interfaccia ISmartMarkerCallBack per definire una nuova classe che gestisce il richiamo per il metodo WorkbookDesigner.Process.

**C#**

{{< highlight csharp >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Il resto del processo include il caricamento del foglio di lavoro del designer contenente gli Smart Markers con WorkbookDesigner e il suo elaborazione impostando la fonte dei dati. Tuttavia, per abilitare le notifiche, è necessario impostare la proprietà WorkbookDesigner.CallBack prima di richiamare il metodo WorkbookDesigner.Process come dimostrato di seguito.

**C#**

{{< highlight csharp >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Aggiunto il metodo Chart.ToPdf**
Aspose.Cells for .NET 8.6.2 ha esposto il metodo Chart.ToPdf che può essere utilizzato per [rendere direttamente la forma del grafico nel formato PDF](/cells/it/net/convert-an-excel-chart-to-image/). Il suddetto metodo attualmente accetta un parametro di tipo stringa come percorso del file per memorizzare il file risultante su disco.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Aggiunto il metodo Workbook.RemoveUnusedStyles**
Aspose.Cells for .NET 8.6.2 ha esposto il metodo Workbook.RemoveUnusedStyles che può essere utilizzato per [rimuovere tutti gli oggetti Style non utilizzati dal pool di stili](/cells/it/net/remove-unused-styles-inside-the-workbook/).

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Aggiunta la proprietà Cells.Style**
La proprietà Cells.Style può essere utilizzata per accedere allo stile per il foglio di lavoro che rappresenta lo stile predefinito.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Eventi aggiunti per GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 ha esposto i seguenti due nuovi eventi.

1. AjaxCallFinished: Viene attivato quando l'aggiornamento AJAX del controllo è completato. (EnableAJAX deve essere impostato su true).
1. CellModifiedOnAjax: Viene attivato quando la cella viene modificata in una chiamata AJAX.
{{< app/cells/assistant language="csharp" >}}
