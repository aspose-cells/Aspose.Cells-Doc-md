---
title: Unterschriftenzeile in einer Excel Arbeitsmappe mit C++ und Aspose.Cells erstellen
linktitle: Unterschriftenzeile in einer Excel Arbeitsmappe erstellen
type: docs
weight: 150
url: /de/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Dieser Artikel beschreibt, wie man mit C++ Codes eine Unterschriftenzeile in eine Excel Arbeitsmappe mit Aspose.Cells for C++ erstellt.
keywords: Signaturlinie in einer Excel Arbeitsmappe erstellen, Wie man eine Signaturlinie in einer Excel Arbeitsmappe erstellt, Wie man eine Signaturlinie hinzufügt, Wie man eine Signaturlinie zur Excel Datei hinzufügt.
---

## **Einführung**

Microsoft Excel bietet die Möglichkeit, **Signaturlinie** in Excel-Arbeitsmappen hinzuzufügen. Sie können eine Signaturlinie hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann **Signaturlinie** aus der Gruppe **Text** auswählen.

## **Wie man eine Signaturlinie für Excel erstellt**

Aspose.Cells bietet diese Funktion ebenfalls und hat die Eigenschaft [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) für diesen Zweck freigegeben. Dieser Artikel erläutert, wie diese Eigenschaft verwendet werden kann, um eine Signaturlinie mit Aspose.Cells hinzuzufügen.

Der folgende Beispielcode fügt mit der Eigenschaft [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) eine Signaturlinie hinzu und speichert die Arbeitsmappe.

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
