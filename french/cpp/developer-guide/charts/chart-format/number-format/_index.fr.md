---
title: Définir le code du format des valeurs de la série de graphique avec C++
linktitle: Format numérique
type: docs
weight: 100
url: /fr/cpp/set-the-values-format-code-of-chart-series/
description: Apprenez à définir le code du format des valeurs de la série de graphique dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment formater les données de votre série de graphique en utilisant le code de format approprié, pour présenter vos données de manière précise et professionnelle.
keywords: Aspose.Cells for C++, série de graphique, code de format des valeurs, mise en forme, présentation des données, précision, professionnalisme.
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir le code du format des valeurs de la série de graphique en utilisant la propriété [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/). Cette propriété est utile non seulement pour la série basée sur la plage dans la feuille de calcul, mais aussi pour la série créée avec un tableau de valeurs.

## **Définir le code de format des valeurs de la série du graphique**
 Le code d'exemple suivant ajoute une série dans le graphique vide qui n'avait pas de série auparavant. Il ajoute la série en utilisant le tableau de valeurs. Une fois la série ajoutée, elle est formatée avec le code `$#,##0` en utilisant la propriété [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) et le nombre `10000` devient `$10,000`. La capture d'écran montre l'effet du code sur le [fichier Excel d'exemple](51740712.xlsx) et le [fichier Excel de sortie](51740713.xlsx) après exécution.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Code d'exemple**
```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
