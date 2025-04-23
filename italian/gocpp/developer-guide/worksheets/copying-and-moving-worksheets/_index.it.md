---
title: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 10
url: /it/go-cpp/copying-and-moving-worksheets/
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

Aspose.Cells fornisce un metodo sovraccaricato [AddCopy()](https://reference.aspose.com/cells/go-cpp/worksheetcollection/addcopy_string/) usato per aggiungere un foglio di lavoro alla collezione e copiare i dati da un foglio di lavoro esistente. Una versione del metodo prende in input l'indice del foglio di lavoro sorgente. L'altra versione prende il nome del foglio di lavoro sorgente. L'esempio seguente mostra come copiare un foglio di lavoro esistente all’interno di un libro di lavoro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyWorksheetsWithinWorkbook.go" >}}

### **Sposta i fogli di lavoro all'interno del libro di lavoro**

Aspose.Cells fornisce un metodo [MoveTo()](https://reference.aspose.com/cells/go-cpp/worksheet/moveto/) usato per spostare un foglio di lavoro in un’altra posizione nello stesso file di Excel. Il metodo prende come parametro l’indice del foglio di lavoro di destinazione. L’esempio seguente mostra come spostare un foglio di lavoro in un’altra posizione all’interno del libro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MoveWorksheetsWithinWorkbook.go" >}}
