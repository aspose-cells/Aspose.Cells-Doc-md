---
title: Cambiamenti dell API pubblica in Aspose.Cells 16.12.0
type: docs
weight: 360
url: /it/net/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Oggetti filtro al momento del caricamento**
Aspose.Cells 16.12.0 ha esposto la classe LoadFilter insieme alla proprietà LoadOptions.LoadFilter che insieme possono controllare il tipo di dati da caricare durante l'inizializzazione di un'istanza di Workbook da un file modello.

Ecco uno scenario di utilizzo semplice per caricare solo le proprietà del documento da un file modello.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Il seguente snippet carica tutto da un foglio di calcolo esistente tranne i grafici.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Il seguente codice carica solo i dati delle celle (insieme alle formule) e la formattazione da un foglio di calcolo esistente.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



La classe LoadFilter consente anche di personalizzare il processo di caricamento in base alle proprietà del Foglio di lavoro. Per personalizzare il processo di caricamento in base al foglio di lavoro, è necessario eseguire l'override del metodo LoadFilter.StartSheet come dimostrato di seguito.

**C#**

{{< highlight csharp >}}

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



Il seguente snippet utilizza la classe CustomFilter definita sopra.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Aggiunta enumerazione FileFormatType.OTS**
Aspose.Cells 16.12.0 ha aggiunto l'elemento OTS all'enumerazione FileFormatType per rilevare il formato dei file OTS.

Il seguente snippet fa uso di FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Aggiunta proprietà FontConfigs.PreferSystemFontSubstitutes**
Aspose.Cells 16.12.0 ha esposto la proprietà PreferSystemFontSubstitutes per la classe FontConfigs. La proprietà FontConfigs.PreferSystemFontSubstitutes è di tipo Booleano, indicando se l'API dovrebbe utilizzare prima il meccanismo di sostituzione del font di sistema, nel caso in cui un determinato font richiesto non sia presente e nessuna sostituzione per quel particolare font sia stata definita. Il valore predefinito della proprietà FontConfigs.PreferSystemFontSubstitutes è false.
### **Aggiunta proprietà BuiltInDocumentPropertyCollection.ScaleCrop**
Aspose.Cells 16.12.0 ha aggiunto la proprietà ScaleCrop alla classe BuiltInDocumentPropertyCollection. ScaleCrop indica la modalità di visualizzazione dell'anteprima del documento. Impostando questo elemento su true abilita il ridimensionamento dell'anteprima del documento come da display, mentre impostandolo su false abilita il ritaglio dell'anteprima del documento per mostrare la sezione che si adatta al display.
### **Aggiunta proprietà BuiltInDocumentPropertyCollection.LinksUpToDate**
Aspose.Cells 16.12.0 ha anche esposto la proprietà LinksUpToDate per la classe BuiltInDocumentPropertyCollection. La proprietà LinksUpToDate indica se i collegamenti ipertestuali in un documento sono aggiornati.
### **Aggiunto il metodo Workbook.ExportXml**
Aspose.Cells 16.12.0 ha esposto il metodo Workbook.ExportXml che consente di memorizzare i dati della mappa XML nel percorso del file specificato. Il metodo Workbook.ExportXml accetta 2 parametri in cui il primo parametro di tipo stringa dovrebbe essere il nome della mappa XML e il secondo parametro dovrebbe essere il percorso del file in cui memorizzare i dati XML.
### **Aggiunto il metodo WorksheetCollection.CreateRange**
Aspose.Cells 16.12.0 ha aggiunto il metodo WorksheetCollection.CreateRange che consente di creare un intervallo basato su un indirizzo (riferimento all'area della cella) e sull'indice del foglio di lavoro.

Il seguente frammento fa uso del metodo WorksheetCollection.CreateRange per creare un intervallo di celle che vanno da A1 a A2 nel primo foglio di lavoro (predefinito).

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

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
