---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/nodejs-cpp/formatting-pivot-table/
description: Как форматировать сводную таблицу с помощью Aspose.Cells for Node.js via C++.
keywords: Форматирование сводной таблицы.
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Как установить параметры форматирования сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Как установить тип автоформата**

Microsoft Excel предлагает ряд заранее заданных форматов отчетов. Aspose.Cells for Node.js via C++ также поддерживает эти параметры форматирования. Для доступа к ним:

1. Установите [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **Как устанавливать параметры форматирования**

Приведенный ниже пример кода показывает, как отформатировать сводную таблицу для отображения общих итогов для строк и столбцов, а также как установить порядок полей отчета. Он также показывает, как установить пользовательскую строку для пустых значений.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **Форматирование внешнего вида вручную**

Чтобы вручную форматировать отчет сводной таблицы, вместо использования предустановленных форматов отчетов, используйте методы [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) и [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-). Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **Как установить параметры форматирования поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Как установить формат полей строк/столбцов/страниц**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **Как установить формат полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **Как очистить поля сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) есть метод с именем [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
