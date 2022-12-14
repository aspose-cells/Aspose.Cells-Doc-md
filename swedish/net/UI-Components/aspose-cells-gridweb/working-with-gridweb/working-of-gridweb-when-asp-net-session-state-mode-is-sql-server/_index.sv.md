---
title: Fungerar med GridWeb när ASP.NET Session tillståndsläge är SQL Server
type: docs
weight: 160
url: /sv/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Möjliga användningsscenarier**
Den här artikeln förklarar hur GridWeb fungerar när ASP.NET-sessionstillståndet är SQL Server.
## **Fungerar med GridWeb när ASP.NET Session tillståndsläge är SQL Server**
Om du vill använda SQL Server eller StateServer för att hålla sessioner, använd GridWeb Session Mode. GridWeb-kontrollen stöder nu serialisering av dess data till SQL Server eller StateServer.

Du kommer att ställa in GridWeb.SessionMode till SessionMode.Session och använda följande exempel på Web.Config-inställningar. Ändra sessionState-attributen enligt dina behov.
## **Exempel på Web.Config-inställningar för sessionstillstånd**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referensartikel**
- [Aktivera olika GridWeb-lägen](/cells/sv/net/enable-different-gridweb-modes/)
