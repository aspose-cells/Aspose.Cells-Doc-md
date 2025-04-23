---
title: Cambiamenti dell API pubblica in Aspose.Cells 16.12.0
type: docs
weight: 370
url: /it/java/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Oggetti filtro al momento del caricamento**
Aspose.Cells 16.12.0 ha esposto la classe LoadFilter insieme alla proprietà LoadOptions.LoadFilter che insieme possono controllare il tipo di dati da caricare durante l'inizializzazione di un'istanza di Workbook da un file modello.

Ecco uno scenario di utilizzo semplice per caricare solo le proprietà del documento da un file modello.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Il seguente snippet carica tutto da un foglio di calcolo esistente tranne i grafici.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}

Il seguente codice carica solo i dati delle celle (insieme alle formule) e la formattazione da un foglio di calcolo esistente.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions class

LoadOptions options = new LoadOptions();

//Create an instance of LoadFilter class

//Select to load document properties by passing parameter to the constructor

LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);

//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above

options.setLoadFilter(filter);

//Load a template file by passing file path as well as instance of LoadOptions class

Workbook book = new Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}
### **Aggiunta enumerazione FileFormatType.OTS**
Aspose.Cells 16.12.0 ha aggiunto l'elemento OTS all'enumerazione FileFormatType per rilevare il formato dei file OTS.

Il seguente snippet fa uso di FileFormatType.OTS.

**Java**

{{< highlight csharp >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Aggiunta proprietà BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 ha aggiunto la proprietà ScaleCrop alla classe BuiltInDocumentPropertyCollection. ScaleCrop indica la modalità di visualizzazione dell'anteprima del documento. Impostando questo elemento su true abilita il ridimensionamento dell'anteprima del documento come da display, mentre impostandolo su false abilita il ritaglio dell'anteprima del documento per mostrare la sezione che si adatta al display.
### **Aggiunta proprietà BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 ha anche esposto la proprietà LinksUpToDate per la classe BuiltInDocumentPropertyCollection. La proprietà LinksUpToDate indica se i collegamenti ipertestuali in un documento sono aggiornati. 
### **Metodo Workbook.exportXml aggiunto**
Aspose.Cells 16.12.0 ha esposto il metodo Workbook.exportXml che consente di memorizzare i dati della mappa XML nel percorso del file specificato. Il metodo Workbook.exportXml accetta 2 parametri in cui il primo parametro di tipo stringa dovrebbe essere il nome della mappa XML e il secondo parametro dovrebbe essere il percorso del file in cui memorizzare i dati XML.
### **Metodo WorksheetCollection.createRange aggiunto**
Aspose.Cells 16.12.0 ha aggiunto il metodo WorksheetCollection.createRange che consente di creare un intervallo in base a un indirizzo (riferimento area cella) e all'indice del foglio di lavoro.

Il seguente snippet utilizza il metodo WorksheetCollection.createRange per creare un intervallo di celle che vanno da A1 a A2 nel primo (predefinito) foglio di lavoro.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **API deprecate**
### **Proprietà LoadOptions.LoadDataOptions deprecata**
Si prega di utilizzare la proprietà LoadOptions.LoadFilter come alternativa.
### **Proprietà LoadOptions.LoadDataFilterOptions deprecata**
Si prega di utilizzare la proprietà LoadOptions.LoadFilter al suo posto.
### **Proprietà LoadOptions.OnlyLoadDocumentProperties deprecata**
Si prega di utilizzare la proprietà LoadOptions.LoadFilter come alternativa.
### **Proprietà LoadOptions.LoadDataAndFormatting deprecata**
Si prega di utilizzare la proprietà LoadOptions.LoadFilter al suo posto.

{{% alert color="primary" %}} 

Sono stati condivisi snippet di codice per tutte le API deprecate.

{{% /alert %}}
## **API eliminate**
### **Proprietà DataLabels.Rotation eliminata**
Si prega di utilizzare la proprietà DataLabels.RotationAngle al suo posto.
### **Proprietà Title.Rotation eliminata**
Si prega di utilizzare la proprietà Title.RotationAngle come alternativa.
### **Proprietà Deleted DataLabels.Background**
Si consiglia di utilizzare la proprietà DataLabels.BackgroundMode invece.
### **Proprietà Deleted DisplayUnitLabel.Rotation**
Si prega di considerare l'utilizzo della proprietà DisplayUnitLabel.RotationAngle per raggiungere lo stesso obiettivo.
### **Metodo Deleted Title.getCharacters**
Si prega di utilizzare il metodo Title.characters invece.
{{< app/cells/assistant language="java" >}}
