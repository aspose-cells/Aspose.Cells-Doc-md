---
title: チャートの操作
type: docs
weight: 110
url: /ja/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Aspose.CellsレポートテンプレートはMicrosoft Excelチャートをサポートしています。レポートを実行するたびに、チャートに最新のデータが表示されます。 

{{% /alert %}} 

レポートテンプレートにチャートを追加するには:

1. まず、チャートのデータソースとなるデータセットを作成します。
   以下は、SQL Server Reporting Services 2005に同梱されているAdventureWorksサンプルデータベースを使用し、Salesという名前のデータセットを作成します。
   このSQLはデータセットを定義しています: 

**SQL**

{{< highlight csharp >}}

 SELECT DATEPART(yy,SOH.OrderDate) 'Year',

'Q'+DATENAME(qq,SOH.OrderDate) 'Quarter',

SUM(SOD.UnitPrice*SOD.OrderQty) 'Sales'

FROMAdventureWorks.Sales.SalesOrderDetail SOD,

AdventureWorks.Sales.SalesOrderHeader SOH

WHERE SOH.SalesOrderID = SOD.SalesOrderID

AND ((DATEPART(yy,SOH.OrderDate)=2002))

GROUP BY DATEPART(yy,SOH.OrderDate), 'Q'+DATENAME(qq,SOH.OrderDate)



{{< /highlight >}}



データソースとクエリ[Data Sources and Queries](/cells/ja/reportingservices/data-sources-and-queries/)を参照して、Aspose.Cells.Report.Designerでデータソースとデータセットを作成する方法について詳しく学んでください。

1. [Creating Tabular Report](/cells/ja/reportingservices/creating-tabular-report/)の指示に従って表形式のレポートを作成します。この例では以下のように作成したレポートを使用しています。表はチャートのデータソースです。 

![todo:image_alt_text](working-with-charts_1.png)




1. Microsoft Excelで**挿入**メニューをクリックし、**グラフ**を選択します。
1. **次へ** をクリックします。 

![todo:image_alt_text](working-with-charts_2.png)




1. **系列**タブをクリックします。 

![todo:image_alt_text](working-with-charts_3.png)




1. **追加** をクリックします。 

![todo:image_alt_text](working-with-charts_4.png)




1. ダイアログボックスで、Series1(四半期シリーズ)の値を表の最初のデータフィールドに設定します。
   例では、これは「CompanySales!$C$3:$C$3」です。「$C$3」は「Quarter」の最初の行インデックスで、「$C$3」は「Quarter」の最後の行のインデックスのプレースホルダですが、レンダリング時に表データの実際の行インデックスに置き換えられます。「=CompanySales!$C$3:$C$3」としてカテゴリ(X)軸ラベルを設定します。 

![todo:image_alt_text](working-with-charts_5.png)




1. もう一つの系列を追加するには**追加**をクリックします。
   例では、売上シリーズを追加しました。 
1. Series2(売上シリーズ)の値を表の2番目のデータフィールドに設定します。
   例では、「CompanySales!$D$3:$D$3」となります。「$D$3」は「Sales」の最初の行インデックスで、「$D$3」は「Sales」の最後の行のインデックスのプレースホルダですが、レンダリング時に表データの実際の行インデックスに置き換えられます。 
1. 次をクリックして続行します。 

![todo:image_alt_text](working-with-charts_6.png)




1. ダイアログボックスで、チャートのタイトルとカテゴリ(X)軸を設定します。
作業を完了するには**完了**をクリックします。 

![todo:image_alt_text](working-with-charts_7.png)



テンプレートは以下のようになります。 

![todo:image_alt_text](working-with-charts_8.png)




**開くたびにリフレッシュ**が選択されていることを確認します。
レポートを保存して、Report Serverに公開します。
   結果は以下のようになります。 

![todo:image_alt_text](working-with-charts_9.png)
