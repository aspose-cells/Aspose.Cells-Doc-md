---
title: Funzionamento di GridWeb quando la modalità dello stato della sessione ASP.NET è SQL Server
type: docs
weight: 160
url: /it/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Possibili scenari di utilizzo**
Questo articolo illustra il funzionamento di GridWeb quando la modalità dello stato della sessione ASP.NET è SQL Server.
## **Funzionamento di GridWeb quando la modalità dello stato della sessione ASP.NET è SQL Server**
Se si desidera utilizzare SQL Server o StateServer per tenere le sessioni, utilizzare la modalità sessione GridWeb. Il controllo GridWeb ora supporta la serializzazione dei dati in SQL Server o StateServer.

Imposterai GridWeb.SessionMode su SessionMode.Session e utilizzerai le seguenti impostazioni Web.Config di esempio. Si prega di modificare gli attributi sessionState in base alle proprie esigenze.
## **Esempio di impostazioni dello stato della sessione Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Articolo di riferimento**
- [Abilita diverse modalità GridWeb](/cells/it/net/enable-different-gridweb-modes/)
