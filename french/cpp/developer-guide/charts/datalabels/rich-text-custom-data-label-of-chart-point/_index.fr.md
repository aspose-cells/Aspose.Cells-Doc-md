---
title: Étiquette de données personnalisée enrichie d’un texte riche d’un point de graphique avec C++
description: Apprenez comment ajouter des étiquettes de données personnalisées en texte enrichi aux points de graphique dans Aspose.Cells for C++. Notre guide vous montrera comment formater les étiquettes avec différentes polices, couleurs et options d alignement pour améliorer l apparence et la lisibilité de vos graphiques.
keywords: Aspose.Cells for C++, création de graphiques, texte enrichi, étiquettes de données personnalisées, polices, couleurs, alignement, apparence, lisibilité.
type: docs
weight: 10
url: /fr/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour créer une étiquette de données personnalisée en texte enrichi pour le point du graphique. Aspose.Cells fournit la méthode [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) pour retourner l'objet [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) qui peut être utilisé pour définir les propriétés de la police du texte comme sa couleur, sa graisse, etc.

{{% /alert %}}

## Étiquette de données personnalisée en texte enrichi du point du graphique

Le code suivant accède au premier point du graphique de la première série, définit son texte, puis définit la police des 10 premiers caractères en réglant leur couleur en rouge et leur graisse à **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
