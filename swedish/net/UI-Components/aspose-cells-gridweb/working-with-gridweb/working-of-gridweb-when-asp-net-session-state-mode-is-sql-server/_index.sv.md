---
title: Arbete med GridWeb när ASP.NET Session state mode är SQL Server
type: docs
weight: 160
url: /sv/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, webbsessionsstat, sqlserver, session state mode
description: Den här artikeln introducerar hur man konfigurerar i GridWeb när webbsessionsläget är SQL Server.
---

## **Möjliga användningsscenario**
Den här artikeln förklarar arbetet med GridWeb när ASP.NET Session state mode är SQL Server.
## **Arbete med GridWeb när ASP.NET Session state mode är SQL Server**
Om du vill använda SQL Server eller StateServer för att hålla sessioner, använd GridWeb Session Mode. GridWeb-kontrollen stöder nu serialisering av sina data till SQL Server eller StateServer.

Du kommer att ställa in GridWeb.SessionMode till SessionMode.Session och använda följande exempel på Web.Config-inställningar. Ändra sessionState-attributen enligt dina behov.
## **Exempel på Web.Config Session State-inställningar**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referensartikel**
- [Aktivera olika GridWeb-lägen](/cells/sv/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
