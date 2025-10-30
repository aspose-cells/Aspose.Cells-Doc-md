---
title: Specifica come incrociare la stringa nell HTML di output usando HtmlCrossType con C++
linktitle: Specifica HtmlCrossType nell HTML di output
type: docs
weight: 140
url: /it/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Impara come controllare il trabocco di stringhe in output HTML usando Aspose.Cells for C++ con HtmlCrossType.
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene un testo o una stringa più grande della larghezza della cella, la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in HTML, puoi controllare questo trabocco specificando il tipo di incrocio usando l'enumerazione [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Ha i seguenti valori:

- **HtmlCrossType.Default**: Visualizza come MS Excel, dipende dalla prossima cella. Se la prossima cella è nulla, la stringa verrà attraversata o verrà troncata.

- **HtmlCrossType.MSExport**: Visualizza la stringa come esportazione HTML di MS Excel.

- **HtmlCrossType.Cross**: Visualizza una stringa attraversata HTML, le prestazioni per la creazione di file HTML di grandi dimensioni saranno più di dieci volte più veloci rispetto all'impostazione del valore su Default o FitToCell.

- **HtmlCrossType.FitToCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType**

Il codice di esempio seguente carica il [file Excel di esempio](51740732.xlsx) e lo salva in formato HTML specificando diversi [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Si prega di scaricare gli [HTML di output](51740734.zip) generati con questo codice. Il file Excel di esempio contiene l'immagine bordata di colore rosso come mostrato in questo screenshot che mostra l'effetto dei valori [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) sull'HTML di output.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
