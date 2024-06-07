---
title: 当ASP.NET会话状态模式为SQL Server时GridWeb的工作方式
type: docs
weight: 160
url: /zh/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb,web会话状态,sqlserver,会话状态模式
description: 当 Web 会话状态模式为 SQL Server 时，本文介绍了如何在 GridWeb 中进行配置。
---

## **可能的使用场景**
本文解释了当 ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作原理。
## **ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作原理**
如果想要使用 SQL Server 或 StateServer 来保存会话，请使用 GridWeb 会话模式。GridWeb 控件现在支持将其数据序列化到 SQL Server 或 StateServer。

将 GridWeb.SessionMode 设置为 SessionMode.Session，使用以下示例 Web.Config 设置。请根据您的需求更改 sessionState 属性。
## **示例 Web.Config 会话状态设置**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **参考文章**
- [启用不同的 GridWeb 模式](/cells/zh/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
