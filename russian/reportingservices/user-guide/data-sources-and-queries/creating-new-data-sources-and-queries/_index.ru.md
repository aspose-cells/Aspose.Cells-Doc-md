---
title: Создание новых источников данных и запросов
type: docs
weight: 20
url: /ru/reportingservices/creating-new-data-sources-and-queries/
---
{{% alert color="primary" %}} 

 Aspose.Cells.Report.Designer интегрируется с MS Query и использует MS Query в качестве инструмента для создания источников данных и запросов. Чтобы создать новый источник данных и запрос в Aspose.Cells.Report.Designer, выполните следующие действия:

{{% /alert %}} 

Чтобы создать новый источник данных и запрос в Aspose.Cells.Report.Designer:

1. Откройте Microsoft Excel.
1.  Нажмите**Построить набор данных** на панели инструментов Aspose.Cells.Report.Designer:

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_1.png)


Все источники данных и запросы перечислены в диалоговом окне.

1.  Узел источника данных:

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_2.png)

1.  Узел набора данных:

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_3.png)

1. Выберите корневой узел дерева.
1.  Нажмите**Добавлять**. 

   **Добавление источников данных и наборов данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_4.png)




1.  В диалоговом окне вызовите источник данных**SQLServer** и набор данных**EmpsSalesDetail**.
1.  Нажмите**Следующий**. 

   **Добавление наборов данных и источников данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_5.png)



 Aspose.Cells.Report.Designer запускает Microsoft Запрос.

1.  В диалоговом окне «Выбор источника данных» выберите**Новый источник данных**.
1.  Нажмите**ХОРОШО**.
 Вы также можете выбрать существующий источник данных.

   **Выбор источника данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_6.png)




1. Введите имя источника данных и выберите SQL Server из раскрывающегося списка драйверов базы данных.
1.  Нажмите**Соединять**. 

   **Создание нового источника данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_7.png)




1. В диалоговом окне входа в SQL Server выберите соответствующее значение для каждого элемента.
 Например, установите сервер как локальный, выберите базу данных AdventureWorks и выберите**Использовать доверенное соединение**.
1.  Нажмите**ХОРОШО**. 

   **Вход на SQL-сервер** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_8.png)




1.  Нажмите**ХОРОШО**. 

   **Обратите внимание, что мы вошли в систему на SQL-сервере.** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_9.png)



Новый источник данных появится в**Выберите источник данных** диалог.

1.  Выберите новый источник данных.

   **Новый источник данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_10.png)




1.  Нажмите**ХОРОШО** чтобы открыть Microsoft Запрос.
1.  Чтобы создать запрос в Microsoft Query, обратитесь к Microsoft Query Helper. В следующем примере мы создаем запрос с параметрами.

   **Создание запроса** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_11.png)



 SQL выглядит следующим образом:

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


Запрос имеет три параметра: ReportYear, ReportMonth и EmpID.

1.  От Microsoft Запросы**Файл** меню, выберите**Вернуться к Aspose.Cells.Отчет.Дизайнер**. 

   **Возврат к дизайнеру отчетов** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_12.png)



 Источник данных и созданный выше запрос перечислены в диалоговом окне.

1.  Щелкните источник данных**SQLServer** для просмотра его подробной информации.

   **Новый источник данных** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_13.png)




1.  Щелкните запрос EmpSalesDetails, чтобы просмотреть подробные сведения о нем.

   **Щелкните вкладку SQL, чтобы просмотреть sql для запроса.** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_14.png)



**Щелкните вкладку «Столбцы», чтобы просмотреть столбцы запроса.** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_15.png)



**Щелкните вкладку «Параметры», чтобы просмотреть параметры запроса.** 

![дело:изображение_альтернативный_текст](creating-new-data-sources-and-queries_16.png)



