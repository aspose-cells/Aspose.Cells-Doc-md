---
title: Copia di righe e colonne
type: docs
weight: 30
url: /it/java/copying-rows-and-columns/
---
## **introduzione**
A volte, è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells, è possibile copiare righe e colonne all'interno o tra cartelle di lavoro.

Quando una riga (o colonna) viene copiata, vengono copiati anche i dati in essa contenuti, incluse formule - con riferimenti aggiornati - e valori, commenti, formattazione, celle nascoste, immagini e altri oggetti di disegno.
## **Copia di righe e colonne con Microsoft Excel**
1. Seleziona la riga o la colonna che desideri copiare.
1.  Per copiare righe o colonne, fare clic su**copia** sul**Standard** barra degli strumenti o premere**CTRL**+**C**.
1. Seleziona una riga o una colonna sotto o a destra del punto in cui desideri copiare la selezione.
1.  Quando si copiano righe o colonne, fare clic su**Copiato Cells** sul**Inserire** menù.

{{% alert color="primary" %}} 

 Se clicchi**Incolla** sul**Standard** barra degli strumenti o premere**CTRL**+** V** invece di fare clic su un comando sul file**Nel menu Inserisci**, l'eventuale contenuto delle celle di destinazione viene sostituito.

{{% /alert %}} 

## **Copia di una singola riga**

 Aspose.Cells fornisce il[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)classe. Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.

 Il[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) accetta i seguenti parametri:

-  la fonte[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)oggetto,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

 Utilizzare questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, anche quel valore viene copiato.

L'esempio seguente mostra come copiare una riga in un foglio di lavoro. Utilizza un file Excel modello Microsoft e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga nello stesso foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Il seguente output viene generato quando viene eseguito il codice seguente.

**La riga viene copiata con il massimo grado di precisione e accuratezza** 

![cose da fare:immagine_alt_testo](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Quando si copiano le righe, è importante notare le immagini, i grafici o altri oggetti di disegno correlati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc. viene copiato se è contenuto nelle tre righe (l'indice della riga iniziale è 4 e l'indice della riga finale è 6).
1. Le immagini, i grafici e così via esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}} 

## **Copia di più righe**

 Puoi anche copiare più righe su una nuova destinazione mentre usi il file[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) che accetta un parametro aggiuntivo di tipo integer per specificare il numero di righe di origine da copiare.

Di seguito è riportata un'istantanea del foglio di calcolo di input contenente 3 righe di dati, mentre lo snippet di codice fornito di seguito copia tutte e 3 le righe in una nuova posizione a partire dalla settima riga.

![cose da fare:immagine_alt_testo](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Ecco la visualizzazione del foglio di calcolo risultante dopo l'esecuzione dello snippet di codice sopra.

![cose da fare:immagine_alt_testo](copy-rows-and-columns_4.png)

## **Copia di una singola colonna**

 Aspose.Cells fornisce il[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)class, questo metodo copia tutti i tipi di dati, incluse formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti di disegno dalla colonna di origine alla colonna di destinazione.

 Il[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) accetta i seguenti parametri:

-  la fonte[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)oggetto,
- indice della colonna di origine e
- l'indice della colonna di destinazione.

 Utilizzare il[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metodo per copiare una colonna all'interno di un foglio o in un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un'altra cartella di lavoro.

**Una colonna viene copiata da una cartella di lavoro a un'altra** 

![cose da fare:immagine_alt_testo](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copia di più colonne**

 Simile a[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ), le API Aspose.Cells forniscono anche il[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) per copiare più colonne di origine in una nuova posizione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Ecco come appaiono i fogli di calcolo di origine e risultanti in Excel.

![cose da fare:immagine_alt_testo](copy-rows-and-columns_7.png)

![cose da fare:immagine_alt_testo](copy-rows-and-columns_8.png)


## **Incollare righe/colonne con le opzioni Incolla**
 Aspose.Cells ora fornisce[PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) durante l'utilizzo delle funzioni[CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) e[Copiacolonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Consente di impostare opzioni di incolla appropriate simili a Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

