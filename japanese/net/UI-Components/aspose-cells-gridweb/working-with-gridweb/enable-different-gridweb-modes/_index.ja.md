---
title: さまざまな GridWeb モードを有効にする
type: docs
weight: 60
url: /ja/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

この記事では、Aspose.Cells.GridWeb のさまざまなモードについて説明します。これらのモードは、機能と動作が異なるため、論理的に区別されます。モードにはいくつかのタイプがあります。

- 編集モード
- ビューモード
- セッションモード
- セッションレス モード

これらのモードにはすべて独自の特徴があります。開発者は、要件に応じて任意のモードで Aspose.Cells.GridWeb を操作できます。以下、各モードについて見ていきます。

{{% /alert %}} 
## **編集モード**
デフォルトでは、Aspose.Cells.GridWeb コントロールは編集モードになっています。編集モードでは、Aspose.Cells.GridWeb コントロールによって提供されるすべての機能を使用して、グリッド コンテンツを完全に編集または変更できます。これらの機能は次のとおりです。

- グリッド コンテンツを Microsoft Excel ファイルに保存します。
- サーバーへのデータの送信。
- 数式の計算。
- 以前のアクションを元に戻すまたは破棄する。
- 行と列の管理。
- データの切り取り、コピー、または貼り付け。
- セルの書式設定など

**編集モードの GridWeb コントロール** 

![todo:画像_代替_文章](enable-different-gridweb-modes_1.png)

開発者は、GridWeb コントロールの EditMode プロパティを true に設定することにより、プログラムで編集モードに切り替えることもできます。

次の例は、プログラムで編集モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

ユーザーが**元に戻す**ボタンをクリックすると、GridWeb が以前の状態 (サーバーへの最後のポストバックの前の状態) に戻ります。前のアクションを 1 つずつキャンセルするわけではありません。

{{% /alert %}} 
## **ビューモード**
GridWeb コントロールが表示モードの場合、ユーザーはグリッド コンテンツを編集または変更できません。つまり、ユーザーはグリッド コンテンツのみを表示できます。そのため、このモードはビュー モードと呼ばれます。表示モードでは、いくつかのボタン (**送信**, **セーブ**と**元に戻す** ) が非表示になり、右クリックしたときに表示されるメニューには**コピー**オプション。

**表示モードの GridWeb コントロール** 

![todo:画像_代替_文章](enable-different-gridweb-modes_1.png)

開発者がユーザーにデータの表示のみを許可する場合は、GridWeb コントロールの EditMode プロパティを false に設定することにより、プログラムで表示モードに切り替えることができます。

以下の例は、プログラムで表示モードを有効にする方法を示しています



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

表示モードでも、ユーザーは行と列の高さと幅を変更できます。

{{% /alert %}} 
## **セッションモード**
Aspose.Cells.GridWeb コントロールは、Web ユーザーの各要求間で Web サーバーのユーザー セッションにシート データを保持します。これは、GridWeb コントロールがデフォルトで常にセッション モードで動作することを意味します。ただし、セッション モードで作業していない場合は、GridWEb コントロールの SessionMode プロパティを SessionMode.Session に設定してオンに切り替えます。

以下の例は、プログラムでセッション モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **セッションレス モード**
ユーザー セッションを使用してシート データを読み込んで保存することにより、セッション モードのアプローチが最高のパフォーマンスを提供することは既に説明しました。ただし、サーバーのメモリを消費します。そのため、多数の同時ユーザーが存在する場合、メモリの問題が発生する可能性があります。サーバーのメモリを節約し、多数の同時ユーザーをサポートするには、セッションレス モードを検討してください。

GridWeb コントロールの SessionMode プロパティを SessionMode.ViewState に設定することで、セッションレス モードをオンにすることができます。

以下の例は、プログラムでセッションレス モードを有効にする方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

重要: GridWeb の SessionMode プロパティが SessionMode.ViewState に設定されている場合、グリッドはページの ViewState にデータを格納します。これは、レンダリングされたページが大きくなり、より多くのネットワーク トラフィックを消費することを意味します。

{{% /alert %}} {{% alert color="primary" %}} 

SQL Server または StateServer を使用してセッションを保持する場合は、セッション モードを使用します。 GridWeb コントロールは、SQL Server または StateServer へのデータのシリアル化をサポートしています。

詳細については、次の記事を参照してください。

- [ASP.NET セッション状態モードが SQL Server の場合の GridWeb の動作](/cells/ja/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
