---
title: Форматирование строк и столбцов
linktitle: Строки и столбцы
type: docs
weight: 100
url: /ru/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET может поддерживать изменение высоты строки или ширины столбца, а также применять форматирование к строкам или столбцам.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

При работе с электронными таблицами и добавлении данных в строки или столбцы вам может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что для отображения данных необходимо изменить текущую высоту или ширину. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG, используя Microsoft Excel. Но с помощью Aspose.Cells разработчики могут выполнять эти операции во время выполнения.

{{% /alert %}}

##  **Работа со строками**

###  **Как отрегулировать высоту строки**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочий ЛистКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)это обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция, представляющая все ячейки на листе.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Коллекция предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них обсуждаются ниже более подробно.

###  **Как установить высоту строки**

 Можно установить высоту одной строки, вызвав функцию[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) метод.[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)метод принимает следующие параметры следующим образом:

- *Индекс строки** — индекс строки, высоту которой вы меняете.
- *Высота строки**: высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **Как установить высоту всех строк на листе**

 Если разработчикам необходимо установить одинаковую высоту для всех строк на листе, они могут сделать это с помощью[**Стандартная высота**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) собственность[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция.

**Пример:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Работа со столбцами**

###  **Как установить ширину столбца**

 Установите ширину столбца, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) метод.[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)метод принимает следующие параметры:

- *Индекс столбца** — индекс столбца, ширину которого вы меняете.
- *Ширина столбца** — желаемая ширина столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **Как установить ширину столбца в пикселях**

Установите ширину столбца, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)метод.[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)метод принимает следующие параметры:

- *Индекс столбца** — индекс столбца, ширину которого вы меняете.
- *Ширина столбца** — желаемая ширина столбца в пикселях.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **Как установить ширину всех столбцов на листе**

 Чтобы установить одинаковую ширину столбца для всех столбцов на листе, используйте[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Стандартная ширина**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **Предварительные темы**
- [Автоподбор строк и столбцов](/cells/ru/net/autofit-rows-and-columns/)
- [Преобразуйте текст в столбцы, используя Aspose.Cells](/cells/ru/net/convert-text-to-columns-using-aspose-cells/)
- [Копирование строк и столбцов](/cells/ru/net/copying-rows-and-columns/)
- [Удалить пустые строки и столбцы на листе](/cells/ru/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Группировка и разгруппировка строк и столбцов](/cells/ru/net/grouping-and-ungrouping-rows-and-columns/)
- [Скрытие и отображение строк и столбцов](/cells/ru/net/hiding-and-showing-rows-and-columns/)
- [Вставка или удаление строк на листе Excel](/cells/ru/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Вставка и удаление строк и столбцов файла Excel](/cells/ru/net/inserting-and-deleting-rows-and-columns/)
- [Удаление повторяющихся строк на листе](/cells/ru/net/remove-duplicate-rows-in-a-worksheet/)
- [Обновите ссылки на других листах, удалив пустые столбцы и строки на листе.](/cells/ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
