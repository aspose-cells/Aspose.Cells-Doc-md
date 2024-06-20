---
title: Форматирование строк и столбцов
linktitle: Строки и столбцы
type: docs
weight: 100
url: /ru/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells для Python via .NET поддерживает изменение высоты строки или ширины столбца, а также применение форматирования к строкам или столбцам.
keywords: Python библиотека для Excel, Python Установить высоту строки и ширину столбца, Python настроить высоту строки и ширину столбца, Изменить высоту строки или ширину столбца в Python, Форматирование строк и столбцов в Python, Как установить высоту строки и ширину столбца в Python.
---


{{% alert color="primary" %}}

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должна быть изменена для отображения данных. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Однако разработчики могут выполнять эти операции во время выполнения с помощью Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Работа со строками**

### **Как настроить высоту строки**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), которая представляет все ячейки в листе.

Коллекция [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже более подробно.

### **Как установить высоту строки**

Можно установить высоту отдельной строки, вызвав метод [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Метод [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) принимает следующие параметры:

- **row**, индекс строки, высоту которой вы хотите изменить.
- **height**, высота строки для применения на строку.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Как установить высоту всех строк на листе**

Если разработчикам необходимо установить одинаковую высоту всех строк на листе, они могут сделать это, используя свойство [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**Пример:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Работа с колонками**

### **Как установить ширину столбца**

Установите ширину столбца, вызвав метод коллекции [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Метод [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) принимает следующие параметры:

- **столбец**, индекс столбца, ширину которого вы изменяете.
- **ширина**, желаемая ширина столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Как установить ширину столбца в пикселях**

Установите ширину столбца, вызвав метод коллекции [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Метод [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) принимает следующие параметры:

- **столбец**, индекс столбца, ширину которого вы изменяете.
- **пиксели**, желаемая ширина столбца в пикселях.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Как установить ширину всех столбцов в листе Excel**

Чтобы установить одинаковую ширину столбца для всех столбцов в листе, используйте свойство [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Продвинутые темы**
- [Автоподгонка строк и столбцов](/cells/ru/python-net/autofit-rows-and-columns/)
- [Преобразование текста в столбцы с использованием Aspose.Cells](/cells/ru/python-net/convert-text-to-columns-using-aspose-cells/)
- [Копирование строк и столбцов](/cells/ru/python-net/copying-rows-and-columns/)
- [Удаление пустых строк и столбцов в листе Excel](/cells/ru/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Группировка и разгруппировка строк и столбцов](/cells/ru/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Скрытие и отображение строк и столбцов](/cells/ru/python-net/hiding-and-showing-rows-and-columns/)
- [Вставка или удаление строк в листе Excel](/cells/ru/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Вставка и удаление строк и столбцов в файле Excel](/cells/ru/python-net/inserting-and-deleting-rows-and-columns/)
- [Удалить дублирующиеся строки в рабочем листе](/cells/ru/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Обновление ссылок в других листах при удалении пустых столбцов и строк на листе](/cells/ru/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
