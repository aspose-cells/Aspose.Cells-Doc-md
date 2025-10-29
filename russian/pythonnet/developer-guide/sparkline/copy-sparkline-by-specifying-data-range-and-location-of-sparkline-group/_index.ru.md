---
title: Копирование мини графиков, указав диапазон данных и расположение группы мини графиков
type: docs
weight: 300
url: /ru/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel позволяет копировать искруйн по указанию диапазона данных и расположения группы искруйнов. Aspose.Cells for Python via .NET поддерживает эту функцию.

{{% /alert %}}

Для копирования минидиаграммы в другие ячейки в Microsoft Excel:

1. Выберите ячейку, содержащую минидиаграмму.
1. Выберите **Edit Data** в разделе **Sparkline** вкладки **Design**.
1. Выберите **Edit Group Location & Data**.
1. Укажите диапазон данных и местоположение.
1. Нажмите **ОК**.

Aspose.Cells for Python via .NET предоставляет метод SparklineCollection.Add(dataRange, row, column) для указания диапазона данных и расположения группы искруйнов. Следующий пример кода загружает исходный файл Excel, как показано на скриншоте выше, затем получает первую группу искруйнов и добавляет диапазоны данных и расположения в группу. В конце он сохраняет итоговый файл Excel на диск, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
