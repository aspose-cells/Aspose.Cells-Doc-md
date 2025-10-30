---
title: Bestehende SQL Datenverbindung mit C++ unter Verwendung von Aspose.Cells ändern
linktitle: Bestehende SQL Datenverbindung ändern
type: docs
weight: 20
url: /de/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Lernen, wie man bestehende SQL Datenverbindung in Excel Dateien mit Aspose.Cells und C++ ändert.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Änderung bestehender SQL-Datenverbindungen. Dieser Artikel erklärt, wie man Aspose.Cells verwendet, um verschiedene Eigenschaften der SQL-Datenverbindung zu ändern.

Sie können Datenverbindungen in Microsoft Excel hinzufügen oder anzeigen, indem Sie den Menübefehl **Daten > Verbindungen** befolgen.

 Ebenso ermöglicht Aspose.Cells den Zugriff auf und die Änderung der Datenverbindungen über die Sammlung `Workbook.DataConnections`.

{{% /alert %}}

## Ändern einer bestehenden SQL-Datenverbindung mit Aspose.Cells

Das folgende Beispiel veranschaulicht die Verwendung von Aspose.Cells, um die SQL-Datenverbindung der Arbeitsmappe zu ändern. Sie können die Quelldatei, die in diesem Code verwendet wird, und die vom Code generierte Ausgabedatei unter den folgenden Links herunterladen.

- [Quelldatei](5112357.xlsx)
- [Ausgabedatei](5112356.xlsx)

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
