---
title: Imposta la larghezza della colonna in unità scalabili come em o percentuale con C++
linktitle: Imposta la larghezza della colonna su unità scalabili come em o percentuale
type: docs
weight: 130
url: /it/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Impara come impostare la larghezza della colonna in unità scalabili come em o percentuale usando Aspose.Cells for C++.
---

Generare un file HTML da un foglio di calcolo è molto comune. Le dimensioni delle colonne sono definite in "pt", che funziona in molti casi. Tuttavia, può esserci un caso in cui questa dimensione fissa non sia richiesta. Ad esempio, se la larghezza del pannello contenitore è 600px dove viene visualizzata questa pagina HTML. In questo caso, potresti ottenere una barra di scorrimento orizzontale se la larghezza della tabella generata è maggiore. Era necessario che questa dimensione fissa fosse cambiata in un'unità scalabile come em o percentuale per ottenere una migliore presentazione. Il codice di esempio seguente può essere utilizzato dove [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) è impostato su **true** per creare una larghezza scalabile.

I file di origine e i file di output di esempio possono essere scaricati dai seguenti collegamenti:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
