---
title: ASP.NET セッション状態モードが SQL Server の場合の GridWeb の動作
type: docs
weight: 160
url: /ja/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **考えられる使用シナリオ**
この記事では、ASP.NET セッション状態モードが SQL Server の場合の GridWeb の動作について説明します。
## **ASP.NET セッション状態モードが SQL Server の場合の GridWeb の動作**
SQL Server または StateServer を使用してセッションを保持する場合は、GridWeb セッション モードを使用します。 GridWeb コントロールは、SQL Server または StateServer へのデータのシリアル化をサポートするようになりました。

GridWeb.SessionMode を SessionMode.Session に設定し、次のサンプル Web.Config 設定を使用します。必要に応じて sessionState 属性を変更してください。
## **サンプル Web.Config セッション状態設定**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **参考記事**
- [さまざまな GridWeb モードを有効にする](/cells/ja/net/enable-different-gridweb-modes/)
