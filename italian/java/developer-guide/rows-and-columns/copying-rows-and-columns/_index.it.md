---
title: Copiatura di righe e colonne
type: docs
weight: 30
url: /it/java/copying-rows-and-columns/
---

## **Introduzione**
A volte è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells, è possibile copiare righe e colonne all'interno o tra i fogli di lavoro.

Quando viene copiata una riga (o colonna), vengono copiati anche i dati contenuti al suo interno, inclusi formule - con riferimenti aggiornati - e valori, commenti, formattazione, celle nascoste, immagini e altri oggetti grafici.
## **Copiatura di righe e colonne con Microsoft Excel**
1. Seleziona la riga o la colonna che desideri copiare.
1. Per copiare righe o colonne, fai clic su **Copia** sulla barra degli strumenti **Standard**, oppure premi **CTRL**+**C**.
1. Seleziona una riga o una colonna sotto o alla destra di dove desideri copiare la tua selezione.
1. Quando stai copiando righe o colonne, fai clic su **Celle Copiate** nel menu **Inserisci**.

{{% alert color="primary" %}} 

Se fai clic su **Incolla** sulla barra degli strumenti **Standard** o premi **CTRL**+**V** anziché fare clic su un comando nel menu **Inserisci**, i contenuti delle celle di destinazione vengono sostituiti.

{{% /alert %}} 

## **Copia di una singola riga**

Aspose.Cells fornisce il metodo [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) della classe [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti grafici dalla riga di origine alla riga di destinazione.

Il metodo [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) richiede i seguenti parametri:

- l'oggetto [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) di origine,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

Usa questo metodo per copiare una riga all'interno di un foglio, o verso un altro foglio. Il metodo [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, tale valore viene copiato anche.

Nell'esempio seguente viene mostrato come copiare una riga in un foglio di lavoro. Utilizza un file modello di Microsoft Excel e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga nello stesso foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



L'output seguente viene generato quando il codice sottostante viene eseguito.

**La riga viene copiata con il massimo grado di precisione e accuratezza** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Quando si copiano le righe, è importante notare immagini correlate, grafici o altri oggetti disegnati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc., vengono copiati se sono contenuti nelle tre righe (l'indice della riga di inizio è 4 e l'indice della riga di fine è 6).
1. Le immagini, i grafici, ecc., esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}} 

## **Copia di più righe**

È inoltre possibile copiare più righe su una nuova destinazione utilizzando il metodo [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) che richiede un parametro aggiuntivo di tipo integer per specificare il numero di righe di origine da copiare.

Di seguito è presentato uno snapshot del foglio di calcolo di input contenente 3 righe di dati, mentre il frammento di codice fornito di seguito copia tutte e 3 le righe in una nuova posizione a partire dalla 7ª riga.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Ecco la visualizzazione del foglio di calcolo risultante dopo l'esecuzione del frammento di codice sopra.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Copia di una singola colonna**

Aspose.Cells fornisce il metodo [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) della classe [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), questo metodo copia tutti i tipi di dati, inclusi formule - con riferimenti aggiornati - e valori, commenti, formati delle celle, celle nascoste, immagini ed altri oggetti disegnati dalla colonna di origine a quella di destinazione.

Il metodo [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) accetta i seguenti parametri:

- l'oggetto [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) di origine,
- l'indice della colonna di origine e
- l'indice della colonna di destinazione.

Usa il metodo [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) per copiare una colonna all'interno di un foglio, o verso un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un altro documento.

**Viene copiata una colonna da un altro foglio di lavoro** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copia di più colonne**

Similmente al metodo [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)), le API di Aspose.Cells forniscono anche il metodo [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) per copiare più colonne di origine in una nuova posizione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Ecco come si presentano i fogli di calcolo di origine e risultante in Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Incollaggio di righe/colonne con opzioni di incolla**
Aspose.Cells fornisce ora [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) durante l'utilizzo delle funzioni [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) e [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Consente di impostare opportune opzioni di incolla simili a Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

