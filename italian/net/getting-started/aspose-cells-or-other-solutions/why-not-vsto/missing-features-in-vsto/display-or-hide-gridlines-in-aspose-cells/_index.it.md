---
title: Mostra o Nascondi le Linee di Griglia in Aspose.Cells
type: docs
weight: 50
url: /it/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle, in modo che sia facile inserire dati in particolari celle. Le linee di griglia ci consentono di visualizzare un foglio di lavoro come una collezione di celle, dove ogni cella è facilmente identificabile.

{{% /alert %}}

## **Controllo della visibilità delle linee della griglia**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle linee di griglia, utilizzare la proprietà [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) è una proprietà booleana, il che significa che può solo memorizzare un valore **vero** o **falso**.

Di seguito è riportato un esempio completo che dimostra l'uso della proprietà [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) per nascondere le linee di griglia del primo foglio di lavoro del file Excel.

Nella schermata sottostante, puoi vedere che il file Book1.xls contiene tre fogli di lavoro: Sheet1, Sheet2 e Sheet3. Tutti i fogli di lavoro hanno linee di griglia.

**Book1.xls: visualizzazione del foglio di lavoro prima della modifica** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Il file Book1.xls viene aperto utilizzando la classe Workbook e le linee di griglia sul primo foglio di lavoro vengono nascoste. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Scarica il codice di esempio**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
