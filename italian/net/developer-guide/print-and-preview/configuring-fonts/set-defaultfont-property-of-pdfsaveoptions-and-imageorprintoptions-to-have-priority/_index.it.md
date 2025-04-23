---
title: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per avere la priorità
type: docs
weight: 30
url: /it/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Possibili Scenari di Utilizzo**

Mentre si imposta la proprietà **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), potresti aspettarti che il salvataggio in PDF o immagine imposti quel DefaultFont a tutto il testo in un foglio di lavoro che ha un carattere mancante (non installato).

In generale, durante il salvataggio in PDF o immagine, Aspose.Cells cercherà prima di impostare il carattere predefinito del foglio di lavoro (cioè, Workbook.DefaultStyle.Font). Se il carattere predefinito del foglio di lavoro non riesce ancora a mostrare/rappresentare correttamente il testo, allora Aspose.Cells cercherà di rappresentare con il carattere menzionato nel attributo DefaultFont in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

Per far fronte alle tue aspettative, abbiamo una proprietà booleana chiamata "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Puoi impostarla su **false** per disabilitare il tentativo del carattere predefinito del foglio di lavoro o lasciare che l'impostazione **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) abbia la priorità.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

Il seguente esempio di codice apre un file Excel. La cella A1 (nel primo foglio di lavoro) contiene un testo impostato su "Testo carattere Christmas Time". Il nome del carattere è "Christmas Time Personal Use" che non è installato sulla macchina. Abbiamo impostato l'attributo ***DefaultFont*** di [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)  su "Times New Roman". Abbiamo anche impostato la proprietà booleana **CheckWorkbookDefaultFont** su **"false"** che garantisce che il testo della cella A1 venga rappresentato con il carattere "Times New Roman" e non dovrebbe utilizzare il carattere predefinito del foglio di lavoro ("Calibri" in questo caso). Il codice rappresenta il primo foglio di lavoro nei formati di immagine PNG e TIFF. Infine rappresenta in un formato di file PDF.

{{% alert color="primary" %}}

Il valore predefinito dell'attributo ***CheckWorkbookDefaultFont*** è **true**.

{{% /alert %}}

Questa è la schermata del file di [modello](49446913.xlsx) utilizzato nel codice di esempio.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Questa è l'immagine PNG di output dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) su "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Vedi l'immagine TIFF di output dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) su "Times New Roman".

Vedi il file [PDF](48496673.pdf) di output dopo aver impostato la proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) su "Times New Roman".

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
{{< app/cells/assistant language="csharp" >}}
