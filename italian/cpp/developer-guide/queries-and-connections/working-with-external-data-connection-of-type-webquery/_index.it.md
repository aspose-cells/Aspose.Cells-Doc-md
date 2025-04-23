---
title: Lavorare con la Connessione a Dati Esterni di tipo WebQuery con C++
linktitle: Lavorare con la connessione dati esterna di tipo WebQuery
type: docs
weight: 30
url: /it/cpp/working-with-external-data-connection-of-type-webquery/
description: Impara come lavorare con la connessione ai dati WebQuery in Microsoft Excel utilizzando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puoi accedere alle connessioni dati esterne di qualsiasi tipo utilizzando la raccolta Workbook.DataConnections. Un tipo di connessione dati del genere è WebQuery. Questo articolo ti mostrerà come lavorare con la connessione dati WebQuery. Puoi creare una connessione dati WebQuery in Microsoft Excel utilizzando il menu **Dati** > **Da Web**.

{{% /alert %}}

## Lavorare con la connessione dati esterna di tipo WebQuery

Il seguente codice mostra come lavorare con la connessione dati esterna di tipo **WebQuery**. Utilizza il [file di Excel di esempio](5112365.xlsx), che puoi scaricare dal link fornito. Puoi anche vedere l'output della console di questo codice di seguito.

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

## Output della console

Ecco l'output della console del codice precedente con questo [file di Excel di esempio](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
