---
title: Salva la cartella di lavoro in formato testo o CSV in Aspose.Cells
type: docs
weight: 110
url: /it/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---
{{% alert color="primary" %}} 

A volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio di lavoro attivo.

{{% /alert %}} 

L'esempio di codice seguente spiega come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine che potrebbe essere qualsiasi file di foglio di calcolo di Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nella cartella di lavoro in formato TXT.

Puoi modificare lo stesso esempio per salvare il tuo file in formato CSV. Per impostazione predefinita, TxtSaveOptions.Separator è una virgola, quindi non specificare un separatore se si salva in formato CSV.

**C#**

{{< highlight "csharp" >}}

 string filePath = "source.xlsx";

//Carica la cartella di lavoro di origine

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro(filePath);

//array da 0 byte

byte[]workbookData = nuovo byte[0];

// Opzioni di salvataggio del testo. È possibile utilizzare qualsiasi tipo di separatore

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copia i dati di ogni foglio di lavoro in formato testo all'interno dell'array di dati della cartella di lavoro

 per (int idx = 0; idx< workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
