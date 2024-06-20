---
title: Получить рабочий лист диаграммы
description: Узнайте, как получить рабочий лист, связанный с диаграммой Excel, используя Aspose.Cells for .NET. Наше руководство покажет вам, как получить доступ к рабочему листу и выполнить операции над ним для изменения основных данных диаграммы.
keywords: Aspose.Cells for .NET, диаграммы Excel, рабочие листы, манипулирование данными, основные данные, операции.
type: docs
weight: 1000
url: /ru/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда вам нужно получить доступ к листу рабочей книги из ссылки на диаграмму. Aspose.Cells предоставляет свойство [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet), которое возвращает ссылку на лист рабочей книги, содержащий диаграмму.

{{% /alert %}}

В следующем примере показано, как использовать свойство [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet). Сначала код выводит имя листа, затем получает доступ к первой диаграмме на листе. Затем он снова выводит имя листа, используя свойство [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Ниже приведен вывод консоли, который получается в результате примера. Как видно, он дважды выводит одно и то же имя листа.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
