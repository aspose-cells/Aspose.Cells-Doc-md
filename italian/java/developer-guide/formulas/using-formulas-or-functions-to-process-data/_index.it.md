---
title: Utilizzo di formule o funzioni per elaborare i dati
type: docs
weight: 5
url: /it/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Una delle funzionalità più interessanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce un insieme di funzioni e formule integrate che aiutano gli utenti a eseguire rapidamente calcoli complessi. Aspose.Cells fornisce anche un vasto insieme di funzioni e formule integrate che aiutano i programmatori a calcolare facilmente i valori. Aspose.Cells supporta anche le funzioni di complemento. Inoltre, Aspose.Cells supporta le formule matriciali e R1C1 in Aspose.Cells.

{{% /alert %}}

## **Utilizzo di formule e funzioni**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente di accedere a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Ogni elemento nella raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

È possibile applicare formule alle celle utilizzando le proprietà e i metodi offerti dalla classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), discussi in dettaglio di seguito.

- [Utilizzo di funzioni integrate](/cells/it/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Utilizzo di funzioni di complemento](/cells/it/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Lavoro con formule matriciali](/cells/it/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Creazione di una formula R1C1](/cells/it/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Utilizzo di funzioni integrate**

Le funzioni integrate o le formule vengono fornite come funzioni predefinite per ridurre gli sforzi e il tempo dei programmatori. Consulta [un elenco di funzioni integrate](/cells/it/java/supported-formula-functions/). Le funzioni sono elencate in ordine alfabetico. Ulteriori funzioni saranno supportate in futuro.

Aspose.Cells supporta la maggior parte delle formule o funzioni offerte da Microsoft Excel. I programmatori possono utilizzare queste formule attraverso l'API o il [foglio di calcolo del designer](/cells/it/java/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un vasto insieme di formule matematiche, stringhe, booleane, data/ora, statistiche, database, ricerche e riferimento.

Usa la proprietà [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) per aggiungere una formula a una cella. **Le formule complesse**, ad esempio

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportate anche in Aspose.Cells. Quando si applica una formula a una cella, inizia sempre la stringa con un segno uguale (=) come fai quando crei una formula in Microsoft Excel e utilizza una virgola (,) per delimitare i parametri della funzione.

Nell'esempio seguente, viene applicata una formula complessa alla prima cella della raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) di un foglio di lavoro. La formula utilizza una funzione **IF** integrata fornita da Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Utilizzo delle funzioni di Add-in**

Possiamo avere alcune formule definite dall'utente che vogliamo includere come add-in di Excel. Quando si imposta la funzione incorporata [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) le funzioni integrate funzionano bene, tuttavia c'è bisogno di impostare le funzioni o formule personalizzate utilizzando le funzioni di add-in.

Aspose.Cells fornisce funzionalità per registrare le funzioni di add-in utilizzando [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). In seguito, quando impostiamo [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Il file XLAM seguente verrà scaricato per registrare la funzione di add-in nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per verificare l'output.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Utilizzo della Formula Array**

Le formule array sono formule che lavorano con array, invece di numeri individuali, come argomenti delle funzioni che compongono la formula. Quando una formula array viene visualizzata, è circondata da parentesi graffe ({}) come mostrato di seguito.

**Impostare una formula array sulla cella G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Alcune funzioni di Microsoft Excel restituiscono array di valori. Per calcolare più risultati con una formula matriciale, inserisci l'array in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti dell'array.

È possibile applicare una formula array a una cella chiamando il metodo [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Il metodo [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) accetta i seguenti parametri:

- **Formula Matriciale**, la formula matriciale.
- **Numero di righe**, il numero di righe per popolare il risultato della formula matriciale.
- **Numero di Colonne**, il numero di colonne per popolare il risultato della formula array.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Utilizzo della Formula R1C1**

Applicare una formula di stile di riferimento **R1C1** a una cella con la proprietà [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) della classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

