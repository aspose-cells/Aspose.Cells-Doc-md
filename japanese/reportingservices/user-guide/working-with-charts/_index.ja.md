---
title: チャートの操作
type: docs
weight: 110
url: /ja/reportingservices/working-with-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells レポート テンプレートは Microsoft Excel チャートをサポートします。レポートを実行するたびに、チャートに最新のデータが取り込まれます。

{{% /alert %}} 

レポート テンプレートにグラフを追加するには:

1. まず、グラフのデータ ソースとなるデータセットを作成します。
以下では、SQL Server Reporting Services 2005 に同梱されている AdventureWorks サンプル データベースを使用して、Sales という名前のデータセットを作成します。
この SQL は、データセットを定義します。

**SQL**

{{< highlight "csharp" >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



を参照してください。[データ ソースとクエリ](/cells/ja/reportingservices/data-sources-and-queries/) Aspose.Cells.Report.Designer でデータ ソースとデータセットを作成する方法の詳細については、

1. の指示に従って、表形式のレポートを作成します。[表形式レポートの作成](/cells/ja/reportingservices/creating-tabular-report/) .この例で作成したレポートを以下に示します。テーブルはチャートのデータ ソースです。

![todo:画像_代替_文章](working-with-charts_1.png)




1.  Microsoft Excel で、**入れる**メニューと選択**チャート**.
1. クリック**次**. 

![todo:画像_代替_文章](working-with-charts_2.png)




1. クリック**シリーズ**タブ。

![todo:画像_代替_文章](working-with-charts_3.png)




1. クリック**追加**. 

![todo:画像_代替_文章](working-with-charts_4.png)




1. ダイアログ ボックスで、Series1 (Quarter シリーズ) の値をテーブルの最初のデータ フィールドに設定します。
サンプルでは、「CompanySales!$C$3:$C$3」です。最初の $C$3 は「Quarter」の最初の行インデックスで、2 番目の $C$3 は「Quarter」の最後の行インデックスのプレースホルダーであり、レンダリング時にテーブル データの実際の行インデックスに置き換えられます。カテゴリ (X) 軸ラベルを「=CompanySales!$C$3:$C$3」に設定します。

![todo:画像_代替_文章](working-with-charts_5.png)




1. クリック**追加**別のシリーズを追加します。
サンプルでは、セールス シリーズを追加しました。
1. Series2 (販売系列) の値をテーブルの 2 番目のデータ フィールドに設定します。
サンプルでは「CompanySales!$D$3:$D$3」です。最初の $D$3 は "Sales" の最初の行インデックスで、2 番目の $D$3 は "Sales" の最後の行インデックスのプレースホルダーであり、レンダリング時にテーブル データの実際の行インデックスに置き換えられます。
1. クリック**次**続ける。

![todo:画像_代替_文章](working-with-charts_6.png)




1. ダイアログ ボックスで、グラフのタイトルとカテゴリ (X) 軸を設定します。
1. クリック**終了**作業を完了します。

![todo:画像_代替_文章](working-with-charts_7.png)



テンプレートは以下のようになります。

![todo:画像_代替_文章](working-with-charts_8.png)




1. レポートを保存し、レポート サーバーに公開します。
1. レポート サーバーからレポートをエクスポートします。
結果は以下の通り。

![todo:画像_代替_文章](working-with-charts_9.png)
