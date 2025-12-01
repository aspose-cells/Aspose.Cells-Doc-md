---
title: Retrieving SQL Connection Data
type: docs
weight: 10
url: /python-net/retrieving-sql-connection-data/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET can help you retrieve SQL connection data. This includes any and all data that is required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.

{{% /alert %}}

In Microsoft Excel, connect to a database by:

1. Clicking the **Data** menu and selecting **From Other Sources** followed by **From SQL Server**.
1. Then select **Data** followed by **Connections**.
1. Use the Connections wizard to connect to the database and create a database query.

Aspose.Cells for Python via .NET provides the Workbook.DataConnections property for retrieving external connections. It returns a collection of ExternalConnection objects in the workbook.

If the ExternalConnection object contains SQL connection data, it can be type-caste to a DBConnection object and its properties can be used to retrieve database command, command type, connection description, connection information, credentials, and so on.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
