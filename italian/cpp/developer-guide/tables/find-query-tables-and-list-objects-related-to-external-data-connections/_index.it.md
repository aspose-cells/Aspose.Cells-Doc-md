---
title: Trova tabelle di query e elenco oggetti correlati a connessioni dati esterni con C++
linktitle: Trova tabelle di query e elenco oggetti
type: docs
weight: 20
url: /it/cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Scopri come trovare tabelle di query e oggetti correlati a connessioni dati esterni usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte è necessario scoprire le Tabelle di Query e gli Oggetti Elenco relativi a alcune Connessioni Dati Esterne. Le Tabelle di Query sono correlate all'oggetto Connessione Dati Esterne con Id Connessione, mentre gli Oggetti Elenco sono correlati a una Tabella di Query.

{{% /alert %}}

## **Trova query tabelle e oggetti elenco relativi alle connessioni esterne dei dati**
I seguenti codici di esempio con [file Excel di esempio](5115493.xlsm) spiegano come trovare tabelle di query e oggetti elenco correlati a una connessione dati esterne.

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

Il seguente è l'output della console dell'esecuzione dei codici di esempio precedenti con questo [file Excel di esempio](5115493.xlsm).

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
