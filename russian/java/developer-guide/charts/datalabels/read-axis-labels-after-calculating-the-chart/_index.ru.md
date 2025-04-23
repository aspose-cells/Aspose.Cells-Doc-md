---
title: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать метки оси в Aspose.Cells for Java после вычисления диаграммы. Наш руководство покажет вам, как получить доступ к меткам оси и извлечь их, включая их форматирование и позиционирование.
keywords: Aspose.Cells for Java, диаграмма, метки оси, вычисление, чтение, доступ, извлечение, форматирование, позиционирование.
type: docs
weight: 90
url: /ru/java/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете прочитать метки оси вашей диаграммы после вычисления ее значений с использованием метода [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--). Пожалуйста, используйте метод [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) для этой цели, который вернет список меток оси.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, ознакомьтесь с примером кода ниже, который загружает [образец файла Excel](64716829.xlsx) и считывает метки оси категорий диаграммы на первом рабочем листе. Затем печатается значения меток оси в консоли. Пожалуйста, ознакомьтесь с выводом консоли приведенного ниже образца кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
