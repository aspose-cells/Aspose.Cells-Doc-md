---
title: Zellen Ausrichtung ändern und bestehendes Format beibehalten mit C++
description: Verwenden Sie die Aspose.Cells Bibliothek, um die Zellenausrichtung zu ändern und das vorhandene Format beizubehalten
keywords: Aspose.Cells, C++, Zellen Ausrichtung, bestehendes Format beibehalten
type: docs
weight: 340
url: /de/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, aber das bestehende Format beibehalten. Aspose.Cells ermöglicht dies durch die Eigenschaft [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/). Wenn Sie sie auf **true** setzen, werden Änderungen an der Ausrichtung vorgenommen, andernfalls nicht. Bitte beachten Sie, dass das [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag)-Objekt als Parameter an die Methode [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) übergeben wird, die tatsächlich das Format auf einen Zellbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
