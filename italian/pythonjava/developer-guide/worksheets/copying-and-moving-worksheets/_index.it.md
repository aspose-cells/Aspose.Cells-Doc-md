---
title: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 20
url: /it/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

A volte è necessario avere un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se si lavora con budget trimestrali, potrebbe essere necessario creare un libro con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento dei fogli di lavoro all'interno o tra i file di lavoro. I fogli di lavoro, completi di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}} 
## **Spostare o Copiare Fogli Usando Microsoft Excel**
Di seguito sono illustrati i passaggi coinvolti nella copia e nello spostamento dei fogli di lavoro all'interno o tra i file di lavoro.

1. Aprire il file di lavoro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o copia foglio**.
1. Nella casella Di libro, fare clic sul libro che riceverà i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo file di lavoro, fare clic su **nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli anziché spostarli, selezionare la casella **Crea una copia**.
### **Copiare i Fogli di Lavoro all'interno di una Cartella di Lavoro**
Aspose.Cells fornisce un metodo sovraccaricato [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) utilizzato per copiare un foglio di lavoro esistente. Una versione del metodo richiede l'indice del foglio di lavoro di origine come parametro. L'altra versione richiede il nome del foglio di lavoro di origine.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Copiare i Fogli di Lavoro tra Cartelle di Lavoro**
Aspose.Cells fornisce il metodo [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) utilizzato per copiare fogli di lavoro in altri file di lavoro. Il metodo richiede l'oggetto foglio di lavoro di origine come parametro.

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Sposta i fogli di lavoro all'interno del libro di lavoro**
Aspose.Cells fornisce il metodo [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) utilizzato per spostare un foglio di lavoro in un'altra posizione nel medesimo foglio elettronico.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del libro di lavoro.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
