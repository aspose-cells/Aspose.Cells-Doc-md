---
title: Вставка сводной таблицы
linktitle: Сводные таблицы
type: docs
weight: 160
url: /ru/nodejs-cpp/create-pivot-table/
description: Создание и форматирование сводных таблиц файла электронной таблицы Excel.
---

## **Создать сводную таблицу**

 Возможна программаmatically добавлять сводные таблицы в таблицы с помощью Aspose.Cells for Node.js via C++.

### **Модель объекта сводной таблицы**

Aspose.Cells for Node.js via C++ предоставляет набор специальных классов для создания и управления сводными таблицами. Эти классы используются для создания и установки объектов [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), которые являются строительными блоками сводной таблицы. Объекты:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) в [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) представляет собой сводную таблицу на листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) представляет собой коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) на листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**

1. Добавьте данные на лист с использованием метода [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) объекта [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).
   Эти данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) коллекции [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), который инкапсулирован в объекте Лист.
1. Получите доступ к новому объекту [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) из коллекции [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), передав индекс сводной таблицы.
1. Используйте любые из объектов [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) (описанных выше), чтобы управлять сводной таблицей.

После выполнения примера кода сводная таблица добавляется на лист.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен проходить сверху вниз. Например, "A1:C3" допустим, но "C3:A1" - нет.

{{% /alert %}}
