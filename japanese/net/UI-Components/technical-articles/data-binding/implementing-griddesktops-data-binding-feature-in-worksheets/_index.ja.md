---
title: ワークシートに GridDesktop データ バインディング機能を実装する
type: docs
weight: 10
url: /ja/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

データ バインディングは、Microsoft .NET フレームワークによって提供される興味深い機能です。 Microsoft によって提供される DataGrid コントロールがデータ バインディングをサポートしていることはわかっています。つまり、DataGrid は任意のデータ ソースにバインドできます (DataSet、DataTable、および DataView オブジェクトを使用)。この機能により、開発者の作業が大幅に楽になりました。同じ概念に基づいて、Aspose.Cells.GridDesktop はデータ バインディングもサポートしているため、開発者はワークシートを任意のデータ ソースにバインドできます。この記事では、この機能について説明します。

{{% /alert %}} 
## **サンプル データベースの作成**
1. この例で使用するサンプル データベースを作成します。 Microsoft Access を使用して、Products テーブルを含むサンプル データベースを作成しました (以下のスキーマ)。

![todo:画像_代替_文章](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Products テーブルに 3 つのダミー レコードが追加されます。
   **Products テーブルのレコード** 

![todo:画像_代替_文章](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **サンプル アプリケーションの作成**
ここで、Visual Studio で簡単なデスクトップ アプリケーションを作成し、次の操作を行います。

1. ツールボックスから「GridControl」コントロールをドラッグし、フォームにドロップします。
1. フォームの下部にあるツールボックスから 4 つのボタンをドロップし、それらのテキスト プロパティを次のように設定します。**ワークシートをバインド**, **行を追加する**, **行を削除**と**データベースへの更新**それぞれ。
## **名前空間の追加とグローバル変数の宣言**
この例では Microsoft Access データベースを使用しているため、コードの先頭に System.Data.OleDb 名前空間を追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


この名前空間でパッケージ化されたクラスを使用できるようになりました。

1. グローバル変数を宣言します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **データベースからのデータを DataSet に入力する**
サンプル データベースに接続して、データを取得し、DataSet オブジェクトに入力します。

1. 以下のコードに示すように、OleDbDataAdapter オブジェクトを使用してサンプル データベースに接続し、データベースの Products テーブルから取得したデータを DataSet に入力します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **ワークシートを DataSet にバインドする**
ワークシートを DataSet の Products テーブルにバインドします。

1. 目的のワークシートにアクセスします。
1. ワークシートを DataSet の Products テーブルにバインドします。

次のコードを**ワークシートをバインド**ボタンのクリックイベント。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **ワークシートの列ヘッダーの設定**
バインドされたワークシートはデータを正常にロードするようになりましたが、列ヘッダーにはデフォルトで A、B、および C というラベルが付けられています。列ヘッダーをデータベース テーブルの列名に設定することをお勧めします。

ワークシートの列ヘッダーを設定するには:

1. DataSet の DataTable (Products) の各列のキャプションを取得します。
1. ワークシート列のヘッダーにキャプションを割り当てます。

に書かれたコードを追記**ワークシートをバインド**次のコード スニペットを使用して、ボタンのクリック イベントを作成します。これにより、古い列ヘッダー (A、B、および C) が ProductID、ProductName、および ProductPrice に置き換えられます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **列の幅とスタイルのカスタマイズ**
ワークシートの外観をさらに改善するために、列の幅とスタイルを設定することができます。たとえば、列ヘッダーまたは列内の値が、セル内に収まらない長い文字数で構成されている場合があります。このような問題を解決するために、Aspose.Cells.GridDesktop は列の幅の変更をサポートしています。

次のコードを**ワークシートをバインド**ボタン。列幅は、新しい設定に従ってカスタマイズされます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop は、列へのカスタム スタイルの適用もサポートしています。に追加された次のコード**ワークシートをバインド**ボタンをクリックして、列のスタイルをカスタマイズして見やすくします。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


アプリケーションを実行し、**ワークシートをバインド**ボタン。
## **行の追加**
ワークシートに新しい行を追加するには、Worksheet クラスの AddRow メソッドを使用します。これにより、下部に空の行が追加され、新しい DataRow がデータ ソースに追加されます (ここでは、新しい DataRow が DataSet の DataTable に追加されます)。開発者は、AddRow メソッドを何度も呼び出すことで、必要なだけ行を追加できます。行が追加されると、ユーザーはそれに値を入力できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **行の削除**
Aspose.Cells.GridDesktop は、Worksheet クラスの RemoveRow メソッドを呼び出して行を削除することもサポートしています。 Aspose.Cells.GridDesktop を使用して行を削除するには、行のインデックスを削除する必要があります。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


上記のコードを**行を削除**ボタンをクリックしてアプリケーションを実行します。行が削除される前に、いくつかのレコードが表示されます。行を選択して**行を削除**ボタンは、選択した行を削除します。
## **データベースへの変更の保存**
最後に、ユーザーがワークシートに加えた変更をデータベースに保存するには、OleDbDataAdapter オブジェクトの Update メソッドを使用します。 Update メソッドは、ワークシートのデータ ソース (DataSet、DataTable など) を取得して、データベースを更新します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. 上記のコードを**データベースへの更新**ボタン。
1. アプリケーションを実行します。
1. ワークシート データに対していくつかの操作を実行します。たとえば、新しい行を追加したり、既存のデータを編集または削除したりします。
1. 次にクリック**データベースへの更新**変更をデータベースに保存します。
1. データベースをチェックして、それに応じてテーブル レコードが更新されていることを確認します。
