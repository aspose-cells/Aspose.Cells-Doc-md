---
title: Modi per calcolare le formule
type: docs
weight: 30
url: /it/cpp/ways-to-calculate-formulas/
---
## **introduzione**
Aspose.Cells ha un motore di calcolo delle formule integrato. Non solo può ricalcolare le formule importate dai modelli del designer, ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.
## **Aggiunta di formule e calcolo dei risultati**
Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel. possono essere utilizzati tramite l'API o utilizzando fogli di calcolo per designer. Aspose.Cells supporta un enorme set di formule matematiche, stringhe, booleane, data/ora, statistiche, di ricerca e di riferimento.

Utilizzare il metodo Cell.Formula per aggiungere una formula a una cella. Quando si applica una formula a una cella, iniziare sempre la stringa con un segno di uguale (=) come si fa quando si crea una formula in Microsoft Excel. Utilizzare una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, chiama il metodo Workbook.CalculateFormula() che elabora tutte le formule incorporate in un file Excel. Vedere il seguente codice di esempio che aggiunge la formula e ne calcola i risultati. Si prega di controllare[file excel di output](38109185.xlsx) generato con questo codice.

**Codice di esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Calcolo diretto della formula**
A volte, è necessario calcolare direttamente i risultati delle formule senza aggiungerli a un foglio di lavoro. I valori delle celle utilizzate nella formula esistono già in un foglio di lavoro e tutto ciò che serve è trovare il risultato di quei valori in base a una formula di Microsoft Excel senza aggiungere la formula in un foglio di lavoro.

È possibile utilizzare il metodo Worksheet.CalculateFormula(String formula) per calcolare i risultati di tali formule senza aggiungerli al foglio di lavoro.

Il codice seguente produce il seguente output.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Codice di esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Calcolo delle formule una sola volta**
Quando Workbook.CalculateFormula() viene chiamato per calcolare i valori delle formule in un modello di cartella di lavoro, Aspose.Cells crea una catena di calcolo. Aumenta le prestazioni quando le formule vengono calcolate per la seconda o terza volta.

Tuttavia, se il modello contiene molte formule, la prima volta che la formula viene calcolata può consumare molto tempo di elaborazione della CPU e molta memoria.

Aspose.Cells consente di disattivare la creazione di una catena di calcolo utile quando si desidera calcolare le formule una sola volta.

 Si prega di chiamare Workbook.GetISettings().SetCreateCalcChain() con il parametro false. Puoi usare il[file excel fornito](38109186.xlsx) per testare questo codice.

**Codice di esempio**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
