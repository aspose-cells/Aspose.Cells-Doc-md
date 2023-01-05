---
title: Fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server
type: docs
weight: 160
url: /fr/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Scénarios d'utilisation possibles**
Cet article explique le fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server.
## **Fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server**
Si vous souhaitez utiliser SQL Server ou StateServer pour organiser des sessions, utilisez le mode Session GridWeb. Le contrôle GridWeb prend désormais en charge la sérialisation de ses données vers SQL Server ou StateServer.

Vous allez définir GridWeb.SessionMode sur SessionMode.Session et utiliser les exemples de paramètres Web.Config suivants. Veuillez modifier les attributs sessionState selon vos besoins.
## **Exemple de paramètres d'état de session Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Article de référence**
- [Activer différents modes GridWeb](/cells/fr/net/enable-different-gridweb-modes/)
