---
title: Форматирование строк и столбцов
linktitle: Строки и столбцы
type: docs
weight: 100
url: /ru/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET может поддерживать изменение высоты строки или ширины столбца, а также применение форматирования к строкам или столбцам.
keywords: Настройте высоту строки и ширину столбца, отрегулируйте высоту строки и ширину столбца, измените высоту строки или ширину столбца, форматируйте строки и столбцы, как установить высоту строки и ширину столбца.
---


{{% alert color="primary" %}}

При работе со таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться, чтобы показать данные. Обычно пользователи регулируют высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Однако разработчики Aspose.Cells могут выполнять эти операции во время выполнения.

{{% /alert %}}

## **Работа со строками**

### **Как настроить высоту строки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), позволяющий получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), которая представляет все ячейки на листе.

Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже более подробно.

### **Как установить высоту строки**

Можно установить высоту отдельной строки, вызвав метод [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Метод [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Как установить высоту всех строк на листе**

Если разработчикам необходимо установить одинаковую высоту всех строк на листе, они могут сделать это, используя свойство [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

**Пример:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Работа с колонками**

### **Как установить ширину столбца**

Установите ширину столбца, вызвав метод коллекции [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Метод [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Как установить ширину столбца в пикселях**

Установите ширину столбца, вызвав метод коллекции [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Метод [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина столбца**, желаемая ширина столбца в пикселях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Как установить ширину всех столбцов в листе Excel**

Чтобы установить одинаковую ширину столбца для всех столбцов в листе, используйте свойство [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Продвинутые темы**
- [Автоподгонка строк и столбцов](/cells/ru/net/autofit-rows-and-columns/)
- [Преобразование текста в столбцы с использованием Aspose.Cells](/cells/ru/net/convert-text-to-columns-using-aspose-cells/)
- [Копирование строк и столбцов](/cells/ru/net/copying-rows-and-columns/)
- [Удаление пустых строк и столбцов в листе Excel](/cells/ru/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Группировка и разгруппировка строк и столбцов](/cells/ru/net/grouping-and-ungrouping-rows-and-columns/)
- [Скрытие и отображение строк и столбцов](/cells/ru/net/hiding-and-showing-rows-and-columns/)
- [Вставка или удаление строк в листе Excel](/cells/ru/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Вставка и удаление строк и столбцов в файле Excel](/cells/ru/net/inserting-and-deleting-rows-and-columns/)
- [Удалить дублирующиеся строки в рабочем листе](/cells/ru/net/remove-duplicate-rows-in-a-worksheet/)
- [Обновление ссылок в других листах при удалении пустых столбцов и строк на листе](/cells/ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
