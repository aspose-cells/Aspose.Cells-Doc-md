---
title: Funktionieren von GridWeb, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist
type: docs
weight: 160
url: /de/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Mögliche Nutzungsszenarien**
In diesem Artikel wird die Funktionsweise von GridWeb erläutert, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist.
## **Funktionieren von GridWeb, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist**
Wenn Sie SQL Server oder StateServer zum Abhalten von Sitzungen verwenden möchten, verwenden Sie den GridWeb-Sitzungsmodus. Das GridWeb-Steuerelement unterstützt jetzt die Serialisierung seiner Daten zu SQL Server oder StateServer.

Sie legen GridWeb.SessionMode auf SessionMode.Session fest und verwenden die folgenden Web.Config-Beispieleinstellungen. Bitte ändern Sie die sessionState-Attribute nach Ihren Bedürfnissen.
## **Beispieleinstellungen für den Sitzungsstatus von Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referenzartikel**
- [Aktivieren Sie verschiedene GridWeb-Modi](/cells/de/net/enable-different-gridweb-modes/)
