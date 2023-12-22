---
title: Вставка и удаление строк и столбцов
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns/
description: Узнайте, как вставлять и удалять строки и столбцы с помощью API Aspose.Cells for Java.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **Введение**
Независимо от того, создаете ли вы новый лист с нуля или работаете над существующим листом, нам может потребоваться добавить дополнительные строки или столбцы, чтобы разместить больше данных. И наоборот, нам также может потребоваться удалить строки или столбцы из указанных позиций на листе.

Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.
##  **Как управлять строками/столбцами**
 Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий ЛистКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) это обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) сорт.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс обеспечивает[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)коллекция, представляющая все ячейки на листе.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Коллекция предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое листа смещается вниз или вправо, но если строки или столбцы удаляются, содержимое смещается вверх или влево.

{{% /alert %}} 
##  **Как вставить строку**
 Вставьте строку в любое место, вызвав метод[вставитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[вставитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))метод принимает индекс строки, в которую будет вставлена новая строка, в качестве первого аргумента, а количество строк, которые будут вставлены, в качестве второго аргумента.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Как вставить несколько строк**
 Чтобы вставить несколько строк в лист, вызовите метод[вставитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[вставитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) метод принимает два параметра:

- Индекс строки: индекс строки, из которой будут вставлены новые строки.
- Количество строк: общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Как вставить строку с форматированием**
Чтобы вставить строку с параметрами форматирования, используйте команду[вставитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)перегрузка, которая занимает[Параметры вставки](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)в качестве параметра. Установить[Копиформаттипе](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)свойство[Параметры вставки](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)класс с[Копиформаттипе](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Перечисление.[Копиформаттипе](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Перечисление состоит из трех членов, перечисленных ниже.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): форматирует строку так же, как и строку выше.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): форматирует строку так же, как строку ниже.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Очищает форматирование.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Как удалить строку**
 Чтобы удалить строку в любом месте, вызовите метод[удалитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) метод принимает два параметра:

- Индекс строки: индекс строки, из которой строки будут удалены.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Как удалить несколько строк**
 Чтобы удалить несколько строк из листа, вызовите метод[удалитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалитьстроки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) метод принимает два параметра:

- Индекс строки: индекс строки, из которой строки будут удалены.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Как вставить один или несколько столбцов**
 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[вставить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция.[вставить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) метод принимает два параметра:

- Индекс столбца, индекс столбца, из которого столбец будет вставлен.
- Количество столбцов, общее количество столбцов, которые необходимо вставить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Как удалить столбец**
 Чтобы удалить столбец с листа в любом месте, вызовите метод[удалить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) метод принимает следующие параметры:

- Индекс столбца: индекс столбца, из которого столбец будет удален.
- Количество столбцов: общее количество столбцов, которые необходимо удалить.
- Обновить ссылку: логический параметр, указывающий, следует ли обновлять ссылки на других листах.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

