---
title: 在ASP.NET会话状态模式为SQL Server时的GridWeb的工作
type: docs
weight: 160
url: /zh/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, web会话状态, sqlserver, 会话状态模式
description: 本文介绍了在Web会话状态模式为SQL Server时如何配置GridWeb。
---

## **可能的使用场景**
本文解释了在ASP.NET会话状态模式为SQL Server时GridWeb的工作。
## **ASP.NET会话状态模式为SQL Server时的GridWeb的工作**
如果要使用SQL Server或StateServer保存会话，请使用GridWeb会话模式。GridWeb控件现在支持将其数据序列化到SQL Server或StateServer。

将GridWeb.SessionMode设置为SessionMode.Session，并使用以下示例的Web.Config设置。根据您的需要更改sessionState属性。
## **示例Web.Config会话状态设置**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **参考文章**
- [启用不同的GridWeb模式](/cells/zh/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
