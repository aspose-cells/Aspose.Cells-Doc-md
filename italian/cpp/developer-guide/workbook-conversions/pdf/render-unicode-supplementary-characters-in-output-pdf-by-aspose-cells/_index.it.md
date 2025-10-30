---
title: Renderizza caratteri Supplementari Unicode nel PDF di output con C++ di Aspose.Cells
linktitle: Renderizza caratteri Supplementari Unicode
type: docs
weight: 350
url: /it/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Scopri come rendere i caratteri Supplementari Unicode nel PDF di output usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati a punti codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità di 16 bit).

{{% /alert %}}

## Rendere i caratteri supplementari Unicode nel PDF di output con Aspose.Cells

La seguente schermata mostra come Aspose.Cells ha reso il [file di Excel di origine](5115563.xlsx) nel [PDF di output](5115564.pdf). Come puoi vedere, tutti e tre i caratteri supplementari Unicode sono stati resi esattamente come fatto da Microsoft Excel.

![todo:image_alt_text](output.png)

## Codice di esempio

Puoi utilizzare questo codice di esempio per convertire [file di Excel di origine](5115563.xlsx) in [PDF di output](5115564.pdf).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
