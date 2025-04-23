---
title: Formater les cellules du tableau croisé dynamique avec C++
linktitle: Formatter les cellules du tableau croisé dynamique
type: docs
weight: 30
url: /fr/cpp/format-pivot-table-cells/
description: Apprenez comment formater les cellules du tableau croisé dynamique avec Aspose.Cells en C++.
---

{{% alert color="primary" %}}

Parfois, vous souhaitez formater les cellules du tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur de fond aux cellules du tableau croisé dynamique. Aspose.Cells fournit deux méthodes [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) et [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), que vous pouvez utiliser à cette fin.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) applique le style à l'ensemble du tableau croisé dynamique tandis que [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}

Le code d'exemple ci-dessous charge le fichier Excel d'exemple (pivot_format.xlsx) qui contient deux tableaux croisés dynamiques, et réalise l'opération de mise en forme de l'ensemble du tableau croisé dynamique et la mise en forme des cellules individuelles dans le tableau croisé dynamique.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Articles Connexes

- [Formatage du tableau croisé dynamique](/cells/fr/cpp/formatting-pivot-table/)
- [Travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique](/cells/fr/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
