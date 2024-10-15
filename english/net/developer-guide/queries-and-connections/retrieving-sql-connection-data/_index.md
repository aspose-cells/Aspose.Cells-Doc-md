---
title: Retrieving SQL Connection Data
type: docs
weight: 10
url: /net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells can help you retrieve SQL connection data. This includes any and all data that is required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.

{{% /alert %}}

In Microsoft Excel, connect to a database by:

1. Clicking the **Data** menu and selecting **From Other Sources** followed by **From SQL Server**.
1. Then select **Data** followed by **Connections**.
1. Use the Connections wizard to connect to the database and create a database query.

Aspose.Cells provides the Workbook.DataConnections property for retrieving external connections. It returns a collection of ExternalConnection objects in the workbook.

If the ExternalConnection object contains SQL connection data, it can be type-caste to a DBConnection object and its properties can be used to retrieve database command, command type, connection description, connection information, credentials, and so on.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}