---
title: 使用C++处理WebQuery类型的外部数据连接
linktitle: 使用  WebQuery  类型的外部数据连接
type: docs
weight: 30
url: /zh/cpp/working-with-external-data-connection-of-type-webquery/
description: 学习如何使用Aspose.Cells和C++处理Microsoft Excel中的WebQuery数据连接。
---

{{% alert color="primary" %}}

您可以使用 Workbook.DataConnections 集合访问任何类型的外部数据连接。其中一种数据连接类型是 WebQuery。本文将向您展示如何处理 WebQuery 数据连接。您可以使用 Microsoft Excel 中的 **数据** > **来自网络** 菜单创建 WebQuery 数据连接。

{{% /alert %}}

## 使用 **WebQuery** 类型的外部数据连接

以下代码显示了如何处理类型为 **WebQuery** 的外部数据连接。它使用了您可以从提供的链接下载的 [示例 Excel 文件](5112365.xlsx)。您还可以在下文看到此代码的控制台输出。

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

## 控制台输出

这是上述代码与此 [示例 Excel 文件](5112365.xlsx) 的控制台输出。

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
