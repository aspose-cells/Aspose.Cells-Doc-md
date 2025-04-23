---
title: Работа с внешним подключением данных типа WebQuery с помощью C++
linktitle: Работа с внешним подключением данных типа WebQuery
type: docs
weight: 30
url: /ru/cpp/working-with-external-data-connection-of-type-webquery/
description: Узнайте, как работать с подключением данных WebQuery в Microsoft Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Вы можете получить доступ к внешнему подключению данных любого типа, используя коллекцию Workbook.DataConnections. Одним из таких подключений данных является WebQuery. В этой статье будет показано, как работать с подключением данных WebQuery. Вы можете создать подключение данных WebQuery в Microsoft Excel, используя меню **Данные** > **Из Интернета**.

{{% /alert %}}

## Работа с внешним подключением данных типа WebQuery

В следующем коде показано, как работать с внешним подключением данных типа **WebQuery**. Он использует [образец электронного файла](5112365.xlsx), который вы можете скачать по предоставленной ссылке. Вы также можете увидеть вывод консоли этого кода ниже.

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

## Вывод в консоль

Вот вывод консоли вышеуказанного кода с этим [образцом электронного файла](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
