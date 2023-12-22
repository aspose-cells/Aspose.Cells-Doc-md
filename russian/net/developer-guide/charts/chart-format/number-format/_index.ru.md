---
title: Установите код формата значений серии диаграмм
description: Узнайте, как установить код формата значений серии диаграмм в Aspose.Cells for .NET. Наше руководство поможет вам понять, как форматировать данные серии диаграмм с использованием соответствующего кода формата, что позволит вам представлять данные точно и профессионально.
keywords: Aspose.Cells for .NET, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Числовой формат
type: docs
weight: 100
url: /ru/net/set-the-values-format-code-of-chart-series/
---
##  **Возможные сценарии использования**
Вы можете установить код формата значений серии диаграмм с помощью[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)свойство. Это свойство полезно не только для серий, основанных на диапазоне внутри листа, но также хорошо работает для серий, созданных с помощью массива значений.
##  **Установите код формата значений серии диаграмм**
 Следующий пример кода добавляет ряд в пустую диаграмму, на которой ранее не было рядов. Он добавляет серию, используя массив значений. После добавления серии он форматирует ее с помощью кода $#,##0, используя[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)собственности, и число 10 000 становится 10 000 долларов. На снимке экрана показано влияние кода на[образец файла Excel](51740712.xlsx) и[выходной файл Excel](51740713.xlsx) после исполнения.

![задача: image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
