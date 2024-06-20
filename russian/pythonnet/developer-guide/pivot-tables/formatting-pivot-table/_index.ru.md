---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/python-net/formatting-pivot-table/
description: Как форматировать сводную таблицу с помощью Aspose.Cells для Python via .NET.
keywords: Форматирование сводной таблицы.
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Как установить параметры форматирования сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Как установить тип автоформата**

Microsoft Excel предлагает несколько различных предустановленных форматов отчетов. Aspose.Cells for Python via .NET также поддерживает эти варианты форматирования. Чтобы получить к ним доступ:

1. Установите [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **Как устанавливать параметры форматирования**

Приведенный ниже пример кода показывает, как отформатировать сводную таблицу для отображения общих итогов для строк и столбцов, а также как установить порядок полей отчета. Он также показывает, как установить пользовательскую строку для пустых значений.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **Форматирование внешнего вида вручную**

Чтобы вручную форматировать отчет сводной таблицы, вместо использования предустановленных форматов отчетов, используйте методы [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) и [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/). Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **Как установить параметры форматирования поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Как установить формат полей строк/столбцов/страниц**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **Как установить формат полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **Как очистить поля сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) есть метод с именем [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
