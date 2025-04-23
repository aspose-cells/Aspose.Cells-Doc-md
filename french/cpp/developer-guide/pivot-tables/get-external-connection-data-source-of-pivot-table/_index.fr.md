---
title: Obtenir la source de donnée de la connexion extérieure du tableau croisé dynamique avec C++
linktitle: Obtenir la source de données de connexion externe de la table de données
type: docs
weight: 150
url: /fr/cpp/get-external-connection-data-source-of-pivot-table/
description: Apprenez comment récupérer la source de données de la connexion extérieure d’un tableau croisé dynamique en utilisant Aspose.Cells for C++.
---

## **Obtenir la source de données de connexion externe du tableau croisé dynamique**

Aspose.Cells permet d’obtenir la source de données de connexion extérieure du tableau croisé dynamique. Pour cela, l’API fournit la propriété [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) de la classe [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/). La propriété [**GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) retourne l’objet [**ExternalConnection**](https://reference.aspose.com/cells/cpp/aspose.cells.externalconnections/externalconnection/). Le code ci-dessous montre comment utiliser la propriété [**PivotTable.GetExternalConnectionDataSource()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getexternalconnectiondatasource/) pour obtenir la source de connexion extérieure du tableau croisé dynamique.

## Code d'exemple

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample file
    Workbook workbook(srcDir + u"SamplePivotTableExternalConnection.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the pivot table
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Print External Connection Details
    std::cout << "External Connection Data Source" << std::endl;

    // Get the source data connections
    Vector<ExternalConnection> connections = pivotTable.GetSourceDataConnections();

    // Iterate through each connection and print details
    int32_t connectionCount = connections.GetLength();
    for (int32_t i = 0; i < connectionCount; ++i)
    {
        ExternalConnection conn = connections[i];
        std::cout << "Name: " << conn.GetName().ToUtf8() << std::endl;
        std::cout << "Type: " << static_cast<int>(conn.GetSourceType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Le fichier source utilisé dans l'exemple de code est joint à titre de référence.

[Fichier source](104398862.xlsx)
