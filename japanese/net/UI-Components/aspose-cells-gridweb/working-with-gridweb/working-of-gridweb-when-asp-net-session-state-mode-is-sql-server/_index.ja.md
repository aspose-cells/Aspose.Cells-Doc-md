---
title: ASP.NETセッション状態モードがSQL Serverの場合のGridWebの動作
type: docs
weight: 160
url: /ja/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb,webセッション状態,sqlserver,セッション状態モード
description: この記事では、webセッション状態モードがSQL Serverの場合のGridWebの構成方法について紹介しています。
---

## **可能な使用シナリオ**
この記事では、ASP.NETセッション状態モードがSQL Serverの場合のGridWebの動作について説明しています。
## **ASP.NETセッション状態モードがSQL Serverの場合のGridWebの動作**
セッションを保持するためにSQL ServerまたはStateServerを使用したい場合は、GridWeb Session Modeを使用します。GridWebコントロールは、データをSQL ServerまたはStateServerにシリアライズすることができます。

GridWeb.SessionModeをSessionMode.Sessionに設定し、以下のサンプルWeb.Config設定を使用します。必要に応じてsessionState属性を変更してください。
## **サンプルWeb.Configセッション状態設定**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **参考記事**
- [異なる GridWeb モードを有効にする](/cells/ja/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
