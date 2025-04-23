---
title: Mergen von Zellen in einem Arbeitsblatt mit C++ erkennen
linktitle: Zellen zusammenführen erkennen
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt die Erkennung zusammengeführter Zellen in einem Arbeitsblatt, sodass Benutzer diese Zellen leicht identifizieren und manipulieren können. Dieser Artikel führt in die Verwendung der Aspose.Cells Bibliothek zur Erkennung zusammengeführter Zellen ein.
keywords: Aspose.Cells, Arbeitsblatt, Zellen zusammenführen, erkennen, identifizieren, bearbeiten
type: docs
weight: 80
url: /de/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Dieser Artikel enthält Informationen dazu, wie man zusammengeführte Zellenbereiche in einem Arbeitsblatt erhält.

Aspose.Cells ermöglicht es Ihnen, zusammengeführte Zellenbereiche in einem Arbeitsblatt zu erhalten. Sie können sie auch aufheben (teilen). Dieser Artikel zeigt den einfachsten Code, der die **Aspose.Cells-API** verwendet, um die Aufgabe auszuführen.

{{% /alert %}}

Die Komponente stellt die [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/)-Methode bereit, mit der alle zusammengeführten Zellen abgerufen werden können. Das folgende Codebeispiel zeigt, wie Sie zusammengeführte Zellen in einem Arbeitsblatt erkennen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
