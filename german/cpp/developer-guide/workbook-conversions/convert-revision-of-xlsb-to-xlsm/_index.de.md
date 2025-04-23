---
title: Konsolidierung von Revisionen von XLSB zu XLSM mit C++
linktitle: Revision von XLSB zu XLSM konvertieren
type: docs
weight: 290
url: /de/cpp/convert-revision-of-xlsb-to-xlsm/
description: Erfahren Sie, wie Sie Revisionen von XLSB Dateien mithilfe von Aspose.Cells in das XLSM Format konvertieren.
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt jetzt die vollständige Konvertierung von Revisionen der XLSB-Dateien in XLSM-Dateien. Revisionen befinden sich im Pfad \xl\revisions. Sie können sie anzeigen, indem Sie die Erweiterung Ihrer XLSB-Datei in ZIP ändern. Der Pfad \xl\revisions enthält Dateien mit der Endung .bin.

Wenn Sie Ihre XLSB-Datei in eine XLSM-Datei mit Aspose.Cells konvertieren, werden diese .bin-Dateien erfolgreich in .xml-Dateien umgewandelt, wie in diesen beiden Screenshots zu sehen ist.

{{% /alert %}} 

Das folgende Codebeispiel zeigt, wie Sie die XLSB-Datei mit Aspose.Cells in das XLSM-Format konvertieren.

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
