---
title: Gestire le formule dei file Excel
linktitle: Formule
type: docs
weight: 122
url: /it/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells può semplicemente ottenere, impostare e calcolare formule dei file excel.
description: Scopri come gestire le formule dei file Excel attraverso le API Aspose.Cells for NET.
keywords: Come calcolare formule in C#, formule e funzioni usando C#, Gestione delle funzioni incorporate in C#, Come utilizzare le funzioni add in con C#, Come utilizzare la formula matriciale tramite C#, Come utilizzare la formula R1C1 in C#.
---

## **Introduzione**

Una delle funzionalità più interessanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce un insieme di funzioni e formule incorporate che aiutano gli utenti a eseguire rapidamente calcoli complessi. Aspose.Cells fornisce anche un'ampia serie di funzioni e formule incorporate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells supporta anche le funzioni add-in. Inoltre, Aspose.Cells supporta le formule matriciali e R1C1 in Aspose.Cells.

## **Come utilizzare formule e funzioni**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ogni elemento nella raccolta Cells rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

È possibile applicare formule alle celle utilizzando le proprietà e i metodi offerti dalla classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), discussi in dettaglio di seguito.

- Utilizzo di funzioni incorporate.
- Utilizzo di funzioni add-in.
- Lavorare con formule matriciali.
- Creazione di una formula R1C1.

## **Come utilizzare le funzioni incorporate**

Le funzioni incorporate o le formule vengono fornite come funzioni predefinite per ridurre gli sforzi e il tempo degli sviluppatori. Consulta [un elenco di funzioni incorporate](/cells/it/net/supported-formula-functions/) supportate da Aspose.Cells. Le funzioni sono elencate in ordine alfabetico. Saranno supportate più funzioni in futuro.

Aspose.Cells supporta la maggior parte delle formule o funzioni offerte da Microsoft Excel. Gli sviluppatori possono utilizzare queste formule tramite l’API o il [foglio di calcolo del progettista](/cells/it/net/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto insieme di formule matematiche, stringhe, Boolean, data/ora, statistiche, database, ricerca e riferimento.

Utilizza la proprietà [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) per aggiungere una formula a una cella. **Formule complesse**, per esempio

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportate anche in Aspose.Cells. Quando si applica una formula a una cella, inizia sempre la stringa con un segno uguale (=) come fai quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Nell'esempio seguente, viene applicata una formula complessa alla prima cella di una raccolta di [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) fogli di lavoro. La formula utilizza una funzione built-in **IF** fornita da Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Come utilizzare le funzioni aggiuntive**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come un add-in di Excel. Quando si imposta la funzione cella.Formula, le funzioni built-in funzionano correttamente, tuttavia c'è bisogno di impostare le funzioni o formule personalizzate utilizzando le funzioni aggiuntive.

Aspose.Cells fornisce funzionalità per registrare le funzioni aggiuntive utilizzando [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Successivamente, quando impostiamo cella.Formula = anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il seguente file XLAM deve essere scaricato per registrare la funzione add-in nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per controllare i risultati.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Come utilizzare la formula matriciale**

Le formule matriciali sono formule che prendono array, invece di numeri singoli, come argomenti delle funzioni che compongono la formula. Quando una formula matriciale viene visualizzata, è racchiusa da parentesi graffe ({}).

Alcune funzioni di Microsoft Excel restituiscono array di valori. Per calcolare più risultati con una formula matriciale, inserisci l'array in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti dell'array.

È possibile applicare una formula matriciale a una cella chiamando il metodo [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Il metodo [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) richiede i seguenti parametri:

- **Formula Matriciale**, la formula matriciale.
- **Numero di righe**, il numero di righe per popolare il risultato della formula matriciale.
- **Numero di colonne**, il numero di colonne per popolare il risultato della formula matriciale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Come utilizzare la formula R1C1**

Aggiungi una formula di stile di riferimento **R1C1** a una cella con la proprietà [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Argomenti avanzati**
- [Predecessori e Dipendenti](/cells/it/net/precedents-and-dependents/)
- [Imposta i collegamenti esterni nelle formule](/cells/it/net/set-external-links-in-formulas/)
- [Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe](/cells/it/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Impostazione della formula per il intervallo nominato](/cells/it/net/setting-formula-for-named-range/)
- [Impostazione della formula - Avviso per gli utenti non anglofoni](/cells/it/net/setting-formulas-notice-for-non-english-users/)
- [Impostazione della formula condivisa](/cells/it/net/setting-shared-formula/)
- [Specificare il numero massimo di righe della formula condivisa](/cells/it/net/specify-maximum-rows-of-shared-formula/)
- [Funzioni Excel supportate](/cells/it/net/supported-formula-functions/)

