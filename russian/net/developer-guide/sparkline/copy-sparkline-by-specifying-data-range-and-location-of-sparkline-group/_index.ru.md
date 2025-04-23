---
title: Копирование мини графиков, указав диапазон данных и расположение группы мини графиков
type: docs
weight: 300
url: /ru/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel позволяет копировать минидиаграмму, указывая диапазон данных и местоположение группы минидиаграмм. Aspose.Cells поддерживает эту функцию.

{{% /alert %}}

Для копирования минидиаграммы в другие ячейки в Microsoft Excel:

1. Выберите ячейку, содержащую минидиаграмму.
1. Выберите **Edit Data** в разделе **Sparkline** вкладки **Design**.
1. Выберите **Edit Group Location & Data**.
1. Укажите диапазон данных и местоположение.
1. Нажмите **ОК**.

Aspose.Cells предоставляет метод SparklineCollection.Add(dataRange, row, column) для указания диапазона данных и местоположения группы минидиаграмм. В следующем образце кода загружается исходный файл Excel, как показано на скриншоте выше, затем обращается к первой группе минидиаграмм и добавляет диапазоны данных и местоположения в группу минидиаграмм. Наконец, он записывает выходной файл Excel на диск, который также показан на скриншоте выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
