---
title: Find Query Tables and List Objects related to External Data Connections with C++
linktitle: Find Query Tables and List Objects
type: docs
weight: 20
url: /cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Learn how to find Query Tables and List Objects related to External Data Connections using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes, you need to find out Query Tables and List Objects related to some External Data Connection. Query Tables are related to External Data Connection object with Connection Id, while List Objects are related to a Query Table.

{{% /alert %}}

## **Find Query Tables and List Objects related to External Data Connections**
The following sample codes with [sample excel file](5115493.xlsm) explain how to find Query Tables and List Objects related to External Data Connection.

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
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;
using namespace Aspose::Cells::Tables;

void PrintTables(Workbook workbook, ExternalConnection ec)
{
    // Iterate all the worksheets
    for (int j = 0; j < workbook.GetWorksheets().GetCount(); j++)
    {
        Worksheet worksheet = workbook.GetWorksheets().Get(j);

        // Check all the query tables in a worksheet
        for (int k = 0; k < worksheet.GetQueryTables().GetCount(); k++)
        {
            QueryTable qt = worksheet.GetQueryTables().Get(k);

            // Check if query table is related to this external connection
            if (ec.GetId() == qt.GetConnectionId() && qt.GetConnectionId() >= 0)
            {
                // Print the query table name and print its refersto range
                std::cout << "querytable " << qt.GetName().ToUtf8() << std::endl;
                U16String n = qt.GetName().Replace(u'+', u'_').Replace(u'=', u'_');
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

        // Iterate all the list objects in this worksheet
        for (int k = 0; k < worksheet.GetListObjects().GetCount(); k++)
        {
            ListObject table = worksheet.GetListObjects().Get(k);

            // Check the data source type if it is query table
            if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
            {
                // Access the query table related to list object
                QueryTable qt = table.GetQueryTable();

                // Check if query table is related to this external connection
                if (ec.GetId() == qt.GetConnectionId() && qt.GetConnectionId() >= 0)
                {
                    // Print the query table name and print its refersto range
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

The following is the console output of running the above sample codes with this [sample excel file](5115493.xlsm).

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