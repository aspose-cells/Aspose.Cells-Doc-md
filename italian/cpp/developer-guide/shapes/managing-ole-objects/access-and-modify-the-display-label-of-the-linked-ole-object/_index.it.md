---
title: Accedi e modifica l etichetta di visualizzazione dell Ole Object collegato con C++
linktitle: Accesso e modifica dell etichetta di visualizzazione dell oggetto Ole collegato
type: docs
weight: 100
url: /it/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Impara come accedere e modificare l etichetta di visualizzazione degli Ole Object collegati nei file Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel permette di cambiare l'etichetta di visualizzazione dell'Ole Object come mostrato nello screenshot seguente. Puoi anche accedere o modificare l'etichetta di visualizzazione dell'Ole object usando le API di Aspose.Cells con i metodi [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) e [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato**

Si prega di vedere il seguente codice di esempio, carica il [file Excel di esempio](64716810.xlsx) che contiene l'oggetto Ole. Il codice accede all'oggetto Ole e ne cambia l'etichetta da Sample APIs a Aspose APIs. Si prega di vedere l'output della console qui sotto che mostra l'effetto del codice di esempio sul file Excel di esempio per un riferimento.

## **Codice di Esempio**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
