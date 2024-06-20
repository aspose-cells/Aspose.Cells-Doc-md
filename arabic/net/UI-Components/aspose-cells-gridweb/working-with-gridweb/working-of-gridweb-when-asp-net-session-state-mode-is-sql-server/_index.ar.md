---
title: عند عمل GridWeb عندما يكون وضع حالة جلسة ASP.NET هو SQL Server
type: docs
weight: 160
url: /ar/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, وضع حالة الجلسة على الويب, SQL Server, وضع حالة الجلسة
description: يقدم هذا المقال كيفية التكوين في GridWeb عندما يكون وضع حالة الجلسة على الويب هو SQL Server.
---

## **سيناريوهات الاستخدام المحتملة**
يشرح هذا المقال عمل GridWeb عندما يكون وضع حالة جلسة ASP.NET هو SQL Server.
## ** عند عمل GridWeb عندما يكون وضع حالة جلسة ASP.NET هو SQL Server**
إذا كنت ترغب في استخدام SQL Server أو StateServer لاحتواء الجلسات, استخدم وضع الجلسة لـ GridWeb. يدعم السيطرة GridWeb الآن تسلسل بياناتها إلى SQL Server أو StateServer.

ستضبط GridWeb.SessionMode إلى SessionMode.Session واستخدم إعدادات Web.Config العينية التالية. يرجى تغيير سمات sessionState حسب احتياجاتك.
## **إعدادات عينية لـ Web.Config عن وضع حالة الجلسة**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **مقال الإحالة**
- [تمكين أوضاع GridWeb المختلفة](/cells/ar/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
