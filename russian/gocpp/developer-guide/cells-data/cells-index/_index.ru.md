---
title: Получение индексов ячеек с Golang через C++
linktitle: Для получения индексов ячеек
type: docs
weight: 600
url: /ru/go-cpp/get-cells-index/
description: Узнайте, как получить индекс строки или столбца по названию строки, столбца или ячейки. Преобразуйте название ячейки в индекс строки и столбца с нуля с помощью Aspose.Cells и Golang через C++.
keywords: Получить индекс строки и столбца по имени ячейки, Получить индекс столбца по имени столбца, Получить индекс строки по имени строки, Получить индекс по имени ячейки.
---

{{% alert color="primary" %}}
По умолчанию представление Excel использует ссылку в стиле A1, где каждый столбец обозначается как A, B, C..., а ячейки обозначаются как A1, B2, C3... и так далее.
Вам может понадобиться знать, в какой строке и столбце находится эта ячейка.

{{% /alert %}}

## **Возможные сценарии использования**

Когда вам нужно манипулировать только определенными данными на листе, по индексу строки и столбца, необходимо знать эти индексы.
Aspose.Cells предоставляет эту возможность получать индекс строки и столбца по имени строки, столбца и ячейки.
Aspose.Cells предоставляет следующие свойства и методы для достижения ваших целей:

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Примечание: Индексация в Aspose.Cells for C++ нулевая, но ID строки в MS Excel — единичная.

## **Получить индексы ячеек с использованием Aspose.Cells**

Этот пример показывает, как:

1. Создать книгу и добавить некоторые данные.
1. Найдите конкретную ячейку на первом рабочем листе.
1. Получите индекс строки и столбца по имени ячейки.
1. Получите индекс столбца по имени столбца.
1. Получите индекс строки по имени строки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
