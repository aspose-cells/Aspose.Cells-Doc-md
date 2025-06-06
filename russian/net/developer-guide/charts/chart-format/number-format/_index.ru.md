---
title: Установите код формата значений серии графика
description: Узнайте, как установить формат значений серии диаграммы в Aspose.Cells for .NET. Наше руководство поможет вам понять, как форматировать данные серии диаграмм с использованием соответствующего кода формата, что позволит представить ваши данные точно и профессионально.
keywords: Aspose.Cells for .NET, серия диаграммы, код формата значений, форматирование, представление данных, точность, профессионализм.
linktitle: Формат числа
type: docs
weight: 100
url: /ru/net/set-the-values-format-code-of-chart-series/
---

## **Возможные сценарии использования**
Вы можете установить код формата значений серии диаграммы с использованием свойства [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). Это свойство полезно не только для серии, основанной на диапазоне внутри листа, но также работает хорошо для серии, созданной с использованием массива значений.
## **Установить код формата значений серии графика**
В приведенном ниже образцовом коде добавляется серия в пустую диаграмму, в которой до этого не было серии. Она добавляет серию, используя массив значений. После добавления серии она форматируется с помощью кода $#,##0, используя свойство [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) и число 10000 становится $10,000. Снимок экрана показывает эффект кода на [образцовом файле Excel](51740712.xlsx) и [выходном файле Excel](51740713.xlsx) после выполнения.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
{{< app/cells/assistant language="csharp" >}}
