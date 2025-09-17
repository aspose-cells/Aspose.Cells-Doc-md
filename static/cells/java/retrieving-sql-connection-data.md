##Retrieving SQL Connection Data
Aspose.Cells can help you retrieve SQL connection data. This includes any and all data required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.
In Microsoft Excel, connect to a database by:
1. Clicking the **Data** menu and selecting **From Other Sources** followed by **From SQL Server**.
1. Then select **Data** followed by **Connections**.
1. Use the Connections wizard to connect to the database and create a database query.
**Showing the SQL connection option in Microsoft Excel**
![todo:image_alt_text](retrieving-sql-connection-data_1.png)
Aspose.Cells provides the Workbook.getDataConnections() method for retrieving external connections. It returns a collection of ExternalConnection objects in the workbook.
If the ExternalConnection object contains SQL connection data, it can be type-caste into a DBConnection object its properties used to retrieve database command, command type, connection description, connection info, credentials, and so on.
