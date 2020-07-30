---
title : "Retrieving SQL Connection Data" 
description : "" 
weight : 20534 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngdatabaseconnections/retrieving+sql+connection+data/
---

# Aspose.Cells for .NET : Retrieving SQL Connection Data


Aspose.Cells can help you retrieve SQL connection data. This includes any and all data that is required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.

In Microsoft Excel, connect to a database by:

1.  Clicking the **Data** menu and selecting **From Other Sources** followed by **From SQL Server**.
2.  Then select **Data** followed by **Connections**.
3.  Use the Connections wizard to connect to the database and create a database query.

Aspose.Cells provides the `Workbook.DataConnections` property for retrieving external connections. It returns a collection of `ExternalConnection` objects in the workbook.

If the `ExternalConnection` object contains SQL connection data, it can be type-caste to a `DBConnection` object and its properties can be used to retrieve database command, command type, connection description, connection information, credentials, and so on.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [SQL-Connection-Data.PNG](https://docs2.aspose.com/cells/net/attachments/5017319/5112355.png) (image/png)  

