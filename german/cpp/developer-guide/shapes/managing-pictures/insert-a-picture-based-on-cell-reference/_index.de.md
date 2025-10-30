---
title: Fügen Sie ein Bild basierend auf Zellreferenz mit C++ ein
linktitle: Bild anhand eines Zellbezugs einfügen
type: docs
weight: 150
url: /de/cpp/insert-a-picture-based-on-cell-reference/
description: Erfahren Sie, wie Sie ein Bild basierend auf Zellreferenz mit Aspose.Cells for C++ einfügen.
---

{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie einen Zellbezug in der Formel-Leiste festlegen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells unterstützt das Anzeigen des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die anzuzeigenden Daten enthält. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder diesem Zellbereich vornehmen, automatisch im Grafikobjekt. Fügen Sie ein Bild dem Arbeitsblatt hinzu, indem Sie die [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) Methode der [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) Sammlung aufrufen (die im [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Objekt gekapselt ist). Geben Sie den Zellbereich an, indem Sie das [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) Attribut des [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) Objekts verwenden.

### Codebeispiel

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
