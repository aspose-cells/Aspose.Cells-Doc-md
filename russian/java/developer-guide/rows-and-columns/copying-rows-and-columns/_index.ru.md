---
title: Копирование строк и столбцов
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns/
---
## **Вступление**
Иногда вам нужно скопировать строки и столбцы на листе, не копируя весь лист. С помощью Aspose.Cells можно копировать строки и столбцы внутри или между книгами.

При копировании строки (или столбца) содержащиеся в ней данные, включая формулы (с обновленными ссылками), а также значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты чертежа также копируются.
## **Копирование строк и столбцов с помощью Microsoft Excel**
1. Выберите строку или столбец, которые вы хотите скопировать.
1.  Чтобы скопировать строки или столбцы, щелкните**Копировать** на**Стандарт** панели инструментов или нажмите**CTRL**+**С**.
1. Выберите строку или столбец ниже или справа от того места, куда вы хотите скопировать свой выбор.
1.  При копировании строк или столбцов щелкните**Скопировано Cells** на**Вставлять** меню.

{{% alert color="primary" %}} 

 Если вы нажмете**Вставить** на**Стандарт** панель инструментов или нажмите**CTRL**+** V** вместо нажатия команды на**В меню «Вставка**» любое содержимое ячеек назначения заменяется.

{{% /alert %}} 

## **Копирование одной строки**

 Aspose.Cells обеспечивает[копиряд](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)учебный класс. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

[копиряд](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) принимает следующие параметры:

-  источник[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)объект,
- индекс исходной строки и
- индекс строки назначения.

 Используйте этот метод, чтобы скопировать строку на листе или на другой лист.[копиряд](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) работает аналогично Microsoft Excel. Так, например, вам не нужно явно задавать высоту строки назначения, это значение также копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблон файла Excel Microsoft и копирует вторую строку (вместе с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в 12-ю строку на том же рабочем листе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Следующий вывод генерируется при выполнении приведенного ниже кода.

**Строка копируется с высочайшей степенью точности и аккуратности** 

![дело:изображение_альтернативный_текст](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

При копировании строк важно отметить связанные изображения, диаграммы или другие объекты рисования, так как это то же самое с Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (индекс начальной строки равен 4, а индекс конечной строки равен 6).
1. Существующие изображения, диаграммы и т. д. в строке назначения не будут удалены.

{{% /alert %}} 

## **Копирование нескольких строк**

 Вы также можете скопировать несколько строк в новое место назначения, используя[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)), который принимает дополнительный параметр типа integer для указания количества копируемых исходных строк.

Ниже приведен снимок входной электронной таблицы, содержащей 3 строки данных, тогда как приведенный ниже фрагмент кода копирует все 3 строки в новое место, начиная с 7-й строки.

![дело:изображение_альтернативный_текст](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Вот результирующий вид электронной таблицы после выполнения приведенного выше фрагмента кода.

![дело:изображение_альтернативный_текст](copy-rows-and-columns_4.png)

## **Копирование одного столбца**

 Aspose.Cells обеспечивает[копиколонн](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)class этот метод копирует все типы данных, включая формулы (с обновленными ссылками) и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

[копиколонн](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) принимает следующие параметры:

-  источник[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)объект,
- индекс исходного столбца и
- индекс столбца назначения.

 Использовать[копиколонн](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) способ копирования столбца на лист или на другой лист.

В этом примере столбец копируется с листа и вставляется на лист в другой книге.

**Столбец копируется из одной книги в другую** 

![дело:изображение_альтернативный_текст](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Копирование нескольких столбцов**

 Похожий на[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ), API-интерфейсы Aspose.Cells также предоставляют[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) для копирования нескольких исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Вот как исходная и результирующая электронные таблицы выглядят в Excel.

![дело:изображение_альтернативный_текст](copy-rows-and-columns_7.png)

![дело:изображение_альтернативный_текст](copy-rows-and-columns_8.png)


## **Вставка строк/столбцов с параметрами вставки**
 Aspose.Cells теперь обеспечивает[Параметры вставки](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) при использовании функций[КопиРовс](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) и[КопиКолонкс](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Это позволяет установить соответствующие параметры вставки, аналогичные Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

