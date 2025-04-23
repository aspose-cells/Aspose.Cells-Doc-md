---
title: Calcola le formule
type: docs
weight: 110
url: /it/java/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Non solo può ricalcolare le formule importate dai modelli di progettazione ma supporta anche il calcolo dei risultati delle formule aggiunte durante l'esecuzione.

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel (Leggi [un elenco delle funzioni supportate dal motore di calcolo](/cells/it/java/supported-formula-functions/)). Queste funzioni possono essere utilizzate tramite le API o fogli di calcolo di progettazione. Aspose.Cells supporta un ampio set di formule matematiche, per stringhe, booleane, data/ora, statistiche, di database, di ricerca e di riferimento.

Utilizza la proprietà [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) o i metodi [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) per aggiungere una formula a una cella. Quando si applica una formula, inizia sempre la stringa con un segno uguale (=) come faresti quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-- ) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che elabora tutte le formule incorporate in un file Excel. Oppure, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-com.aspose.cells.CalculationOptions-boolean-) della classe [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) che elabora tutte le formule incorporate in un foglio. Oppure, può anche chiamare il metodo [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate-com.aspose.cells.CalculationOptions-) della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) che elabora la formula di una singola Cella:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Importante sapere**

{{% alert color="primary" %}}

La proprietà **Formula** e i metodi **SetFormula(...)** della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) funzionano in modo diverso dai metodi **Calcola** delle classi [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) e [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). La proprietà **Formula** e i metodi **SetFormula(...)** aggiungono semplicemente la formula a una cella ma non calcolano il risultato durante l'esecuzione. Per ottenere il risultato delle formule, si prega di chiamare i metodi **Calcola**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte è necessario calcolare direttamente i risultati delle formule senza aggiungerli in un foglio di lavoro. I valori delle celle utilizzati nella formula esistono già in un foglio di lavoro e tutto ciò che serve è trovare il risultato di quei valori in base a una certa formula di Microsoft Excel senza aggiungere la formula in un foglio di lavoro.

Puoi utilizzare le API del motore di calcolo delle formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) per [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) i risultati di tali formule senza aggiungerle al foglio di lavoro:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Il codice sopra produce il seguente output:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Calcolando le Formule ripetutamente**

Quando ci sono molte formule nel workbook e l'utente ha bisogno di calcolarle ripetutamente modificandone solo una piccola parte, potrebbe essere utile per le prestazioni abilitare la catena di calcolo delle formule: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita, la catena di calcolo è disabilitata. Poiché creare la catena richiede anche tempo extra, la prima volta che si calcolano le formule ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--)) potrebbe consumare più tempo di CPU e memoria rispetto al calcolo senza catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolare direttamente la formula senza creare una catena di calcolo) dovrebbe essere la scelta migliore.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Motore di calcolo delle formule Aspose.Cells](/cells/it/java/aspose-cells-formula-calculation-engine/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/java/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/java/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il tempo di calcolo del metodo Cell.Calculate](/cells/it/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Individuazione di riferimento circolare](/cells/it/java/detecting-circular-reference/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompere o annullare il calcolo della formula del foglio di lavoro](/cells/it/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Restituire una gamma di valori utilizzando ICustomFunction](/cells/it/java/returning-a-range-of-values-using-icustomfunction/)
- [Utilizzare la funzione ICustomFunction](/cells/it/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
