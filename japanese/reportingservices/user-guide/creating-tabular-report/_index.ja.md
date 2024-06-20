---
title: タブル型レポートの作成
type: docs
weight: 70
url: /ja/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Aspose.Cells レポート テンプレートのテーブルは、ヘッダー、表データ行、行グループ、およびフッターで構成されています。次に示すのはサンプルテーブルです。

**サンプルのテーブル** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **テーブル ヘッダー**
テーブルヘッダーには通常、各テーブル列のタイトルやその他のテキスト項目（静的テキスト、レポートパラメータ、グローバルレポート変数など）が含まれます。テーブルヘッダーはオプションです。ヘッダーを使用する場合は、ヘッダータグをテーブルデータの最初の列の左側に配置して、その行がヘッダーであることを示す必要があります。
#### **テーブルデータ行**
テーブルデータ行はスマートマーカーを含むセルの行です。テーブルには単一のデータ行のみを含めることができます。
#### **行グループ**
行グループは通常、テーブルデータ行の直後に続き、グループタグとグループデータ行の 2 つのパーツで構成されています。 

グループタグは、行グループのデータ行であることを示すために、テーブルデータ列の最初の左側に配置されます。グループタグの形式は ##group{GroupColumn} であり、SalesOrderNumber など、データセットの列名の一つです。テーブルには 1 つの行グループのみを含めることができますが、行グループには 1 つ以上のグループデータ行を含めることができます。グループタグは、サンプルの最初のデータ行にのみ配置できます。

レンダリング時には出力のMicrosoft Excelファイルからグループタグが削除されます。行グループは任意です。
#### **フッター**
フッターは行グループの後に配置され、フッタータグ、フッターデータ行、およびフッターテキストエリアから構成されます。 

フッタータグは、テーブルデータ列の最初の列の左側に配置されるべきであり、その行がテーブルフッターであることを示します。1つのテーブルには複数のフッターデータ行を含めることができ、各フッター行はフッタータグでマークする必要があります。 

フッターテキストエリアには静的テキスト、レポートパラメータ、グローバルレポート変数を含めることができます。上記のサンプルに示されています。

レンダリング時には出力のMicrosoft Excelファイルからフッタータグが削除されます。フッターは任意です。

サンプルテンプレートの出力は以下に示されています。

サンプルテンプレート 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **このセクションには以下のトピックが含まれています:** 
- [テーブルレポートの作成の準備](/cells/ja/reportingservices/preparing-for-creating-table-report/)
- [テーブルの基本情報を追加](/cells/ja/reportingservices/adding-base-information-for-table/)
- [レポートサービスの数式を追加](/cells/ja/reportingservices/adding-reporting-services-formulas/)
- [テーブルグループを追加](/cells/ja/reportingservices/adding-table-group/)
- [テーブルフッターを追加](/cells/ja/reportingservices/adding-table-footers/)
- [レポートにレポートパラメータを追加](/cells/ja/reportingservices/adding-report-parameters-to-report/)
- [レポートにレポートサービスのグローバル変数を追加](/cells/ja/reportingservices/adding-reporting-services-global-variables-to-report/)
- [レポート属性を設定](/cells/ja/reportingservices/setting-report-attributes/)
- [レポート属性を変更](/cells/ja/reportingservices/modifying-report-attributes/)
