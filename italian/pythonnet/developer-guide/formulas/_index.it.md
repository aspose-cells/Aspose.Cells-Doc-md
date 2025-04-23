---
title: Gestire le formule dei file Excel
linktitle: Formule
type: docs
weight: 122
url: /it/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for Python via .NET può semplicemente ottenere, impostare e calcolare formule dei file Excel.
description: Impara come Gestire le formule dei file Excel tramite le API Aspose.Cells for Python via .NET per .NET.
keywords: Come calcolare le formule in Python, Formule e Funzioni usando Python, Gestire le Funzioni Incorporate in Python, Come Usare Funzioni di Add in con Python, Come Usare la Formula di Array tramite Python, Come Usare la Formula R1C1 in Python.
---

## **Introduzione**

Una delle caratteristiche più interessanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce un insieme di funzioni e formule incorporate che aiutano gli utenti a eseguire calcoli complessi rapidamente. Aspose.Cells per Python via .NET offre anche un vasto insieme di funzioni e formule incorporate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells for Python via .NET supporta anche funzioni di add-in. Inoltre, Aspose.Cells per Python via .NET supporta formule di Array e R1C1.

## **Come utilizzare formule e funzioni**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Ogni elemento nella collezione Cells rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

È possibile applicare formule alle celle utilizzando le proprietà e i metodi offerti dalla classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), discussi in dettaglio di seguito.

- Utilizzo di funzioni incorporate.
- Utilizzo di funzioni add-in.
- Lavorare con formule matriciali.
- Creazione di una formula R1C1.

## **Come utilizzare le funzioni incorporate**

Le funzioni o formule incorporate sono fornite come funzioni pronte per ridurre gli sforzi e i tempi degli sviluppatori. Vedi [una lista di funzioni incorporate](/cells/it/python-net/supported-formula-functions/) supportate da Aspose.Cells for Python via .NET. Le funzioni sono elencate in ordine alfabetico. Più funzioni saranno supportate in futuro.

Aspose.Cells for Python via .NET supporta la maggior parte delle formule o funzioni offerte da Microsoft Excel. Gli sviluppatori possono usare queste formule tramite l'API o [designer spreadsheet](/cells/it/net/what-is-a-designer-spreadsheet/). Aspose.Cells per Python via .NET supporta un ampio insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimento.

Utilizza la proprietà [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) per aggiungere una formula a una cella. **Formule complesse**, per esempio

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono anche supportate in Aspose.Cells for Python via .NET. Quando si applica una formula a una cella, si inizia sempre la stringa con un segno uguale (=) come quando si crea una formula in Microsoft Excel e si usa una virgola (,) per delimitare i parametri delle funzioni.

 Nell'esempio sotto, una formula complessa viene applicata alla prima cella di una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) di un foglio di lavoro. La formula utilizza una funzione **SE** incorporata fornita da Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Come utilizzare le funzioni aggiuntive**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come un add-in di Excel. Quando si imposta la funzione cella.Formula, le funzioni built-in funzionano correttamente, tuttavia c'è bisogno di impostare le funzioni o formule personalizzate utilizzando le funzioni aggiuntive.

Aspose.Cells for Python via .NET fornisce funzionalità per registrare funzioni add-in usando [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). Successivamente, quando impostiamo cell.Formula = anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il seguente file XLAM deve essere scaricato per registrare la funzione add-in nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per controllare i risultati.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Come utilizzare la formula matriciale**

Le formule matriciali sono formule che prendono array, invece di numeri singoli, come argomenti delle funzioni che compongono la formula. Quando una formula matriciale viene visualizzata, è racchiusa da parentesi graffe ({}).

Alcune funzioni di Microsoft Excel restituiscono array di valori. Per calcolare più risultati con una formula matriciale, inserisci l'array in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti dell'array.

È possibile applicare una formula matriciale a una cella chiamando il metodo [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Il metodo [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) richiede i seguenti parametri:

- **Formula Matriciale**, la formula matriciale.
- **Numero di righe**, il numero di righe per popolare il risultato della formula matriciale.
- **Numero di colonne**, il numero di colonne per popolare il risultato della formula matriciale.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Come utilizzare la formula R1C1**

Aggiungi una formula di stile di riferimento **R1C1** a una cella con la proprietà [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Argomenti avanzati**
- [Predecessori e Dipendenti](/cells/it/python-net/precedents-and-dependents/)
- [Imposta i collegamenti esterni nelle formule](/cells/it/python-net/set-external-links-in-formulas/)
- [Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe](/cells/it/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Impostazione della formula per il intervallo nominato](/cells/it/python-net/setting-formula-for-named-range/)
- [Impostazione della formula - Avviso per gli utenti non anglofoni](/cells/it/python-net/setting-formulas-notice-for-non-english-users/)
- [Impostazione della formula condivisa](/cells/it/python-net/setting-shared-formula/)
- [Specificare il numero massimo di righe della formula condivisa](/cells/it/python-net/specify-maximum-rows-of-shared-formula/)
- [Funzioni Excel supportate](/cells/it/python-net/supported-formula-functions/)


