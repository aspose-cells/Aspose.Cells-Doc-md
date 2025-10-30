---
title: Inserisci un immagine basata sul riferimento di cella con C++
linktitle: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/cpp/insert-a-picture-based-on-cell-reference/
description: Impara come inserire un immagine basata sul riferimento di cella usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells supporta mostrare i contenuti di una cella del foglio di lavoro in una forma di immagine. Puoi collegare l'immagine alla cella che contiene i dati che desideri visualizzare. Poiché la cella o il range di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle compariranno automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Specifica il range di celle utilizzando l'attributo [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) dell'oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Esempio di codice

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
