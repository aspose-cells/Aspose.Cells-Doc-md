---
title: Arbeiten von GridWeb, wenn der ASP.NET Sitzungsstatusmodus SQL Server ist
type: docs
weight: 160
url: /de/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, Web Sitzungsstatus, SQL Server, Sitzungsstatusmodus
description: Dieser Artikel zeigt, wie man GridWeb konfiguriert, wenn der Web Sitzungsstatusmodus SQL Server ist.
---

## **Mögliche Verwendungsszenarien**
Dieser Artikel erläutert, wie GridWeb funktioniert, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist.
## **Arbeiten von GridWeb, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist**
Wenn Sie SQL Server oder StateServer verwenden möchten, um Sitzungen zu speichern, verwenden Sie den GridWeb-Sitzungsmodus. Die GridWeb-Kontrolle unterstützt jetzt das Serialisieren ihrer Daten in SQL Server oder StateServer.

Sie legen den GridWeb.SessionMode auf SessionMode.Session fest und verwenden die folgenden Beispiele für Web.Config-Einstellungen. Bitte ändern Sie die sessionState-Attribute entsprechend Ihren Bedürfnissen.
## **Beispiel Web.Config-Einstellungen für den Sitzungsstatus**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referenzartikel**
- [Verschiedene GridWeb-Modi aktivieren](/cells/de/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
