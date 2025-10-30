---
title: Copiatura di righe e colonne
type: docs
weight: 20
url: /it/cpp/copying-rows-and-columns/
---

## **Introduzione**
A volte è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells, è possibile copiare righe e colonne all'interno o tra cartelle di lavoro.
Quando viene copiata una riga (o colonna), vengono copiati anche i dati in essa contenuti, comprese formule - con riferimenti aggiornati - e valori, commenti, formattazioni, celle nascoste, immagini e altri oggetti disegnati.
## **Copiatura di righe e colonne con Microsoft Excel**
1. Seleziona la riga o la colonna che desideri copiare.
1. Per copiare righe o colonne, fai clic su **Copia** sulla barra degli strumenti **Standard**, oppure premi **CTRL**+**C**.
1. Seleziona una riga o una colonna sotto o alla destra di dove desideri copiare la tua selezione.
1. Quando stai copiando righe o colonne, fai clic su **Celle Copiate** nel menu **Inserisci**.

{{% alert color="primary" %}} 

Se fai clic su **Incolla** sulla barra degli strumenti **Standard** oppure premi **CTRL**+**V** anziché fare clic su un comando nel menu **Inserisci**, il contenuto delle celle di destinazione verrà sostituito.

{{% /alert %}} 
## **Usare Aspose.Cells**
### **Copia delle Righe**
Aspose.Cells fornisce il metodo CopyRow della classe Aspose::Cells::ICells. Questo metodo copia tutti i tipi di dati, inclusi formule, valori, commenti, formati delle celle, celle nascoste, immagini e altri oggetti grafici dalla riga di origine alla riga di destinazione.

Il metodo CopyRow richiede i seguenti parametri:

- l'oggetto di origine Cells,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

Utilizza questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il metodo CopyRow funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, quel valore viene copiato automaticamente.

Nell'esempio seguente viene mostrato come copiare una riga in un foglio di lavoro. Viene utilizzato un file modello di Microsoft Excel e viene copiata la seconda riga (completa di dati, formattazione, commenti, immagini e altro) e incollata nella dodicesima riga nello stesso foglio di lavoro.

È possibile omettere il passaggio che ottiene l'altezza della riga di origine utilizzando il metodo **GetRowHeigh** e poi imposta l'altezza della riga di destinazione utilizzando il metodo **SetRowHeight** poiché il metodo **CopyRow** si occupa automaticamente dell'altezza della riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

Quando si copiano righe, è importante notare le immagini, i grafici o altri oggetti grafici correlati, poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc., viene copiato se è contenuto nelle tre righe (l'indice della riga di inizio è 4 e l'indice della riga finale è 6).
1. Le immagini, i grafici, ecc. esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}} 
### **Copia delle Colonne**
Aspose.Cells fornisce il metodo CopyColumn della classe Aspose::Cells::ICells, questo metodo copia tutti i tipi di dati, inclusi formule - con riferimenti aggiornati - e valori, commenti, formati delle celle, celle nascoste, immagini e altri oggetti grafici dalla colonna di origine alla colonna di destinazione.

Il metodo CopyColumn richiede i seguenti parametri:

- l'oggetto di origine Cells,
- l'indice della colonna di origine e
- l'indice della colonna di destinazione.

Utilizzare il metodo CopyColumn per copiare una colonna all'interno di un foglio o in un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un altro documento.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
