---
title: Crea intervallo di unione con C++
linktitle: Crea un intervallo di unione
type: docs
weight: 360
url: /it/cpp/create-union-range/
description: Crea intervallo di unione nei file Excel usando Aspose.Cells con C++.
---

## **Crea un intervallo di unione**
Aspose.Cells consente di creare intervallo di unione utilizzando il metodo [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Il metodo [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) accetta due parametri, l'indirizzo per creare l'intervallo di unione e l'indice del foglio di lavoro. Il metodo [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) restituisce un oggetto [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/).

Il seguente esempio di codice dimostra come creare un intervallo di unione usando il metodo [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Il file di output generato dal codice è allegato come riferimento.

- [File di output](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
