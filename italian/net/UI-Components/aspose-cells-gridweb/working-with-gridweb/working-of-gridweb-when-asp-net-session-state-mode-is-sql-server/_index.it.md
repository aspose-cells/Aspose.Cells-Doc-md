---
title: Funzionamento di GridWeb quando la modalità di stato di sessione ASP.NET è SQL Server
type: docs
weight: 160
url: /it/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, stato di sessione web, sqlserver, modalità di stato di sessione
description: Questo articolo illustra come configurare in GridWeb quando la modalità di stato di sessione web è SQL Server.
---

## **Possibili Scenari di Utilizzo**
Questo articolo spiega il funzionamento di GridWeb quando la modalità di stato di sessione ASP.NET è SQL Server.
## **Funzionamento di GridWeb quando la modalità di stato di sessione ASP.NET è SQL Server**
Se si desidera utilizzare SQL Server o StateServer per memorizzare le sessioni, utilizzare la modalità di sessione GridWeb. Il controllo GridWeb supporta ora la serializzazione dei suoi dati in SQL Server o StateServer.

Imposterai GridWeb.SessionMode su SessionMode.Session e utilizzerai le seguenti impostazioni di esempio Web.Config. Si prega di modificare gli attributi sessionState secondo le proprie esigenze.
## **Impostazioni di esempio dello stato di sessione Web.Config**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Articolo di riferimento**
- [Abilitare diversi modi di GridWeb](/cells/it/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
