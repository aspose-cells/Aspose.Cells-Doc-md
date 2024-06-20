---
title: ワークシートでのGridDesktopデータバインディング機能の実装
type: docs
weight: 10
url: /ja/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop、データ バインディング、データ、バインド
description: この記事では、GridDesktop でのデータ バインディングの方法について紹介します。
---

{{% alert color="primary" %}} 

データ バインディングは、Microsoft .NET Framework が提供する興味深い機能です。Microsoft によって提供されている DataGrid コントロールは、データ バインディングをサポートしており、これにより DataGrid は DataSet、DataTable、DataView オブジェクトなど、任意のデータ ソースにバインドできます。この機能により、開発者の生活がずっと簡単になりました。同様のコンセプトに基づいて、Aspose.Cells.GridDesktop もデータ バインディングをサポートし、開発者はワークシートを任意のデータ ソースにバインドすることができます。この記事では、その機能を探ります。

{{% /alert %}} 
## **サンプル データベースの作成**
1. 例と一緒に使用するためのサンプル データベースを作成します。Microsoft Access を使用して、Products テーブルを含むサンプル データベースを作成しました(以下にスキーマを示します)。 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Productsテーブルにダミーレコード3件を追加します。
   Productsテーブルのレコード 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **サンプルアプリケーションの作成**
Visual Studioでシンプルなデスクトップアプリケーションを作成し、以下の手順を実行します。

1. ツールボックスから"GridControl"コントロールをドラッグしてフォーム上に配置します。
1. ツールボックスからボタンを4つフォームの下部にドロップし、それぞれのテキストプロパティを**Bind Worksheet**、**Add Row**、**Delete Row**、**Update to Database**に設定します。
## **名前空間の追加とグローバル変数の宣言**
この例では、Microsoft Accessデータベースを使用しているため、コードの先頭にSystem.Data.OleDb名前空間を追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


この名前空間で提供されているクラスを使用できます。

1. グローバル変数を宣言します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **データベースからデータを取得してDataSetを埋める**
サンプルデータベースに接続して、DataSetオブジェクトにデータを取得して埋めます。

1. OleDbDataAdapterオブジェクトを使用してサンプルデータベースに接続し、データベースのProductsテーブルから取得したデータでDataSetを埋めます。以下のコードに示すように。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **DataSetとWorksheetのバインディング**
WorksheetをDataSetのProductsテーブルにバインドします:

1. 任意のワークシートにアクセスします。
1. ワークシートをDataSetのProductsテーブルにバインドします。

**Bind Worksheet**ボタンのクリックイベントに以下のコードを追加します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **ワークシートの列見出しの設定**
バインドされたワークシートはデータを正常に読み込みますが、列見出しはデフォルトでA、B、Cとラベル付けされています。データベーステーブルの列名に列見出しを設定するのがより良いでしょう。

ワークシートの列見出しを設定するには:

1. DataSetのDataTable(Products)の各列のキャプションを取得します。
1. キャプションをワークシートの列見出しに割り当てます。

**Bind Worksheet**ボタンのクリックイベントに以下のコードスニペットを追加します。これにより、古い列見出し(A、B、C)はProductID、ProductName、ProductPriceで置き換えられます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **列の幅とスタイルのカスタマイズ**
さらにワークシートの外観を改善するために、列の幅とスタイルを設定することができます。たとえば、列見出しや列内の値がセルに収まらない長い文字数で構成されている場合があります。このような問題を解決するために、Aspose.Cells.GridDesktopは列の幅を変更することをサポートしています。

**Bind Worksheet**ボタンに以下のコードを追加します。列の幅は新しい設定に従ってカスタマイズされます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktopは列にカスタムスタイルを適用することもサポートしています。**Bind Worksheet**ボタンに追加された以下のコードは、列のスタイルをカスタマイズして見栄えを向上させます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


アプリケーションを実行し、**Bind Worksheet**ボタンをクリックします。
## **行の追加**
ワークシートに新しい行を追加するには、WorksheetクラスのAddRowメソッドを使用します。これにより、空の行が一番下に追加され、新しいDataRowがデータソースに追加されます（ここでは、新しいDataRowがDataSetのDataTableに追加されます）。開発者は、AddRowメソッドを繰り返し呼び出すことで、必要なだけ多くの行を追加できます。行が追加された後、ユーザーはその行に値を入力することができます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **行の削除**
Aspose.Cells.GridDesktopでは、WorksheetクラスのRemoveRowメソッドを呼び出すことで行を削除することもサポートされています。Aspose.Cells.GridDesktopを使用して行を削除するには、削除する行のインデックスが必要です。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


上記のコードを**行の削除**ボタンに追加し、アプリケーションを実行します。行が削除される前にいくつかのレコードが表示されます。行を選択し、**行の削除**ボタンをクリックすると、選択した行が削除されます。
## **データベースへの変更の保存**
最後に、ユーザーがワークシートに行った変更をデータベースに保存するには、OleDbDataAdapterオブジェクトのUpdateメソッドを使用します。Updateメソッドは、ワークシートのデータソース（DataSet、DataTableなど）を取り、それらの変更をデータベースに反映させます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. 上記のコードを**データベースに更新**ボタンに追加します。
1. アプリケーションを実行します。
1. ワークシートのデータに操作を行い、新しい行を追加したり、既存のデータを編集したり削除することがあります。
1. 次に**データベースに更新**をクリックして、変更をデータベースに保存します。
1. テーブルのレコードが適切に更新されたかどうかを確認します。
