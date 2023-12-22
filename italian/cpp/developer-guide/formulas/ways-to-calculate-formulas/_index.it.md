---
title: Modi per calcolare le formule
type: docs
weight: 30
url: /it/cpp/ways-to-calculate-formulas/
---
##  **introduzione**
Aspose.Cells ha un motore di calcolo delle formule incorporato. Non solo può ricalcolare le formule importate dai modelli di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.
##  **Aggiunta di formule e calcolo dei risultati**
Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel. possono essere utilizzati tramite lo API o utilizzando i fogli di calcolo del designer. Aspose.Cells supporta un vasto set di formule matematiche, di stringa, booleane, di data/ora, statistiche, di ricerca e di riferimento.

Utilizza il metodo Cell.SetFormula per aggiungere una formula a una cella. Quando applichi una formula a una cella, inizia sempre la stringa con un segno uguale (=) come fai quando crei una formula in Microsoft Excel. Utilizzare una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, chiama il metodo Workbook.CalculateFormula() che elabora tutte le formule incorporate in un file Excel. Consulta il seguente codice di esempio che aggiunge la formula e ne calcola i risultati. Si prega di controllare[file Excel di output](38109185.xlsx) generato con questo codice.

**Codice d'esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **Calcolo delle formule una sola volta**
Quando Workbook.CalculateFormula() viene chiamato per calcolare i valori delle formule in un modello di cartella di lavoro, Aspose.Cells crea una catena di calcolo. Aumenta le prestazioni quando le formule vengono calcolate per la seconda o terza volta.

Tuttavia, se il modello contiene molte formule, la prima volta che la formula viene calcolata può consumare molto tempo di elaborazione e memoria della CPU.

Aspose.Cells permette di disattivare la creazione di una catena di calcolo utile quando si vogliono calcolare le formule una sola volta.

 Chiama Workbook.GetISettings().SetCreateCalcChain() con il parametro false. Puoi usare il[file Excel fornito](38109186.xlsx) per testare questo codice.

**Codice d'esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
