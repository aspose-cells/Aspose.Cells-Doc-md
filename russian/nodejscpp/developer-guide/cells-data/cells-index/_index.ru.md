---
title: Для получения индексов ячеек
type: docs
weight: 600
url: /ru/nodejs-cpp/get-cells-index/
description: Узнайте, как получить строку или столбец по имени строки, столбца или ячеек. Преобразуйте имя ячейки в индекс строки и столбца с нулевой основой.
keywords: Получить индекс строки и столбца по имени ячейки, Получить индекс столбца по имени столбца, Получить индекс строки по имени строки, Получить индекс по имени ячейки. 
---

{{% alert color="primary" %}}
Представление Excel по умолчанию - это ссылка стиля A1, каждый столбец определен как A, B, C..., а ячейки называются A1, B2, C3... и так далее.
Возможно, вам захочется узнать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}


## **Возможные сценарии использования**
Когда вам нужно обрабатывать конкретные данные на листе по индексу строки и столбца, вам нужно знать индексы строки и столбца этой конкретной ячейки. 
Aspose.Cells for Node.js via C++ предлагает эту функцию для получения индексов строк и столбцов по имени строки, столбца и ячейки. 
Aspose.Cells for Node.js via C++ предоставляет следующие свойства и методы, которые помогают вам достигнуть ваших целей.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Примечание: Индексация нулевая в Aspose.Cells for Node.js via C++, но идентификатор строки в MS Excel имеет один-based нумерацию.

## **Получение индексов ячеек с помощью Aspose.Cells for Node.js via C++**
Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Найдите конкретную ячейку на первом рабочем листе.
1. Получите индекс строки и столбца по имени ячейки.
1. Получите индекс столбца по имени столбца.
1. Получите индекс строки по имени строки.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
