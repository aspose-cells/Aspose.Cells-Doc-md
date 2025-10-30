---
title: Implementering av ej sammanhängande områden med C++
linktitle: Implementera icke sekventiella intervaller
type: docs
weight: 700
url: /sv/cpp/implementing-non-sequential-ranges/
description: Lär dig hur man skapar namngivna områden med oavhängiga celler med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Normalt sett är namngivna områden rektangulära med celler som är kontinuerliga och intill varandra. Men ibland kan du behöva använda en icke-sekventiellt cellintervall där cellerna inte är intill varandra. Aspose.Cells stöder skapandet av ett namngivet område med icke-intilliggande celler.

{{% /alert %}} 

Koden nedan visar hur man skapar ett namngivet ej-sammanhängande område med Aspose.Cells for C++.

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
{{< app/cells/assistant language="cpp" >}}
