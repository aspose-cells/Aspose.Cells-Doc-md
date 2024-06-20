---
title: ピボットテーブルを使用する
type: docs
weight: 100
url: /ja/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

ピボットテーブルは、データを集計し意味のある方法で表示するインタラクティブなテーブルです。SQL Server Reporting Services はピボットテーブルを維持したままレポートをMicrosoft Excel形式にエクスポートすることができません。レポートユーザーは、Reporting ServicesからMicrosoft Excelにピボットテーブルレポートをエクスポートするたびに、手動でピボットテーブルを作成する必要があります。Aspose.Cells for Reporting Servicesを使用すると、レポートの設計時に一度だけピボットテーブルを設計できます。レポートが実行されるたびに、Aspose.Cells for Reporting ServicesはレポートをMicrosoft Excelにエクスポートし、データをピボットテーブルにリフレッシュします。

{{% /alert %}} 

ピボットテーブルレポートを作成するには:

1. ピボットテーブルのデータソースとしてデータセットを作成します。
   以下では、SQL Server Reporting Services 2005に含まれるAdventureWorksサンプルデータベースを使用し、「sales」という名前のデータセットを作成します。
   データセットのSQLは次のようになります: 

**SQL**

{{< highlight csharp >}}

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

[データソースとクエリ](/cells/ja/reportingservices/data-sources-and-queries/)を参照して、Aspose.Cells.Report.Designerを使用してデータソースとデータセットを作成する方法について詳しく学んでください。

{{% /alert %}} 

1. [タブラーレポートの作成](/cells/ja/reportingservices/creating-tabular-report/)の指示に従って、テーブルレポートを作成します。下図のようになります。
   このテーブルは、ピボットテーブルのデータソースになります。 

![todo:image_alt_text](working-with-pivottable_1.png)




1. Microsoft Excelで、**挿入**メニューから**名前**を選択し、**定義**を選択します。
1. 「sales」という名前を定義します。
   名前の範囲は、ヘッダータイトルの最初のセルからテーブルデータ行の最後のセルであることを示します。 

![todo:image_alt_text](working-with-pivottable_2.png)




1. 終了するには**OK**をクリックします。
1. ピボットテーブル用に新しいシートを作成します。
**データ**メニューから**ピボットテーブルおよびピボットチャート レポート**を選択して、ピボットテーブルを追加します。
   ダイアログが表示されます。
1. **Microsoft Office Excelリストまたはデータベース**をデータソースとし、**ピボットテーブル**をレポートの種類として選択します。
1. 次をクリックして続行します。 

![todo:image_alt_text](working-with-pivottable_3.png)




ダイアログボックスで、先ほど定義した「sales」と入力します。
1. 次をクリックして続行します。 

![todo:image_alt_text](working-with-pivottable_4.png)




1. **完了**をクリックします。 

![todo:image_alt_text](working-with-pivottable_5.png)




Excelでピボットテーブルを設計します。 

![todo:image_alt_text](working-with-pivottable_6.png)



設計されたピボットテーブルが以下に表示されます。 

![todo:image_alt_text](working-with-pivottable_7.png)




設計したピボットテーブルが以下に示されています。
ピボットテーブルを右クリックし、**テーブル オプション**を選択します。 

![todo:image_alt_text](working-with-pivottable_8.png)




**開くたびにリフレッシュ**が選択されていることを確認します。
レポートを保存して、Report Serverに公開します。
   Report Serverからレポートをエクスポートします。 

![todo:image_alt_text](working-with-pivottable_9.png)
