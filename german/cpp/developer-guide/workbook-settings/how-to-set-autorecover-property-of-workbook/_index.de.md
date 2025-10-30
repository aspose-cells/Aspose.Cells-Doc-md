---
title: So setzen Sie die AutoWiederherstellen Eigenschaft der Arbeitsmappe mit C++
linktitle: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 220
url: /de/cpp/how-to-set-autorecover-property-of-workbook/
description: Erfahren Sie, wie Sie die AutoWiederherstellen Eigenschaft einer Arbeitsmappe mit Aspose.Cells for C++ aktivieren oder deaktivieren.
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die AutoWiederherstellen-Eigenschaft einer Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie sie auf **false** setzen, deaktiviert Microsoft Excel die AutoWiederherstellen-Funktion (Autospeichern) für diese Excel-Datei.

Aspose.Cells stellt die Eigenschaft [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) bereit, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Code erklärt, wie die [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/)-Eigenschaft der Arbeitsmappe verwendet wird. Der Code liest zuerst den Standardwert dieser Eigenschaft aus, der **true** ist, setzt ihn dann auf **false** und speichert die Arbeitsmappe. Danach liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der jetzt **false** ist.

## C++-Code zum Setzen der AutoRecover-Eigenschaft der Arbeitsmappe

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ergebnis**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
