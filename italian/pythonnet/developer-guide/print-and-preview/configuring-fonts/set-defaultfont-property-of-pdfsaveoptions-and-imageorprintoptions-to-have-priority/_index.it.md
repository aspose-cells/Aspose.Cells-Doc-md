---
title: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per avere la priorità
type: docs
weight: 30
url: /it/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Possibili Scenari di Utilizzo**

Mentre si imposta la proprietà **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), potresti aspettarti che il salvataggio in PDF o immagine imposti quel DefaultFont a tutto il testo in un foglio di lavoro che ha un carattere mancante (non installato).

In generale, quando si salva in PDF o immagine, Aspose.Cells per Python via .NET cercherà prima di impostare il font predefinito del Workbook (cioè, Workbook.DefaultStyle.Font). Se il font predefinito del workbook ancora non può mostrare/renderizzare correttamente il testo, Aspose.Cells per Python via .NET tenterà di renderizzare con il font indicato contro l'attributo DefaultFont in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

Per soddisfare le tue aspettative, abbiamo una proprietà booleana chiamata "**check_workbook_default_font**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Puoi impostarla su **false** per disabilitare il tentativo con il font predefinito del workbook o permettere alla impostazione **default_font** in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) di avere priorità.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

Il seguente esempio di codice apre un file Excel. La cella A1 (nel primo foglio di lavoro) ha un testo impostato su "Christmas Time Font text". Il nome del font è "Christmas Time Personal Use" che non è installato sulla macchina. Impostiamo l'attributo ***default_font*** di [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) su "Times New Roman". Impostiamo anche la proprietà booleana **check_workbook_default_font** su **"false"** per garantire che il testo della cella A1 venga renderizzato con il font "Times New Roman" e non venga usato il font predefinito del workbook ("Calibri" in questo caso). Il codice rende il primo foglio di lavoro in formati immagine PNG e TIFF. Infine, rende in formato PDF.

{{% alert color="primary" %}}

Il valore predefinito dell'attributo ***CheckWorkbookDefaultFont*** è **true**.

{{% /alert %}}

Questa è la schermata del file di [modello](49446913.xlsx) utilizzato nel codice di esempio.

![todo:image_alt_text](1.png)

Questa è l'immagine PNG di output dopo aver impostato la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su "Times New Roman".

![todo:image_alt_text](2.png)

Vedi l'immagine TIFF di output dopo aver impostato la proprietà [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) su "Times New Roman".

Vedi il file [PDF](48496673.pdf) di output dopo aver impostato la proprietà [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) su "Times New Roman".

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
