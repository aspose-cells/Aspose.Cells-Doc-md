---
title: Trabajando con conexión de datos externa de tipo WebQuery en C++
linktitle: Trabajar con conexión de datos externos de tipo WebQuery
type: docs
weight: 30
url: /es/cpp/working-with-external-data-connection-of-type-webquery/
description: Aprenda cómo trabajar con la conexión de datos WebQuery en Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puede acceder a conexiones de datos externas de cualquier tipo utilizando la colección Workbook.DataConnections. Un tipo de dicha conexión de datos es WebQuery. Este artículo le mostrará cómo trabajar con una conexión de datos de tipo WebQuery. Puede crear una conexión de datos de tipo WebQuery en Microsoft Excel utilizando el menú **Datos** > **Desde la Web**.

{{% /alert %}}

## Trabajando con Conexiones de Datos Externas de tipo WebQuery

El siguiente código muestra cómo trabajar con una conexión de datos externa de tipo **WebQuery**. Utiliza el [archivo de Excel de ejemplo](5112365.xlsx) que puede descargar desde el enlace proporcionado. También puede ver la salida de la consola de este código más abajo.

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

## Salida de la consola

Aquí está la salida de la consola del código anterior con este [archivo de Excel de ejemplo](5112365.xlsx).

{{< highlight java >}}

Web Query URL: https://docs.aspose.com/cells/net/

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
