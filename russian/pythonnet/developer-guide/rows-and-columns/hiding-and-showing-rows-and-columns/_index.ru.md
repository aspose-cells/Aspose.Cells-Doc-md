---
title: Скрытие и отображение строк и столбцов
type: docs
weight: 60
url: /ru/python-net/hiding-and-showing-rows-and-columns/
description: В этой статье показано, как скрывать и отображать строки и столбцы с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python для Excel, Скрытие и отображение строк Aspose.Cells Python, Скрытие и отображение столбцов Python, Скрытие строк и столбцов Python, Отображение строк и столбцов Python.
---

{{% alert color="primary" %}}

Иногда имеет смысл скрывать определенные строки или столбцы на листе и отображать их позже. Эту функцию предоставляет Microsoft Excel, также как и Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Управление видимостью строк и столбцов**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), позволяющий разработчикам получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), представляющую все ячейки на листе. Коллекция [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе. Ниже приведено несколько из них.

## **Как скрыть строки и столбцы**

Разработчики могут скрыть строку или столбец, вызвав методы [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) и [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) соответственно из коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Оба метода принимают индекс строки и столбца в качестве параметра для скрытия конкретной строки или столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

## **Как показать строки и столбцы**

Разработчики могут показать любую скрытую строку или столбец, вызвав методы [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) и [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) из коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

При восстановлении ширины скрытого столбца до ранее назначенной ширины или до его исходной ширины рекомендуется отобразить столбец с отрицательной шириной. Например: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Как скрыть несколько строк и столбцов**

Разработчики могут скрыть сразу несколько строк или столбцов, вызвав методы [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) и [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) из коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Оба метода принимают начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Также можно использовать методы [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) и [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), чтобы сделать видимыми несколько строк и столбцов.

{{% /alert %}}
