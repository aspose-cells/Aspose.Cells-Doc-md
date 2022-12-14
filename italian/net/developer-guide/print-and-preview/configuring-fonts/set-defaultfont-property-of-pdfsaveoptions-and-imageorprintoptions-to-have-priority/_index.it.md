---
title: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions in modo che abbia la priorità
type: docs
weight: 30
url: /it/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Possibili scenari di utilizzo**

 Durante l'impostazione del**Carattere predefinito** proprietà di**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** e**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, potresti aspettarti che il salvataggio in PDF o immagine imposti DefaultFont su tutto il testo in una cartella di lavoro con un carattere mancante (non installato).

 Generalmente, durante il salvataggio in PDF o immagine, Aspose.Cells tenterà prima di impostare il carattere predefinito della cartella di lavoro (ad esempio, Workbook.DefaultStyle.Font). Se il carattere predefinito della cartella di lavoro non è ancora in grado di mostrare/visualizzare correttamente il testo, allora Aspose.Cells proverà a eseguire il rendering con il carattere menzionato rispetto all'attributo DefaultFont in**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Per far fronte alle tue aspettative, abbiamo una proprietà booleana denominata "**CheckWorkbookDefaultFont** " in**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Puoi impostarlo su**falso**per disabilitare il tentativo di utilizzare il carattere predefinito della cartella di lavoro o lasciare che il file**Carattere predefinito** sistemarsi**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** avere la precedenza.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

 Il codice di esempio seguente apre un file Excel. La cella A1 (nel primo foglio di lavoro) ha un testo impostato su "Christmas Time Font text". Il nome del font è "Christmas Time Personal Use" che non è installato sulla macchina. Prepariamo***Carattere predefinito*** attributo di**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** al "Times New Roman". Abbiamo anche impostato**CheckWorkbookDefaultFont** Proprietà booleana a**"falso"** che garantisce che il testo della cella A1 sia reso con il carattere "Times New Roman" e non dovrebbe utilizzare il carattere predefinito della cartella di lavoro ("Calibri" in questo caso). Il codice esegue il rendering del primo foglio di lavoro nei formati immagine PNG e TIFF. Infine esegue il rendering in un formato di file PDF.

{{% alert color="primary" %}}

 Il valore predefinito di***CheckWorkbookDefaultFont*** attributo è**VERO**.

{{% /alert %}}

 Questo è lo screenshot del[file modello](49446913.xlsx) utilizzato nel codice di esempio.

![cose da fare:immagine_alt_testo](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Questa è l'immagine PNG di output dopo aver impostato il file**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**proprietà a "Times New Roman".

![cose da fare:immagine_alt_testo](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Guarda l'uscita[TIPO](48496672.tiff) immagine dopo aver impostato il**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**proprietà a "Times New Roman".

Guarda l'uscita[PDF](48496673.pdf)file dopo aver impostato il file**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**proprietà a "Times New Roman".

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
