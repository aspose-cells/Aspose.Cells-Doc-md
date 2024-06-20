---
title: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов
type: docs
weight: 230
url: /ru/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.

Чтобы получить доступ к объекту Table или List из ячейки, используйте метод {0}. Чтобы добавлять значения в него, используя смещения строки и столбца, используйте методы {1} и {2}.

{{% /alert %}}

На следующем скриншоте показан исходный файл Excel, используемый в коде. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя метод [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable), а затем добавим значения в нее, используя методы [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) и [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

## Пример

### Снимки экрана сравнивают исходные и выходные файлы

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Код C# для доступа к таблице из ячейки и добавления значений в нее с использованием смещений строки и столбца

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
