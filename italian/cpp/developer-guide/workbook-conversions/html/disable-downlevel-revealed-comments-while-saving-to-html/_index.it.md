---
title: Disabilita Commenti Rivelati di livello inferiore durante il salvataggio in HTML con C++
linktitle: Disabilita Commenti Rivelati di livello inferiore
type: docs
weight: 20
url: /it/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Elimina Commenti Rivelati Downlevel durante il salvataggio di file Excel in HTML usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, Aspose.Cells rivela i Commenti Condizionali Downlevel. Questi commenti condizionali sono per lo più rilevanti per versioni più vecchie di Internet Explorer e sono irrilevanti per browser Web moderni. Puoi leggerne i dettagli al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ti permette di eliminare questi Commenti Rivelati Downlevel impostando la proprietà [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/). Lo screenshot mostra l'effetto di questa proprietà quando non è impostata su true. Scarica il [file Excel di esempio](50528257.xlsx) usato in questo codice e l'[HTML di output](50528258.zip) generato per un riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
