---
title: Copia foglio all'interno della cartella di lavoro
type: docs
weight: 40
url: /it/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - Spostamento o copia di fogli all'interno della cartella di lavoro**
Di seguito sono riportati i passaggi necessari per copiare e spostare i fogli di lavoro all'interno o tra le cartelle di lavoro.

1. Per spostare o copiare fogli all'interno o tra cartelle di lavoro, aprire la cartella di lavoro che riceverà i fogli.
1. Passare alla cartella di lavoro che contiene i fogli che si desidera spostare o copiare e quindi selezionare i fogli.
1.  Sul**Modificare** menu, fare clic**Sposta o copia foglio**.
1. Nella casella Per prenotare fare clic sulla cartella di lavoro per ricevere i fogli.
1.  Per spostare o copiare i fogli selezionati in una nuova cartella di lavoro, fare clic su**nuovo libro**.
1.  Nel**Prima foglio** fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1.  Per copiare i fogli invece di spostarli, seleziona il file**Crea una copia** casella di controllo.
## **Aspose.Cells - Copia foglio all'interno della cartella di lavoro**
{{% alert color="primary" %}} 

Aspose.Cells fornisce un metodo di overload, WorksheetCollection.addCopy(), utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo accetta l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine.

L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di una cartella di lavoro.

{{% /alert %}} 

Copiare fogli utilizzando Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copia foglio all'interno della cartella di lavoro**
{{% alert color="primary" %}} 

Workbook.cloneSheet() viene utilizzato per copiare i fogli con la cartella di lavoro.

{{% /alert %}} 

Copia i fogli utilizzando Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featuresconfrontison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Copiare e spostare fogli di lavoro](/cells/it/java/copying-and-moving-worksheets).

{{% /alert %}}
