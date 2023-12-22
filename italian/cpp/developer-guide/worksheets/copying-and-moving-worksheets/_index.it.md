---
title: Copiare e spostare fogli di lavoro
type: docs
weight: 10
url: /it/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

A volte è necessario un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare una cartella di lavoro con fogli che contengono le stesse intestazioni di colonna, intestazioni di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento di fogli di lavoro all'interno o tra cartelle di lavoro. Un foglio di lavoro, completo di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}} 
##  **Spostamento o copia di fogli utilizzando Microsoft Excel**
Di seguito sono riportati i passaggi necessari per copiare e spostare fogli di lavoro all'interno o tra cartelle di lavoro in Microsoft Excel.

1. Per spostare o copiare i fogli in un'altra cartella di lavoro, aprire la cartella di lavoro che riceverà i fogli.
1. Passa alla cartella di lavoro che contiene i fogli che desideri spostare o copiare, quindi seleziona i fogli.
1.  Sul**Modificare** menu, fare clic su *Sposta o copia foglio**.
1. Nel**Prenotare** finestra di dialogo, fare clic sulla cartella di lavoro per ricevere i fogli.
1. Per spostare o copiare i fogli selezionati in una nuova cartella di lavoro, fare clic su *Nuovo libro**.
1. Nel**Prima del foglio** casella, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1.  Per copiare i fogli invece di spostarli, seleziona il file**Crea una copia** casella di controllo.
###  **Copia fogli di lavoro all'interno di una cartella di lavoro con Aspose.Cells**
 Aspose.Cells fornisce un metodo sovraccaricato[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo accetta come parametro l'indice del foglio di lavoro di origine. L'altra versione prende il nome del foglio di lavoro di origine. L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di una cartella di lavoro.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Sposta i fogli di lavoro all'interno della cartella di lavoro**
 Aspose.Cells fornisce un metodo[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di calcolo. Il metodo accetta l'indice del foglio di lavoro di destinazione come parametro. L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno della cartella di lavoro.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
