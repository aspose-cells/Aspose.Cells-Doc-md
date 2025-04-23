---
title: Stampa e anteprima del libro
linktitle: Stampa e anteprima
type: docs
weight: 70
url: /it/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells per Python via .NET supporta la stampa e l anteprima di file Excel senza installazione di Microsoft Excel.
---

{{% alert color="primary" %}}

Dopo aver creato un foglio di lavoro, spesso si desidera stampare una copia fisica. Questo articolo spiega come stampare fogli di calcolo con Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Introduzione alla stampa**

Microsoft Excel presume che si voglia stampare l'intera area del foglio di lavoro a meno che non si specifichi una selezione. Per stampare usando Aspose.Cells per Python via .NET, prima importa lo spazio dei nomi aspose.cells.rendering nel programma. Ha diverse classi utili, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) e [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Stampa utilizzando SheetRender**

La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) rappresenta un foglio di lavoro e ha il metodo [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) che può stampare un foglio di lavoro. Il seguente codice di esempio mostra come stampare un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Stampa utilizzando WorkbookRender**

Per stampare un intero workbook, iterare attraverso i fogli e stamparli, o utilizzare la classe [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET fornisce anche sovraccarichi per i metodi [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) e [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), quindi è possibile impostare il nome del lavoro di stampa durante la stampa di fogli Excel. Per impostazione predefinita, tutti i lavori di stampa vengono creati con il nome "Document".

{{% /alert %}}

## **Anteprima di stampa**

Potrebbero esserci casi in cui file di Excel con milioni di pagine devono essere convertiti in PDF o immagini. Il processo di tali file consumerà molto tempo e risorse. In tali situazioni, la funzione di Anteprima di stampa del Workbook e del Foglio di lavoro potrebbe rivelarsi utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e poi decidere se convertire il file o meno. Questo articolo si concentra sull'utilizzo delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) per scoprire il numero totale di pagine.

Aspose.Cells per Python via .NET fornisce la funzione di anteprima di stampa. Per questo, l'API offre le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview). Per creare l'anteprima di stampa di tutto il workbook, crea un'istanza della classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) passando gli oggetti [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) al costruttore. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) fornisce un metodo [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) che restituisce il numero di pagine nell'anteprima generata. Simile alla classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) viene usata per generare un'anteprima di stampa di un singolo foglio di lavoro. Per creare l'anteprima di stampa di un foglio, crea un'istanza della classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) passando gli oggetti [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) al costruttore. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) offre anche un metodo [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/) che restituisce il numero di pagine dell'anteprima generata.

Il seguente frammento di codice dimostra l'utilizzo sia delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) che [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) utilizzando il [file Excel di esempio](94896177.xlsx).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Quello che segue è l'output generato eseguendo il codice sopra.

### **Output della console**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

