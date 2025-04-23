---
title: Benutzerdefiniertes Datumsmuster g und ge mm dd mit C++ rendern
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die unterstützt, Daten mit benutzerdefinierten Datumsmustern g und ge zu rendern. Dieser Artikel beschreibt, wie man benutzerdefinierte Datumsmuster mit der Aspose.Cells Bibliothek rendert, sodass Nutzer die Anzeige von Daten steuern können.
keywords: Aspose.Cells, C++ Bibliothek, elektronische Tabelle, benutzerdefiniertes Datumsmuster, Rendern, Muster g , Muster ge , Anzeige steuern
type: docs
weight: 160
url: /de/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cells kann jetzt benutzerdefinierte Datumsformatmuster wie g, ge.mm.tt und ähnliche rendern. Bitte überprüfen Sie die angehängte [Quellexceldatei](5112361.xlsx) und die [konvertierte PDF-Datei](5112360.pdf) von Aspose.Cells zu Ihrer Referenz.

{{% /alert %}}

Der folgende Beispielcode wandelt die [Quellexceldatei](5112361.xlsx) um, die Datumsangaben mit benutzerdefinierten Formatmustern wie g und ge.mm.tt enthält, in eine [Ausgabedatei im PDF-Format](5112360.pdf) um.

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
