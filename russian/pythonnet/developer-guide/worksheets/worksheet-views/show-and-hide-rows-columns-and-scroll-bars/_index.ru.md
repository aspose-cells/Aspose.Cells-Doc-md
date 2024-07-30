---
title: Показать и скрыть строки, столбцы и полосы прокрутки
type: docs
weight: 20
url: /ru/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: В этой статье демонстрируется, как программно отображать и скрывать строки и столбцы листа Excel с использованием Aspose.Cells для Python via .NET. Видимость полос прокрутки можно настроить, и можно скрыть несколько строк и столбцов.
keywords: Библиотека Python Excel, Показывает строки и столбцы Python, Скрывает строки и столбцы Python, Показывает вертикальную полосу прокрутки Python, Показывает горизонтальную полосу прокрутки Python, Скрывает вертикальную полосу прокрутки Python, Скрывает горизонтальную полосу прокрутки Python, Показывает и скрывает строки, столбцы и полосы прокрутки в Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET предоставляет способы контроля видимости строк, столбцов и полос прокрутки листа.

{{% /alert %}}

## **Показ и скрытие строк и столбцов**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет разработчикам получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells), представляющую все ячейки листа. Коллекция [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) предоставляет несколько методов для управления строками или столбцами в листе. Несколько из них обсуждаются ниже.

### **Показать строки и столбцы**

Разработчики могут показать любую скрытую строку или столбец, вызвав методы [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) и [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) из коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

При восстановлении ширины скрытого столбца до ранее назначенной ширины или до его исходной ширины рекомендуется отобразить столбец с отрицательной шириной. Например: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Скрыть строки и столбцы**

Разработчики могут скрыть строку или столбец, вызвав методы [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) и [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) соответственно из коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Оба метода принимают индекс строки и столбца в качестве параметра для скрытия конкретной строки или столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Скрыть несколько строк и столбцов**

Разработчики могут скрыть сразу несколько строк или столбцов, вызвав методы [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) и [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) из коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Оба метода принимают начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Показывать и скрывать полосы прокрутки**

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли прокручивать содержимое листа. С помощью Aspose.Cells для Python via .NET разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.

### **Управление видимостью полос прокрутки**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) предоставляет широкий диапазон свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте свойства класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) и [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible). [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) и [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) - это булевы свойства, что означает, что они могут хранить только значения **true** или **false**.

#### **Отображение полос прокрутки**

Сделать полосы прокрутки видимыми, установив свойство [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) или [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) в **true**.

#### **Скрытие полос прокрутки**

Скрыть полосы прокрутки, установив свойство [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) или [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) в **false**.

**Пример кода**

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает оба ползунка прокрутки, а затем сохраняет измененный файл как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
