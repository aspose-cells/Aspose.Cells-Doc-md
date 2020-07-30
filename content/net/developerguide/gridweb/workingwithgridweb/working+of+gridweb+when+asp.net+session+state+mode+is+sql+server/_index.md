---
title : "Working of GridWeb when ASP.NET Session state mode is SQL Server" 
description : "" 
weight : 16675 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridweb/working+of+gridweb+when+asp.net+session+state+mode+is+sql+server/
---

# Aspose.Cells for .NET : Working of GridWeb when ASP.NET Session state mode is SQL Server


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Working of GridWeb when ASP.NET Session state mode is SQL Server](#working-of-gridweb-when-asp.net-session-state-mode-is-sql-server)
*   3 [Sample Web.Config Session State Settings](#sample-web.config-session-state-settings)
*   4 [Reference Article](#reference-article)
{{< /panel >}}
 

## Possible Usage Scenarios

This article explains working of GridWeb when ASP.NET Session state mode is SQL Server.

## Working of GridWeb when ASP.NET Session state mode is SQL Server

If you want to use `SQL Server` or `StateServer` to hold sessions, use `GridWeb Session Mode`. The GridWeb control now supports serializing its data to SQL Server or StateServer.

You will set the `GridWeb.SessionMode` to `SessionMode.Session` and use the following sample `Web.Config` settings. Please change the `sessionState` attributes as per your needs.

## Sample Web.Config Session State Settings

<sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\\NASIRSQL" timeout="20"></sessionState>

## Reference Article

*   [Enable Different GridWeb Modes](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridweb/enable+different+gridweb+modes)

