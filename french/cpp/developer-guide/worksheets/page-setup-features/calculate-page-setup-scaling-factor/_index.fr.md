---
title: Calculer le facteur de mise à l échelle de la configuration de la page avec C++
linktitle: Calculer le facteur d échelle de la mise en page
type: docs
weight: 300
url: /fr/cpp/calculate-page-setup-scaling-factor/
description: Cet article fournit un exemple de code expliquant comment utiliser l API ou la bibliothèque C++ pour calculer le facteur de mise à l échelle de la configuration de la page en utilisant l option Ajuster à n page(s) en largeur par m en hauteur de la feuille Excel.
keywords: Ajuster à n pages en largeur par m en hauteur dans Excel C++, calculer le facteur de mise à l échelle de la configuration de la page en C++
---

{{% alert color="primary" %}}

Lorsque vous définissez l'échelle de la mise en page en utilisant l'option **Ajuster à n page(s) de largeur sur m page(s) de hauteur**, Microsoft Excel calcule le facteur d'échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/). Cette propriété renvoie une valeur double qui peut être convertie en pourcentage. Par exemple, si elle renvoie 0.5, cela signifie que le facteur d'échelle est de 50%.

{{% /alert %}}

Le code d'exemple suivant illustre comment calculer le facteur d'échelle de la mise en page en utilisant la propriété [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
