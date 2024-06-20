---
title: Funcionamiento de GridWeb cuando el modo de estado de sesión de ASP.NET es SQL Server
type: docs
weight: 160
url: /es/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb,estado de sesión web,sqlserver,modo de estado de sesión
description: Este artículo describe cómo configurar en GridWeb cuando el modo de estado de sesión web es SQL Server.
---

## **Escenarios de uso posibles**
Este artículo explica el funcionamiento de GridWeb cuando el modo de estado de sesión de ASP.NET es SQL Server.
## **Funcionamiento de GridWeb cuando el modo de estado de sesión de ASP.NET es SQL Server**
Si desea usar SQL Server o StateServer para retener sesiones, use el modo de sesión GridWeb. El control GridWeb ahora admite la serialización de sus datos a SQL Server o StateServer.

Debe establecer GridWeb.SessionMode en SessionMode.Session y utilizar la siguiente configuración de muestra Web.Config. Cambie los atributos sessionState según sus necesidades.
## **Configuración de estado de sesión de Web.Config de muestra**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Artículo de referencia**
- [Activar diferentes modos de GridWeb](/cells/es/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
