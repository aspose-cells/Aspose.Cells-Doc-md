---
title: Come impostare la proprietà AutoRecover di Workbook con C++
linktitle: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 220
url: /it/cpp/how-to-set-autorecover-property-of-workbook/
description: Impara come abilitare o disabilitare la proprietà AutoRecover di un workbook usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per impostare la proprietà AutoRecover di un workbook. Il valore predefinito di questa proprietà è **true**. Quando la imposti a **false** su un workbook, Microsoft Excel disabilita AutoRecover (Autosave) su quel file Excel.

Aspose.Cells fornisce la proprietà [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) per abilitare o disabilitare questa opzione.

{{% /alert %}}

Il seguente codice spiega come usare la proprietà [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) del workbook. Il codice prima legge il valore predefinito di questa proprietà, che è **true**, quindi impostala a **false** e salva il workbook. Poi rilegge il workbook e legge il valore di questa proprietà, che in questo momento è **false**.

## Codice C++ per impostare la proprietà AutoRecover di Workbook

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

## **Output**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
