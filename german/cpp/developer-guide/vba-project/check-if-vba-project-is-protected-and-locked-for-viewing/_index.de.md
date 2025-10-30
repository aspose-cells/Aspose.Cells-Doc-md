---
title: VBA Projekt vor Ansicht schützen und sperren mit C++
linktitle: Überprüfen, ob das VBA Projekt geschützt und für die Anzeige gesperrt ist
type: docs
weight: 30
url: /de/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Erfahren Sie, wie Sie überprüfen, ob das VBA Projekt in Excel Dateien geschützt und zum Betrachten gesperrt ist, mithilfe von Aspose.Cells for C++.
---

## Überprüfen, ob das VBA-Projekt geschützt und zum Betrachten gesperrt ist in C++

Aspose.Cells ermöglicht es, zu überprüfen, ob das VBA (Visual Basic for Applications)-Projekt einer Excel-Datei geschützt und zum Betrachten gesperrt ist. Für diese API bietet die [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)-Eigenschaft. Wenn es gesperrt ist, dann gibt die [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/)-Eigenschaft **true** zurück.

## **Beispielcode**

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](43352065.xlsm) und überprüft, ob das VBA (Visual Basic for Applications)-Projekt der Excel-Datei geschützt und zum Betrachten gesperrt ist. Bitte sehen Sie auch die Konsolenausgabe als Referenz an.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, dass mit der bereitgestellten [Beispiel-Excel-Datei](43352065.xlsm) ausgeführt wird.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
