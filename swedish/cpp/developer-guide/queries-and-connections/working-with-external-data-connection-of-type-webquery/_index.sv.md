---
title: Arbete med extern datakoppling av typen WebQuery med C++
linktitle: Arbeta med extern datanslutning av typ WebQuery
type: docs
weight: 30
url: /sv/cpp/working-with-external-data-connection-of-type-webquery/
description: Lär dig hur man arbetar med WebQuery datakoppling i Microsoft Excel med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Du kan komma åt extern datanslutning av vilken typ som helst genom att använda Workbook.DataConnections-samlingen. En typ av sådan datanslutning är WebQuery. Den här artikeln visar hur du arbetar med WebQuery-datanslutning. Du kan skapa WebQuery-datanslutning i Microsoft Excel med menyn **Data** > **Från webben**.

{{% /alert %}}

## Arbeta med extern datanslutning av typ WebQuery

Följande kod visar hur man arbetar med extern datanslutning av typ **WebQuery**. Den använder [exempel excelfilen](5112365.xlsx) som du kan ladda ner från den angivna länken. Du kan också se konsolens utdata av den här koden längre ner.

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

## Konsoloutput

Här är konsolens utdata av den ovanstående koden med denna [exempel excelfilen](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
