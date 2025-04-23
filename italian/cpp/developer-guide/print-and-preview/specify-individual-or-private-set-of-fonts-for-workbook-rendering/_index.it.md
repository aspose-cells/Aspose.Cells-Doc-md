---
title: Specificare set di font individuali o privati per il rendering del workbook con C++
linktitle: Specificare un insieme individuale o privato di caratteri per la rappresentazione del workbook
type: docs
weight: 40
url: /it/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Scopri come specificare set di font individuali o privati per il rendering del workbook utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

In generale, si specifica la directory dei font o l'elenco dei font per tutti i workbook, ma a volte è necessario specificare set di font individuali o privati per i propri workbook. Aspose.Cells fornisce la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) che può essere usata per specificare set di font individuali o privati per il proprio workbook.

## **Specificare un insieme individuale o privato di caratteri per la rappresentazione del foglio di lavoro**

Il seguente esempio di codice carica il [file Excel di esempio](67338268.xlsx) con set di font individuali o privati, specificati utilizzando la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). Si prega di vedere anche il [font di esempio](67338271.zip) usato nel codice e il [PDF di output](67338269.pdf) generato da esso. La seguente schermata mostra come appare il PDF di output se il font viene trovato con successo.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
