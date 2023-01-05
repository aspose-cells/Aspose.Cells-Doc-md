---
title: ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作
type: docs
weight: 160
url: /zh/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **可能的使用场景**
本文解释了 ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作。
## **ASP.NET 会话状态模式为 SQL Server 时 GridWeb 的工作**
如果要使用 SQL Server 或 StateServer 来保持会话，请使用 GridWeb 会话模式。 GridWeb 控件现在支持将其数据序列化到 SQL Server 或 StateServer。

您将 GridWeb.SessionMode 设置为 SessionMode.Session 并使用以下示例 Web.Config 设置。请根据您的需要更改 sessionState 属性。
## **示例 Web.Config 会话状态设置**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **参考文章**
- [启用不同的 GridWeb 模式](/cells/zh/net/enable-different-gridweb-modes/)
