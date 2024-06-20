---
title: Копирование строк и колонок
type: docs
weight: 40
url: /ru/python-net/copying-rows-and-columns/
description: Эта статья показывает, как копировать строки и столбцы при помощи Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, как копировать строки и столбцы в Python, копировать строки в Python, копировать столбцы с использованием Python, как вставить строки и столбцы с Aspose.Cells для Python via .NET, Python вставить несколько строк и столбцов, как скопировать и вставить одиночную строку или столбец.
---

## **Введение**

Иногда вам нужно скопировать строки и столбцы в рабочем листе без копирования всего листа. С помощью Aspose.Cells это возможно скопировать строки и столбцы внутри или между книгами.
При копировании строки (или столбца) копируются также содержащиеся в нем данные, включая формулы - с обновленными ссылками - и значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты рисования.

## **Как скопировать строки и столбцы с помощью Microsoft Excel**

1. Выберите строку или колонку, которую вы хотите скопировать.
1. Чтобы скопировать строки или колонки, нажмите **Копировать** на панели **Стандартные функции** или нажмите **CTRL**+**C**.
1. Выберите строку или колонку ниже или справа от места, куда вы хотите скопировать ваш выбор.
1. При копировании строк или колонок нажмите **Скопированные ячейки** на меню **Вставка**.

{{% alert color="primary" %}}

Если вы щелкнете **Вставить** на панели инструментов **Стандарт** или нажмете **CTRL**+**V** вместо того, чтобы щелкнуть команду на вкладке **Вставка**, содержимое ячеек назначения будет заменено.

{{% /alert %}}

## **Как вставить строки и столбцы с использованием опций вставки в программе Microsoft Excel**

1. Выберите ячейки, содержащие данные или другие параметры, которые вы хотите скопировать.
1. На вкладке "Главная" нажмите **Копировать**.
1. Щелкните первую ячейку в области, куда вы хотите **вставить** скопированное.
1. На вкладке "Главная" щелкните стрелку рядом с **Вставить**, затем выберите **Специальная вставка**.
1. Выберите нужные **опции**.

## **Как скопировать строки и столбцы с помощью Aspose.Cells for .NET**

## **Как скопировать отдельные строки**

Aspose.Cells предоставляет метод [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) принимает следующие параметры:

- исходный объект [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- индекс исходной строки и
- индекс целевой строки.

Используйте этот метод для копирования строки внутри листа или на другой лист. Метод [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) работает аналогично Microsoft Excel. Так, например, вам не нужно устанавливать высоту целевой строки явно, это значение также копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблонный файл Microsoft Excel и копирует вторую строку (с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в двенадцатую строку на том же листе.

Вы можете пропустить шаг, который получает высоту исходной строки с помощью метода [**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int), а затем задает высоту целевой строки с помощью метода [**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float), поскольку метод [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) автоматически учитывает высоту строки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

При копировании строк важно учитывать связанные изображения, диаграммы или другие объекты рисования, так же как и в Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (начальный индекс строки равен 4, а конечный индекс строки равен 6).
1. Существующие изображения, диаграммы и т. д. в целевой строке не будут удалены.

{{% /alert %}}

## **Как скопировать несколько строк**

Вы также можете скопировать несколько строк на новое место, используя метод [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int), который принимает дополнительный параметр типа целое число для указания количества исходных строк, которые нужно скопировать.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **Как копировать столбцы**

Aspose.Cells предоставляет метод [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), этот метод копирует все типы данных, включая формулы - с обновленными ссылками - и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

Метод [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) принимает следующие параметры:

- исходный объект [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- индекс исходного столбца, и
- индекс столбца назначения.

Используйте метод [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) для копирования столбца в листе или на другой лист.

В этом примере копируется столбец из листа и вставляется в лист другой книги.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **Как скопировать несколько столбцов**

Подобно методу [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int), API Aspose.Cells также предоставляют метод [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) для копирования нескольких исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **Как вставить строки и столбцы с параметрами вставки**

Теперь Aspose.Cells предоставляет [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) при использовании функций [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) и [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions). Это позволяет установить соответствующий параметр вставки, аналогичный Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

