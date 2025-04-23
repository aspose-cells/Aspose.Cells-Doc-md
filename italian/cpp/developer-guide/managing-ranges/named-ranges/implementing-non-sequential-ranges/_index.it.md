---
title: Implementare intervalli non sequenziali con C++
linktitle: Implementazione di Ranges Non Sequenziali
type: docs
weight: 700
url: /it/cpp/implementing-non-sequential-ranges/
description: Impara come creare intervalli nominati con celle non adiacenti usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Normalmente, i range nominati sono rettangolari con celle continue e adiacenti l'una all'altra. Ma a volte potresti dover utilizzare un intervallo di celle non sequenziale in cui le celle non sono adiacenti. Aspose.Cells supporta la creazione di un intervallo nominato con celle non adiacenti.

{{% /alert %}} 

Il codice di esempio seguente mostra come creare un intervallo non sequenziale nominato con Aspose.Cells for C++.

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
