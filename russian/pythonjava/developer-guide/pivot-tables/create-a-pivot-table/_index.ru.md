---
title: Создание сводной таблицы
type: docs
weight: 10
url: /ru/python-java/create-a-pivot-table/
---

## **Создание сводной таблицы**
Aspose.Cells для Python via Java предоставляет возможность создания сводных таблиц. Для создания сводной таблицы с помощью Aspose.Cells следуйте следующим шагам:

1. Добавьте некоторые данные в ячейки листа, используя свойство [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) объекта [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell). Эти данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) у [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), инкапсулированного в объекте [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet).
1. Получите объект [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) из [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), передав индекс [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable).
1. Используйте любой из объектов сводной таблицы (объяснено выше), инкапсулированных в [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), для управления сводной таблицей.

Приведенный ниже фрагмент кода демонстрирует создание сводной таблицы с помощью Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
