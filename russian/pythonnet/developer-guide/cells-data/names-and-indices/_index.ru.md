---
title: Преобразование между именем ячейки и индексом строки/столбца
linktitle: Преобразование имени ячейки и индекса
type: docs
weight: 10
url: /ru/python-net/names-and-indices/
description: Узнайте, как получить преобразование между именем ячейки и индексом строки/столбца через API Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, Python Получить имя ячейки по индексам строки и столбца, Python Получить индексы строки и столбца по имени ячейки, Python Создать безопасные имена листов, Python Добавить безопасные имена листов
---

## **Получить имя ячейки по индексам строки и столбца**
Возможно определить имя ячейки по индексам строки и столбца. В этой статье объясняется как это сделать.
Aspose.Cells для Python via .NET предоставляет метод [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int), который позволяет разработчикам получить имя ячейки, если они предоставляют индекс строки и столбца.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, в Aspose.Cells для Python via .NET индексы строк и столбцов начинаются с 0.

{{% /alert %}} 

В следующем образцовом коде показано, как использовать [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) для доступа к имени ячейки при известном индексе строки и столбца. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Получить индексы строки и столбца из имени ячейки**
Возможно определить индекс строки и столбца ячейки по ее имени. В этой статье объясняется как это сделать.
Aspose.Cells для Python via .NET предоставляет метод [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any), который позволяет разработчикам получить индекс строки и столбца по имени ячейки.

{{% alert color="primary" %}} 

В отличие от Microsoft Excel, где индексы строк и столбцов начинаются с 1, в Aspose.Cells для Python via .NET индексы строк и столбцов начинаются с 0.

{{% /alert %}} 

В следующем образцовом коде показано, как использовать [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) для получения индекса строки и столбца по имени ячейки. Код генерирует следующий вывод.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Создать безопасные имена листов**
Иногда возникает необходимость назначать имя листа во время выполнения. В этом случае имена листов могут содержать дополнительные символы, такие как <>+(?”. Необходимо заменить любой такой символ, который не допускается в качестве имени листа, на некоторый предварительно определенный символ, предоставленный пользователем. Аналогичная функция создания безопасных имен предоставляется Aspose.Cells для Python via .NET для решения всех этих проблем. Вот образец кода, демонстрирующий эту функцию:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Вывод:

это первое имя, которое создано

` `< > + (adj.Private _"Частный"
{{< app/cells/assistant language="python-net" >}}
