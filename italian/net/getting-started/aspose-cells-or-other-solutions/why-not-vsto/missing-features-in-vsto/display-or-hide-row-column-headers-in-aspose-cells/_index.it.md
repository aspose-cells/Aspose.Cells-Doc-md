---
title: Mostra o Nasconde Intestazioni di Riga Colonna in Aspose.Cells
type: docs
weight: 60
url: /it/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare singole celle. Ad esempio, le righe sono numerate - 1, 2, 3, 4, ecc. - e le colonne sono ordinate in ordine alfabetico - A, B, C, D, ecc. I valori di riga e colonna vengono visualizzati negli intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni di riga e colonna.

{{% /alert %}}

## **Controllo della visibilità dei fogli di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per controllare la visibilità delle intestazioni di riga e colonna, utilizzare la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) è una proprietà booleana, il che significa che può memorizzare solo un valore **true** o **false**.

Di seguito è fornito un esempio completo che mostra come utilizzare la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) per nascondere le intestazioni di riga e colonna sul primo foglio di lavoro in un file.

La schermata mostra Book1.xls, il file di input. Contiene tre fogli di lavoro: Sheet1, Sheet2 e Sheet3. Ogni foglio di lavoro mostra le intestazioni di riga e colonna.

**Book1.xls: foglio di lavoro prima della modifica**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls viene aperto chiamando il metodo Open della classe Workbook e le intestazioni di riga e colonna sul primo foglio di lavoro vengono nascoste. Il file modificato viene salvato come output.xls.

**Output.xls: foglio di lavoro dopo la modifica** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Scarica il codice in esecuzione**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
