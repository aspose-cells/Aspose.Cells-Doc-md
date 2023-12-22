---
title: Вставка и удаление строк и столбцов файла Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/net/inserting-and-deleting-rows-and-columns/
description: В этой статье показано, как вставлять и удалять строки и столбцы по номеру Aspose.Cells for .NET API.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **Введение**

Независимо от того, создаете ли вы новый лист с нуля или работаете над существующим листом, нам может потребоваться добавить дополнительные строки или столбцы, чтобы разместить больше данных. И наоборот, нам также может потребоваться удалить строки или столбцы из указанных позиций на листе.
Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.

###  **Управление строками и столбцами**

Aspose.Cells предоставляет класс[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция, представляющая все ячейки на листе.

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Коллекция предоставляет несколько методов управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, а если строки или столбцы удаляются, содержимое смещается вверх или влево.

{{% /alert %}}


##  **Вставка строк и столбцов**

###  **Как вставить строку**

 Вставьте строку на лист в любое место, вызвав метод[**Вставитьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Вставитьстроку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)Метод принимает индекс строки, в которую будет вставлена новая строка.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **Как вставить несколько строк**

 Чтобы вставить несколько строк в лист, вызовите метод[**Вставитьстроки**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Вставитьстроки**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)метод принимает два параметра:

- Индекс строки — индекс строки, из которой будут вставлены новые строки.
- Количество строк — общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **Как вставить строку с форматированием**

Чтобы вставить строку с параметрами форматирования, используйте команду[**Вставитьстроки**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)перегрузка, которая занимает[**Параметры вставки**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) в качестве параметра. Установить[**Копиформаттипе**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) свойство[**Параметры вставки**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) класс с[**Копиформаттипе**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Перечисление.[**Копиформаттипе**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Перечисление состоит из трех членов, перечисленных ниже.

- SameAsAbove: форматирует строку так же, как и строку выше.
- SameAsBelow: форматирует строку так же, как строку ниже.
- Очистить: Очищает форматирование.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **Как вставить столбец**

 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[**Вставитьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)коллекция.[**Вставитьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)Метод принимает индекс столбца, в который будет вставлен новый столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Удалить строки и столбцы**

###  **Как удалить несколько строк**

 Чтобы удалить несколько строк из листа, вызовите метод[**Удалитьстроки**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Удалитьстроки**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)метод принимает два параметра:

- Индекс строки — индекс строки, из которой строки будут удалены.
- Количество строк — общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **Как удалить столбец**

 Чтобы удалить столбец с листа в любом месте, вызовите метод[**Удалитьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция.[**Удалитьколонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)Метод принимает индекс столбца, который нужно удалить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
