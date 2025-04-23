---
title: Unicode Sonderzeichen im Ausgabepdf mit C++ rendern durch Aspose.Cells
linktitle: Unicode Sonderzeichen rendern
type: docs
weight: 350
url: /de/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Erfahren Sie, wie Sie Unicode Sonderzeichen im Ausgabepdf mit Aspose.Cells for C++ rendern.
---

{{% alert color="primary" %}}

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Supplementary-Zeichen 4 Byte lang sind. Aspose.Cells unterstützt jetzt das Rendern dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Standard für Zeichen handelt es sich bei den Supplementary-Zeichen um Zeichen, denen die Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten, dies sind die Unicode-Zeichen größer als U+FFFF.

- In UTF-8 sind diese Zeichen jeweils 4 Bytes lang.
- In UTF-16 benötigen diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}}

## Rendern von Unicode-Zusatzzeichen im Ausgabepdf von Aspose.Cells

Der folgende Screenshot zeigt, wie Aspose.Cells die [Quellexceldatei](5115563.xlsx) in die [Ausgabepdf](5115564.pdf) gerendert hat. Wie Sie sehen können, wurden alle drei Unicode-Zusatzzeichen genau so gerendert wie von Microsoft Excel durchgeführt.

![todo:image_alt_text](output.png)

## Beispielcode

Sie können diesen Beispiellcode verwenden, um die [Quellexceldatei](5115563.xlsx) in die [Ausgabepdf](5115564.pdf) zu konvertieren.

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
