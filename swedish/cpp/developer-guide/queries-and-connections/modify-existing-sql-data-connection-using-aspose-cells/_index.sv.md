---
title: Modifiera befintlig SQL dataanslutning med C++ med Aspose.Cells
linktitle: Modifiera befintlig SQL Data Connection
type: docs
weight: 20
url: /sv/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Lär dig hur man modifierar befintlig SQL dataanslutning i Excel filer med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder att modifiera befintlig SQL-dataanslutning. Denna artikel förklarar hur man använder Aspose.Cells för att ändra olika egenskaper hos SQL-dataanslutning.

Du kan lägga till eller se dataanslutningar inne i Microsoft Excel genom att följa menyn **Data > Connections**.

På samma sätt ger Aspose.Cells möjlighet att komma åt och ändra datakopplingar med hjälp av `Workbook.DataConnections`-samlingen.

{{% /alert %}}

## Modifiera befintlig SQL Data Connection med hjälp av Aspose.Cells

Det följande exempel illustrerar användningen av Aspose.Cells för att ändra SQL Data Connection hos arbetsboken. Du kan ladda ned den angivna källfilen Excel och den genererade utdatafilen Excel med hjälp av följande länkar.

- [Käll-Excel-fil](5112357.xlsx)
- [Utdata-Excel-fil](5112356.xlsx)

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
