---
title: Чтение меток осей после вычисления графика с помощью Golang через C++
linktitle: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать метки осей в Aspose.Cells for C++ после расчета графика. Наше руководство покажет, как получить доступ и извлечь метки осей, включая их форматирование и позиционирование.
keywords: Aspose.Cells for C++, график, метки осей, расчет, чтение, доступ, извлечение, форматирование, позиционирование.
type: docs
weight: 90
url: /ru/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете прочитать подписи осей вашей диаграммы после вычисления их значений с помощью метода [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/). Для этой цели используйте метод [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/), который вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **Вывод в консоль**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
