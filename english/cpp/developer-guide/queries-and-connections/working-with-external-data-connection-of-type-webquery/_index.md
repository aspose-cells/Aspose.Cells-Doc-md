---
title: Working with External Data Connection of type WebQuery with C++
linktitle: Working with External Data Connection of type WebQuery
type: docs
weight: 30
url: /cpp/working-with-external-data-connection-of-type-webquery/
description: Learn how to work with WebQuery data connection in Microsoft Excel using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

You can access external data connection of any type using the Workbook.DataConnections collection. One type of such data connection is WebQuery. This article will show you how to work with WebQuery data connection. You can create WebQuery data connection in Microsoft Excel using the **Data** > **From Web** menu.

{{% /alert %}}

## Working with External Data Connection of type WebQuery

The following code shows how to work with external data connection of type **WebQuery**. It uses the [sample excel file](5112365.xlsx) which you can download from the provided link. You can also see the console output of this code further below.

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

## Console Output

Here is the console output of the above code with this [sample excel file](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}