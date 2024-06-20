---
title: Установите код формата значений серии графика
description: Узнайте, как установить код формата значений серии графика в Aspose.Cells for Java. Наше руководство поможет вам понять, как форматировать данные вашего графика, используя соответствующий код формата, что позволит вам представлять свои данные точно и профессионально.
keywords: Aspose.Cells for Java, серия графика, код формата значений, форматирование, представление данных, точность, профессионализм.
linktitle: Формат числа
type: docs
weight: 100
url: /ru/java/set-the-values-format-code-of-chart-series/
---

## **Возможные сценарии использования**
Вы можете установить код формата значений серии графика, используя метод [Series.setValuesFormatCode] (https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-). Этот метод полезен не только для серии, основанной на диапазоне внутри рабочего листа, но также хорошо работает для серии, созданных с помощью массива значений.
## **Установить код формата значений серии графика**
Приведенный ниже образец кода добавляет серию в пустой график, который не имеет серий до этого. Он добавляет серию, используя массив значений. После добавления серии он форматирует ее с помощью кода $ #, ## 0 с помощью метода [Series.setValuesFormatCode] (https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) и число 10000 становится $ 10,000. Скриншот показывает эффект кода на [образцовый файл Excel] (51740712.xlsx) и [выходной файл Excel] (51740713.xlsx) после выполнения.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
