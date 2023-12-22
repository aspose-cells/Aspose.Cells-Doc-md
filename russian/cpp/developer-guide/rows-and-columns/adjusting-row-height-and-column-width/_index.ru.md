---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

При работе с электронными таблицами и добавлении данных в строки или столбцы вам может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что для отображения данных необходимо изменить текущую высоту или ширину. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG, используя Microsoft Excel. Но с помощью Aspose.Cells разработчики могут выполнять эти операции во время выполнения.

{{% /alert %}} 
##  **Работа со строками**
###  **Настройка высоты строки**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочий ЛистКоллекция](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)это обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция, представляющая все ячейки на листе.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Коллекция предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них обсуждаются ниже более подробно.
####  **Установка высоты строки**
 Можно установить высоту одной строки, вызвав функцию[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) метод.[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)метод принимает следующие параметры следующим образом:

- *Индекс строки** — индекс строки, высоту которой вы меняете.
- *Высота строки**: высота строки, применяемая к строке.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Установка высоты всех строк на листе**
 Если разработчикам необходимо установить одинаковую высоту для всех строк на листе, они могут сделать это с помощью[УстановитьСтандартнуюВысоту](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Работа со столбцами**
###  **Установка ширины столбца**
 Установите ширину столбца, вызвав метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) метод.[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)метод принимает следующие параметры:

- *Индекс столбца** — индекс столбца, ширину которого вы меняете.
- *Ширина столбца** — желаемая ширина столбца.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Установка ширины всех столбцов на листе**
 Чтобы установить одинаковую ширину столбца для всех столбцов на листе, используйте[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[Установитьстандартную ширину](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)метод.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
