---
title: Rendering di un modello di formato data personalizzato g e mm dd con C++
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta la visualizzazione di date utilizzando modelli di formato data personalizzati g e ge . Questo articolo descriverà come rendere i modelli di formato data personalizzati usando la libreria Aspose.Cells in modo che gli utenti possano controllare come vengono visualizzate le date, se desiderano.
keywords: Aspose.Cells, libreria C++, foglio di calcolo elettronico, formato data personalizzato, rendering, modello g , modello ge , controllo visualizzazione
type: docs
weight: 160
url: /it/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cells è ora in grado di renderizzare i modelli di formato data personalizzati come g, ge.mm.dd e simili. Si prega di controllare il file Excel di origine allegato (5112361.xlsx) e il PDF convertito (5112360.pdf) da Aspose.Cells per il tuo riferimento.

{{% /alert %}}

Il seguente codice di esempio converte il file Excel di origine (5112361.xlsx) che contiene valori di data con modelli di formato personalizzati come g e ge.mm.dd in un PDF di output (5112360.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
