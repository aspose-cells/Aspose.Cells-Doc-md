---
title: Infoga en bild baserad på cellreferens med C++
linktitle: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/cpp/insert-a-picture-based-on-cell-reference/
description: Lär dig hur man infogar en bild baserad på cellreferens med hjälp av Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells stöder att visa innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller datan du vill visa. Eftersom cellen eller cellintervallet är länkad till den grafiska objektet visar ändringar som du gör i datan i den cellen eller cellintervallet automatiskt upp i det grafiska objektet. Lägg till en bild i kalkylbladet genom att använda [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) metoden i [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) objektet). Ange cellintervallet genom att använda [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attributet i [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) objektet.

### Kodexempel

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
