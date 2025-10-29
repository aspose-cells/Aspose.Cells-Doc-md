---
title: Convertir Excel en JSON avec C++
linktitle: Convertir Excel en JSON
type: docs
weight: 300
url: /fr/cpp/convert-excel-to-json/
description: Apprenez comment convertir un fichier Excel en JSON avec Aspose.Cells en utilisant C++.
keywords: Exporter le classeur au format JSON sans office 2013, office 2016, office 2019 et office 365
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json(JavaScript Object Notation).

{{% /alert %}}

## **Convertir un classeur Excel en JSON**

Inutile de vous demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for C++ offre la meilleure solution. L’API Aspose.Cells supporte la conversion des feuilles de calcul en format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) comme deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) pour spécifier des paramètres additionnels d’exportation de la feuille de calcul en JSON.

L’exemple de code ci-dessous montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code en référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

L’exemple de code suivant utilisant la classe JsonSaveOptions pour spécifier des paramètres additionnels montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code en référence.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
