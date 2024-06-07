---
title: 检索SQL连接数据
type: docs
weight: 10
url: /zh/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells可以帮助您检索SQL连接数据。这包括连接到SQL服务器所需的所有数据，例如**服务器URL**、**用户名**、**表名**、**完整SQL查询**、**查询类型**、**表的位置**和与之关联的**命名范围的名称**。

{{% /alert %}}

在Microsoft Excel中，连接到数据库的方法是：

1. 单击**数据**菜单，选择**其他来源** ，然后选择**从SQL Server**。
1. 然后选择**数据**，接着选择**连接**。
1. 使用连接向导连接到数据库并创建数据库查询。

Aspose.Cells提供了Workbook.DataConnections属性以检索外部连接。它返回工作簿中的ExternalConnection对象集合。

如果ExternalConnection对象包含SQL连接数据，则可以将其类型转换为DBConnection对象，并可使用其属性来检索数据库命令、命令类型、连接描述、连接信息、凭据等。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
