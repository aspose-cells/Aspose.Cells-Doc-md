---
title: ピボットテーブルの操作
type: docs
weight: 100
url: /ja/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

あ*ピボットテーブル*データを要約し、意味のある方法で表示するインタラクティブなテーブルです。 SQL Server Reporting Services は、ピボット テーブルを保持している間、レポートを Microsft Excel 形式にエクスポートできません。レポート ユーザーは、ピボット テーブル レポートを Reporting Services から Microsoft Excel にエクスポートするたびに、ピボット テーブルを手動で作成する必要があります。 Aspose.Cells for Reporting Services を使用すると、レポートのデザイン時に一度ピボット テーブルをデザインできます。レポートが実行されるたびに、Aspose.Cells for Reporting Services はレポートを Microsoft Excel にエクスポートし、データをピボット テーブルに更新します。

{{% /alert %}} 

ピボット テーブル レポートを作成するには:

1. ピボット テーブルのデータ ソースとしてデータセットを作成します。
以下では、SQL Server Reporting Services 2005 に同梱されている AdventureWorks サンプル データベースを使用して、"sales" という名前のデータセットを作成します。
データセットの SQL は次のとおりです。

**SQL**

{{< highlight "csharp" >}}

 SELECT  PC.Name AS ProdCat,

	    PS.Name AS SubCat,

	    DATEPART(yy, SOH.OrderDate) AS OrderYear,

	    'Q' + DATENAME(qq, SOH.OrderDate) AS OrderQtr,

         SUM(SOD.UnitPrice * SOD.OrderQty) AS Sales

FROM    Production.ProductSubcategory PS INNER JOIN

         Sales.SalesOrderHeader SOH INNER JOIN

         Sales.SalesOrderDetail SOD ON SOH.SalesOrderID = SOD.SalesOrderID INNER JOIN

         Production.Product P ON SOD.ProductID = P.ProductID ON PS.ProductSubcategoryID = P.ProductSubcategoryID INNER JOIN

         Production.ProductCategory PC ON PS.ProductCategoryID = PC.ProductCategoryID

WHERE   (SOH.OrderDate BETWEEN '1/1/2002' AND '12/31/2003')

GROUP BY  DATEPART(yy, SOH.OrderDate), PC.Name, PS.Name, 'Q' + DATENAME(qq, SOH.OrderDate), PS.ProductSubcategoryID



{{< /highlight >}}



{{% alert color="primary" %}} 

を参照してください。[データ ソースとクエリ](/cells/ja/reportingservices/data-sources-and-queries/) Aspose.Cells.Report.Designer を使用してデータ ソースとデータセットを作成する方法の詳細については、

{{% /alert %}} 

1. の指示に従ってテーブル レポートを作成します。[表形式レポートの作成](/cells/ja/reportingservices/creating-tabular-report/)、以下に示すように。
テーブルは、ピボット テーブルのデータ ソースになります。

![todo:画像_代替_文章](working-with-pivottable_1.png)




1.  Microsoft エクセルで、**入れる**メニュー、選択**名前**その後**定義**.
1. 名前を「営業」と定義します。
名前の範囲は、以下に示すように、ヘッダー タイトルの最初のセルから始まり、テーブル データ行の最後のセルで終わります。

![todo:画像_代替_文章](working-with-pivottable_2.png)




1. クリック**わかった**終わる。
1. ピボット テーブル用の新しいシートを作成します。
1. から**データ**メニュー、選択**ピボットテーブルとピボットグラフ レポート**ピボット テーブルを追加します。
ダイアログが表示されます。
1. 選択する**Microsoft Office Excel リストまたはデータベース**データソースとして**ピボットテーブル**レポートの種類として。
1. クリック**次**続ける。

![todo:画像_代替_文章](working-with-pivottable_3.png)




1. ダイアログ ボックスに、上で定義した名前「sales」を入力します。
1. クリック**次**続ける。

![todo:画像_代替_文章](working-with-pivottable_4.png)




1. クリック**終了**. 

![todo:画像_代替_文章](working-with-pivottable_5.png)




1.  Excel でピボット テーブルを設計します。

![todo:画像_代替_文章](working-with-pivottable_6.png)



設計されたピボット テーブルを以下に示します。

![todo:画像_代替_文章](working-with-pivottable_7.png)




1. ピボット テーブルを右クリックし、**テーブル オプション**.
1. ことを確認してください**開いたらリフレッシュ**が選択されます。

![todo:画像_代替_文章](working-with-pivottable_8.png)




1. レポートを保存し、レポート サーバーに公開します。
1. レポート サーバーからレポートをエクスポートします。
結果を以下に示します。

![todo:画像_代替_文章](working-with-pivottable_9.png)
