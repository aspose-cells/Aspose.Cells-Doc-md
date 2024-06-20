---
title: Создание новых источников данных и запросов
type: docs
weight: 20
url: /ru/reportingservices/creating-new-data-sources-and-queries/
---

{{% alert color="primary" %}} 

Aspose.Cells.Report.Designer интегрируется с MS Query и использует MS Query в качестве инструмента для создания источников данных и запросов. Для создания нового источника данных и запроса в Aspose.Cells.Report.Designer выполните следующие шаги: 

{{% /alert %}} 

Для создания нового источника данных и запроса в Aspose.Cells.Report.Designer:

1. Откройте Microsoft Excel.
1. Нажмите **Построить набор данных** на панели инструментов Aspose.Cells.Report.Designer: 

![todo:image_alt_text](creating-new-data-sources-and-queries_1.png)


Все источники данных и запросы перечислены в диалоговом окне. 

1. Узел источника данных: 

![todo:image_alt_text](creating-new-data-sources-and-queries_2.png)

1. Узел набора данных: 

![todo:image_alt_text](creating-new-data-sources-and-queries_3.png)

1. Выберите корневой узел дерева.
1. Нажмите **Добавить**. 

   **Добавление источников данных и наборов данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_4.png)




1. В диалоговом окне назовите источник данных **SqlServer**, а набор данных - **EmpsSalesDetail**.
1. Нажмите **Далее**. 

   **Добавление наборов данных и источников данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_5.png)



Aspose.Cells.Report.Designer запускает Microsoft Query. 

1. В диалоговом окне выбора источника данных выберите **Новый источник данных**.
1. Нажмите **ОК**.
   Вы также можете выбрать существующий источник данных. 

   **Выбор источника данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_6.png)




1. Введите имя источника данных и выберите SQL Server из выпадающего списка драйверов базы данных.
1. Нажмите **Подключить**. 

   **Создание нового источника данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_7.png)




1. В диалоговом окне входа в SQL Server выберите соответствующее значение для каждого пункта.
   Например, установите сервер на **local**, выберите базу данных AdventureWorks и выберите **Использовать доверенное подключение**.
1. Нажмите **ОК**. 

   **Вход в SQL сервер** 

![todo:image_alt_text](creating-new-data-sources-and-queries_8.png)




1. Нажмите **ОК**. 

   **Обратите внимание, что мы теперь вошли в SQL сервер** 

![todo:image_alt_text](creating-new-data-sources-and-queries_9.png)



Новый источник данных появляется в диалоговом окне **Выбор источника данных**. 

1. Выберите новый источник данных. 

   **Новый источник данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_10.png)




1. Нажмите **OK**, чтобы открыть Microsoft Query.
1. Для создания запроса в Microsoft Query обратитесь к функции помощника Microsoft Query. В следующем примере мы создадим запрос с параметрами. 

   **Построение запроса** 

![todo:image_alt_text](creating-new-data-sources-and-queries_11.png)



SQL выглядит следующим образом: 

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


Запрос содержит три параметра: ReportYear, ReportMonth и EmpID.

1. В меню **Файл** Microsoft Query выберите **Вернуться в Aspose.Cells.Report.Designer**. 

   **Возвращение в конструктор отчетов** 

![todo:image_alt_text](creating-new-data-sources-and-queries_12.png)



Данные и созданный запрос из вышеуказанного перечислены в диалоговом окне. 

1. Нажмите на источник данных **SqlServer**, чтобы просмотреть его подробную информацию. 

   **Новый источник данных** 

![todo:image_alt_text](creating-new-data-sources-and-queries_13.png)




1. Щелкните на запрос EmpSalesDetails, чтобы просмотреть его подробную информацию. 

   **Щелкните вкладку SQL, чтобы просмотреть SQL для запроса** 

![todo:image_alt_text](creating-new-data-sources-and-queries_14.png)



**Щелкните вкладку Столбцы, чтобы просмотреть столбцы запроса** 

![todo:image_alt_text](creating-new-data-sources-and-queries_15.png)



**Щелкните вкладку Параметры, чтобы просмотреть параметры запроса** 

![todo:image_alt_text](creating-new-data-sources-and-queries_16.png)



