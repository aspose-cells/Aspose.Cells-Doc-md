---
title: Adatta automaticamente le righe per il rendering con C++
linktitle: AutoAdattamento righe per il rendering
type: docs
weight: 130
url: /it/cpp/autofit-rows-for-rendering/
description: Impara come adattare automaticamente le righe per il rendering nei file Excel usando Aspose.Cells con C++.
---

In generale, quando si vuole visualizzare tutto il testo in una cella, è possibile adattare automaticamente la riga nella visualizzazione Normale con zoom al 100% in Microsoft Excel. Questo consente al testo di essere completamente visibile nella visualizzazione Normale, e anche quando si stampa o si salva il file in formato PDF, il testo verrà visualizzato correttamente.

Tuttavia, in alcuni casi, l'adattamento automatico della riga funziona bene nella visualizzazione Normale, ma quando si passa alla visualizzazione di stampa o si salva il file in formato PDF, il testo viene tagliato. Si prega di controllare il file sorgente [Book1.xlsx](Book1.xlsx) e gli screenshot.

![il testo viene tagliato nella visualizzazione di stampa](text_clipped_in_printview.png)

Se vuoi evitare che il testo venga tagliato nel file PDF salvato, puoi adattare automaticamente le righe con l'opzione [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Ora, il testo non è tagliato nel file PDF di output.

![il testo non è tagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)
