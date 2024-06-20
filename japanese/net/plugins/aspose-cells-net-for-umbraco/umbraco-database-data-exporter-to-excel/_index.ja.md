---
title: Umbraco データベースデータエクスポーターを Excel にエクスポート
type: docs
weight: 20
url: /ja/net/umbraco-database-data-exporter-to-excel/
---

## **紹介**
Aspose .NET Database Data Exporter to Excel for Umbraco Moduleは、ユーザーがローカルまたはリモートのデータベーステーブル、ビュー、およびカスタムクエリからデータをMicrosoft ExcelまたはOpenOfficeスプレッドシートに直接エクスポートできるようにします。このモジュールは、Aspose.Cellsが提供する強力なスプレッドシート作成機能をデモンストレーションしています。この初期バージョンのモジュールには、エクスポートプロセスをシンプルで使いやすくする以下のクールな機能が搭載されています。
### **モジュールの機能**
このアドオンの最初のバージョンには、次の機能があります:

- ローカルMS SQL Serverデータベースに接続を許可
- リモートMS SQL Serverデータベースに接続を許可
- 接続したデータベースからすべてのテーブルをポップアップ
- 接続したデータベースからすべてのビューをポップアップ
- カスタムクエリの記述を許可
- コンテンツの長さに合わせて列の幅を自動調整
- エクセルセル内の32kを超える文字列をスキップすることを許可（LoadOptions）
- ヘッダーカラムの書式を太字テキストに適用
- データソースとして使用を許可（テーブル、ビュー、カスタムクエリ）
- マイクロソフトエクセルドキュメント（.xls、.xlsx、.xlsb）へのデータのエクスポートを許可
- タブ区切りテキストドキュメント（*.txt）へのデータのエクスポートを許可
- CSV（カンマ区切り）（*.csv）へのデータのエクスポートを許可
- OpenDocumentスプレッドシート（*.ods）へのデータのエクスポートを許可
- エクスポート前に出力形式を選択するオプションを提供
- エクスポートされたドキュメントは自動的にブラウザに送信されてダウンロードされます 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **システム要件およびサポートされるプラットフォーム**
### **システム要件**
Aspose .NET Database Data Exporter to Excel for Umbracoモジュールを設定するには、次の要件を満たしている必要があります:

- Umbraco 6.2.5およびUmbraco 6バージョン
- MS SQL Serverを搭載したUmbraco
- Microsoft .Net Framework 4.0

**注意:** このリリースではUmbraco 7およびそれ以上のバージョンはサポートされていません。次のバージョンでUmbraco 7のサポートを追加するためのフィードバックをお待ちしております。
### **サポートされているプラットフォーム**
このモジュールはすべてのバージョンでサポートされています

- ASP.NET 4.0で動作しているUmbraco 6.0
## **ダウンロード**
Aspose .NET Cells Database Data Exporter to Excel for Umbracoモジュールは、次のいずれかの場所からダウンロードできます

- [Umbracoプロジェクト](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **インストール**
ダウンロードしたら、次の手順に従ってこのパッケージをUmbracoウェブサイトにインストールしてください:

1. たとえば以下のURLに移動してUmbracoの**Developer**セクションにログインします: `http://www.myblog.com/umbraco`
1. ツリーから**パッケージ**フォルダーを展開します。
1. ここからパッケージをインストールする方法は2つあります: **Install local package**を選択するか、**Umbraco Package Respository**を閲覧します。
1. **ローカルパッケージをインストール**を選択する場合は、パッケージを解凍せずにzipをUmbracoに読み込んでください。
1. 画面の指示に従います。

**注意:** インストール中に「最大リクエスト長が超過しました」というエラーが発生することがあります。Umbraco web.config ファイルの 'maxRequestLength' 値を更新することで簡単にこの問題を解決できます。
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **を使用する**
Aspose .NETデータベースデータエクスポータをExcel for Umbracoモジュールをインストールしたら、ウェブサイトでそれを使用するのはとても簡単です。以下のシンプルなステップに従って始めることができます。

1. たとえば`http://www.myblog.com/umbraco/` のような、Umbracoの**Developer**セクションにログインしていることを確認します。
1. 画面下部のセクションリストで**Settings**をクリックします。
1. **Templates**ノードを展開し、たとえばTextpageのように追加したいテンプレートを選択します。
1. 選択したテンプレート内でエクスポートボタンを追加したい位置を選択します。通常、ページの右上やページの下部などに追加したい場合があります。
1. 上部リボンで**Insert Macro**をクリックします。
1. **Choose a macro**（Aspose .NETデータベースデータエクスポータをExcel for Umbraco）から、最近インストールしたAspose .NETデータベースデータエクスポータをExcel for Umbracoのマクロを選択し、**OK**をクリックします。

詳細については、以下のスクリーンショットをご確認ください。 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

Aspose .NETデータベースデータエクスポータをExcelモジュールをページに追加することができました。

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. MS SQL Server Connection Stringを入力するか、事前に入力されたものを使用します。
1. データソースタイプ（Table、View、Custom Query）を選択します。
1. データソース（Table、View、Custom Query）を選択または入力します。
1. エクスポートタイプを選択します。
1. データをエクスポートします。
1. 希望のファイルが自動的にダウンロードされます。
## **ビデオデモ**
モジュールの動作を確認するために、下記の[ビデオ](https://www.youtube.com/watch?v=MkfKyeLTauE)をご覧ください。
## **サポート、拡張、貢献**
### **サポート**
Asposeが立ち上がって最初の日から、良い製品だけを提供するだけでは不十分だと分かっていました。良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときにどれだけイライラするか理解しています。私たちは問題を解決するためにここにいて、それを作り出すためではありません。

そのため、無料サポートを提供しています。製品を購入したか、評価を使用しているかに関わらず、私たちの製品を使用するすべての人にフルの注意と尊敬を提供する価値があります。

Aspose.Words .NET for Umbraco Modules に関連する問題や提案をログに記録できます。以下のプラットフォームのいずれかを使用してください

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **拡張と貢献**
Export Members to Excel はオープンソースのアドオンで、そのソースコードは以下の主要なソーシャルコーディングウェブサイトで利用できます。開発者はソースコードをダウンロードして、自分の要件に応じて機能を拡張することができます。
#### **ソースコード**
最新のソースコードを以下の場所から取得できます

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **ソースコードの構成方法**
以下のアイテムがインストールされている必要があります

- Visual Studio 2010 またはそれ以降

開始するための簡単なステップに従ってください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010を開き、**ファイル** > **プロジェクトを開く** を選択してください
1. ダウンロードした最新のソースコードに移動し、**e.g Aspose.DatabaseDataExportertoExcel.sln**を開きます。
