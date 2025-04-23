---
title: Modificar conexión de datos SQL existente con C++ usando Aspose.Cells
linktitle: Modificar conexión de datos SQL existente
type: docs
weight: 20
url: /es/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Aprenda cómo modificar una conexión de datos SQL existente en archivos de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells soporta la modificación de conexiones de datos SQL existentes. Este artículo explicará cómo utilizar Aspose.Cells para modificar diferentes propiedades de una conexión de datos SQL.

Puedes añadir o ver Conexiones de Datos dentro de Microsoft Excel siguiendo el comando de menú **Datos > Conexiones**.

De manera similar, Aspose.Cells proporciona los medios para acceder y modificar las conexiones de datos usando la colección `Workbook.DataConnections`.

{{% /alert %}}

## Modificar una conexión de datos SQL existente usando Aspose.Cells

El siguiente ejemplo ilustra el uso de Aspose.Cells para modificar la Conexión de Datos SQL del libro de trabajo. Puede descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5112357.xlsx)
- [Archivo de Excel de Salida](5112356.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataConnection.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Access first Data Connection
    ExternalConnection conn = workbook.GetDataConnections().Get(0);

    // Change the Data Connection Name and Odc file
    conn.SetName(u"MyConnectionName");
    conn.SetOdcFile(u"C:\\Users\\MyDefaulConnection.odc");

    // Change the Command Type, Command and Connection String
    DBConnection dbConn = conn;
    dbConn.SetCommandType(OLEDBCommandType::SqlStatement);
    dbConn.SetCommand(u"Select * from AdminTable");
    dbConn.SetConnectionString(u"Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Data connection updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
