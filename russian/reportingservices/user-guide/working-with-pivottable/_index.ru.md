---
title: Работа со сводной таблицей
type: docs
weight: 100
url: /ru/reportingservices/working-with-pivottable/
---
{{% alert color="primary" %}} 

 А*сводная таблица* представляет собой интерактивную таблицу, которая обобщает данные и представляет их осмысленным образом. Службы отчетов SQL Server не могут экспортировать отчет в формат Microsoft Excel при сохранении сводной таблицы. Пользователи отчетов должны вручную создавать сводные таблицы каждый раз, когда они экспортируют отчет сводной таблицы из Reporting Services в Microsoft Excel. С помощью Aspose.Cells for Reporting Services вы можете создать сводную таблицу один раз во время разработки отчета. При каждом запуске отчета Aspose.Cells for Reporting Services экспортирует отчет в Microsoft Excel и обновляет данные в сводной таблице.

{{% /alert %}} 

Чтобы создать отчет сводной таблицы:

1. Создайте набор данных в качестве источника данных для сводной таблицы.
 Ниже мы используем образец базы данных AdventureWorks, поставляемый с SQL Server Reporting Services 2005, и создаем набор данных с именем «продажи».
SQL для набора данных выглядит следующим образом:

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

 Пожалуйста, обратитесь к[Источники данных и запросы](/cells/ru/reportingservices/data-sources-and-queries/) чтобы узнать больше о том, как создать источник данных и набор данных с помощью Aspose.Cells.Report.Designer.

{{% /alert %}} 

1.  Создайте табличный отчет по инструкции в[Создание табличного отчета](/cells/ru/reportingservices/creating-tabular-report/), как показано ниже.
 Эта таблица будет источником данных для сводной таблицы.

![дело:изображение_альтернативный_текст](working-with-pivottable_1.png)




1.  В Microsoft Excel, из**Вставлять** меню, выберите**Имя** а потом**Определять**.
1. Определите имя как «продажи».
 Диапазон имени начинается с первой ячейки заголовка заголовка и заканчивается последней ячейкой строки данных таблицы, как показано ниже.

![дело:изображение_альтернативный_текст](working-with-pivottable_2.png)




1.  Нажмите**ХОРОШО** заканчивать.
1. Создайте новый лист для сводной таблицы.
1.  От**Данные** меню, выберите**Отчет сводной таблицы и сводной диаграммы** добавить сводную таблицу.
 Отображается диалоговое окно.
1.  Выбирать**Microsoft Список или база данных Office Excel** как источник данных и**сводная таблица** как тип отчета.
1.  Нажмите**Следующий** продолжить.

![дело:изображение_альтернативный_текст](working-with-pivottable_3.png)




1. В диалоговом окне введите «продажи», имя, которое вы определили выше.
1.  Нажмите**Следующий** продолжить.

![дело:изображение_альтернативный_текст](working-with-pivottable_4.png)




1.  Нажмите**Заканчивать**. 

![дело:изображение_альтернативный_текст](working-with-pivottable_5.png)




1.  Спроектируйте сводную таблицу в Excel.

![дело:изображение_альтернативный_текст](working-with-pivottable_6.png)



 Разработанная сводная таблица показана ниже.

![дело:изображение_альтернативный_текст](working-with-pivottable_7.png)




1.  Щелкните правой кнопкой мыши сводную таблицу и выберите**Параметры таблицы**.
1.  Убедись в том, что**Обновлять при открытии** выбран.

![дело:изображение_альтернативный_текст](working-with-pivottable_8.png)




1. Сохраните отчет и опубликуйте его на сервере отчетов.
1. Экспортируйте отчет с сервера отчетов.
 Результат показан ниже.

![дело:изображение_альтернативный_текст](working-with-pivottable_9.png)
