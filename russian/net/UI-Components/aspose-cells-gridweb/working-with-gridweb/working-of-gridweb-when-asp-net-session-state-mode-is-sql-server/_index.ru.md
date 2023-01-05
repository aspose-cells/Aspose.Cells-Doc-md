---
title: Работа GridWeb, когда режим состояния сеанса ASP.NET — SQL Server
type: docs
weight: 160
url: /ru/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Возможные сценарии использования**
В этой статье объясняется работа GridWeb, когда режим состояния сеанса ASP.NET — SQL Server.
## **Работа GridWeb, когда режим состояния сеанса ASP.NET — SQL Server**
Если вы хотите использовать SQL Server или StateServer для проведения сеансов, используйте режим сеанса GridWeb. Элемент управления GridWeb теперь поддерживает сериализацию своих данных в SQL Server или StateServer.

Вы зададите для GridWeb.SessionMode значение SessionMode.Session и будете использовать следующие примеры параметров Web.Config. Пожалуйста, измените атрибуты sessionState в соответствии с вашими потребностями.
## **Пример параметров состояния сеанса Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Справочная статья**
- [Включить различные режимы GridWeb](/cells/ru/net/enable-different-gridweb-modes/)
