---
title: Modifica la connessione dati SQL esistente con C++ usando Aspose.Cells
linktitle: Modifica la connessione dati SQL esistente
type: docs
weight: 20
url: /it/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Impara come modificare una connessione dati SQL esistente nei file Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la modifica di connessioni dati SQL esistenti. Questo articolo spiegherà come utilizzare Aspose.Cells per modificare varie proprietà della connessione dati SQL.

È possibile aggiungere o visualizzare le connessioni dati all'interno di Microsoft Excel seguendo il comando di menu **Dati > Connessioni**.

Analogamente, Aspose.Cells fornisce i mezzi per accedere e modificare le Connessioni Dati usando la collezione `Workbook.DataConnections`.

{{% /alert %}}

## Modificare la connessione dati SQL esistente usando Aspose.Cells

Il seguente esempio illustra l'uso di Aspose.Cells per modificare la connessione dati SQL del foglio di lavoro. Puoi scaricare il file di origine di Excel utilizzato in questo codice e il file di output di Excel generato dal codice dai seguenti collegamenti.

- [File Excel di Origine](5112357.xlsx)
- [File Excel di Output](5112356.xlsx)

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
{{< app/cells/assistant language="cpp" >}}
