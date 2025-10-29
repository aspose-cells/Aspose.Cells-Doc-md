---
title: Получить рабочий лист диаграммы
description: Узнайте, как получить рабочий лист, связанный с графиком Excel, с помощью Aspose.Cells для Python via .NET. Наше руководство покажет вам, как получить доступ к рабочему листу и выполнять операции с ним для манипуляции исходными данными графика.
keywords: Aspose.Cells для Python via .NET, графики Excel, рабочие листы, манипуляции с данными, исходные данные, операции.
type: docs
weight: 1000
url: /ru/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Иногда вы хотите получить доступ к рабочему листу по ссылке графика. Aspose.Cells для Python via .NET предоставляет свойство [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet), которое возвращает ссылку на рабочий лист, содержащий график.

{{% /alert %}}

В следующем примере показано, как использовать свойство [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet). Сначала код выводит имя листа, затем получает доступ к первой диаграмме на листе. Затем он снова выводит имя листа, используя свойство [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Ниже приведен вывод консоли, который получается в результате примера. Как видно, он дважды выводит одно и то же имя листа.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
