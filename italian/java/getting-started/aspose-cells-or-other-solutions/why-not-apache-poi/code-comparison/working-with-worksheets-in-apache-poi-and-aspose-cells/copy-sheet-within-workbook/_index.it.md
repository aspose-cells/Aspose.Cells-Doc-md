---
title: Copia foglio all interno del libro
type: docs
weight: 40
url: /it/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Spostare o Copiare fogli all'interno del libro**
Di seguito sono riportati i passaggi coinvolti per copiare e spostare i fogli di lavoro all'interno o tra cartelle di lavoro.

1. Per spostare o copiare i fogli all'interno o tra cartelle di lavoro, apri la cartella di lavoro che riceverà i fogli.
1. Passare al libro che contiene i fogli da spostare o copiare, e quindi selezionare i fogli.
1. Nel menu **Modifica**, fare clic su **Sposta o Copia Foglio**.
1. Nella casella Di libro, fare clic sul libro che riceverà i fogli.
1. Per spostare o copiare i fogli selezionati in un nuovo libro, fare clic su **nuovo libro**.
1. Nella casella **Prima del foglio**, fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1. Per copiare i fogli invece di spostarli, seleziona la casella di controllo **Crea una copia**.
## **Aspose.Cells - Copia foglio all'interno del libro**
{{% alert color="primary" %}} 

Aspose.Cells fornisce un metodo sovraccaricato, WorksheetCollection.addCopy(), che viene utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo richiede l'indice del foglio di lavoro di origine come parametro. L'altra versione richiede il nome del foglio di lavoro di origine.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.

{{% /alert %}} 

Copia fogli utilizzando Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copia foglio all'interno del workbook**
{{% alert color="primary" %}} 

Workbook.cloneSheet() è utilizzato per copiare fogli all'interno del workbook.

{{% /alert %}} 

Copia fogli utilizzando Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visitare [Copia e Spostamento dei Fogli di Lavoro](/cells/it/java/copying-and-moving-worksheets).

{{% /alert %}}
