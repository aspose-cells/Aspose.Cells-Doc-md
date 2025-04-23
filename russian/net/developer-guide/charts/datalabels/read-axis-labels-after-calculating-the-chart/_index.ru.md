---
title: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать подписи осей в Aspose.Cells for .NET после вычисления диаграммы. Наше руководство покажет вам, как получить доступ к подписям осей, включая их форматирование и позиционирование.
keywords: Aspose.Cells for .NET, диаграмма, подписи осей, вычисление, чтение, доступ, извлечение, форматирование, позиционирование.
type: docs
weight: 90
url: /ru/net/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете прочитать подписи осей вашей диаграммы после вычисления их значений с помощью метода [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/). Для этой цели используйте метод [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/), который вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

## **Вывод в консоль**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
