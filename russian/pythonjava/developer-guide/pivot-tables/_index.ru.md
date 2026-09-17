---
title: Сводные таблицы
description: Создание и форматирование сводных таблиц файла электронной таблицы Excel.
linktitle: Сводные таблицы
url: /ru/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Создание сводной таблицы, вставка сводной таблицы, форматирование сводной таблицы.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Создание сводной таблицы**
С помощью Aspose.Cells можно программно добавлять сводные таблицы в электронные таблицы.

### **Объектная модель сводной таблицы**
Aspose.Cells предоставляет набор классов, используемых для создания сводных таблиц и управления ими. Основные строительные блоки:
- `PivotField` представляет поле в `PivotTable`.
- `PivotFieldCollection` представляет коллекцию всех объектов `PivotField` в `PivotTable`.
- `PivotTable` представляет сводную таблицу на листе.
- `PivotTableCollection` представляет коллекцию всех объектов `PivotTable` на листе.

### **Создание простой сводной таблицы с помощью Aspose.Cells**
1. Добавьте данные на лист с помощью метода `putValue` ячейки. Эти данные будут использоваться в качестве источника данных сводной таблицы.
2. Добавьте сводную таблицу на лист, вызвав метод `add` коллекции `PivotTables`, инкапсулированной в объекте листа.
3. Получите доступ к новому объекту `PivotTable` из коллекции `PivotTables`, передав индекс сводной таблицы.
4. Используйте любой из объектов `PivotTable` (описанных выше) для управления сводной таблицей.

После выполнения примера кода сводная таблица добавляется на лист.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
При назначении диапазона ячеек в качестве источника данных диапазон должен идти от верхнего левого угла к нижнему правому. Например, "A1:C3" допустимо, но "C3:A1" — нет.
{{% /alert %}}

## Связанные статьи
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/ru/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/ru/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/ru/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/ru/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/ru/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}