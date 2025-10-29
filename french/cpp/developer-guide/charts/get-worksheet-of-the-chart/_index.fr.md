---
title: Obtenir la feuille de calcul du graphique avec C++
linktitle: Obtenir la feuille de calcul du graphique
description: Découvrez comment récupérer la feuille associée à un graphique Excel à l aide de Aspose.Cells for C++. Notre guide vous montrera comment accéder à la feuille et y effectuer des opérations pour manipuler les données sous jacentes du graphique.
keywords: Aspose.Cells for C++, graphiques Excel, feuilles de calcul, manipulation de données, données sous jacentes, opérations.
type: docs
weight: 1000
url: /fr/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez accéder à une feuille de calcul à partir d'une référence de graphique. Aspose.Cells fournit la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) qui retourne la référence de la feuille contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/). Le code affiche d'abord le nom de la feuille, puis accède au premier graphique de la feuille. Ensuite, il affiche à nouveau le nom de la feuille en utilisant la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
