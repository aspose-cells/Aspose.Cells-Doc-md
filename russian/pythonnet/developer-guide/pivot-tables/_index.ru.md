---
title: Вставка сводной таблицы
description: Создание и форматирование сводной таблицы с помощью Aspose.Cells для Python via .NET.
linktitle: Сводные таблицы
url: /ru/python-net/create-pivot-table/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Создание сводной таблицы, вставка сводной таблицы, форматирование сводной таблицы.
---

## **Создать сводную таблицу**
С помощью Aspose.Cells для Python via .NET можно программно добавлять сводные таблицы к таблицам.

### **Модель объекта сводной таблицы**
Aspose.Cells для Python via .NET предоставляет специальный набор классов в пространстве имен [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/), которые используются для создания и управления сводными таблицами. Эти классы используются для создания и установки объектов [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), строительных блоков сводной таблицы. Объекты:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) в [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) представляет собой сводную таблицу на листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) представляет собой коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) на листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**
1. Добавьте данные на лист с использованием метода [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) объекта [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Эти данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) коллекции [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), который инкапсулирован в объекте Лист.
1. Получите доступ к новому объекту [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) из коллекции [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), передав индекс сводной таблицы.
1. Используйте любые из объектов [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (описанных выше), чтобы управлять сводной таблицей.
После выполнения примера кода сводная таблица добавляется на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен проходить сверху вниз. Например, "A1:C3" допустим, но "C3:A1" - нет.
{{% /alert %}}

## **Продвинутые темы**

{{< app/cells/assistant language="python-net" >}}