---
title: Вставка сводной таблицы
description: Создание и форматирование сводных таблиц файла электронной таблицы Excel.
linktitle: Сводные таблицы
url: /ru/net/create-pivot-table/
type: docs
weight: 160
keywords: Создание сводной таблицы, вставка сводной таблицы, форматирование сводной таблицы.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Создать сводную таблицу**
Возможно использовать Aspose.Cells для добавления сводных таблиц в электронные таблицы программно.

### **Модель объекта сводной таблицы**
Aspose.Cells предоставляет специальный набор классов в пространстве имен [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot), которые используются для создания и управления сводными таблицами. Эти классы используются для создания и установки объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), строительных блоков сводной таблицы. Объекты представляют собой:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) в [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) представляет собой сводную таблицу на листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) представляет собой коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) на листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**
1. Добавьте данные на лист с использованием метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) объекта [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Эти данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) коллекции [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), который инкапсулирован в объекте Лист.
1. Получите доступ к новому объекту [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) из коллекции [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), передав индекс сводной таблицы.
1. Используйте любые из объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (описанных выше), чтобы управлять сводной таблицей.
После выполнения примера кода сводная таблица добавляется на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен проходить сверху вниз. Например, "A1:C3" допустим, но "C3:A1" - нет.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}