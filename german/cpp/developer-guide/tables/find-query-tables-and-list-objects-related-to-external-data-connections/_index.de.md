---
title: Finden Sie Abfrage Tabellen und Listenobjekte im Zusammenhang mit Externen Datenverbindungen mit C++
linktitle: Finden Sie Abfrage Tabellen und Listenobjekte
type: docs
weight: 20
url: /de/cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Erfahren Sie, wie Sie mit Aspose.Cells für C++ Abfrage Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Abfrage-Tabellen und Listenobjekte im Zusammenhang mit einer externen Datenverbindung finden. Abfrage-Tabellen sind mit der Verbindungs-ID des externen Datenverbindungsobjekts verbunden, während Listenobjekte mit einer Abfrage-Tabelle verbunden sind.

{{% /alert %}}

## **Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden**
Die folgenden Beispielcodes mit der [Beispiel-Excel-Datei](5115493.xlsm) erläutern, wie man Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden kann.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

void PrintTables(Workbook& workbook, ExternalConnection& externalConnection)
{
    // Implementation of PrintTables function
    // This function should print tables related to the external connection
    // Placeholder for actual implementation
}

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load workbook object
    Workbook workbook(srcDir + u"sample.xlsm");

    // Check all the connections inside the workbook
    ExternalConnectionCollection dataConnections = workbook.GetDataConnections();
    for (int i = 0; i < dataConnections.GetCount(); i++)
    {
        ExternalConnection externalConnection = dataConnections.Get(i);
        std::cout << "connection: " << externalConnection.GetName().ToUtf8() << std::endl;
        PrintTables(workbook, externalConnection);
        std::cout << std::endl;
    }

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <algorithm>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;
using namespace Aspose::Cells::Tables;

void PrintTables(Workbook workbook, ExternalConnection ec)
{
    for (int j = 0; j < workbook.GetWorksheets().GetCount(); j++)
    {
        Worksheet worksheet = workbook.GetWorksheets().Get(j);

        for (int k = 0; k < worksheet.GetQueryTables().GetCount(); k++)
        {
            QueryTable qt = worksheet.GetQueryTables().Get(k);

            if (ec.GetId() == qt.GetConnectionId() && qt.GetConnectionId() >= 0)
            {
                std::cout << "querytable " << qt.GetName().ToUtf8() << std::endl;
                std::u16string nameStr = qt.GetName().GetData();
                std::replace(nameStr.begin(), nameStr.end(), u'+', u'_');
                std::replace(nameStr.begin(), nameStr.end(), u'=', u'_');
                U16String n(nameStr.c_str());
                Name name = workbook.GetWorksheets().GetNames().Get(U16String(u"'") + worksheet.GetName() + U16String(u"'!") + n);
                if (name)
                {
                    Range range = name.GetRange();
                    if (range)
                    {
                        std::cout << "refersto: " << range.GetRefersTo().ToUtf8() << std::endl;
                    }
                }
            }
        }

        for (int k = 0; k < worksheet.GetListObjects().GetCount(); k++)
        {
            ListObject table = worksheet.GetListObjects().Get(k);

            if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
            {
                QueryTable qt = table.GetQueryTable();

                if (ec.GetId() == qt.GetConnectionId() && qt.GetConnectionId() >= 0)
                {
                    std::cout << "querytable " << qt.GetName().ToUtf8() << std::endl;
                    std::cout << "Table " << table.GetDisplayName().ToUtf8() << std::endl;
                    std::cout << "refersto: " << worksheet.GetName().ToUtf8() << "!" 
                              << CellsHelper::CellIndexToName(table.GetStartRow(), table.GetStartColumn()).ToUtf8() 
                              << ":" 
                              << CellsHelper::CellIndexToName(table.GetEndRow(), table.GetEndColumn()).ToUtf8() 
                              << std::endl;
                }
            }
        }
    }
}
```

Folgendes ist die Konsolenausgabe beim Ausführen der oben genannten Beispielcodes mit dieser [Beispiel-Excel-Datei](5115493.xlsm).

{{< highlight java >}}

connection: AAPL Connection

querytable hp?s=AAPL+Historical+Prices

refersto: =Sheet1!$Q$1:$W$69

connection: BOSL066360W7_SQLEXPRESS Test

querytable BOSL066360W7_SQLEXPRESS Test

Table Table_BOSL066360W7_SQLEXPRESS_Test

refersto: Sheet1!A1:B3

connection: BOSL066360W7_SQLEXPRESS Test1

querytable BOSL066360W7_SQLEXPRESS Test_1

Table Table_BOSL066360W7_SQLEXPRESS_Test_1

refersto: Sheet1!D1:E2

connection: UWTI Connection

querytable hp?s=UWTI+Historical+Prices

refersto: =Sheet1!$H$1:$N$69

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
