---
title: Копирование диапазонов Excel
linktitle: Копирование диапазонов
type: docs
weight: 105
url: /ru/net/copy-ranges-of-Excel/
---

## **Введение**

В Excel вы можете выбрать диапазон, скопировать его, а затем вставить его с определенными параметрами на ту же рабочую книгу, другие листы или другие файлы.

## **Копирование диапазонов с использованием Aspose.Cells**

Aspose.Cells предоставляет несколько перегрузок метода [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) для копирования диапазона.
И [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) только копировать стиль диапазона; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) только копировать значение диапазона

## **Копировать диапазон**

Создание двух диапазонов: исходного диапазона, целевого диапазона, а затем копирование исходного диапазона в целевой диапазон с помощью метода Range.Copy.

См. следующий код:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Вставка диапазона с параметрами**

Aspose.Cells поддерживает вставку диапазона с определенным типом.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Только копирование данных из диапазона**
Также вы можете скопировать данные с помощью метода Range.CopyData, как показано в следующем коде:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Продвинутые темы**
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
