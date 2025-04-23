---
title: Copiare e Spostare Fogli di Lavoro
type: docs
weight: 10
url: /it/python-net/copying-and-moving-worksheets/
description: Questo articolo include codice di esempio e descrive come copiare e spostare fogli di lavoro programmaticamente sia all interno di un workbook Excel sia tra diversi workbook utilizzando l API Aspose.Cells for Python via .NET.
keywords: Biblioteca Excel Python, copia foglio di lavoro Python, sposta foglio di lavoro Python, copia fogli di lavoro tra workbook Python, sposta fogli di lavoro all interno del workbook Python, copia fogli di lavoro tra workbook Python, copia fogli di lavoro all interno di un workbook Python.
---

{{% alert color="primary" %}}

A volte è necessario avere un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se si lavora con budget trimestrali, potrebbe essere necessario creare un libro con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells for Python via .NET supporta la copia e lo spostamento di fogli di lavoro all'interno o tra i workbook. I fogli di lavoro, completi di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, sono copiati con il massimo livello di precisione.

{{% /alert %}}

## **Come spostare o copiare fogli usando Microsoft Excel**

Di seguito sono riportati i passaggi coinvolti nella copia e nel trasferimento dei fogli di lavoro all'interno o tra i fogli di lavoro in Microsoft Excel.

1. Per spostare o copiare i fogli in un altro libro, aprire il libro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o Copia Foglio**.
1. Nella finestra di dialogo **Al libro**, fare clic sul workbook per ricevere i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo workbook, fare clic su **Nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli anziché spostarli, selezionare la casella **Crea copia**.

## **Come copiare fogli di lavoro all'interno di un workbook con Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET fornisce un metodo sovraccarico, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio esistente. Una versione del metodo prende come parametro l'indice del foglio di lavoro di origine. L'altra versione prende il nome del foglio di lavoro di origine.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Come copiare fogli di lavoro tra i workbook**

Aspose.Cells for Python via .NET fornisce un metodo, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet), utilizzato per copiare dati e formattazione da un foglio di lavoro di origine a un altro all'interno o tra i workbook. Il metodo prende come parametro l'oggetto del foglio di lavoro di origine.

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Come spostare fogli di lavoro all'interno del workbook**

Aspose.Cells for Python via .NET fornisce un metodo [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di calcolo. Il metodo prende come parametro l'indice del foglio di lavoro di destinazione.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno del libro di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
