﻿---
title: Copiare e spostare fogli di lavoro
type: docs
weight: 10
url: /it/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

A volte, hai bisogno di un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare una cartella di lavoro con fogli che contengono le stesse intestazioni di colonna, intestazioni di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento di fogli di lavoro all'interno o tra cartelle di lavoro. Un foglio di lavoro, completo di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, viene copiato con il massimo grado di precisione.

{{% /alert %}} 
## **Spostare o copiare fogli utilizzando Microsoft Excel**
Di seguito sono riportati i passaggi necessari per copiare e spostare i fogli di lavoro all'interno o tra le cartelle di lavoro in Microsoft Excel.

1. Per spostare o copiare fogli in un'altra cartella di lavoro, apri la cartella di lavoro che riceverà i fogli.
1. Passare alla cartella di lavoro che contiene i fogli che si desidera spostare o copiare e quindi selezionare i fogli.
1.  Sul**Modificare** menu, fare clic**Sposta o copia foglio**.
1.  Nel**Prenotare** finestra di dialogo, fare clic sulla cartella di lavoro per ricevere i fogli.
1.  Per spostare o copiare i fogli selezionati in una nuova cartella di lavoro, fare clic su**Nuovo libro**.
1.  Nel**Prima foglio** fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1.  Per copiare i fogli invece di spostarli, seleziona il file**Crea una copia** casella di controllo.
### **Copia i fogli di lavoro all'interno di una cartella di lavoro con Aspose.Cells**
 Aspose.Cells fornisce un metodo sovraccarico[AggiungiCopia()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa1e73c54ea19bb7aa0f9f197c2baa5ba)utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo accetta l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine. L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di una cartella di lavoro.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook.cpp" >}}
### **Sposta i fogli di lavoro all'interno della cartella di lavoro**
 Aspose.Cells fornisce un metodo[Sposta in()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a240bf1d3d52ea8c8bfd54ffa320921b7)utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di lavoro. Il metodo accetta l'indice del foglio di lavoro di destinazione come parametro. L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno della cartella di lavoro.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook.cpp" >}}