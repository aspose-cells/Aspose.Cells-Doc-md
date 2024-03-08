---
title: Установите код формата значений серии диаграмм
description: Узнайте, как установить код формата значений серии диаграмм в Aspose.Cells for Java. Наше руководство поможет вам понять, как форматировать данные серии диаграмм с использованием соответствующего кода формата, что позволит вам представлять данные точно и профессионально.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Числовой формат
type: docs
weight: 100
url: /ru/java/set-the-values-format-code-of-chart-series/
---
##  **Возможные сценарии использования**
Вы можете установить код формата значений серии диаграмм с помощью[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) метод. Этот метод полезен не только для серий, основанных на диапазоне внутри листа, но также хорошо работает для серий, созданных с массивом значений.
##  **Установите код формата значений серии диаграмм**
 Следующий пример кода добавляет ряд в пустую диаграмму, на которой ранее не было рядов. Он добавляет серию, используя массив значений. После добавления серии он форматирует ее с помощью кода $#,##0, используя[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) метод, и число 10000 становится 10000 долларов. На снимке экрана показано влияние кода на[образец файла Excel](51740712.xlsx) и[выходной файл Excel](51740713.xlsx) после исполнения.

![задача: image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
