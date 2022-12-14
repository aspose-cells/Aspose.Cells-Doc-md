---
title: Utilizzo di formule o funzioni per elaborare i dati
type: docs
weight: 5
url: /it/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Una delle caratteristiche interessanti di Microsoft Excel è la sua capacità di elaborare dati con formule e funzioni. Microsoft Excel fornisce una serie di funzioni e formule integrate che consentono agli utenti di eseguire rapidamente calcoli complessi. Aspose.Cells fornisce anche un vasto set di funzioni e formule integrate che aiutano gli sviluppatori a calcolare facilmente i valori. Aspose.Cells supporta anche funzioni aggiuntive. Inoltre, Aspose.Cells supporta l'array e le formule R1C1 in Aspose.Cells.

{{% /alert %}}

## **Uso di formule e funzioni**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione. Ogni elemento del[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione rappresenta un oggetto della[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 È possibile applicare formule alle celle utilizzando proprietà e metodi offerti dal[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe, discussa più dettagliatamente di seguito.

- [Utilizzo delle funzioni integrate](/cells/it/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Utilizzo delle funzioni aggiuntive](/cells/it/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Lavorare con le formule di matrice](/cells/it/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Creazione di una formula R1C1](/cells/it/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Utilizzo delle funzioni integrate**

 Le funzioni o le formule integrate vengono fornite come funzioni già pronte per ridurre gli sforzi e il tempo degli sviluppatori. Vedere[un elenco di funzioni integrate](/cells/it/java/supported-formula-functions/). Le funzioni sono elencate in ordine alfabetico. Altre funzioni saranno supportate in futuro.

 Aspose.Cells supporta la maggior parte delle formule o delle funzioni offerte da Microsoft Excel. Gli sviluppatori possono utilizzare queste formule tramite API o[foglio di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/). Aspose.Cells supporta un enorme set di formule matematiche, stringhe, booleane, data/ora, statistiche, database, di ricerca e di riferimento.

 Utilizzare il[**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)proprietà del[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class per aggiungere una formula a una cella.**Formule complesse**, Per esempio

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sono supportati anche in Aspose.Cells. Quando si applica una formula a una cella, iniziare sempre la stringa con un segno di uguale (=) come si fa quando si crea una formula in Microsoft Excel e utilizzare una virgola (,) per delimitare i parametri della funzione.

 Nell'esempio seguente, una formula complessa viene applicata alla prima cella di un foglio di lavoro[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione. La formula utilizza un built-in**SE** funzione fornita da Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Utilizzo delle funzioni aggiuntive**

 Possiamo avere alcune formule definite dall'utente che vogliamo includere come componente aggiuntivo di Excel. Quando si imposta il[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) function le funzioni integrate funzionano correttamente, tuttavia è necessario impostare le funzioni o le formule personalizzate utilizzando le funzioni aggiuntive.

 Aspose.Cells fornisce funzionalità per registrare le funzioni aggiuntive utilizzando[**Fogli di lavoro.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Successivamente, quando siamo tramontati[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, il file Excel di output contiene il valore calcolato dalla funzione AddIn.

Dopo il file XLAM deve essere scaricato per la registrazione della funzione di componente aggiuntivo nel codice di esempio sottostante. Allo stesso modo, il file di output "test_udf.xlsx" può essere scaricato per controllare l'output.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Usando la formula di matrice**

Le formule di matrice sono formule che funzionano con matrici, invece che con singoli numeri, come argomenti delle funzioni che compongono la formula. Quando viene visualizzata una formula di matrice, è racchiusa tra parentesi graffe ({}) come mostrato di seguito.

**Impostazione di una formula di matrice sulla cella G2** 

![cose da fare:immagine_alt_testo](using-formulas-or-functions-to-process-data_1.png)

Alcune funzioni di Excel Microsoft restituiscono matrici di valori. Per calcolare più risultati con una formula di matrice, inserisci la matrice in un intervallo di celle con lo stesso numero di righe e colonne degli argomenti della matrice.

 È possibile applicare una formula di matrice a una cella chiamando il metodo[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) metodo. Il[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) accetta i seguenti parametri:

- **Formula matrice**, la formula di matrice.
- **Numero di righe**il numero di righe da popolare risultato della formula di matrice.
- **Numero di colonne**, il numero di colonne per popolare il risultato della formula di matrice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Utilizzando la formula R1C1**

 Applicare un**R1C1** formula di stile di riferimento a una cella con il[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

