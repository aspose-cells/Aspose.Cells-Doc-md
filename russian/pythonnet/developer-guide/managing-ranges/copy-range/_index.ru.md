---
title: Копирование диапазонов Excel
linktitle: Копирование диапазонов
type: docs
weight: 105
url: /ru/python-net/copy-ranges-of-excel/
description: В этой статье описано, как копировать диапазоны Excel с использованием библиотеки Aspose.Cells for Python via .NET.
keywords: Библиотека Python Excel, Как копировать диапазоны Excel на Python, Как копировать только данные диапазона с помощью библиотеки Python для Excel, Как вставить диапазон с опциями, Как скопировать только данные диапазона.
---

## **Введение**

В Excel вы можете выбрать диапазон, скопировать его, а затем вставить его с определенными параметрами на ту же рабочую книгу, другие листы или другие файлы.

## **Копирование диапазонов с использованием библиотеки Aspose.Cells for Python Excel**

Aspose.Cells for Python via .NET предоставляет несколько перегруженных методов [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) для копирования диапазона.
И [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) только стиль копирования диапазона; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) только значение копирования диапазона

## **Копировать диапазон**

Создание двух диапазонов: исходного диапазона, целевого диапазона, затем копирование исходного диапазона в целевой диапазон с помощью метода [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range).

См. следующий код:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Вставка диапазона с параметрами**

Aspose.Cells for Python via .NET поддерживает вставку диапазона с определенным типом.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Только копирование данных из диапазона**
Также вы можете скопировать данные с помощью метода [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range), как показано в следующих кодах:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Продвинутые темы**
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/python-net/copy-row-heights-of-source-range-to-destination-range/)


