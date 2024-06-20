---
title: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 10
url: /it/net/copying-and-moving-worksheets/
description: Questo articolo include codice di esempio e descrive come copiare e spostare le schede in modo programmato sia all interno di un workbook di Excel che tra i workbook di Excel utilizzando l API C# o la libreria .NET.
keywords: copia scheda c#, sposta scheda c#
---

{{% alert color="primary" %}}

A volte è necessario avere un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se si lavora con budget trimestrali, potrebbe essere necessario creare un libro con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento dei fogli di lavoro all'interno o tra cartelle di lavoro. I fogli di lavoro, completi di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Spostare o Copiare Fogli Usando Microsoft Excel**

Di seguito sono riportati i passaggi coinvolti nella copia e nel trasferimento dei fogli di lavoro all'interno o tra i fogli di lavoro in Microsoft Excel.

1. Per spostare o copiare i fogli in un altro libro, aprire il libro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o Copia Foglio**.
1. Nella finestra di dialogo **Al libro**, fare clic sul workbook per ricevere i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo workbook, fare clic su **Nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli anziché spostarli, selezionare la casella **Crea copia**.

### **Copiare Fogli di Lavoro all'interno di un Workbook con Aspose.Cells**

Aspose.Cells fornisce un metodo sovraccaricato, [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index), che viene utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo prende l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **Copiare i Fogli di Lavoro tra Cartelle di Lavoro**

Aspose.Cells fornisce un metodo, [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) utilizzato per copiare dati e formattazione da un foglio di lavoro di origine a un altro foglio di lavoro all'interno o tra i fogli di lavoro. Il metodo prende l'oggetto del foglio di lavoro di origine come parametro.

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **Sposta i fogli di lavoro all'interno del libro di lavoro**

Aspose.Cells fornisce un metodo [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) che viene utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di calcolo. Il metodo prende l'indice del foglio di lavoro di destinazione come parametro.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del libro di lavoro.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
