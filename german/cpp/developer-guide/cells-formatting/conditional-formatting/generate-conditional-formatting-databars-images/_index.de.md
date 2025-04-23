---
title: Generieren von Conditional Formatting DataBars Bildern mit C++
linktitle: Generieren von Miniaturbildern für bedingte Formatierung DataBars
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt die Generierung bedingt formatierter Datenbalken und Bilder, sodass Benutzer die Anzeige der Tabelle basierend auf dem Zellwert anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek zur Erzeugung bedingt formatierter Datenbalken und Bilder nutzt.
keywords: Aspose.Cells, Bedingte Formatierung, Datenleisten, Bilder, Tabellendokumente
type: docs
weight: 40
url: /de/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal muss man Bilder von bedingten Formatierungen DataBars generieren. Sie können die Methode von Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) verwenden, um diese Bilder zu generieren. In diesem Artikel wird gezeigt, wie man ein DataBar-Bild mit Aspose.Cells generiert.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift es auf das Formatierungsbedingungsobjekt der Zelle zu, dann aus diesem Objekt auf das [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/)-Objekt und verwendet seine [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/)-Methode, um das Bild der Zelle zu erstellen. Schließlich wird das Bild auf der Festplatte gespeichert.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
