---
title: C++ ile WebQuery türündeki Dış Veri Bağlantısıyla Çalışma
linktitle: WebQuery Türünden Dış Veri Bağlantısı ile Çalışmak
type: docs
weight: 30
url: /tr/cpp/working-with-external-data-connection-of-type-webquery/
description: Aspose.Cells kullanarak C++ ile Microsoft Excel de WebQuery veri bağlantısı ile nasıl çalışılacağını öğrenin.
---

{{% alert color="primary" %}}

Çalışma Kitabı.DataConnections koleksiyonunu kullanarak herhangi bir türdeki harici veri bağlantısına erişebilirsiniz. Bu türden bir veri bağlantısı WebQuery'dir. Bu makale, WebQuery veri bağlantısıyla nasıl çalışılacağını gösterecektir. Microsoft Excel'de **Veri** > **Web'den** menüsünü kullanarak WebQuery veri bağlantısı oluşturabilirsiniz.

{{% /alert %}}

## WebQuery türündeki Harici Veri Bağlantısı ile Çalışma

Aşağıdaki kod, **WebQuery** türündeki harici veri bağlantısıyla nasıl çalışılacağını göstermektedir. İndirebileceğiniz [örnek excel dosyası](5112365.xlsx) kullanılmaktadır. Ayrıca bu kodun konsol çıktısını aşağıda görebilirsiniz.

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

## Konsol Çıkışı

Yukarıdaki kodun [örnek excel dosyası](5112365.xlsx)'nın konsol çıktısı aşağıda verilmiştir.

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
