---
title: Calcola o ricalcola le formule in modo dinamico
type: docs
weight: 10
url: /it/net/calculate-or-recalculate-formulas-dynamically/
---
**Calcolo della formula** motore è incorporato**Aspose.Cells**. Non solo può ricalcolare la formula importata dal file di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.
## **Aggiunta di formule e calcolo dei risultati**
Aspose.Cells supporta la maggior parte delle formule o delle funzioni che fanno parte di Microsoft Excel. Gli sviluppatori possono utilizzare queste formule utilizzando API o Designer Spreadsheets. Aspose.Excel supporta un vasto set di formule matematiche, stringhe, booleane, data/ora, statistiche, database, di ricerca e di riferimento.

Utilizzare la proprietà Formula della classe Cell per aggiungere una formula a una cella. Quando si applica una formula a una cella, iniziare sempre la stringa con un segno di uguale (=) come si fa quando si crea una formula in Microsoft Excel. Utilizzare una virgola (,) per delimitare i parametri della funzione.

 Per calcolare i risultati delle formule, chiamare il metodo CalculateFormula della classe Excel che elabora tutte le formule incorporate in un file Excel. Leggi il[url:elenco delle funzioni supportate dal metodo CalculateFormula](/cells/it/net/supported-formula-functions/).

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **Calcolo delle formule una sola volta**
Quando l'utente chiama Workbook.CalculateFormula() per calcolare i valori delle formule all'interno del modello di cartella di lavoro, Aspose.Cells crea una catena di calcolo. Aumenta le prestazioni quando le formule vengono calcolate per la seconda o terza volta ecc.
Tuttavia, se il modello utente contiene molte formule diverse, la prima volta del calcolo della formula può consumare molto tempo di elaborazione della CPU e memoria.

Aspose.Cells ti consente di disattivare la creazione di una catena di calcolo utile negli scenari in cui desideri calcolare le formule del tuo file solo una volta.

 Se stai cercando di migliorare le prestazioni dei calcoli delle formule entro Aspose.Cells e non desideri creare una catena di calcolo delle formule, imposta**FormulaSettings.EnableCalculationChain** come**falso** . Per impostazione predefinita, è impostato come**VERO**.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **Calcolo diretto della formula**
Il motore di calcolo delle formule è incorporato in Aspose.Cells. Inoltre, ricalcolando la formula importata dal file di progettazione, Aspose.Cells supporta anche il calcolo diretto dei risultati delle formule.
A volte, è necessario calcolare direttamente i risultati delle formule senza aggiungerli effettivamente in un foglio di lavoro. I valori delle celle utilizzate nella formula esistono già in un foglio di lavoro e tutto ciò che serve è trovare il risultato di quei valori in base a una formula Ms-Excel senza aggiungere la formula in un foglio di lavoro.

 È possibile utilizzare Aspose.Cells Formula Calculation Engine API ie**foglio di lavoro.Calcola(formula stringa)**per calcolare i risultati di tali formule senza aggiungerli effettivamente nel foglio di lavoro.

{{< highlight "csharp" >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
