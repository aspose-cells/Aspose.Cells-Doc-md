---
title: Fonctionnement de GridWeb lorsque le mode d état de session ASP.NET est SQL Server
type: docs
weight: 160
url: /fr/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, état de session web, sqlserver, mode d état de session
description: Cet article présente comment configurer GridWeb lorsque le mode d état de session web est SQL Server.
---

## **Scénarios d'utilisation possibles**
Cet article explique le fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server.
## **Fonctionnement de GridWeb lorsque le mode d'état de session ASP.NET est SQL Server**
Si vous souhaitez utiliser SQL Server ou StateServer pour conserver les sessions, utilisez le mode de session GridWeb. Le contrôle GridWeb prend désormais en charge la sérialisation de ses données vers SQL Server ou StateServer.

Vous définirez GridWeb.SessionMode sur SessionMode.Session et utiliserez les paramètres Web.Config suivants. Veuillez modifier les attributs sessionState selon vos besoins.
## **Paramètres d'état de session du fichier Web.Config d'exemple**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Article de référence**
- [Activer différents modes GridWeb](/cells/fr/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
