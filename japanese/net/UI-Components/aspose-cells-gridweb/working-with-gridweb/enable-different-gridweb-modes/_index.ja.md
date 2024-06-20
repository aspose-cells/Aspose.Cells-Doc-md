---
title: 異なる GridWeb モードを有効にする
type: docs
weight: 60
url: /ja/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: この記事では、GridWeb の EditMode と SessionMode との作業方法について紹介します。
---

{{% alert color="primary" %}} 

この記事では、Aspose.Cells.GridWeb のさまざまなモードについて説明します。これらのモードは、異なる機能と振る舞いを持つため、論理的に区別されます。次の種類のモードが特定されています:

- Edit モード
- View モード
- Session モード
- Sessionless モード

これらのモードはそれぞれ独自の特性を持ちます。開発者は、必要に応じて任意のモードで Aspose.Cells.GridWeb と連携できます。以下で各モードを見ていきます。

{{% /alert %}} 
## **Edit モード**
デフォルトでは、Aspose.Cells.GridWeb コントロールは Edit モードになっています。Edit モードでは、Aspose.Cells.GridWeb コントロールが提供するすべての機能を使用して、グリッドコンテンツを完全に編集したり修正したりできます。これらの機能には次のものが含まれます:

- グリッドのコンテンツを Microsoft Excel ファイルに保存する。
- サーバーにデータを送信する。
- 数式の計算。
- 前のアクションを取り消す、または破棄する。
- 行と列を管理する。
- データを切り取り、コピー、または貼り付ける。
- セルなどの書式を設定する。

**編集モードのGridWebコントロール** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

開発者は、GridWebコントロールのEditModeプロパティをtrueに設定することでプログラムで編集モードに切り替えることもできます。

以下の例は、プログラムで編集モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

ユーザーが**元に戻す**ボタンをクリックするたびに、GridWebは前の状態（サーバーへの最後のポストバックの前の状態）に戻ります。それは前のアクションを一つずつキャンセルするものではありません。

{{% /alert %}} 
## **ビューモード**
GridWebコントロールがビューモードになっているとき、ユーザーはグリッドのコンテンツを編集または修正することはできませんので、ユーザーはグリッドのコンテンツを表示することしかできません。そのためこのモードはビューモードと呼ばれています。ビューモードでは、一部のボタン（**送信**、**保存**、**元に戻す**）は非表示であり、右クリックした際に表示されるメニューには**コピー**オプションのみが含まれます。

**ビューモードのGridWebコントロール** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

開発者がユーザーにデータを表示のみに制限したい場合は、GridWebコントロールのEditModeプロパティをfalseに設定することでプログラムでビューモードに切り替えることができます。

以下の例は、プログラムでビューモードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

ビューモードでも、ユーザーは行と列の高さと幅を変更することができます。

{{% /alert %}} 
## **セッションモード**
Aspose.Cells.GridWebコントロールは、Webユーザーの各リクエスト間にWebサーバーのユーザーセッションにシートデータを保持します。つまり、GridWebコントロールはデフォルトで常にセッションモードで動作します。ただし、セッションモードで動作していない場合は、GridWebコントロールのSessionModeプロパティをSessionMode.Sessionに設定することでオンに切り替えることができます。

以下の例は、プログラムでセッションモードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **セッションレスモード**
セッションモードのアプローチは、ユーザーセッションを使用してシートデータを読み込み、保存することで最高のパフォーマンスを提供します。ただし、サーバーメモリを消費します。したがって、大量の同時ユーザーがある場合はメモリの問題が発生する可能性があります。サーバーメモリを節約し、大量の同時ユーザーをサポートするためには、セッションレスモードを検討してください。

セッションレスモードは、GridWebコントロールのSessionModeプロパティをSessionMode.ViewStateに設定することでオンにすることができます。

以下の例は、プログラムでセッションレスモードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

重要：GridWebのSessionModeプロパティがSessionMode.ViewStateに設定されている場合、グリッドはページのViewStateにデータを保存します。これにより、レンダリングされるページが大きくなり、ネットワークトラフィックをより多く消費します。

{{% /alert %}} {{% alert color="primary" %}} 

SQL ServerやStateServerを使用してセッションを保持したい場合は、セッションモードを使用してください。GridWebコントロールは、データをSQL ServerやStateServerにシリアライズすることをサポートしています。

詳細については、次の記事を参照してください。

- [ASP.NETセッション状態モードがSQL Serverの場合のGridWebの動作](/cells/ja/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
