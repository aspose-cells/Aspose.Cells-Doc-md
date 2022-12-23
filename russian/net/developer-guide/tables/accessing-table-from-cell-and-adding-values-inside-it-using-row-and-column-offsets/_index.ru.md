---
title: Доступ к таблице из Cell и добавление значений внутри нее с использованием смещений строк и столбцов
type: docs
weight: 230
url: /ru/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Обычно вы добавляете значения в объект таблицы или списка, используя[**Cell.Поместить Значение()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)метод. Но иногда вам может понадобиться добавить значения в объект таблицы или списка, используя смещения строк и столбцов.

Чтобы получить доступ к таблице или объекту списка из ячейки, используйте[**Cell.ПолучитьТаблицу()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) метод. Чтобы добавить значения внутри него, используя смещения строки и столбца, используйте[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) метод.

{{% /alert %}}

 На следующем снимке экрана показан исходный файл Excel, используемый внутри кода. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя[**Cell.ПолучитьТаблицу()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) метод, а затем добавьте значения внутри него, используя оба[**Cell.Поместить Значение()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) и[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)методы.

## Пример

### Скриншоты, сравнивающие исходный и выходной файлы

|![дело:изображение_альтернативный_текст](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

На следующем снимке экрана показан выходной файл Excel, сгенерированный кодом. Как видите, ячейка D5 имеет значение, а ячейка F6, которая находится по смещению 2,2 в таблице, имеет значение.

|![дело:изображение_альтернативный_текст](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C# код для доступа к таблице из ячейки и добавления значений внутри нее с использованием смещений строк и столбцов

Следующий пример кода загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
