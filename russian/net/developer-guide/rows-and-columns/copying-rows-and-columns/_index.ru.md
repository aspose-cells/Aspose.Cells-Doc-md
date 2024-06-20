---
title: Копирование строк и колонок
type: docs
weight: 40
url: /ru/net/copying-rows-and-columns/
description: Эта статья показывает, как копировать строки и столбцы с помощью API Aspose.Cells for .NET.
keywords: C# Как копировать строки и столбцы, Копирование строк в C#, Копирование столбцов с использованием C#, Как вставить строки и столбцы с использованием Aspose.Cells for .NET, Вставить несколько строк и столбцов, Как скопировать и вставить одну строку или столбец.
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

Aspose.Cells предоставляет метод [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) принимает следующие параметры:

- исходный объект [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- индекс исходной строки, и
- индекс строки назначения.

Используйте этот метод для копирования строки внутри листа или на другой лист. Метод [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) работает аналогично Microsoft Excel. Так, например, вам не нужно устанавливать высоту целевой строки явно, это значение также копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблонный файл Microsoft Excel и копирует вторую строку (с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в двенадцатую строку на том же листе.

Вы можете пропустить шаг, который получает высоту исходной строки с помощью метода [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight), а затем задает высоту целевой строки с помощью метода [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight), поскольку метод [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) автоматически учитывает высоту строки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

При копировании строк важно учитывать связанные изображения, диаграммы или другие объекты рисования, так же как и в Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (начальный индекс строки равен 4, а конечный индекс строки равен 6).
1. Существующие изображения, диаграммы и т. д. в целевой строке не будут удалены.

{{% /alert %}}

## **Как скопировать несколько строк**

Вы также можете скопировать несколько строк на новое место, используя метод [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), который принимает дополнительный параметр типа целое число для указания количества исходных строк, которые нужно скопировать.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Как копировать столбцы**

Aspose.Cells предоставляет метод [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), этот метод копирует все типы данных, включая формулы - с обновленными ссылками - и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

Метод [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) принимает следующие параметры:

- исходный объект [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- индекс исходного столбца, и
- индекс столбца назначения.

Используйте метод [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) для копирования столбца в листе или на другой лист.

В этом примере копируется столбец из листа и вставляется в лист другой книги.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Как скопировать несколько столбцов**

Подобно методу [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), API Aspose.Cells также предоставляют метод [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) для копирования нескольких исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Как вставить строки и столбцы с параметрами вставки**

Теперь Aspose.Cells предоставляет [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) при использовании функций [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) и [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Это позволяет установить соответствующий параметр вставки, аналогичный Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

