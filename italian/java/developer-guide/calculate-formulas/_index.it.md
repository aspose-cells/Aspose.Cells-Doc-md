---
title: Calcola formule
type: docs
weight: 110
url: /it/java/calculate-formulas/
---
## **Aggiunta di formule e calcolo dei risultati**

Aspose.Cells ha un motore di calcolo delle formule integrato. Non solo può ricalcolare le formule importate dai modelli di designer, ma supporta anche il calcolo dei risultati delle formule aggiunte in fase di esecuzione.

 Aspose.Cells supporta la maggior parte delle formule o delle funzioni che fanno parte di Microsoft Excel(Leggi[un elenco delle funzioni supportate dal motore di calcolo](/cells/it/java/supported-formula-functions/)). Tali funzioni possono essere utilizzate tramite le API o i fogli di calcolo dei designer. Aspose.Cells supporta un enorme set di formule matematiche, stringhe, booleane, data/ora, statistiche, database, di ricerca e di riferimento.

 Utilizzare il[**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) proprietà o[**ImpostaFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) metodi del[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)class per aggiungere una formula a una cella. Quando si applica una formula, iniziare sempre la stringa con un segno di uguale (=) come si fa quando si crea una formula in Microsoft Excel e utilizzare una virgola (,) per delimitare i parametri della funzione.

 Per calcolare i risultati delle formule, l'utente può chiamare il file[**CalcolaFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) metodo del[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)classe che elabora tutte le formule incorporate in un file Excel. Oppure, l'utente può chiamare il[**CalcolaFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) metodo del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe che elabora tutte le formule incorporate in un foglio. Oppure, l'utente può anche chiamare il[**Calcolare**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) metodo del[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)classe che elabora la formula di uno Cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Importante da sapere**

{{% alert color="primary" %}}

 Il**Formula** proprietà e**ImpostaFormula(...)** metodi del[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)lavoro di classe in modo diverso dal**Calcolare** metodi del[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) e[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) classi. Il**Formula** proprietà e**ImpostaFormula(...)** i metodi aggiungono semplicemente la formula a una cella ma non calcolano il risultato in fase di esecuzione. Per ottenere il risultato delle formule, si prega di chiamare**Calcolare** metodi.

{{% /alert %}}

## **Calcolo diretto della formula**

Aspose.Cells ha un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file di progettazione, Aspose.Cells può calcolare direttamente i risultati delle formule.

volte, è necessario calcolare direttamente i risultati delle formule senza aggiungerli a un foglio di lavoro. I valori delle celle utilizzate nella formula esistono già in un foglio di lavoro e tutto ciò che serve è trovare il risultato di quei valori in base a una formula di Excel Microsoft senza aggiungere la formula in un foglio di lavoro.

 È possibile utilizzare le API del motore di calcolo della formula Aspose.Cells per[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) a[**calcolare**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) i risultati di tali formule senza aggiungerli al foglio di lavoro:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Il codice precedente produce il seguente output:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calcolo di formule ripetutamente**

 Quando sono presenti molte formule nella cartella di lavoro e l'utente deve calcolarle ripetutamente modificandone solo una piccola parte, potrebbe essere utile per le prestazioni abilitare la catena di calcolo della formula:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Importante da sapere**

{{% alert color="primary" %}}

Di default la catena di calcolo è disabilitata. Poiché la creazione della catena richiede anche più tempo, la prima volta di calcolare le formule([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) può consumare più tempo di elaborazione della CPU e memoria rispetto al calcolo delle formule senza catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolo della formula direttamente senza creare una catena di calcolo) dovrebbe essere il modo migliore.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi Cells a Microsoft Finestra di controllo della formula di Excel](/cells/it/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Motore di calcolo delle formule](/cells/it/java/aspose-cells-formula-calculation-engine/)
- [Calcolo della funzione IFNA utilizzando Aspose.Cells](/cells/it/java/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula di matrice delle tabelle di dati](/cells/it/java/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Diminuire il tempo di calcolo del metodo Cell.Calculate](/cells/it/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Rilevamento del riferimento circolare](/cells/it/java/detecting-circular-reference/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompere o annullare il calcolo della formula della cartella di lavoro](/cells/it/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Restituzione di un intervallo di valori tramite ICustomFunction](/cells/it/java/returning-a-range-of-values-using-icustomfunction/)
- [Utilizzo della funzione ICustomFunction](/cells/it/java/using-icustomfunction-feature/)
