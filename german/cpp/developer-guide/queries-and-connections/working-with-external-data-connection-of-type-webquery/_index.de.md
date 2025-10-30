---
title: Arbeiten mit externer Datenverbindung vom Typ WebQuery mit C++
linktitle: Arbeiten mit externer Datenverbindungstyp WebQuery
type: docs
weight: 30
url: /de/cpp/working-with-external-data-connection-of-type-webquery/
description: Lernen Sie, wie Sie mit Aspose.Cells in C++ in Microsoft Excel mit WebQuery Datenverbindung arbeiten.
---

{{% alert color="primary" %}}

Sie können auf eine externe Datenverbindung beliebigen Typs über die Workbook.DataConnections-Sammlung zugreifen. Eine solche Datenverbindung ist z.B. WebQuery. In diesem Artikel wird gezeigt, wie Sie mit einer WebQuery-Datenverbindung arbeiten können. Sie können eine WebQuery-Datenverbindung in Microsoft Excel über das **Daten** > **Aus dem Web**-Menü erstellen.

{{% /alert %}}

## Arbeiten mit externer Datenverbindung des Typs WebQuery

Der folgende Code zeigt, wie Sie mit externen Datenverbindungen des Typs **WebQuery** arbeiten. Er verwendet die [Beispieldatei](5112365.xlsx), die Sie von dem bereitgestellten Link herunterladen können. Sie können auch die Konsolenausgabe dieses Codes weiter unten sehen.

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

## Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Codes mit dieser [Beispieldatei](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
