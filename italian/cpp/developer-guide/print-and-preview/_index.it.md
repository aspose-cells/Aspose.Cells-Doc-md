---
title: Stampa e anteprima del workbook con C++
linktitle: Stampa e anteprima
type: docs
weight: 70
url: /it/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells supporta la stampa e l anteprima dei file Excel senza installazione di Microsoft Excel usando C++.
---

{{% alert color="primary" %}}

Dopo aver creato un foglio di lavoro, spesso si desidera stampare una copia cartacea. Questo articolo spiega come stampare i fogli di calcolo con Aspose.Cells.

{{% /alert %}}

## **Introduzione alla stampa**

Microsoft Excel presume che si desideri stampare l'intera area del foglio di lavoro a meno che non si specifichi una selezione. Per stampare utilizzando Aspose.Cells, prima importa il namespace Aspose.Cells.Rendering nel programma. Ha diverse classi utili, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) e [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Anteprima di stampa**

Potrebbero esserci casi in cui file di Excel con milioni di pagine devono essere convertiti in PDF o immagini. Il processo di tali file consumerà molto tempo e risorse. In tali situazioni, la funzione di Anteprima di stampa del Workbook e del Foglio di lavoro potrebbe rivelarsi utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e poi decidere se convertire il file o meno. Questo articolo si concentra sull'utilizzo delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) per scoprire il numero totale di pagine.

Aspose.Cells fornisce la funzione di anteprima di stampa. A questo scopo, l'API fornisce le classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) e [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/). Per creare l'anteprima di stampa dell'intero workbook, creare un'istanza della classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) passando gli oggetti [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) al costruttore. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) fornisce un metodo [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) che restituisce il numero di pagine nell'anteprima generata. Similmente alla classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) viene utilizzata per generare un'anteprima di stampa per un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, creare un'istanza della classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) passando gli oggetti [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) al costruttore. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) fornisce anche un metodo [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) che restituisce il numero di pagine nell'anteprima generata.

Il seguente frammento di codice dimostra l'utilizzo sia delle classi [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) che [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) utilizzando il [file Excel di esempio](94896177.xlsx).

### **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Quello che segue è l'output generato eseguendo il codice sopra.

### **Output della console**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Argomenti avanzati**
- [Configurare i font per la resa dei fogli di calcolo](/cells/it/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Convertire il foglio di lavoro in un'immagine - Rimuovere gli spazi vuoti intorno ai dati](/cells/it/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Convertire il foglio di lavoro in un'immagine e Foglio di lavoro in un'immagine per pagina](/cells/it/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Convertire il foglio di lavoro in un'immagine utilizzando le opzioni ImageOrPrint](/cells/it/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Esportare un intervallo di celle in un foglio di lavoro in un'immagine](/cells/it/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Estrarre immagini dai fogli di lavoro utilizzando ImageOrPrintOptions](/cells/it/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generare l'anteprima del foglio di lavoro](/cells/it/cpp/generate-thumbnail-of-the-worksheet/)
- [Output Pagina Bianca quando non c'è Nulla da Stampare](/cells/it/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Impostazioni di layout pagina e stampa](/cells/it/cpp/page-setup-and-printing-options/)
- [Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Renderizzare il foglio di lavoro al contesto grafico](/cells/it/cpp/render-worksheet-to-graphic-context/)
- [Specificare un insieme individuale o privato di caratteri per la rappresentazione del foglio di lavoro](/cells/it/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
