---
title: 检索SQL连接数据
type: docs
weight: 10
url: /zh/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET可以帮助您检索SQL连接数据。这包括连接到SQL服务器所需的所有数据，例如**服务器URL**、**用户名**、**表名**、**完整SQL查询**、**查询类型**、**表位置**和**关联的命名范围**等。

{{% /alert %}}

在Microsoft Excel中，通过以下步骤连接数据库：

1. 单击**数据**菜单，选择**来自其他源**，然后选择**来自SQL Server**。
2. 然后选择**数据**，然后选择**连接**。
3.使用连接向导连接到数据库并创建数据库查询。

Aspose.Cells for Python via .NET提供Workbook.DataConnections属性，用于检索外部连接。它返回工作簿中的ExternalConnection对象集合。

如果ExternalConnection对象包含SQL连接数据，它可以被类型转换为DBConnection对象，并且它的属性可以用于检索数据库命令、命令类型、连接描述、连接信息、凭据等。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

