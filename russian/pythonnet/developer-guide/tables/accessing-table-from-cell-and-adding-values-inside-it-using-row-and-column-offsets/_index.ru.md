---
title: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов
type: docs
weight: 230
url: /ru/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.

Чтобы получить доступ к объекту Table или List из ячейки, используйте метод {0}. Чтобы добавлять значения в него, используя смещения строки и столбца, используйте методы {1} и {2}.

{{% /alert %}}

На следующем скриншоте показан исходный файл Excel, используемый в коде. Он содержит пустую таблицу и выделяет ячейку D5, которая находится внутри таблицы. Мы получим доступ к этой таблице из ячейки D5, используя метод [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#), а затем добавим значения в нее, используя методы [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) и [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

## Пример

### Снимки экрана сравнивают исходные и выходные файлы

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Пример кода на Python для доступа к таблице из ячейки и добавления значений внутри неё с помощью смещений по строке и столбцу

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
{{< app/cells/assistant language="python-net" >}}
