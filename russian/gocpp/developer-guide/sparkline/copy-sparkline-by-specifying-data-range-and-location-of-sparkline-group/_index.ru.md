---
title: Копирование Sparkline с указанием диапазона данных и местоположения группы Sparkline с Golang через C++
linktitle: Копирование Sparkline по указанию диапазона данных и расположения
type: docs
weight: 300
url: /ru/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Узнайте, как копировать sparklines, указывая диапазон данных и расположение с помощью Aspose.Cells for C++.
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

Aspose.Cells предоставляет метод `SparklineCollection.Add(dataRange, row, column)`, чтобы задать диапазон данных и расположение группы слайсинов. Следующий пример загружает исходный файл Excel, как показано на скриншоте выше, затем обращается к первой группе слайсинов и добавляет диапазоны данных и расположения. В конце он сохраняет итоговый файл Excel на диск, как показано на скриншоте выше.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
