---
title: Создайте сводную таблицу
type: docs
weight: 10
url: /ru/python-java/create-a-pivot-table/
---
## **Создайте сводную таблицу**
Aspose.Cells for Python via Java предоставляет возможность создавать сводные таблицы. Чтобы создать сводную таблицу с использованием Aspose.Cells, выполните следующие действия:

1. Добавьте некоторые данные в ячейки рабочего листа с помощью[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)объекты[установить значение](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)имущество. Эти данные будут использоваться в качестве источника данных для сводной таблицы.
1. Добавьте сводную таблицу на рабочий лист, вызвав метод[сводная таблицаколлекция](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[добавлять](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)), инкапсулированный в[Рабочий лист](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)объект.
1. Доступ к[сводная таблица](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)объект из[сводная таблицаколлекция](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)пройдя[сводная таблица](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)индекс.
1. Используйте любой из объектов сводной таблицы (описанных выше), инкапсулированных в[сводная таблицаколлекция](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)объект для управления сводной таблицей.

Следующий фрагмент кода демонстрирует создание сводной таблицы с Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
