---
title: Cambiamenti della API Pubblica in Aspose.Cells 8.5.0
type: docs
weight: 160
url: /it/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.4.2 alla 8.5.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, [classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-5-0/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Modificato il Parametro del CalcoloCustomFunction di ICustomFunction**
Se un parametro per la funzione personalizzata è un riferimento a celle, nelle vecchie API Aspose.Cells veniva convertito il riferimento a celle in un singolo valore di cella o in un array di oggetti di tutti i valori delle celle nell'area indicata. Tuttavia, per molte funzioni e utenti, non è richiesto l'array di valori delle celle per tutte le celle nell'area indicata, ma è sufficiente una singola cella corrispondente alla posizione della formula, o è necessario solo il riferimento stesso anziché il valore della cella o l'array di valori. Per alcune situazioni, recuperare tutti i valori delle celle ha anche aumentato il rischio di errore di riferimento circolare.

Per supportare questo tipo di requisito, Aspose.Cells for .NET 8.5.0 ha cambiato il valore del parametro in "paramsList" per l'area indicata. Dalla v8.5.0, l'API inserisce solo l'oggetto ReferredArea nel "paramsList" quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. Se è necessario il riferimento stesso, è possibile utilizzare direttamente ReferredArea. Se è necessario ottenere un singolo valore di cella dal riferimento corrispondente alla posizione della formula, è possibile utilizzare il metodo ReferredArea.GetValue(rowOffset, int colOffset). Se è necessario un array di valori delle celle per l'intera area, è possibile utilizzare il metodo ReferredArea.GetValues.

Ora che Aspose.Cells for .NET 8.5.0 fornisce ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non poteva fornire sempre una mappatura uno a uno con i parametri della funzione personalizzata), quindi questa versione l'ha rimossa anche da "contextObjects" ora.

Questa modifica richiede piccole modifiche al codice dell'implementazione per ICustomFunction quando è necessario il valore/valori del parametro di riferimento.

**Vecchia Implementazione**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Nuova implementazione**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Aggiunta la classe CalculationOptions**
Aspose.Cells for .NET 8.5.0 ha esposto la classe CalculationOptions per aggiungere maggiore flessibilità ed estensibilità al motore di calcolo delle formule. La classe appena aggiunta ha le seguenti proprietà.

1. CalculationOptions.CalcStackSize: Specifica la dimensione dello stack per il calcolo delle celle in modo ricorsivo. -1 specifica che il calcolo userà WorkbookSettings.CalcStackSize del workbook corrispondente.
1. CalculationOptions.CustomFunction: Estende il motore di calcolo delle formule con una formula personalizzata.
1. CalculationOptions.IgnoreError: Valore booleano che indica se gli errori devono essere nascosti durante il calcolo delle formule, dove gli errori potrebbero derivare da funzioni non supportate, collegamenti esterni o altro.
1. CalculationOptions.PrecisionStrategy: Valore di tipo CalculationPrecisionStrategy che specifica la strategia per il trattamento della precisione del calcolo.
### **Aggiunta l'enumerazione CalculationPrecisionStrategy**
Aspose.Cells for .NET 8.5.0 ha esposto l'enumerazione CalculationPrecisionStrategy per aggiungere maggiore flessibilità al motore di calcolo delle formule per ottenere i risultati desiderati. Questa enumerazione gestisce la precisione del calcolo. A causa del problema di precisione dell'aritmetica in virgola mobile IEEE 754, alcune formule apparentemente semplici potrebbero non essere calcolate per fornire i risultati attesi, quindi l'ultima versione dell'API ha esposto i seguenti campi per ottenere i risultati desiderati in base alla selezione.

1. CalculationPrecisionStrategy.Decimal: Utilizza il decimale come operando quando possibile ed è inefficiente dal punto di vista delle prestazioni.
1. CalculationPrecisionStrategy.Round: Arrotonda i risultati del calcolo in base alla cifra significativa.
1. CalculationPrecisionStrategy.None: Nessuna strategia viene applicata, quindi durante il calcolo il motore utilizza il valore double originale come operando e restituisce direttamente il risultato. Questa opzione è la più efficiente e si applica alla maggior parte dei casi.
### **Metodi aggiunti per utilizzare CalculationOptions**
Con il rilascio della v8.5.0, l'API Aspose.Cells ha aggiunto le versioni sovraccaricate del metodo CalculateFormula come elencato di seguito.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Aggiunta l'enumerazione Field PasteType.RowHeights**
Le API di Aspose.Cells hanno fornito il campo di enumerazione PasteType.RowHeights allo scopo di copiare le altezze delle righe durante la copia degli intervalli. Impostando la proprietà PasteOptions.PasteType su PasteType.RowHeights, le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Aggiunta la proprietà SheetRender.PageScale**
Quando si imposta il ridimensionamento della configurazione pagina utilizzando l'opzione **Adatta a n pagine in larghezza per m in altezza**, Microsoft Excel calcola il fattore di ridimensionamento della configurazione pagina. Lo stesso può essere raggiunto utilizzando la proprietà SheetRender.PageScale esposta da Aspose.Cells for .NET 8.5.0. Questa proprietà restituisce un valore doppio che può essere convertito in valore percentuale. Ad esempio, se restituisce 0,507968245 significa che il fattore di ridimensionamento è del 51%.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Aggiunta Enumerazione CellValueFormatStrategy**
Aspose.Cells for .NET 8.5.0 ha aggiunto una nuova enumerazione CellValueFormatStrategy per gestire situazioni in cui i valori delle celle devono essere estratti con o senza formattazione applicata. L'enumerazione CellValueFormatStrategy ha i seguenti campi.

1. CellValueFormatStrategy.CellStyle: Solo formattato con il formato originale della cella.
1. CellValueFormatStrategy.DisplayStyle: Formattato con lo stile visualizzato della cella.
1. CellValueFormatStrategy.None: Non formattato.
### **Aggiunto metodo Cell.GetStingValue**
Per utilizzare l'enumerazione CellValueFormatStrategy, v8.5.0 ha esposto il metodo Cell.GetStingValue che potrebbe accettare un parametro di tipo CellValueFormatStrategy e restituisce il valore in base all'opzione specificata.

Il seguente frammento di codice mostra come utilizzare il metodo Cells.GetStingValue appena esposto.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Aggiunta Proprietà ExportTableOptions.FormatStrategy**
Aspose.Cells for .NET 8.5.0 ha esposto la proprietà ExportTableOptions.FormatStrategy per gli utenti che desiderano esportare i dati in DataTable con o senza formattazione. Questa proprietà utilizza l'enumerazione CellValueFormatStrategy ed esporta i dati in base all'opzione specificata.

Il seguente codice spiega l'uso della proprietà ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
