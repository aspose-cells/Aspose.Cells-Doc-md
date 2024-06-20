---
title: Работа с диаграммами
type: docs
weight: 110
url: /ru/reportingservices/working-with-charts/
---

{{% alert color="primary" %}} 

Шаблон отчета Aspose.Cells поддерживает диаграммы Microsoft Excel. Каждый раз при выполнении отчета диаграмма заполняется наиболее свежими данными. 

{{% /alert %}} 

Чтобы добавить диаграмму в шаблон отчета:

1. Сначала создайте набор данных, который будет источником данных для диаграммы.
   Ниже мы используем образец базы данных AdventureWorks, который поставляется с SQL Server Reporting Services 2005, и создаем набор данных с именем Sales.
   Этот SQL определяет набор данных: 

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



Пожалуйста, обратитесь к [Источники данных и запросы](/cells/ru/reportingservices/data-sources-and-queries/), чтобы узнать больше о том, как создать источник данных и набор данных в Aspose.Cells.Report.Designer.

1. Создайте табличный отчет в соответствии с инструкциями в [Создание табличного отчета](/cells/ru/reportingservices/creating-tabular-report/). Созданный нами отчет для этого примера представлен ниже. Таблица является источником данных для графика. 

![todo:image_alt_text](working-with-charts_1.png)




1. В Microsoft Excel выберите меню **Вставка** и выберите **Диаграмма**.
1. Нажмите **Далее**. 

![todo:image_alt_text](working-with-charts_2.png)




1. Выберите вкладку **Графики**. 

![todo:image_alt_text](working-with-charts_3.png)




1. Нажмите **Добавить**. 

![todo:image_alt_text](working-with-charts_4.png)




1. В диалоговом окне установите значение Series1 (серия кварталов) в первое поле данных таблицы.
   В примере это “CompanySales!$C$3:$C$3”. Первый $C$3 - это первый индекс строки “Квартал” и второй $C$3 - заполнитель для последнего индекса строки “Квартал”, который будет заменен на реальный индекс строки данных таблицы во время рендеринга. Установите метки оси категорий (X) равными “=CompanySales!$C$3:$C$3”. 

![todo:image_alt_text](working-with-charts_5.png)




1. Нажмите **Добавить**, чтобы добавить еще одну серию.
   В примере мы добавили серию продаж. 
1. Установите значение Series2 (серия продаж) второго поля данных таблицы.
   В примере это “CompanySales!$D$3:$D$3”. Первый $D$3 - это первый индекс строки “Продажи”, а второй $D$3 - заполнитель для последнего индекса строки “Продажи”, который будет заменен на реальный индекс строки данных таблицы во время рендеринга. 
1. Щелкните **Далее**, чтобы продолжить. 

![todo:image_alt_text](working-with-charts_6.png)




1. В диалоговом окне установите заголовок диаграммы и ось категорий (X).
1. Нажмите **Готово**, чтобы завершить работу. 

![todo:image_alt_text](working-with-charts_7.png)



Шаблон выглядит следующим образом. 

![todo:image_alt_text](working-with-charts_8.png)




1. Сохраните отчет и опубликуйте его на сервере отчетов.
1. Экспортируйте отчет с сервера отчетов.
   Результат представлен ниже. 

![todo:image_alt_text](working-with-charts_9.png)
