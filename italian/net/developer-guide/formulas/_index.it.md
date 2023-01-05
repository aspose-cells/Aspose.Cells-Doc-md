---
title: Gestisci le formule dei file Excel
linktitle: Formule
type: docs
weight: 122
url: /it/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells può semplicemente ottenere, impostare e calcolare formule di file excel.
---
## **introduzione**

Una delle caratteristiche interessanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce una serie di funzioni e formule integrate che consentono agli utenti di eseguire rapidamente calcoli complessi. Aspose.Cells fornisce anche un vasto set di funzioni e formule integrate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells supporta anche funzioni aggiuntive. Inoltre, Aspose.Cells supporta l'array e le formule R1C1 in Aspose.Cells.

## **Uso di formule e funzioni**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni articolo della collezione Cells rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe.

 È possibile applicare formule alle celle utilizzando proprietà e metodi offerti dal[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe, discussa più dettagliatamente di seguito.

- Utilizzo delle funzioni integrate.
- Utilizzo delle funzioni aggiuntive.
- Lavorare con le formule di matrice.
- Creazione di una formula R1C1.

## **Utilizzo delle funzioni integrate**

 Le funzioni o le formule integrate vengono fornite come funzioni già pronte per ridurre gli sforzi e il tempo degli sviluppatori. Vedere[un elenco di funzioni integrate](/cells/it/net/supported-formula-functions/) supportato da Aspose.Cells. Le funzioni sono elencate in ordine alfabetico. Altre funzioni saranno supportate in futuro.

 Aspose.Cells supporta la maggior parte delle formule o delle funzioni offerte da Microsoft Excel. Gli sviluppatori possono utilizzare queste formule tramite API o[foglio di calcolo del progettista](/cells/it/net/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto set di formule matematiche, stringhe, booleane, data/ora, statistiche, database, di ricerca e di riferimento.

 Usa il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)proprietà per aggiungere una formula a una cella.**Formule complesse**, Per esempio

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportati anche in Aspose.Cells. Quando si applica una formula a una cella, iniziare sempre la stringa con un segno di uguale (=) come si fa quando si crea una formula in Microsoft Excel e utilizzare una virgola (,) per delimitare i parametri della funzione.

 Nell'esempio seguente, una formula complessa viene applicata alla prima cella di un foglio di lavoro[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. La formula utilizza un built-in**SE** funzione fornita da Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Utilizzo delle funzioni aggiuntive**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come componente aggiuntivo di Excel. Quando si imposta la funzione cell.Formula, le funzioni integrate funzionano correttamente, tuttavia è necessario impostare le funzioni o le formule personalizzate utilizzando le funzioni aggiuntive.

 Aspose.Cells fornisce funzionalità per registrare le funzioni aggiuntive utilizzando[**Fogli di lavoro.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Successivamente, quando impostiamo cell.Formula = anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il seguente file XLAM deve essere scaricato per la registrazione della funzione di aggiunta nel codice di esempio sottostante. Allo stesso modo è possibile scaricare il file di output "test_udf.xlsx" per controllare l'output.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Usando la formula di matrice**

Le formule di matrice sono formule che accettano matrici, invece di singoli numeri, come argomenti delle funzioni che compongono la formula. Quando viene visualizzata una formula di matrice, è racchiusa tra parentesi graffe ({}).

Alcune funzioni di Excel Microsoft restituiscono matrici di valori. Per calcolare più risultati con una formula di matrice, inserisci la matrice in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti della matrice.

 È possibile applicare una formula di matrice a una cella chiamando il metodo[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) metodo. Il[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) metodo accetta i seguenti parametri:

- **Formula matrice**la formula di matrice.
- **Numero di righe**, il numero di righe da popolare risultato della formula di matrice.
- **Numero di colonne**il numero di colonne da popolare risultato della formula di matrice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Utilizzando la formula R1C1**

 Aggiungi un**R1C1** formula di stile di riferimento a una cella con il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Formula R1C1**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Argomenti avanzati**
- [Precedenti e dipendenti](/cells/it/net/precedents-and-dependents/)
- [Imposta collegamenti esterni nelle formule](/cells/it/net/set-external-links-in-formulas/)
- [Propaga automaticamente la formula nella tabella o nell'oggetto elenco durante l'inserimento dei dati in nuove righe](/cells/it/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Impostazione della formula per l'intervallo denominato](/cells/it/net/setting-formula-for-named-range/)
- [Impostazione delle formule - Avviso per gli utenti non inglesi](/cells/it/net/setting-formulas-notice-for-non-english-users/)
- [Impostazione della formula condivisa](/cells/it/net/setting-shared-formula/)
- [Specifica il numero massimo di righe della formula condivisa](/cells/it/net/specify-maximum-rows-of-shared-formula/)
- [Funzioni di Excel supportate](/cells/it/net/supported-formula-functions/)

