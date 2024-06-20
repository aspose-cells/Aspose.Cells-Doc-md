---
title: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов
type: docs
weight: 110
url: /ru/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.

Для доступа к таблице или объекту списка из ячейки используйте метод [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--). И для добавления значений в него с использованием смещений строк и столбцов используйте метод [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)).

{{% /alert %}}

## Пример

### Снимки экрана сравнивают исходные и выходные файлы

На следующем скриншоте показан исходный файл Excel, используемый в коде. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя метод [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--), а затем добавим значения в нее, используя методы [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) и [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)).

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java-код для доступа к таблице из ячейки и добавления значений в нее с использованием смещений строк и столбцов

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
