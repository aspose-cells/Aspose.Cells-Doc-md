---
title: C++を使用したWebQueryタイプの外部データ接続の操作
linktitle: WebQueryタイプの外部データ接続の操作
type: docs
weight: 30
url: /ja/cpp/working-with-external-data-connection-of-type-webquery/
description: Aspose.Cells を使用したMicrosoft ExcelのWebQueryデータ接続の操作方法を学びます。
---

{{% alert color="primary" %}}

Workbook.DataConnectionsコレクションを使用して、任意の種類の外部データ接続にアクセスできます。そのようなデータ接続の1つはWebQueryです。この記事では、WebQueryデータ接続の操作方法を示します。Microsoft Excelで**Data** > **From Web** メニューを使用してWebQueryデータ接続を作成できます。

{{% /alert %}}

## WebQueryの外部データ接続を操作する

次のコードは、**WebQuery**タイプの外部データ接続を扱う方法を示しています。提供されたリンクからダウンロードできる[サンプルエクセルファイル](5112365.xlsx)を使用しています。コンソールには、このコードの出力も示されています。

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

## コンソール出力

上記コードのコンソール出力は、この[サンプルエクセルファイル](5112365.xlsx)とともに以下に示されています。

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
