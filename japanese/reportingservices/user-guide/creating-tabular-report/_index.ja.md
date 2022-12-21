---
title: 表形式レポートの作成
type: docs
weight: 70
url: /ja/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Aspose.Cells レポート テンプレートのテーブルは、ヘッダー、テーブル データ行、行グループ、およびフッターで構成されます。サンプルテーブルを以下に示します。

**テーブルの例** 

![todo:画像_代替_文章](creating-tabular-report_1.png)
#### **テーブル ヘッダー**
通常、テーブル ヘッダーには、各テーブル列のタイトルと、静的テキスト、レポート パラメータ、グローバル レポート変数などのその他のテキスト項目が含まれます。テーブル ヘッダーはオプションです。ヘッダーを使用する場合、行がヘッダーであることを示すために、ヘッダー タグをテーブル データの最初の列の左側に配置する必要があります。
#### **テーブル データ行**
テーブル データ行は、スマート マーカーを含むセルの行です。テーブルには、単一のデータ行のみを含めることができます。
#### **行グループ**
行グループはテーブル データ行のすぐ後に続き、グループ タグとグループ データ行の 2 つの部分で構成されます。

グループ タグは、行が行グループのデータ行であることを示すために、最初のテーブル データ列の左側に配置する必要があります。グループ タグの形式は ##group{GroupColumn} です。たとえば、##group{SalesOrderNumber} のようになります。ここで、SalesOrderNumber はデータ セットの列名の 1 つです。テーブルには 1 つの行グループのみを含めることができますが、行グループには複数のグループ データ行を含めることができます。上記のサンプルに示すように、グループ タグは最初のデータ行にのみ配置できます。

グループ タグは、レンダリング時に出力 Microsoft Excel ファイルから削除されます。行グループはオプションです。
#### **フッター**
フッターは行グループの後に続き、フッター タグ、フッター データ行、フッター テキスト領域の 3 つの部分で構成されます。

フッター タグは、行がテーブル フッターであることを示すテーブル データ列の最初の列の左側に配置する必要があります。テーブルには複数のフッター データ行を含めることができ、各フッター行はフッター タグでマークする必要があります。

上記のサンプルに示すように、フッター テキスト領域には、静的テキスト、レポート パラメーター、およびグローバル レポート変数を含めることができます。

フッター タグは、レンダリング時に出力 Microsoft Excel ファイルから削除されます。フッターはオプションです。

サンプル テンプレートの出力を以下に示します。

**サンプル テンプレート** 

![todo:画像_代替_文章](creating-tabular-report_2.png)

{{% /alert %}} 
###### **このセクションには、次のトピックが含まれています。**
- [テーブルレポート作成の準備](/cells/ja/reportingservices/preparing-for-creating-table-report/)
- [テーブルの基本情報を追加する](/cells/ja/reportingservices/adding-base-information-for-table/)
- [Reporting Services 式の追加](/cells/ja/reportingservices/adding-reporting-services-formulas/)
- [テーブル グループの追加](/cells/ja/reportingservices/adding-table-group/)
- [テーブル フッターの追加](/cells/ja/reportingservices/adding-table-footers/)
- [レポート パラメータをレポートに追加する](/cells/ja/reportingservices/adding-report-parameters-to-report/)
- [レポートへの Reporting Services グローバル変数の追加](/cells/ja/reportingservices/adding-reporting-services-global-variables-to-report/)
- [レポート属性の設定](/cells/ja/reportingservices/setting-report-attributes/)
- [レポート属性の変更](/cells/ja/reportingservices/modifying-report-attributes/)
