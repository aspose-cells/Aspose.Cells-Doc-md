---
title: Disegna la linea temporale durante il rendering di Excel in PDF con C++
linktitle: Disegna la Timeline durante la rappresentazione di Excel in PDF
type: docs
weight: 60
url: /it/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gestisci le timeline dei file Excel con Aspose.Cells con C++.
keywords: Rappresenta la timeline in PDF senza office 2013, office 2016, office 2019 e office 365
---

## **Disegna la Timeline durante la rappresentazione di Excel in PDF**
Se hai un file Excel con una timeline applicata e vuoi esportarlo in PDF mantenendo le impostazioni della timeline, Aspose.Cells supporta questa funzionalità di default. Puoi esportare semplicemente il file Excel con timeline in PDF, e il PDF risultante mostrerà la timeline applicata.

Il seguente codice di esempio carica il [file di Excel di esempio](input.xlsx) che contiene un timeline esistente. Salva poi il workbook come [file PDF di output](out.pdf). La seguente schermata confronta il file di Excel di origine e il file PDF generato.

<img src="out.png" width="60%">

## **Codice di Esempio**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

{{< app/cells/assistant language="cpp" >}}
