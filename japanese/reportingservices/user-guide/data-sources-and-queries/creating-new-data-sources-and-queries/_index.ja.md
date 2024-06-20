---
title: 新しいデータソースとクエリを作成します
type: docs
weight: 20
url: /ja/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer は MS Query と統合し、MS Query をデータソースとクエリの作成ツールとして使用します。Aspose.Cells.Report.Designer で新しいデータソースとクエリを作成するには、次の手順に従います： 

{{% /alert %}} 

Aspose.Cells.Report.Designer で新しいデータソースとクエリを作成するには：

1. Microsoft Excel を開きます。
1. Aspose.Cells.Report.Designer ツールバーの **Build DataSet** をクリックします。 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


すべてのデータソースとクエリがダイアログボックスにリストされます。 

1. データソースノード： 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. データセットノード： 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

ツリーのルートノードを選択します。
1. **追加** をクリックします。 

   **データソースとデータセットの追加** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. ダイアログボックスで、データソースを **SqlServer**、データセットを **EmpsSalesDetail** と呼び出します。
1. **次へ** をクリックします。 

   **データセットとデータソースの追加** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer が Microsoft Query を起動します。 

1. データソースの選択ダイアログボックスで **新しいデータソース** を選択します。
1. **OK** をクリックします。
   既存のデータソースを選択することもできます。 

   **データソースの選択** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. データソース名を入力し、ドロップダウンリストから SQL Server を選択します。
1. **接続** をクリックします。 

   **新しいデータソースの作成** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. SQL Server ログインダイアログボックスで、各項目に適切な値を選択します。
   たとえば、サーバーをローカルに設定し、AdventureWorks データベースを選択し、**信頼済み接続を使用** を選択します。
1. **OK** をクリックします。 

   **SQL サーバーにログインする** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. **OK** をクリックします。 

   **SQLサーバーにログインしていることに注意してください** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



新しいデータソースが**データソースの選択**ダイアログに表示されます。 

1. 新しいデータソースを選択します。 

   **新しいデータソース** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. **OK** をクリックして Microsoft Query を開きます。
Microsoft Query でクエリを作成するには、Microsoft Query Helper を参照してください。次のサンプルでは、パラメータを使用したクエリを作成します。 

   **クエリの構築** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



SQLは次のようになります: 

**SQL**

{{< highlight csharp >}}

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


クエリには ReportYear、ReportMonth、EmpID の 3 つのパラメータがあります。

1. Microsoft Query の**ファイル**メニューから**Aspose.Cells.Report.Designer に戻る**を選択します。 

   **レポートデザイナーに戻る** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



上記で作成したデータソースとクエリがダイアログボックスにリストされています。 

1. 詳細情報を表示するにはデータソース **SqlServer** をクリックします。 

   **新しいデータソース** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. 詳細情報を表示するにはクエリ EmpSalesDetails をクリックします。 

   **クエリのSQLを表示するには SQL タブをクリックします** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**クエリの列を表示するには列タブをクリックします** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**クエリのパラメータを表示するにはパラメータタブをクリックします** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



