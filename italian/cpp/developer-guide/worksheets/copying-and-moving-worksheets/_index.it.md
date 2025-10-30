---
title: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 10
url: /it/cpp/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

A volte è necessario avere un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se si lavora con budget trimestrali, potrebbe essere necessario creare un libro con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento dei fogli di lavoro all'interno o tra i workbook. Un foglio di lavoro, completo di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, viene copiato con il massimo grado di precisione.

{{% /alert %}} 
## **Spostare o Copiare Fogli Usando Microsoft Excel**
Di seguito sono elencati i passaggi coinvolti nella copia e nello spostamento dei fogli di lavoro all'interno o tra i workbook in Microsoft Excel.

1. Per spostare o copiare i fogli in un altro libro, aprire il libro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o Copia Foglio**.
1. Nella finestra di dialogo **Al libro**, fare clic sul workbook per ricevere i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo workbook, fare clic su **Nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli anziché spostarli, selezionare la casella **Crea copia**.
### **Copiare Fogli di Lavoro all'interno di un Workbook con Aspose.Cells**
Aspose.Cells fornisce un metodo sovraccaricato [AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/) che viene utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo prende l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine. L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di un workbook.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
### **Sposta i fogli di lavoro all'interno del libro di lavoro**
Aspose.Cells fornisce un metodo [MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/) che viene utilizzato per spostare un foglio di lavoro in un'altra posizione nella stessa cartella di lavoro. Il metodo prende l'indice del foglio di lavoro di destinazione come parametro. L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del workbook.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
