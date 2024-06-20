---
title: Calcola le formule
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare formule in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, formule, calcoli, Calcolo Diretto della Formula, Calcola le formule ripetutamente, aggiungi formule.
type: docs
weight: 125
url: /it/net/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Non solo può ricalcolare le formule importate dai modelli di progettazione ma supporta anche il calcolo dei risultati delle formule aggiunte durante l'esecuzione.

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel(Per ulteriori informazioni leggi [una lista delle funzioni supportate dal motore di calcolo](/cells/it/net/supported-formula-functions/)). Queste funzioni possono essere utilizzate tramite le API o i fogli di calcolo del progettista. Aspose.Cells supporta un ampio set di formule matematiche, stringa, booleane, data/ora, statistiche, database, riferimento e ricerca.

Utilizza la proprietà [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) o i metodi [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) per aggiungere una formula a una cella. Quando si applica una formula, inizia sempre la stringa con un segno uguale (=) come faresti quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che elabora tutte le formule incorporate in un file Excel. Oppure, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) della classe [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) che elabora tutte le formule incorporate in un foglio. In alternativa, l'utente può chiamare il metodo [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) che elabora la formula di una cella:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Importante da Sapere per le Formule**

{{% alert color="primary" %}}

La proprietà **Formula** e i metodi **SetFormula(...)** della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) funzionano in modo diverso dai metodi **Calcola** delle classi [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) e [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). La proprietà **Formula** e i metodi **SetFormula(...)** aggiungono semplicemente la formula a una cella ma non calcolano il risultato durante l'esecuzione. Per ottenere il risultato delle formule, si prega di chiamare i metodi **Calcola**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte è necessario calcolare direttamente i risultati delle formule senza aggiungerli in un foglio di lavoro. I valori delle celle utilizzati nella formula esistono già in un foglio di lavoro e tutto ciò che serve è trovare il risultato di quei valori in base a una certa formula di Microsoft Excel senza aggiungere la formula in un foglio di lavoro.

Puoi utilizzare le API del motore di calcolo delle formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) per [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) i risultati di tali formule senza aggiungerle al foglio di lavoro:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Il codice sopra produce il seguente output:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Come Calcolare le Formule ripetutamente**

Quando ci sono molte formule nel workbook e l'utente ha bisogno di calcolarle ripetutamente modificandone solo una piccola parte, potrebbe essere utile per le prestazioni abilitare la catena di calcolo delle formule: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita la catena di calcolo è disabilitata. Poiché la creazione della catena richiede anche del tempo aggiuntivo, la prima volta in cui vengono calcolate le formule([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) può richiedere più tempo di elaborazione della CPU e di memoria rispetto al calcolo delle formule senza catena. Se l'utente non ha bisogno di calcolare ripetutamente le formule, il comportamento predefinito(calcolare la formula direttamente senza creare una catena di calcolo) dovrebbe essere il metodo migliore.

{{% /alert %}}


## **Argomenti avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/net/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/net/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il tempo di calcolo del metodo Cell.Calculate](/cells/it/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Individuazione di riferimento circolare](/cells/it/net/detecting-circular-reference/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompere o annullare il calcolo della formula del foglio di lavoro](/cells/it/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Restituire una gamma di valori utilizzando ICustomFunction](/cells/it/net/returning-a-range-of-values-using-icustomfunction/)
- [Impostare la modalità di calcolo della formula del foglio di lavoro](/cells/it/net/setting-formula-calculation-mode-of-workbook/)
- [Utilizzo della funzione FormulaText in Aspose.Cells](/cells/it/net/using-formulatext-function-in-aspose-cells/)
- [Utilizzare la funzione ICustomFunction](/cells/it/net/using-icustomfunction-feature/)
