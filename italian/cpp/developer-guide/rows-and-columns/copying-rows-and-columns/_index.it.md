---
title: Copia di righe e colonne
type: docs
weight: 20
url: /it/cpp/copying-rows-and-columns/
---
##  **introduzione**
A volte è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells è possibile copiare righe e colonne all'interno o tra cartelle di lavoro.
Quando una riga (o colonna) viene copiata, vengono copiati anche i dati in essa contenuti, comprese formule - con riferimenti aggiornati - e valori, commenti, formattazione, celle nascoste, immagini e altri oggetti di disegno.
##  **Copiare righe e colonne con Microsoft Excel**
1. Seleziona la riga o la colonna che desideri copiare.
1.  Per copiare righe o colonne, fare clic su**copia** sul**Standard** barra degli strumenti oppure premere**CTRL**+*C**.
1. Seleziona una riga o una colonna sotto o a destra del punto in cui desideri copiare la selezione.
1.  Quando copi righe o colonne, fai clic su**Copiato Cells** sul**Inserire** menù.

{{% alert color="primary" %}} 

 Se fai clic**Impasto** sul**Standard** barra degli strumenti o premere**CTRL**+**V** invece di fare clic su un comando nella sezione **Insert** menu, qualsiasi contenuto delle celle di destinazione viene sostituito.

{{% /alert %}} 
##  **Utilizzando Aspose.Cells**
###  **Copia di righe**
Aspose.Cells fornisce il metodo CopyRow della classe Aspose::Cells::ICells. Questo metodo copia tutti i tipi di dati inclusi formule, valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dalla riga di origine alla riga di destinazione.

Il metodo CopyRow accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

Utilizza questo metodo per copiare una riga all'interno di un foglio o su un altro foglio. Il metodo CopyRow funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, anche quel valore viene copiato.

L'esempio seguente mostra come copiare una riga in un foglio di lavoro. Utilizza un file Excel modello Microsoft e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga dello stesso foglio di lavoro.

 Puoi saltare il passaggio che ottiene l'altezza della riga di origine utilizzando il comando**OttieniAltezzaRiga** metodo e quindi imposta l'altezza della riga di destinazione utilizzando il metodo**Imposta altezza riga** metodo come il**CopiaRiga** Il metodo si prende cura automaticamente dell'altezza della riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Quando si copiano righe, è importante notare le immagini, i grafici o altri oggetti di disegno correlati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico ecc. viene copiato se è contenuto nelle tre righe (l'indice della riga iniziale è 4 e l'indice della riga finale è 6).
1. Le immagini, i grafici ecc. esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}} 
###  **Copia di colonne**
Aspose.Cells fornisce il metodo CopyColumn della classe Aspose::Cells::ICells, questo metodo copia tutti i tipi di dati, comprese le formule - con riferimenti aggiornati - e valori, commenti, formati di cella, celle nascoste, immagini e altri oggetti di disegno dall'origine colonna alla colonna di destinazione.

Il metodo CopyColumn accetta i seguenti parametri:

- l'oggetto sorgente Cells,
- indice della colonna di origine e
- l'indice della colonna di destinazione.

Utilizzare il metodo CopyColumn per copiare una colonna all'interno di un foglio o su un altro foglio.

In questo esempio viene copiata una colonna da un foglio di lavoro e incollata in un foglio di lavoro in un'altra cartella di lavoro.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
