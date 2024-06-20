---
title: Визуализировать выбранные элементы диаграмм в виде диаграмм Excel
type: docs
weight: 30
url: /ru/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Для визуализации только некоторых диаграмм в отчете в виде диаграмм Excel:

1. Откройте файл **Aspose.Cells.ReportingServices.xml**.
1. Измените параметры конфигурации файла **Aspose.Cells.ReportingServices.xml**.
1. Добавьте необходимую информацию о конфигурации отчета.
1. Добавьте информацию для элементов диаграмм, которые необходимо экспортировать как редактируемые диаграммы. Эти элементы экспортируются в виде статических изображений.

Например:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Диаграмма, экспортированная как изображение** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Диаграмма, экспортированная в виде редактируемой диаграммы Excel** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
