---
title: Nascondere contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML con C++
linktitle: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Usa CrossHideRight con Aspose.Cells in C++ per nascondere contenuto sovrapposto durante il salvataggio in HTML.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi di incrocio per le stringhe di celle. Per impostazione predefinita, Aspose.Cells genera HTML come Microsoft Excel, ma quando cambi il tipo di incrocio in [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype), allora nasconde tutte le stringhe sul lato destro della cella sovrapposte o sopraffatte dalla stringa della cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il seguente esempio di codice carica il [file Excel di esempio](64716894.xlsx) e lo salva in [HTML di output](64716893.zip) dopo aver impostato [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) come [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Lo screenshot mostra come [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) influenza l'HTML di output rispetto all'output predefinito.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
