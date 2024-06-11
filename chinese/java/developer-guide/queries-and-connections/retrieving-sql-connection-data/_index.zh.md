---
title: 检索SQL连接数据
type: docs
weight: 20
url: /zh/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells可以帮助您检索SQL连接数据。这包括连接到SQL服务器所需的所有数据，例如**服务器URL**，**用户名**，**表名**，**完整SQL查询**，**查询类型**，**表的位置**以及与其关联的**命名范围的名称**。

{{% /alert %}} 

在Microsoft Excel中，通过以下步骤连接数据库：

1. 单击**数据**菜单，选择**来自其他源**，然后选择**来自SQL Server**。
2. 然后选择**数据**，然后选择**连接**。
3.使用连接向导连接到数据库并创建数据库查询。

**在Microsoft Excel中显示SQL连接选项** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells提供了Workbook.getDataConnections()方法来检索外部连接。它返回工作簿中的ExternalConnection对象集合。

如果ExternalConnection对象包含SQL连接数据，则可以将其强制转换为DBConnection对象，使用其属性检索数据库命令，命令类型，连接说明，连接信息，凭证等。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






