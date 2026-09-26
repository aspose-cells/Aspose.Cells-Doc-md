---
title: Retrieving SQL Connection Data with Golang via C++
linktitle: Retrieving SQL Connection Data
type: docs
weight: 10
url: /go-cpp/retrieving-sql-connection-data/
description: Learn how to retrieve SQL connection data, including server URL, username, table name, and more using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

Aspose.Cells can help you retrieve SQL connection data. This includes any and all data that is required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.

{{% /alert %}}

In Microsoft Excel, connect to a database by:

1. Click the **Data** menu and select **From Other Sources**, then **From SQL Server**.
2. Select **Data**, then **Connections**.
3. Use the Connections wizard to connect to the database and create a database query.

Aspose.Cells provides the `Workbook::get_DataConnections()` method for retrieving external connections. It returns a collection of `ExternalConnection` objects in the workbook.

If the `ExternalConnection` object contains SQL connection data, it can be type‑cast to a `DBConnection` object and its properties can be used to retrieve the database command, command type, connection description, connection information, credentials, and so on.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RetrievingSqlConnectionData.go" >}}
{{< app/cells/assistant language="go" >}}
