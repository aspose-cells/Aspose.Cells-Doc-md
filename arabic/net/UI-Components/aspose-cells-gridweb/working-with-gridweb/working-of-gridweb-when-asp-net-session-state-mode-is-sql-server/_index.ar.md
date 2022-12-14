---
title: العمل من GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server
type: docs
weight: 160
url: /ar/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **سيناريوهات الاستخدام الممكنة**
يشرح هذا المقال عمل GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server.
## **العمل من GridWeb عندما يكون وضع حالة الجلسة ASP.NET هو SQL Server**
إذا كنت تريد استخدام SQL Server أو StateServer لعقد الجلسات ، فاستخدم وضع جلسة GridWeb. يدعم عنصر التحكم GridWeb الآن إجراء تسلسل لبياناته إلى SQL Server أو StateServer.

ستقوم بتعيين GridWeb.SessionMode إلى SessionMode.Session واستخدام إعدادات Web.Config النموذجية التالية. يُرجى تغيير سمات حالة الجلسة وفقًا لاحتياجاتك.
## **عينة إعدادات حالة جلسة Web.Config**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **مقالة مرجعية**
- [تمكين أوضاع GridWeb المختلفة](/cells/ar/net/enable-different-gridweb-modes/)
