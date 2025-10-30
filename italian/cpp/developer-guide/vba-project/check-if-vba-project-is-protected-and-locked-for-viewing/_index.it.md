---
title: Verifica se il Progetto VBA è Protetto e Bloccato per la Visualizzazione con C++
linktitle: Verifica se il progetto VBA è protetto e bloccato per la visualizzazione
type: docs
weight: 30
url: /it/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Impara come verificare se il Progetto VBA è protetto e bloccato per la visualizzazione nei file Excel usando Aspose.Cells for C++.
---

## Verifica se il Progetto VBA è Protetto e Bloccato per la Visualizzazione in C++

Aspose.Cells permette di verificare se il Progetto VBA (Visual Basic for Applications) di un file Excel è protetto e bloccato per la visualizzazione. Per questo, l’API fornisce la proprietà [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). Se è bloccato per la visualizzazione, allora la proprietà [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) restituisce **true**.

## **Codice di Esempio**

Il seguente esempio di codice carica il [file Excel di esempio](43352065.xlsm) e verifica se il Progetto VBA (Visual Basic for Applications) del file Excel è protetto e bloccato per la visualizzazione. Si prega di consultare anche la sua Uscita Console come riferimento.

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

## **Output della console**

Questo è l'output della console del codice di esempio precedente quando eseguito con il [file Excel di esempio](43352065.xlsm) fornito.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
