---
title: Converti la revisione di XLSB in XLSM con C++
linktitle: Convertire la Revisione da XLSB a XLSM
type: docs
weight: 290
url: /it/cpp/convert-revision-of-xlsb-to-xlsm/
description: Impara a convertire le revisioni dei file XLSB in formato XLSM usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Aspose.Cells ora supporta la conversione completa delle revisioni dei file XLSB in file XLSM. Le revisioni si trovano all’interno del percorso \xl\revisions. Puoi visualizzarle cambiando l’estensione del file XLSB in ZIP. Il percorso \xl\revisions contiene file che terminano con estensioni .bin.

Quando converti il tuo file XLSB in un file XLSM usando Aspose.Cells, questi file .bin vengono convertiti con successo in file .xml come mostrato in questi due screenshot.

{{% /alert %}} 

Il seguente esempio di codice mostra come convertire il file XLSB in formato XLSM usando Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
