---
title: Работа с сводной таблицей
type: docs
weight: 100
url: /ru/reportingservices/working-with-pivottable/
---

{{% alert color="primary" %}} 

*Сводная таблица* - это интерактивная таблица, которая суммирует данные и представляет их в понятном виде. Службы отчетов SQL Server не могут экспортировать отчет в формате Microsft Excel, сохраняя при этом сводную таблицу. Пользователям отчетов приходится вручную создавать сводные таблицы каждый раз при экспорте сводного отчета из Сервисов отчетов в Microsoft Excel. С Aspose.Cells for Reporting Services вы можете разработать сводную таблицу один раз во время создания отчета. Каждый раз, когда отчет запускается, Aspose.Cells for Reporting Services экспортирует отчет в Microsoft Excel и обновляет данные в сводной таблице.

{{% /alert %}} 

Создание сводного отчета:

1. Создайте набор данных в качестве источника данных для сводной таблицы.
   Ниже мы используем пример базы данных AdventureWorks, который поставляется с SQL Server Reporting Services 2005, и создаем набор данных с названием «sales".
   SQL для набора данных выглядит следующим образом: 

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

Пожалуйста, обратитесь к [Источники данных и запросы](/cells/ru/reportingservices/data-sources-and-queries/) , чтобы узнать больше о создании источника данных и набора данных с использованием Aspose.Cells.Report.Designer.

{{% /alert %}} 

1. Создайте отчет таблицы в соответствии с инструкцией в [Создание табличного отчета](/cells/ru/reportingservices/creating-tabular-report/), как показано ниже.
   Таблица будет источником данных для сводной таблицы. 

![todo:image_alt_text](working-with-pivottable_1.png)




1. В Microsoft Excel перейдите в меню **Вставка**, выберите **Имя** и затем **Определить**.
1. Определите имя как «sales».
   Диапазон имени начинается с первой ячейки заголовка и заканчивается последней ячейкой строки данных таблицы, как показано ниже. 

![todo:image_alt_text](working-with-pivottable_2.png)




1. Щелкните **OK**, чтобы завершить.
1. Создайте новый лист для сводной таблицы.
1. В меню **Данные** выберите **Отчет сводной таблицы и сводной диаграммы** для добавления сводной таблицы.
   Отображается диалоговое окно.
1. Выберите **Список или базу данных Microsoft Office Excel** в качестве источника данных и **сводную таблицу** в качестве типа отчета.
1. Щелкните **Далее**, чтобы продолжить. 

![todo:image_alt_text](working-with-pivottable_3.png)




1. В диалоговом окне введите «sales», имя, которое вы определили выше.
1. Щелкните **Далее**, чтобы продолжить. 

![todo:image_alt_text](working-with-pivottable_4.png)




1. Щелкните **Готово**. 

![todo:image_alt_text](working-with-pivottable_5.png)




1. Создайте сводную таблицу в Excel. 

![todo:image_alt_text](working-with-pivottable_6.png)



Созданная сводная таблица показана ниже. 

![todo:image_alt_text](working-with-pivottable_7.png)




1. Щелкните правой кнопкой мыши на сводной таблице и выберите **Параметры таблицы**.
1. Убедитесь, что выбрана **Обновлять при открытии**. 

![todo:image_alt_text](working-with-pivottable_8.png)




1. Сохраните отчет и опубликуйте его на сервере отчетов.
1. Экспортируйте отчет с сервера отчетов.
   Результат показан ниже. 

![todo:image_alt_text](working-with-pivottable_9.png)
