---
title: Для получения индексов ячеек
type: docs
weight: 600
url: /ru/python-net/get-cells-index/
description: Узнайте, как получить строку или столбец по имени строки через API Aspose.Cells для Python via .NET, столбец или ячейки. Преобразуйте имя ячейки в индекс строки и столбца, начиная с нуля, через API Aspose.Cells для Python via .NET.
keywords: Python Excel, Получение индекса строки и столбца по имени ячейки с помощью Python, Получение индекса столбца по имени столбца с помощью Python, Получение индекса строки по имени строки с помощью Python, Получение индекса по имени ячейки с помощью Python. 
---

{{% alert color="primary" %}}
Представление Excel по умолчанию - это ссылка стиля A1, каждый столбец определен как A, B, C..., а ячейки называются A1, B2, C3... и так далее.
Возможно, вам захочется узнать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}


## **Возможные сценарии использования**
Когда вам нужно обрабатывать конкретные данные на листе по индексу строки и столбца, вам нужно знать индексы строки и столбца этой конкретной ячейки. 
Aspose.Cells для Python via .NET предлагает эту функцию для получения индекса строки и столбца по имени строки, столбца и ячейки. 
Aspose.Cells для Python via .NET предоставляет следующие свойства и методы, чтобы помочь вам достичь ваших целей.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Примечание: Индексация в Aspose.Cells для Python via .NET начинается с нуля, но идентификатор строки начинается с единицы в MS Excel.

## **Получение индексов ячеек с использованием библиотеки Aspose.Cells для Python Excel**
Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Найдите конкретную ячейку на первом рабочем листе.
1. Получите индекс строки и столбца по имени ячейки.
1. Получите индекс столбца по имени столбца.
1. Получите индекс строки по имени строки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
