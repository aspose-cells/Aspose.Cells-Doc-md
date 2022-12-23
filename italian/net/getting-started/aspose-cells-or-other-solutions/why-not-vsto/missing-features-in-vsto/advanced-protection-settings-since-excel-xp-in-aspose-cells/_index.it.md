---
title: Impostazioni di protezione avanzata da Excel XP in Aspose.Cells
type: docs
weight: 20
url: /it/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Elimina righe o colonne.
- Modifica contenuti, oggetti o scenari.
- Formatta celle, righe o colonne.
- Inserisci righe, colonne o collegamenti ipertestuali.
- Seleziona le celle bloccate o sbloccate.
- Usa le tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni di protezione avanzate offerte da Excel XP o versioni successive.

{{% /alert %}}

## **Impostazioni di protezione avanzata tramite Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1.  Dal**Utensili** menù, selezionare**Protezione** seguito da**Proteggi Foglio**.
 Viene visualizzata una finestra di dialogo.

   **Finestra di dialogo per mostrare le opzioni di protezione in Excel XP**

![cose da fare:immagine_alt_testo](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Consenti o limita le funzionalità dei fogli di lavoro o applica una password.

### **Impostazioni di protezione avanzata utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni di protezione avanzate.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe.

 Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce il[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)proprietà utilizzata per applicare queste impostazioni di protezione avanzate. Il[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la proprietà è infatti un oggetto del[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/protection) classe che incapsula diverse proprietà booleane per disabilitare o abilitare le restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni di protezione avanzate supportate da Excel XP e versioni successive.

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
