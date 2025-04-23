---
title: Вставка и удаление строк и столбцов
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns/
description: Узнайте, как вставлять и удалять строки и столбцы с помощью Aspose.Cells for Java API.
keywords: Как вставлять и удалять строки и столбцы в Java, Вставка строк и столбцов с помощью Java, Удаление строк и столбцов в Java, Вставка строк или столбцов с помощью Java, Удаление строк или столбцов via Java.
---

## **Введение**
При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе.

Для выполнения этих требований Aspose.Cells предоставляет очень простой набор классов и методов, рассматриваемых ниже.
## **Как управлять строками/столбцами**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells), которая представляет все ячейки на листе.

Коллекция [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое на листе сдвигается вниз или направо, но если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}} 
## **Как вставить строку**
Добавьте строку в любое место, вызвав метод [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) коллекции [Cells]. Метод [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) принимает индекс строки, в которую будет вставлена новая строка, в качестве первого аргумента, и число строк для вставки в качестве второго.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Как вставить несколько строк**
Чтобы вставить несколько строк в лист, вызовите метод [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) коллекции [Cells]. Метод [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) принимает два параметра:

- Индекс строки: индекс строки, откуда будут вставлены новые строки.
- Количество строк: общее количество строк, которые нужно вставить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Как вставить строку с форматированием**
Для вставки строки с опциями форматирования используйте перегрузку метода [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-), которая принимает [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) в качестве параметра. Установите свойство [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) класса [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) с помощью перечисления [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). Перечисление [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) содержит три варианта, перечисленных ниже.

- [ТОЖЕ_СТРАНИЧНО](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Форматирует строку так же, как и предыдущая.
- [ТОЖЕ_НИЖЕ](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): Форматирует строку так же, как и следующая.
- [ОЧИСТИТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): очищает форматирование.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Как удалить строку**
Чтобы удалить строку в любой точке, вызовите метод [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Метод [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) принимает два параметра:

- Индекс строки: индекс строки, с которой будут удалены строки.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Как удалить несколько строк**
Чтобы удалить несколько строк из листа, вызовите метод [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) коллекции [Cells]. Метод [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) принимает два параметра:

- Индекс строки: индекс строки, с которой будут удалены строки.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Как вставить один или несколько столбцов**
Разработчики также могут вставить столбец в лист в любом месте, вызвав метод [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) коллекции [Cells]. Метод [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) принимает два параметра:

- Индекс столбца, индекс столбца, в который будет вставлен столбец
- Количество столбцов, общее количество столбцов, которые необходимо вставить

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Как удалить столбец**
Чтобы удалить столбец из листа в любом месте, вызовите метод [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) коллекции [Cells]. Метод [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) принимает следующие параметры:

- Индекс столбца: индекс столбца, из которого будет удален столбец.
- Количество столбцов: общее количество столбцов, которые необходимо удалить.
- Обновить ссылку: логический параметр, указывающий, следует ли обновлять ссылки в других листах.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
