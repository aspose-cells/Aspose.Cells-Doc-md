---
title: Преобразование выбранных элементов диаграммы в диаграммы Excel
type: docs
weight: 30
url: /ru/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Чтобы отобразить только некоторые диаграммы в отчете в диаграммы Excel:

1. Открой**Aspose.Cells.ReportingServices.xml** файл.
1.  Измените параметры конфигурации**Aspose.Cells.ReportingServices.xml** файл.
1. Добавьте требуемую информацию о конфигурации отчета.
1. Добавьте информацию об элементах диаграммы, которые вы не хотите экспортировать в виде редактируемых диаграмм. Эти элементы экспортируются как статические изображения.

Например:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Диаграмма, экспортированная как изображение** 

![дело:изображение_альтернативный_текст](render-selected-chart-items-to-excel-charts_1.png)

**Диаграмма, экспортированная как редактируемая диаграмма Excel** 

![дело:изображение_альтернативный_текст](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
