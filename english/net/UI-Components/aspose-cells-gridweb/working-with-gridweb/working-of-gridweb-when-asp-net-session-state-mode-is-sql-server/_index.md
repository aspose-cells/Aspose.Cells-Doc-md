---
title: Working of GridWeb when ASP.NET Session state mode is SQL Server
type: docs
weight: 160
url: /net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb,web session state,sqlserver,session state mode
description: This article introduces how to configure in GridWeb when web session state mode is SQL Server.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
This article explains working of GridWeb when ASP.NET Session state mode is SQL Server.
## **Working of GridWeb when ASP.NET Session state mode is SQL Server**
If you want to use SQL Server or StateServer to hold sessions, use GridWeb Session Mode. The GridWeb control now supports serializing its data to SQL Server or StateServer.

You will set the GridWeb.SessionMode to SessionMode.Session and use the following sample Web.Config settings. Please change the sessionState attributes as per your needs.
## **Sample Web.Config Session State Settings**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Reference Article**
- [Enable Different GridWeb Modes](/cells/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
