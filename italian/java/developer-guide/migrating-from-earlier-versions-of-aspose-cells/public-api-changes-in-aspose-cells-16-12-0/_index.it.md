---
title: Modifiche all'API pubblica in Aspose.Cells 16.12.0
type: docs
weight: 370
url: /it/java/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtra gli oggetti al momento del caricamento**
Aspose.Cells 16.12.0 ha esposto la classe LoadFilter insieme alla proprietà LoadOptions.LoadFilter che insieme possono controllare il tipo di dati da caricare durante l'inizializzazione di un'istanza di Workbook da un file modello.

Ecco un semplice scenario di utilizzo per caricare solo le proprietà del documento da un file modello.

**Giava**

{{< highlight "csharp" >}}

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

Lo snippet seguente carica tutto da un foglio di calcolo esistente ad eccezione dei grafici.

**Giava**

{{< highlight "csharp" >}}

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

Il seguente codice carica solo i dati della cella (insieme alle formule) e la formattazione da un foglio di calcolo esistente.

**Giava**

{{< highlight "csharp" >}}

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
### **Aggiunta l'enumerazione FileFormatType.OTS**
Aspose.Cells 16.12.0 ha aggiunto la voce OTS all'enumerazione FileFormatType per rilevare il formato dei file OTS.

Il seguente frammento utilizza FileFormatType.OTS.

**Giava**

{{< highlight "csharp" >}}

 //Detect the format of the file

FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");



//Check if stream is of type OTS

if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);

{

	System.out.println("It is an OTS file");

}

{{< /highlight >}}
### **Aggiunta la proprietà BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 ha aggiunto la proprietà ScaleCrop alla classe BuiltInDocumentPropertyCollection. ScaleCrop indica la modalità di visualizzazione della miniatura del documento. L'impostazione di questo elemento su true abilita il ridimensionamento della miniatura del documento come per la visualizzazione, mentre impostandolo su false abilita il ritaglio della miniatura del documento per mostrare la sezione che si adatta alla visualizzazione.
### **Aggiunta la proprietà BuiltInDocumentPropertyCollection.LinksUpToDate**
 Aspose.Cells 16.12.0 ha inoltre esposto la proprietà LinksUpToDate per la classe BuiltInDocumentPropertyCollection. La proprietà LinksUpToDate indica se i collegamenti ipertestuali in un documento sono aggiornati.
### **Aggiunto metodo Workbook.exportXml**
Aspose.Cells 16.12.0 ha esposto il metodo Workbook.exportXml che consente di memorizzare i dati della mappa XML nel percorso del file specificato. Il metodo Workbook.exportXml accetta 2 parametri in cui il primo parametro di tipo stringa deve essere il nome della mappa XML e il secondo parametro deve essere il percorso del file in cui archiviare i dati XML.
### **Aggiunto metodo WorksheetCollection.createRange**
Aspose.Cells 16.12.0 ha aggiunto il metodo WorksheetCollection.createRange che consente di creare un intervallo basato su un indirizzo (riferimento area cella) e indice del foglio di lavoro.

Il seguente frammento utilizza il metodo WorksheetCollection.createRange per creare un intervallo di celle che si estende da A1 a A2 nel primo foglio di lavoro (predefinito).

**Giava**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access WorksheetCollection from the Workbook

WorksheetCollection sheets = book.getWorksheets();



//Create a range in first worksheet

Range range = sheets.createRange("A1:A2", 0);

{{< /highlight >}}
## **API obsolete**
### **Proprietà LoadOptions.LoadDataOptions obsoleta**
Utilizzare la proprietà LoadOptions.LoadFilter come alternativa.
### **Proprietà LoadOptions.LoadDataFilterOptions obsoleta**
Utilizzare invece la proprietà LoadOptions.LoadFilter.
### **Proprietà LoadOptions.OnlyLoadDocumentProperties obsoleta**
Utilizzare la proprietà LoadOptions.LoadFilter come alternativa.
### **Proprietà LoadOptions.LoadDataAndFormatting obsoleta**
Utilizzare invece la proprietà LoadOptions.LoadFilter.

{{% alert color="primary" %}} 

I frammenti di codice per tutte le API obsolete sono stati condivisi sopra.

{{% /alert %}}
## **API eliminate**
### **Proprietà DataLabels.Rotation eliminata**
Utilizzare invece la proprietà DataLabels.RotationAngle.
### **Proprietà Title.Rotation eliminata**
Utilizzare la proprietà Title.RotationAngle come alternativa.
### **Proprietà DataLabels.Background eliminata**
Si consiglia invece di utilizzare la proprietà DataLabels.BackgroundMode.
### **Proprietà DisplayUnitLabel.Rotation eliminata**
Si prega di prendere in considerazione l'utilizzo della proprietà DisplayUnitLabel.RotationAngle per raggiungere lo stesso obiettivo.
### **Metodo Title.getCharacters eliminato**
Utilizzare invece il metodo Title.characters.
