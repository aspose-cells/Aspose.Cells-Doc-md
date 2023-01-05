---
title: Funcionamiento de GridWeb cuando el modo de estado de sesión ASP.NET es SQL Server
type: docs
weight: 160
url: /es/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Posibles escenarios de uso**
Este artículo explica el funcionamiento de GridWeb cuando el modo de estado de sesión ASP.NET es SQL Server.
## **Funcionamiento de GridWeb cuando el modo de estado de sesión ASP.NET es SQL Server**
Si desea utilizar SQL Server o StateServer para realizar sesiones, utilice el modo de sesión de GridWeb. El control GridWeb ahora admite la serialización de sus datos en SQL Server o StateServer.

Establecerá GridWeb.SessionMode en SessionMode.Session y utilizará la siguiente configuración de ejemplo de Web.Config. Cambie los atributos de sessionState según sus necesidades.
## **Ejemplo de configuración de estado de sesión de Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Artículo de referencia**
- [Habilitar diferentes modos GridWeb](/cells/es/net/enable-different-gridweb-modes/)
