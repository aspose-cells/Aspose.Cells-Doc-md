---
title: Работа GridWeb при установке режима состояния сеанса ASP.NET на SQL Server
type: docs
weight: 160
url: /ru/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, веб состояние сеанса, sqlserver, режим состояния сеанса
description: Эта статья рассказывает, как настроить GridWeb, когда режим состояния сеанса веб сервера установлен на SQL Server.
---

## **Возможные сценарии использования**
Эта статья объясняет работу GridWeb, когда режим состояния сеанса ASP.NET установлен на SQL Server.
## **Работа GridWeb, когда режим состояния сеанса ASP.NET установлен на SQL Server**
Если вы хотите использовать SQL Server или StateServer для хранения сеансов, используйте режим сеанса GridWeb. Теперь элемент управления GridWeb поддерживает сериализацию своих данных в SQL Server или StateServer.

Вы установите GridWeb.SessionMode в SessionMode.Session и используете следующие примеры настроек Web.Config . Пожалуйста, измените атрибуты sessionState в соответствии с вашими потребностями.
## **Пример настроек состояния сеанса Web.Config**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Справочная статья**
- [Включение различных режимов GridWeb](/cells/ru/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
