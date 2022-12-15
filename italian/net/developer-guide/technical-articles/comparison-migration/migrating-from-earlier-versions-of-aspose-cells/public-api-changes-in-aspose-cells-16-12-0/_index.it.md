---
title: Modifiche all'API pubblica in Aspose.Cells 16.12.0
type: docs
weight: 360
url: /it/net/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtra gli oggetti al momento del caricamento**
Aspose.Cells 16.12.0 ha esposto la classe LoadFilter insieme alla proprietà LoadOptions.LoadFilter che insieme possono controllare il tipo di dati da caricare durante l'inizializzazione di un'istanza di Workbook da un file modello.

Ecco un semplice scenario di utilizzo per caricare solo le proprietà del documento da un file modello.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Lo snippet seguente carica tutto da un foglio di calcolo esistente ad eccezione dei grafici.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Il seguente codice carica solo i dati della cella (insieme alle formule) e la formattazione da un foglio di calcolo esistente.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La classe LoadFilter consente inoltre di personalizzare il processo di caricamento secondo le proprietà del foglio di lavoro. Per personalizzare il processo di caricamento come da foglio di lavoro, è necessario eseguire l'override del metodo LoadFilter.StartSheet come illustrato di seguito.

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



Il seguente frammento utilizza la classe CustomFilter definita sopra.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Aggiunta l'enumerazione FileFormatType.OTS**
Aspose.Cells 16.12.0 ha aggiunto la voce OTS all'enumerazione FileFormatType per rilevare il formato dei file OTS.

Il seguente frammento utilizza FileFormatType.OTS.

**C#**

{{< highlight "csharp" >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Aggiunta proprietà FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 ha esposto la proprietà PreferSystemFontSubstitutes per la classe FontConfigs. La proprietà FontConfigs.PreferSystemFontSubstitutes è di tipo Boolean, indicando se l'API deve utilizzare prima il meccanismo di sostituzione dei caratteri del sistema, nel caso in cui un carattere richiesto non sia presente e non sia stata definita alcuna sostituzione per il carattere specifico. Il valore predefinito della proprietà FontConfigs.PreferSystemFontSubstitutes è false.
### **Aggiunta la proprietà BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 ha aggiunto la proprietà ScaleCrop alla classe BuiltInDocumentPropertyCollection. ScaleCrop indica la modalità di visualizzazione della miniatura del documento. L'impostazione di questo elemento su true abilita il ridimensionamento della miniatura del documento come per la visualizzazione, mentre impostandolo su false abilita il ritaglio della miniatura del documento per mostrare la sezione che si adatta alla visualizzazione.
### **Aggiunta la proprietà BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 ha inoltre esposto la proprietà LinksUpToDate per la classe BuiltInDocumentPropertyCollection. La proprietà LinksUpToDate indica se i collegamenti ipertestuali in un documento sono aggiornati.
### **Aggiunto metodo Workbook.ExportXml**
Aspose.Cells 16.12.0 ha esposto il metodo Workbook.ExportXml che consente di memorizzare i dati della mappa XML nel percorso del file specificato. Il metodo Workbook.ExportXml accetta 2 parametri in cui il primo parametro di tipo stringa deve essere il nome della mappa XML e il secondo parametro deve essere il percorso del file in cui archiviare i dati XML.
### **Aggiunto il metodo WorksheetCollection.CreateRange**
Aspose.Cells 16.12.0 ha aggiunto il metodo WorksheetCollection.CreateRange che consente di creare un intervallo basato su un indirizzo (riferimento area cella) e indice del foglio di lavoro.

Il frammento di codice seguente utilizza il metodo WorksheetCollection.CreateRange per creare un intervallo di celle che si estende da A1 a A2 nel primo foglio di lavoro (predefinito).

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
