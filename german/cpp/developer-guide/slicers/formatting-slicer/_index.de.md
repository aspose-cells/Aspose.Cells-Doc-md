---
title: Slicer mit C++ formatieren
linktitle: Slicer formatieren
type: docs
weight: 20
url: /de/cpp/formatting-slicer/
description: Formatieren von Slicern in Microsoft Excel mit Aspose.Cells und C++.
---

## **Mögliche Verwendungsszenarien**

Sie können den Gliederungsschneider in Microsoft Excel formatieren, indem Sie die Anzahl der Spalten oder den Stil einstellen usw. Aspose.Cells ermöglicht auch die Verwendung der [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/)- und [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/)-Eigenschaften.

## **Formatierung Schneidwerkzeug**

Bitte sehen Sie sich den folgenden Code an; er lädt die [Beispieldatei Excel](67338473.xlsx), die einen Gliederungsschneider enthält. Es greift auf den Gliederungsschneider zu, setzt seine Spaltenanzahl und den Stiltyp und speichert sie als [Ausgabedatei Excel](67338474.xlsx). Der Screenshot zeigt, wie der Gliederungsschneider nach Ausführung des Beispielcodes aussieht.

![todo:image_alt_text](formatting-slicer_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
