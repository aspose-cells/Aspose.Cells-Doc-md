---
title: Cambiamenti della API Pubblica in Aspose.Cells 8.5.0
type: docs
weight: 170
url: /it/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.4.2 alla 8.5.0 che potrebbero essere di interesse per gli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, [classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-5-0/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte di Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Modificato il Parametro del CalcoloCustomFunction di ICustomFunction**
Se un parametro per la funzione personalizzata è un riferimento a celle, nelle vecchie API Aspose.Cells veniva convertito il riferimento a celle in un singolo valore di cella o in un array di oggetti di tutti i valori delle celle nell'area indicata. Tuttavia, per molte funzioni e utenti, non è richiesto l'array di valori delle celle per tutte le celle nell'area indicata, ma è sufficiente una singola cella corrispondente alla posizione della formula, o è necessario solo il riferimento stesso anziché il valore della cella o l'array di valori. Per alcune situazioni, recuperare tutti i valori delle celle ha anche aumentato il rischio di errore di riferimento circolare.

Per supportare questo tipo di requisito, Aspose.Cells for Java 8.5.0 ha cambiato il valore del parametro in "paramsList" per l'area di riferimento. Dal v8.5.0, l'API inserisce semplicemente l'oggetto ReferredArea nel "paramsList" quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. Se hai bisogno del riferimento in sé, puoi utilizzare direttamente l'oggetto ReferredArea. Se hai bisogno di ottenere un singolo valore della cella dal riferimento corrispondente alla posizione della formula, puoi utilizzare il metodo ReferredArea.getValue(rowOffset, int colOffset). Se hai bisogno di un array di valori delle celle per l'intera area, allora puoi utilizzare il metodo ReferredArea.getValues.

Ora, poiché Aspose.Cells for Java 8.5.0 fornisce il ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non poteva dare sempre una corrispondenza uno a uno con i parametri della funzione personalizzata), quindi questo rilascio l'ha anche rimosso da "contextObjects" ora.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Aspose.Cells for Java 8.5.0 ha esposto la classe CalculationOptions per aggiungere maggiore flessibilità ed estensibilità al motore di calcolo delle formule. La classe appena aggiunta ha le seguenti proprietà. 

1. CalculationOptions.CalcStackSize: Specifica la dimensione dello stack per il calcolo delle celle in modo ricorsivo. -1 specifica che il calcolo userà WorkbookSettings.CalcStackSize del workbook corrispondente.
1. CalculationOptions.CustomFunction: Estende il motore di calcolo delle formule con una formula personalizzata.
1. CalculationOptions.IgnoreError: Valore booleano che indica se gli errori devono essere nascosti durante il calcolo delle formule, dove gli errori potrebbero derivare da funzioni non supportate, collegamenti esterni o altro.
1. CalculationOptions.PrecisionStrategy: Valore di tipo CalculationPrecisionStrategy che specifica la strategia per il trattamento della precisione del calcolo.
### **Aggiunta l'enumerazione CalculationPrecisionStrategy**
Aspose.Cells for Java 8.5.0 ha esposto l'enumerazione CalculationPrecisionStrategy per aggiungere maggiore flessibilità al motore di calcolo delle formule per ottenere i risultati desiderati. Questa enumerazione strategizza la gestione della precisione di calcolo. A causa del problema di precisione dell'aritmetica a virgola mobile IEEE 754, alcune formule apparentemente semplici potrebbero non essere calcolate per restituire i risultati attesi, pertanto l'ultima versione dell'API ha esposto i seguenti campi per ottenere i risultati desiderati in base alla selezione.

1. CalculationPrecisionStrategy.DECIMAL: Utilizza decimali come operando quando possibile, ed è il più inefficiente dal punto di vista delle considerazioni sulle prestazioni.
1. CalculationPrecisionStrategy.ROUND: Arrotonda i risultati del calcolo in base al numero di cifre significative.
1. CalculationPrecisionStrategy.NONE: Nessuna strategia viene applicata quindi durante il calcolo il motore utilizza il valore double originale come operando e restituisce il risultato direttamente. Questa opzione è più efficiente ed è applicabile per la maggior parte dei casi.
### **Metodi aggiunti per utilizzare CalculationOptions**
Con il rilascio di v8.5.0, l'API di Aspose.Cells ha aggiunto versioni sovraccaricate del metodo calculateFormula come elencato di seguito.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Enumerazione Campo IncollaTipo.ALTEZZE_RIGHE Aggiunto**
Le API di Aspose.Cells hanno fornito il campo di enumerazione PasteType.ROW_HEIGHTS allo scopo di copiare le altezze delle righe durante la copia degli intervalli. Impostando la proprietà PasteOptions.PasteType su PasteType.ROW_HEIGHTS, le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Aggiunta la proprietà SheetRender.PageScale**
Quando si imposta il ridimensionamento della pagina in **Adatta a n pagine in larghezza per m pagine in altezza**, Microsoft Excel calcola il fattore di ridimensionamento della configurazione di pagina. Lo stesso risultato può essere ottenuto utilizzando la proprietà SheetRender.PageScale esposta da Aspose.Cells for Java 8.5.0. Questa proprietà restituisce un valore double che può essere convertito in un valore percentuale. Ad esempio, se restituisce 0.507968245, significa che il fattore di ridimensionamento è del 51%.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Aggiunta Enumerazione CellValueFormatStrategy**
Aspose.Cells for Java 8.5.0 ha aggiunto una nuova enumerazione CellValueFormatStrategy per gestire situazioni in cui i valori delle celle devono essere estratti con o senza formattazione applicata. L'enumerazione CellValueFormatStrategy ha i seguenti campi. 

1. CellValueFormatStrategy.CELL_STYLE: Solo formattato con il formato originale della cella.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formattato con lo stile visualizzato della cella.
1. CellValueFormatStrategy.NONE: Non formattato.
### **Metodo Cell.getStringValue Aggiunto**
Per utilizzare l'enumerazione CellValueFormatStrategy, v8.5.0 ha esposto il metodo Cell.getStringValue che potrebbe accettare un parametro di tipo CellValueFormatStrategy e restituisce il valore in base all'opzione specificata.

Il seguente frammento di codice mostra come utilizzare il nuovo metodo esposto Cells.getStringValue.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
