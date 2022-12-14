---
title: Доступ к таблице из Cell и добавление значений внутри нее с использованием смещений строк и столбцов
type: docs
weight: 110
url: /ru/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Обычно вы добавляете значения в объект таблицы или списка, используя[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) метод. Но иногда вам может понадобиться добавить значения в объект таблицы или списка, используя смещения строк и столбцов.

Чтобы получить доступ к таблице или объекту списка из ячейки, используйте[**Cell.получитьТаблицу()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) метод. И чтобы добавить значения внутри него, используя смещения строки и столбца, используйте[**ListObject.putCellValue (смещение строки, смещение столбца, значение)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) метод.

{{% /alert %}}

## Пример

### Скриншоты, сравнивающие исходный и выходной файлы

 На следующем снимке экрана показан исходный файл Excel, используемый внутри кода. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя[**Cell.получитьТаблицу()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ), а затем добавьте значения внутри него, используя как[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) а также[**ListObject.putCellValue (смещение строки, смещение столбца, значение)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) методы.

![дело:изображение_альтернативный_текст](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

На следующем снимке экрана показан выходной файл Excel, сгенерированный кодом. Как видите, ячейка D5 имеет значение, а ячейка F6, которая находится по смещению 2,2 в таблице, имеет значение.

![дело:изображение_альтернативный_текст](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java код для доступа к таблице из ячейки и добавления значений внутри нее с использованием смещений строк и столбцов

Следующий пример кода загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
