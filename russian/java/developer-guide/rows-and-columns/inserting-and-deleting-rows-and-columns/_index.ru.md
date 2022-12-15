---
title: Вставка и удаление строк и столбцов
type: docs
weight: 60
url: /ru/java/inserting-and-deleting-rows-and-columns/
---
## **Введение**
Независимо от того, создаете ли вы новый рабочий лист с нуля или работаете с существующим рабочим листом, нам может потребоваться добавить дополнительные строки или столбцы для размещения большего количества данных. И наоборот, нам также может понадобиться удалить строки или столбцы из указанных позиций на листе.

Чтобы выполнить эти требования, Aspose.Cells предоставляет очень простой набор классов и методов, обсуждаемых ниже.
## **Управление строками/столбцами**
 Aspose.Cells предоставляет[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)коллекция, представляющая все ячейки рабочего листа.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них обсуждаются ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое рабочего листа сдвигается вниз или вправо, но если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}} 
## **Вставка строки**
 Вставьте строку в любое место, вызвав метод[вставить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[вставить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) принимает в качестве первого аргумента индекс строки, в которую будет вставлена новая строка, а в качестве второго аргумента — количество вставляемых строк.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Вставка нескольких строк**
 Чтобы вставить несколько строк на лист, вызовите функцию[вставить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[вставить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) принимает два параметра:

- Индекс строки: индекс строки, из которой будут вставлены новые строки.
- Количество строк: общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Вставить строку с форматированием**
Чтобы вставить строку с параметрами форматирования, используйте кнопку[вставить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) перегрузка, которая занимает[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)как параметр. Установить[КопироватьФорматТип](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)свойство[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)класс с[КопироватьФорматТип](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Перечисление.[КопироватьФорматТип](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Перечисление состоит из трех членов, перечисленных ниже.

- [ТАКОЙ ЖЕ_В КАЧЕСТВЕ_ВЫШЕ](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)форматирует строку так же, как указанную выше строку.
- [ТАКОЙ ЖЕ_В КАЧЕСТВЕ_НИЖЕ](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): форматирует строку так же, как строку ниже.
- [ЧИСТО](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): очищает форматирование.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Удаление строки**
 Чтобы удалить строку в любом месте, вызовите метод[удалить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) принимает два параметра:

- Индекс строки: индекс строки, из которой будут удалены строки.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Удаление нескольких строк**
Чтобы удалить несколько строк с рабочего листа, вызовите метод[удалить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалить ряды](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) принимает два параметра:

- Индекс строки: индекс строки, из которой будут удалены строки.
- Количество строк: общее количество строк, которые необходимо удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Вставка одного или нескольких столбцов**
 Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод[вставить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция.[вставить столбцы](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) принимает два параметра:

- Индекс столбца, индекс столбца, из которого столбец будет вставлен
- Количество столбцов, общее количество столбцов, которые необходимо вставить

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Удаление столбца**
 Чтобы удалить столбец из рабочего листа в любом месте, вызовите[удалитьКолонки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция.[удалитьКолонки](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) принимает следующие параметры:

- Индекс столбца: индекс столбца, из которого столбец будет удален.
- Количество столбцов: общее количество столбцов, которые необходимо удалить.
- Обновить ссылку: логический параметр, указывающий, следует ли обновлять ссылки на других листах.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

