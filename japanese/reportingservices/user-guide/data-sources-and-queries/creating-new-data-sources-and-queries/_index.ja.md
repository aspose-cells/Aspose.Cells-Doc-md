---
title: 新しいデータ ソースとクエリの作成
type: docs
weight: 20
url: /ja/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer は MS Query と統合され、MS Query をデータ ソースとクエリを作成するためのツールとして使用します。 Aspose.Cells.Report.Designer で新しいデータ ソースとクエリを作成するには、次の手順に従います。

{{% /alert %}} 

Aspose.Cells.Report.Designer で新しいデータ ソースとクエリを作成するには:

1. Microsoft エクセルを開きます。
1. クリック**DataSet の構築**Aspose.Cells.Report.Designer ツールバーで:

![todo:画像_代替_文章](creating-new-data-sources-and-queries_1.png)


すべてのデータ ソースとクエリがダイアログ ボックスに一覧表示されます。

1. データ ソース ノード:

![todo:画像_代替_文章](creating-new-data-sources-and-queries_2.png)

1. データセットノード:

![todo:画像_代替_文章](creating-new-data-sources-and-queries_3.png)

1. ツリーのルート ノードを選択します。
1. クリック**追加**. 

   **データ ソースとデータ セットの追加** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_4.png)




1. ダイアログ ボックスで、データ ソースを呼び出します。**SQLサーバー**とデータセット**EmpsSalesDetail**.
1. クリック**次**. 

   **データ セットとデータ ソースの追加** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer は Microsoft クエリを開始します。

1.  [データ ソースの選択] ダイアログで、次のように選択します。**新しいデータ ソース**.
1. クリック**わかった**.
既存のデータ ソースを選択することもできます。

   **データ ソースの選択** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_6.png)




1. データ ソース名を入力し、データベース ドライバーのドロップダウン リストから SQL Server を選択します。
1. クリック**接続**. 

   **新しいデータ ソースの作成** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_7.png)




1. [SQL Server ログイン] ダイアログで、各項目に適切な値を選択します。
たとえば、サーバーをローカルに設定し、AdventureWorks データベースを選択して、**信頼できる接続を使用**.
1. クリック**わかった**. 

   **SQL サーバーへのログイン** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_8.png)




1. クリック**わかった**. 

   **SQL サーバーにログインしていることに注意してください。** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_9.png)



新しいデータ ソースが**データ ソースの選択**ダイアログ。

1. 新しいデータ ソースを選択します。

   **新しいデータ ソース** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_10.png)




1. クリック**わかった**Microsoft クエリを開きます。
1.  Microsoft クエリでクエリを作成するには、Microsoft クエリ ヘルパーを参照してください。次のサンプルでは、パラメーターを使用してクエリを作成します。

   **クエリの作成** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_11.png)



SQL は次のとおりです。

**SQL**

{{< highlight "csharp" >}}

 SELECT C.FirstName + ' ' + C.LastName AS Employee,

DATEPART(Month, SOH.OrderDate) AS OrderMonthNum,

PS.Name AS SubCat,

SUM(SOD.LineTotal) AS Sales,

SOH.SalesOrderNumber,

P.Name AS Product,

SUM(SOD.OrderQty) AS OrderQty,

SOD.UnitPrice,

PC.Name AS ProdCat

FROM  Sales.SalesOrderHeader SOH ,

Sales.SalesOrderDetail SOD ,

Sales.SalesPerson SP,

HumanResources.Employee E,

Person.Contact C,

Production.Product P,

Production.ProductSubcategory PS ,

Production.ProductCategory PC

where SOH.SalesOrderID = SOD.SalesOrderID

and SOH.SalesPersonID = SP.SalesPersonID

and SP.SalesPersonID = E.EmployeeID

and E.ContactID = C.ContactID

and SOD.ProductID = P.ProductID

and P.ProductSubcategoryID = PS.ProductSubcategoryID

and PS.ProductCategoryID = PC.ProductCategoryID

and  (DATEPART(Year, SOH.OrderDate) =  ?)

AND (DATEPART(Month, SOH.OrderDate) =  ?)

AND (SOH.SalesPersonID =?)

GROUP BY    C.FirstName + ' ' + C.LastName,

DATEPART(Month, SOH.OrderDate), SOH.SalesOrderNumber,

P.Name, PS.Name, SOD.UnitPrice, PC.Name



{{< /highlight >}}


クエリには、ReportYear、ReportMonth、および EmpID の 3 つのパラメーターがあります。

1.  Microsoftからお問い合わせ**ファイル**メニュー、選択**Aspose.Cells.Report.Designerに戻る**. 

   **レポート デザイナーに戻る** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_12.png)



上記で作成したデータ ソースとクエリがダイアログ ボックスに一覧表示されます。

1. データ ソースをクリックします。**SQLサーバー**詳細情報を表示します。

   **新しいデータ ソース** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_13.png)




1.  EmpSalesDetails クエリをクリックして、その詳細情報を表示します。

   **SQL タブをクリックして、クエリの SQL を表示します。** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_14.png)



**[列] タブをクリックして、クエリの列を表示します。** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_15.png)



**[パラメーター] タブをクリックして、クエリのパラメーターを表示します。** 

![todo:画像_代替_文章](creating-new-data-sources-and-queries_16.png)



