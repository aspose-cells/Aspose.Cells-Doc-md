---
title: Travailler avec la connexion de données externe de type WebQuery avec C++
linktitle: Travailler avec une connexion de données externe de type WebQuery
type: docs
weight: 30
url: /fr/cpp/working-with-external-data-connection-of-type-webquery/
description: Découvrez comment travailler avec la connexion de données WebQuery dans Microsoft Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Vous pouvez accéder à n'importe quel type de connexion de données externe en utilisant la collection Workbook.DataConnections. Un type de cette connexion de données est WebQuery. Cet article vous montrera comment travailler avec la connexion de données WebQuery. Vous pouvez créer une connexion de données WebQuery dans Microsoft Excel en utilisant le menu **Données** > **À partir du Web**.

{{% /alert %}}

## Travail avec une connexion de données externe de type WebQuery

Le code suivant montre comment travailler avec une connexion de données externe de type **WebQuery.** Il utilise le [fichier Excel d'exemple](5112365.xlsx) que vous pouvez télécharger à partir du lien fourni. Vous pouvez également voir la sortie de la console de ce code ci-dessous.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"WebQuerySample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first external connection from the workbook
    ExternalConnection connection = workbook.GetDataConnections().Get(0);

    // Check if the connection is a WebQueryConnection
    if (connection.GetClassType() == ExternalConnectionClassType::WebQuery)
    {
        // Cast to WebQueryConnection
        WebQueryConnection webQuery(connection);

        // Print the URL of the web query
        std::cout << "Web Query URL: " << webQuery.GetUrl().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## Sortie de la console

Voici la sortie de la console du code ci-dessus avec ce [fichier Excel d'exemple](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
