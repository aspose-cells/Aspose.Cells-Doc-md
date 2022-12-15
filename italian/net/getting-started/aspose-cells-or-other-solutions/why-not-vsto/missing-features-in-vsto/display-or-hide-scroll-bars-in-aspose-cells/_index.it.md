---
title: Mostra o nascondi le barre di scorrimento in Aspose.Cells
type: docs
weight: 70
url: /it/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Le barre di scorrimento sono molto utilizzate per navigare nel contenuto di qualsiasi file. Normalmente, ci sono due tipi di barre di scorrimento:

- Barre di scorrimento verticali
- Barre di scorrimento orizzontali

Microsoft Excel fornisce anche barre di scorrimento orizzontali e verticali in modo che gli utenti possano scorrere il contenuto del foglio di lavoro. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di entrambi i tipi di barre di scorrimento nei file Excel.

{{% /alert %}}

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class fornisce un'ampia gamma di proprietà e metodi per la gestione di un file Excel. Per controllare la visibilità delle barre di scorrimento, utilizzare il[**Impostazioni della cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) classe'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) proprietà.[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) e[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)sono proprietà booleane, il che significa che queste proprietà possono solo memorizzare**VERO** o**falso** i valori.

Di seguito è riportato un codice completo che apre un file Excel, book1.xls, nasconde entrambe le barre di scorrimento e quindi salva il file modificato come output.xls .

Lo screenshot seguente mostra il file Book1.xls contenente entrambe le barre di scorrimento. Il file modificato viene salvato come file output.xls, anch'esso mostrato di seguito.

**Book1.xls: file Excel prima di qualsiasi modifica**

![cose da fare:immagine_alt_testo](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: file Excel dopo la modifica**

![cose da fare:immagine_alt_testo](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Scarica il codice di esempio**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
