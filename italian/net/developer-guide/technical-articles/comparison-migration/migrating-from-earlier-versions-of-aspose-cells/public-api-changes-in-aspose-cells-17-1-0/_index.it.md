---
title: Modifiche API pubbliche in Aspose.Cells 17.1.0
type: docs
weight: 370
url: /it/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.12.0 alla 17.1.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per Excel 2016 Grafici**
Aspose.Cells APIs hanno aggiunto il supporto per alcuni grafici di Excel 2016 migliorando l'enumerazione ChartType. I seguenti nuovi campi sono stati aggiunti con il rilascio di Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: La serie è presentata come box e whisker.
- ChartType.Funnel: La serie è presentata come un imbuto.
- ChartType.ParetoLine: La serie è presentata come linee di pareto.
- ChartType.Sunburst: La serie è presentata come un sunburst.
- ChartType.Treemap: La serie è presentata come una mappa a trama.
- ChartType.Waterfall: La serie è presentata come una cascata.
- ChartType.Histogram: La serie è presentata come un istogramma.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Lettura Tipologie di Grafici Excel 2016](/cells/it/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Aggiunto Setter per la Proprietà LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 ha aggiunto il setter per la proprietà LoadFilter.LoadDataFilterOptions per sostituire la variabile di istanza m_LoadDataFilterOptions. Gli utenti possono modificare la proprietà LoadDataFilterOptions nella propria implementazione della classe LoadFilter per cambiare il comportamento del caricamento dei file di modello.

Ecco uno scenario d'uso semplice.

{{% alert color="primary" %}} 

Consultare l'articolo dettagliato su [Filtraggio Personalizzato dei Template](/cells/it/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Aggiunta della proprietà CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 ha esposto la proprietà SignificantDigits dalla classe CellsHelper che consente di ottenere o impostare il numero di cifre significative per i valori numerici in un foglio di calcolo. Il valore predefinito della proprietà CellsHelper.SignificantDigits è 17 ed è applicabile solo se il risultato deve essere memorizzato nel formato file XLSX.

Ecco uno scenario semplice per dimostrare l'uso della proprietà CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Impostazione del numero di cifre significative](/cells/it/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Aggiunta della proprietà GlowEffect.Color**
Aspose.Cells 17.1.0 ha aggiunto la proprietà GlowEffect.Color che può essere utilizzata per recuperare il colore dell'effetto glow.

Il seguente snippet utilizza la proprietà GlowEffect.Color.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Lettura del colore del bagliore della forma](/cells/it/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Aggiunte le proprietà PaperWidth e PaperHeight di PageSetup**
Aspose.Cells 17.1.0 ha esposto le proprietà PaperWidth e PaperHeight per la classe PageSetup. Le proprietà PageSetup.PaperWidth e PageSetup.PaperHeight sono di tipo double e rappresentano la larghezza e l'altezza della carta in unità di pollici, considerando l'orientamento della pagina.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Recupero delle dimensioni della carta del foglio di lavoro](/cells/it/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Aggiunta della proprietà WorkbookSettings.CheckCustomNumberFormat**
Aspose.Cells 17.1.0 ha aggiunto la proprietà CheckCustomNumberFormat alla classe WorkbookSettings. CheckCustomNumberFormat è utile per verificare se la proprietà Style.Custom è stata impostata correttamente o meno. Nel caso in cui la proprietà Style.Custom sia stata impostata in modo improprio, cioè il valore non corrisponde a un modello valido, le API di Aspose.Cells genereranno una CellsException con un messaggio appropriato.

{{% alert color="primary" %}} 

Controlla l'articolo dettagliato su [Verifica del formato personalizzato](/cells/it/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **Aggiunto il campo DisplayUnitType.Percentage**
Aspose.Cells 17.1.0 ha esposto anche il campo Percentage per l'enumerazione DisplayUnitType. Il campo DisplayUnitType.Percentage indica che i valori nel grafico devono essere divisi per 0,01.
## **API rimosse**
### **Rimosso la variabile di istanza m_LoadDataFilterOptions**
Questa versione ha rimosso la variabile di istanza m_LoadDataFilterOptions. Si consiglia di utilizzare invece la proprietà LoadFilter.LoadDataFilterOptions.
