---
title: Mostra o nascondi le linee della griglia in Aspose.Cells
type: docs
weight: 50
url: /it/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Tutti i fogli di lavoro di Excel hanno una griglia per impostazione predefinita. Aiutano a delineare le celle, in modo che sia facile inserire dati in celle particolari. Le linee della griglia ci consentono di visualizzare un foglio di lavoro come una raccolta di celle, in cui ogni cella è facilmente identificabile.

{{% /alert %}}

## **Controllo della visibilità delle linee della griglia**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle linee della griglia, utilizzare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) proprietà.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) è una proprietà booleana, il che significa che può memorizzare solo a**VERO** o**falso** valore.

 Di seguito viene fornito un esempio completo che dimostra l'uso del formato[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) proprietà del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class per nascondere le linee della griglia del primo foglio di lavoro del file Excel.

Nello screenshot qui sotto, puoi vedere che il file Book1.xls contiene tre fogli di lavoro: Sheet1, Sheet2 e Sheet3. Tutti i fogli di lavoro hanno una griglia.

**Book1.xls: vista del foglio di lavoro prima della modifica** 

![cose da fare:immagine_alt_testo](display-or-hide-gridlines-in-aspose-cells_1.png)

Il file Book1.xls viene aperto utilizzando la classe Workbook e le griglie nel primo foglio di lavoro sono nascoste. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![cose da fare:immagine_alt_testo](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Scarica il codice di esempio**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
