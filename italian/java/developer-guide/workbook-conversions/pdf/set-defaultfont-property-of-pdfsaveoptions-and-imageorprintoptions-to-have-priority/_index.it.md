---
title: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per avere la priorità
type: docs
weight: 30
url: /it/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Possibili Scenari di Utilizzo**

Mentre imposti la proprietà **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), potresti aspettarti che il salvataggio in PDF o immagine imposti quel **DefaultFont** a tutti i testi nel foglio di lavoro che hanno un tipo di carattere mancante (non installato).

In generale, quando si salva in PDF o immagine, Aspose.Cells tenterà prima di impostare il font predefinito del Workbook (cioè, [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)). Se il font predefinito del workbook ancora non mostra/rende correttamente il testo, allora Aspose.Cells tenterà di renderlo con il font indicato nell'attributo **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Per soddisfare le tue aspettative, abbiamo una proprietà booleana chiamata "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Puoi impostarla su falso per disabilitare il tentativo del tipo di carattere predefinito del foglio di calcolo o lasciare che l'impostazione **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) abbia la priorità.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

Il codice di esempio seguente apre un file Excel. La cella A1 (nel primo foglio di lavoro) ha un testo impostato su "Testo del font di Natale". Il nome del font è "Christmas Time Personal Use" che non è installato sulla macchina. Impostiamo l'attributo **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) su "Times New Roman". Impostiamo anche la proprietà booleana **CheckWorkbookDefaultFont** su "**false**" che assicura che il testo della cella A1 venga reso con il font "Times New Roman" e non utilizzi il font predefinito del foglio di lavoro ("Calibri" in questo caso). Il codice rende il primo foglio di lavoro nei formati immagine PNG e TIFF. Infine, lo rende nel formato di file PDF.

{{% alert color="primary" %}}

Il valore predefinito dell'attributo ***CheckWorkbookDefaultFont*** è **true**.

{{% /alert %}}

Questa è la schermata del [file di modello](49446914.xlsx) usato nel codice di esempio.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Questa è l'immagine PNG di output dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Guarda l'immagine di output [TIFF](out1_imageTIFF.tiff) dopo aver impostato la proprietà [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) su "Times New Roman".

Guarda il file di output [PDF](out1_pdf.pdf) dopo aver impostato la proprietà [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) su "Times New Roman".

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
