---
title: Вставка, удаление строк и столбцов
type: docs
weight: 40
url: /ru/cpp/inserting-deleting-rows-and-columns/
---
##  **Введение**
Независимо от того, создаете ли вы новый лист с нуля или работаете над существующим листом, нам может потребоваться добавить дополнительные строки или столбцы, чтобы разместить больше данных. И наоборот, нам также может потребоваться удалить строки или столбцы из указанных позиций на листе. Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.
###  **Управление строками и столбцами**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция, представляющая все ячейки на листе.

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Коллекция предоставляет несколько методов управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, а если строки или столбцы удаляются, содержимое смещается вверх или влево.

{{% /alert %}} 
####  **Вставить строку**
 Вставьте строку на лист в любое место, вызвав метод[Вставитьстроку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция.[Вставитьстроку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)Метод принимает индекс строки, в которую будет вставлена новая строка.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Вставка нескольких строк**
 Чтобы вставить несколько строк в лист, вызовите метод[Вставитьстроки](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция.[Вставитьстроки](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)метод принимает два параметра:

- Индекс строки — индекс строки, из которой будут вставлены новые строки.
- Количество строк — общее количество строк, которые необходимо вставить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Удаление нескольких строк**
 Чтобы удалить несколько строк из листа, вызовите метод[Удалитьстроки](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция.[Удалитьстроки](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)метод принимает два параметра:

- Индекс строки — индекс строки, из которой строки будут удалены.
- Количество строк — общее количество строк, которые необходимо удалить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Вставить столбец**
 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[Вставитьколонку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция.[Вставитьколонку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)Метод принимает индекс столбца, в который будет вставлен новый столбец.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Удалить столбец**
 Чтобы удалить столбец с листа в любом месте, вызовите метод[Удалитьколонку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция.[Удалитьколонку](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)Метод принимает индекс столбца, который нужно удалить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
