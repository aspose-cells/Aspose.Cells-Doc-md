---
title: Copia di righe e colonne
type: docs
weight: 40
url: /it/net/copying-rows-and-columns/
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

## **Incollare righe e colonne utilizzando le opzioni Incolla con Microsoft Excel**

1. Seleziona le celle che contengono i dati o altri attributi che desideri copiare.
1.  Nella scheda Home, fare clic su**copia**.
1.  Fare clic sulla prima cella nell'area in cui si desidera**incolla** quello che hai copiato.
1.  Nella scheda Home, fai clic sulla freccia accanto a**Incolla** , quindi selezionare**Incolla** Speciale.
1.  Seleziona il**opzioni** tu vuoi.

## **Utilizzando Aspose.Cells**

## **Copia di righe singole**

 Aspose.Cells fornisce il[**CopiaRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe. Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.

 Il[**CopiaRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)metodo accetta i seguenti parametri:

-  la fonte[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)oggetto,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

 Utilizzare questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il[**CopiaRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Il metodo funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, anche quel valore viene copiato.

L'esempio seguente mostra come copiare una riga in un foglio di lavoro. Utilizza un file Excel modello Microsoft e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga nello stesso foglio di lavoro.

 Puoi saltare il passaggio che ottiene l'altezza della riga di origine utilizzando il[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) metodo e quindi imposta l'altezza della riga di destinazione utilizzando il[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) metodo come il[**CopiaRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Il metodo si occupa automaticamente dell'altezza della riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Quando si copiano le righe, è importante notare le immagini, i grafici o altri oggetti di disegno correlati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc. viene copiato se è contenuto nelle tre righe (l'indice della riga iniziale è 4 e l'indice della riga finale è 6).
1. Le immagini, i grafici e così via esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}}

## **Copia di più righe**

Puoi anche copiare più righe su una nuova destinazione mentre usi il file[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)metodo che accetta un parametro aggiuntivo di tipo integer per specificare il numero di righe di origine da copiare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Copia di colonne**

 Aspose.Cells fornisce il[**Copia colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)class, questo metodo copia tutti i tipi di dati, incluse formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti di disegno dalla colonna di origine alla colonna di destinazione.

 Il[**Copia colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)metodo accetta i seguenti parametri:

-  la fonte[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)oggetto,
- indice della colonna di origine e
- l'indice della colonna di destinazione.

 Utilizzare il[**Copia colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)metodo per copiare una colonna all'interno di un foglio o in un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un'altra cartella di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Copia di più colonne**

 Simile a[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) metodo, le API Aspose.Cells forniscono anche il[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)metodo per copiare più colonne di origine in una nuova posizione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Incollare righe/colonne con le opzioni Incolla**

 Aspose.Cells ora fornisce[**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) durante l'utilizzo delle funzioni[**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) e[**Copiacolonne**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Permette di impostare l'opzione di incolla appropriata simile a Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

