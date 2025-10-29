---
title: Lire le sous titre du graphique dans un fichier ODS avec C++
linktitle: Lire le sous titre du graphique à partir du fichier ODS
description: Apprenez comment utiliser Aspose.Cells for C++ pour lire le sous titre du graphique à partir d un fichier OpenDocument Spreadsheet (ODS). Notre guide montrera comment extraire et accéder au sous titre d un graphique pour une analyse ou une affichage ultérieur.
keywords: Aspose.Cells for C++, Lire le sous titre du graphique, Feuille de calcul OpenDocument, Fichier ODS, Extraction de graphique, Analyse de données.
type: docs
weight: 160
url: /fr/cpp/read-chart-subtitle-from-ods-file/
---

## **Lire le sous-titre du graphique à partir du fichier ODS**

Aspose.Cells vous permet de lire les sous-titres des graphiques dans les fichiers ODS en utilisant la propriété [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). Le code d'exemple suivant charge le [fichier ODS d'exemple](89620481.ods) et lit le sous-titre du graphique en utilisant la propriété [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) et l'affiche dans la fenêtre de la console. Veuillez consulter la sortie de la console du code ci-dessous pour référence.

## **Code d'exemple**

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

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
