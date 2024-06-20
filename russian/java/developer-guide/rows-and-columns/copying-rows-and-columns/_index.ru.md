---
title: Копирование строк и колонок
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns/
---

## **Введение**
Иногда вам нужно скопировать строки и столбцы в рабочем листе без копирования всего листа. С помощью Aspose.Cells это возможно скопировать строки и столбцы внутри или между книгами.

При копировании строки (или столбца) копируются также содержащиеся в нем данные, включая формулы - с обновленными ссылками - и значения, комментарии, форматирование, скрытые ячейки, изображения и другие объекты рисования.
## **Копирование строк и колонок в Microsoft Excel**
1. Выберите строку или колонку, которую вы хотите скопировать.
1. Чтобы скопировать строки или колонки, нажмите **Копировать** на панели **Стандартные функции** или нажмите **CTRL**+**C**.
1. Выберите строку или колонку ниже или справа от места, куда вы хотите скопировать ваш выбор.
1. При копировании строк или колонок нажмите **Скопированные ячейки** на меню **Вставка**.

{{% alert color="primary" %}} 

Если вы щелкнете **Вставить** на панели инструментов **Стандарт** или нажмете **CTRL**+**V** вместо того, чтобы щелкнуть команду на вкладке **Вставка**, содержимое ячеек назначения будет заменено.

{{% /alert %}} 

## **Копирование одной строки**

Aspose.Cells предоставляет метод [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) класса [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) принимает следующие параметры:

- объект исходных [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells),
- индекс исходной строки, и
- индекс строки назначения.

Используйте этот метод для копирования строки в пределах одного рабочего листа или на другой рабочий лист. Метод [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) работает аналогично Microsoft Excel. Например, вам не нужно устанавливать высоту целевой строки явно, это значение тоже копируется.

В следующем примере показано, как скопировать строку на листе. Он использует шаблонный файл Microsoft Excel и копирует вторую строку (с данными, форматированием, комментариями, изображениями и т. д.) и вставляет ее в двенадцатую строку на том же листе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Следующий вывод генерируется при выполнении приведенного ниже кода.

**Строка копируется с наивысшей степенью точности и точности** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

При копировании строк важно учитывать связанные изображения, диаграммы или другие объекты рисования, так же как и в Microsoft Excel:

1. Если индекс исходной строки равен 5, изображение, диаграмма и т. д. копируются, если они содержатся в трех строках (начальный индекс строки равен 4, а конечный индекс строки равен 6).
1. Существующие изображения, диаграммы и т. д. в целевой строке не будут удалены.

{{% /alert %}} 

## **Копирование нескольких строк**

Вы также можете скопировать несколько строк в новое место, используя метод [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)), который принимает дополнительный параметр типа integer для указания количества копируемых строк.

Ниже приведен снимок входной электронной таблицы, содержащей 3 строки данных, тогда как фрагмент кода ниже копирует все 3 строки в новое расположение, начиная с 7-й строки.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Вот результат просмотра электронной таблицы после выполнения приведенного выше фрагмента кода.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Копирование одного столбца**

Aspose.Cells предоставляет метод [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) класса [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), этот метод копирует все типы данных, включая формулы - с обновленными ссылками - и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

Метод [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) принимает следующие параметры:

- объект исходных [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells),
- индекс исходного столбца, и
- индекс столбца назначения.

Используйте метод [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) для копирования столбца внутри листа или на другой лист.

В этом примере копируется столбец из листа и вставляется в лист другой книги.

**Столбец копируется из одной книги в другую** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Копирование нескольких столбцов**

Подобно методу [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)), API Aspose.Cells также предоставляют метод [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) для копирования нескольких исходных столбцов в новое место.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Вот как выглядят исходные и результативные электронные таблицы в Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Вставка строк/столбцов с опциями вставки**
Aspose.Cells теперь предоставляет [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) при использовании функций [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) и [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Это позволяет устанавливать соответствующие параметры вставки, аналогичные Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

