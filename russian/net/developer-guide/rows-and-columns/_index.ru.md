---
title: Форматировать строки и столбцы
linktitle: Строки и столбцы
type: docs
weight: 100
url: /ru/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что для отображения данных необходимо изменить текущую высоту или ширину. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Но с Aspose.Cells разработчики могут выполнять эти операции во время выполнения.

{{% /alert %}}

## **Работа со строками**

### **Регулировка высоты строки**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция, представляющая все ячейки рабочего листа.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже более подробно.

### **Установка высоты строки**

 Можно установить высоту одной строки, вызвав функцию[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) метод.[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)Метод принимает следующие параметры следующим образом:

- **Индекс строки**, индекс строки, высоту которой вы меняете.
- **Высота строки**, высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Установка высоты всех строк на листе**

 Если разработчикам нужно установить одинаковую высоту для всех строк на листе, они могут сделать это с помощью[**СтандартВысота**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) собственность[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция.

**Пример:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Работа со столбцами**

### **Установка ширины столбца**

 Задайте ширину столбца, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) метод.[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)метод принимает следующие параметры:

- **Индекс столбца**, индекс столбца, ширину которого вы меняете.
- **Ширина колонки**, желаемая ширина столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Установка ширины столбца в пикселях**

Задайте ширину столбца, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)метод.[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)метод принимает следующие параметры:

- **Индекс столбца**, индекс столбца, ширину которого вы меняете.
- **Ширина колонки**желаемая ширина столбца в пикселях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Установка ширины всех столбцов на листе**

 Чтобы установить одинаковую ширину столбца для всех столбцов на листе, используйте[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**стандартная ширина**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Предварительные темы**
- [Автоподбор строк и столбцов](/cells/ru/net/autofit-rows-and-columns/)
- [Преобразование текста в столбцы с помощью Aspose.Cells](/cells/ru/net/convert-text-to-columns-using-aspose-cells/)
- [Копирование строк и столбцов](/cells/ru/net/copying-rows-and-columns/)
- [Удалить пустые строки и столбцы на листе](/cells/ru/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Группировка и разгруппировка строк и столбцов](/cells/ru/net/grouping-and-ungrouping-rows-and-columns/)
- [Скрытие и отображение строк и столбцов](/cells/ru/net/hiding-and-showing-rows-and-columns/)
- [Вставка или удаление строк на листе Excel](/cells/ru/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Вставка и удаление строк и столбцов файла Excel](/cells/ru/net/inserting-and-deleting-rows-and-columns/)
- [Удалить повторяющиеся строки на листе](/cells/ru/net/remove-duplicate-rows-in-a-worksheet/)
- [Обновлять ссылки на других листах при удалении пустых столбцов и строк на листе](/cells/ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
