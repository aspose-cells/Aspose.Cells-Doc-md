---
title: ExcelへのUmbracoデータベースデータエクスポーター
type: docs
weight: 20
url: /ja/net/umbraco-database-data-exporter-to-excel/
---
## **序章**
Aspose .NET Umbraco モジュール用の Excel へのデータベース データ エクスポーターを使用すると、ユーザーは、ローカルまたはリモートのデータベース テーブル、ビュー、およびカスタム クエリから Microsoft Excel または OpenOffice スプレッドシートにデータを直接エクスポートできます。このモジュールは、Aspose.Cells が提供する強力なスプレッドシート作成機能を示しています。モジュールのこの初期バージョンには、次の優れた機能が強化されており、エクスポート プロセスがシンプルで使いやすくなっています。
### **モジュールの機能**
このアドオンの初期バージョンには、次の機能があります。

- ローカル MS SQL Server データベースへの接続を許可する
- リモート MS SQL Server データベースへの接続を許可する
- 接続されたデータベースからすべてのテーブルを作成します
- 接続されたデータベースからすべてのビューを取り込みます
- カスタムクエリの書き込みを許可
- コンテンツの長さに合わせて列を自動調整します。
- Excel セルで 32k を超える文字列をスキップできるようにする (LoadOptions)
- ヘッダー列の書式を太字として適用する
- データ ソース (テーブル、ビュー、カスタム クエリ) としての使用を許可する
- データを Microsoft Excel ドキュメント (.xls、.xlsx、および .xlsb) にエクスポート
- データをタブ区切りのテキスト ドキュメント (*.txt) にエクスポート
- データを CSV (カンマ区切り) にエクスポート (*.csv)
- データを OpenDocument スプレッドシート (*.od) にエクスポート
- エクスポートする前に、目的の出力形式を選択するオプション。
- エクスポートされたドキュメントは、ダウンロードのためにブラウザに自動的に送信されます。

.

![todo:画像_代替_文章](umbraco-database-data-exporter-to-excel_1)
## **システム要件とサポートされるプラットフォーム**
### **システム要求**
Aspose .NET Database Data Exporter を Umbraco モジュール用の Excel にセットアップするには、次の要件を満たす必要があります。

- Umbraco 6.2.5 & Umbraco 6 バージョン
- MS SQL Server を使用する Umbraco
- Microsoft .Net フレームワーク 4.0

**ノート：** Umbraco 7 以降は、このリリースではサポートされていません。フィードバックをお待ちしており、次のバージョンで Umbraco 7 のサポートを追加します。
### **サポートされているプラットフォーム**
このモジュールは、のすべてのバージョンでサポートされています。

- ASP.NET 4.0 で実行されている Umbraco 6.0
## **ダウンロード中**
Aspose .NET Cells Database Data Exporter to Excel for Umbraco モジュールは、次のいずれかの場所からダウンロードできます。

- [アンブラコ プロジェクト](https://goo.gl/BPrWm2)
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **インストール**
ダウンロードしたら、次の手順に従って、このパッケージを Umbraco Web サイトにインストールしてください。

1. アンブラコにログインする**デベロッパー**セクション、たとえば `http://www.myblog.com/umbraco`
1. ツリーから、**パッケージ**フォルダ。
1. ここから、パッケージをインストールする方法は 2 つあります。**ローカル パッケージをインストールする**または閲覧する**Umbraco パッケージ リポジトリ。**
1. インストールすれば**ローカル パッケージ**、パッケージを解凍せずに、zip を Umbraco にロードします。
1. 画面の指示に従います。

**ノート：**インストール時に「リクエストの最大長を超えました」というエラーが表示される場合があります。この問題は、Umbraco web.config ファイルの「maxRequestLength」値を更新することで簡単に修正できます。
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **使用する**
Aspose .NET Database Data Exporter to Excel for Umbraco モジュールをインストールすると、Web サイトで簡単に使用できるようになります。開始するには、次の簡単な手順に従ってください

1. Umbraco にログインしていることを確認します。**デベロッパー**セクション、たとえば `http://www.myblog.com/umbraco/`
1. クリック**設定**画面の左下にあるセクションのリストにあります。
1. 拡大する**テンプレート**ノードをクリックして、追加するテンプレート (Textpage など) を選択します。
1. 選択したテンプレートで、追加するボタンをエクスポートする位置を選択します。通常、ページの右上またはページの下部に追加することができます。
1. クリック**マクロを挿入**上のリボンに。
1. から**マクロを選択**(Aspose .NET Database Data Exporter to Excel for Umbraco)、最近インストールされた Aspose .NET Database Data Exporter to Excel for Umbraco マクロを選択し、**わかった**.

詳細については、以下のスクリーンショットを確認してください。

![todo:画像_代替_文章](umbraco-database-data-exporter-to-excel_2)

Aspose .NET Database Data Exporter to Excel モジュールがページに正常に追加されました。

![todo:画像_代替_文章](umbraco-database-data-exporter-to-excel_1)

1. 事前設定された MS SQL Server 接続文字列を入力または使用します
1. Selected データ ソース タイプ (テーブル、ビュー、カスタム クエリ)
1. データ ソースの選択または入力 (テーブル、ビュー、カスタム クエリ)
1. エクスポートの種類を選択
1. [データのエクスポート] をクリックします
1. 目的のファイルが自動的にダウンロードされます。
## **ビデオデモ**
チェックしてください[ビデオ](https://www.youtube.com/watch?v=MkfKyeLTauE)モジュールの動作を確認するには、以下を参照してください。
## **サポート、拡張、貢献**
### **サポート**
Aspose の最初の日から、私たちはお客様に良い製品を提供するだけでは十分ではないことを知っていました。また、優れたサービスを提供する必要もありました。私たち自身も開発者であり、技術的な問題やソフトウェアの異常によって必要な作業ができなくなると、どれほどイライラするかを理解しています。問題を作成するのではなく、問題を解決するためにここにいます。

そのため、無料サポートを提供しています。私たちの製品を購入したか、評価を使用しているかにかかわらず、私たちの製品を使用するすべての人は、私たちの十分な注意と尊敬に値します.

次のプラットフォームのいずれかを使用して、Umbraco モジュールの Aspose.Words .NET に関連する問題または提案を記録できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **拡張して貢献する**
メンバーを Excel にエクスポートは、オープン ソースのアドオンであり、そのソース コードは、以下に示す主要なソーシャル コーディング Web サイトで入手できます。開発者は、ソース コードをダウンロードし、独自の要件に従って機能を拡張することをお勧めします。
#### **ソースコード**
最新のソース コードは、次のいずれかの場所から入手できます。

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **ソースコードの構成方法**
ソースコードを開いて拡張するには、以下をインストールする必要があります

- Visual Studio 2010 以降

開始するには、次の簡単な手順に従ってください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010 を開き、選択します**ファイル** > **プロジェクトを開く**
1. ダウンロードして開いた最新のソースコードを参照します**例: Aspose.DatabaseDataExportertoExcel.sln**
