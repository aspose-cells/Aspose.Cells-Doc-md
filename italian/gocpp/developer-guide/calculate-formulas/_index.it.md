---
title: Calcola le formule con Golang tramite C++
linktitle: Calcola le formule
description: Questo articolo presenta come usare la libreria Aspose.Cells per calcolare le formule in Microsoft Excel con Golang tramite C++. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo usare i metodi forniti da Aspose.Cells per calcolare la formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, formule, calcoli, Calcolo Diretto della Formula, Calcola le formule ripetutamente, aggiungi formule.
type: docs
weight: 125
url: /it/go-cpp/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells ha un motore di calcolo formule integrato. Non solo può ricalcolare le formule importate da modelli di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in runtime.

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel (Leggi [una lista delle funzioni supportate dal motore di calcolo](/cells/it/cpp/supported-formula-functions/)). Queste funzioni possono essere usate tramite API o fogli di lavoro di progettazione. Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimento.

Usa la proprietà [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/) o i metodi [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) per aggiungere una formula a una cella. Quando applichi una formula, inizia sempre la stringa con un segno di uguale (=) come quando crei una formula in Microsoft Excel e usa una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che elabora tutte le formule incorporate in un file Excel. Oppure, può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), che elabora tutte le formule incorporate in un foglio. Oppure, può chiamare anche il metodo [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), che elabora la formula di una singola Cell:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Importante da Sapere per le Formule**

{{% alert color="primary" %}}

La proprietà **GetFormula** e i metodi **SetFormula(...)** della classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) funzionano in modo diverso dai metodi **Calculate** delle classi [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) e [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). La proprietà **GetFormula** e i metodi **SetFormula(...)** aggiungono semplicemente la formula a una cella ma non calcolano il risultato in runtime. Per ottenere il risultato delle formule, chiama i metodi **Calculate**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte, hai bisogno di calcolare i risultati delle formule direttamente senza aggiungerle a un foglio di calcolo. I valori delle celle usate nella formula esistono già in un foglio di calcolo, e tutto ciò che devi fare è trovare il risultato di quei valori in base a una formula di Microsoft Excel senza aggiungere la formula in un foglio.

Puoi usare le API del motore di calcolo formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) a [**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/) calcolare i risultati di tali formule senza aggiungerle al foglio:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Il codice sopra produce il seguente output:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Come calcolare le formule ripetutamente**

Quando ci sono molte formule nel workbook e l'utente ha bisogno di calcolarle ripetutamente modificando solo una piccola parte di esse, può essere utile per le prestazioni abilitare la catena di calcolo delle formule: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita, la catena di calcolo è disattivata. Poiché la creazione della catena richiede anche tempo extra, la prima volta che si calcolano le formule ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) potrebbe richiedere più tempo di elaborazione CPU e memoria rispetto al calcolo delle formule senza catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolare la formula direttamente senza creare una catena di calcolo) dovrebbe essere l'opzione migliore.

{{% /alert %}}

## **Argomenti Avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/cpp/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il tempo di calcolo del metodo Cell.Calculate](/cells/it/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Impostare la modalità di calcolo della formula del foglio di lavoro](/cells/it/cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilizzo della funzione FormulaText in Aspose.Cells](/cells/it/cpp/using-formulatext-function-in-aspose-cells/)
