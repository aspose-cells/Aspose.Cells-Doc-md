---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/net/formatting-pivot-table/
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Настройка параметров формата сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Установка типа автоформата**

Microsoft Excel предлагает несколько различных предустановленных форматов отчетов. Aspose.Cells также поддерживает эти опции форматирования. Чтобы получить к ним доступ:

1. Установите [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Настройка параметров формата**

Приведенный ниже пример кода показывает, как отформатировать сводную таблицу для отображения общих итогов для строк и столбцов, а также как установить порядок полей отчета. Он также показывает, как установить пользовательскую строку для пустых значений.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Форматирование внешнего вида вручную**

Для форматирования отчета сводной таблицы внешний вид вручную, вместо использования предварительно заданных форматов отчетов используйте методы [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) и [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall). Создайте объект стиля для желаемого форматирования, например:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Настройка параметров формата поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Настройка формата полей строки/столбца/страницы**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Настройка формата полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Очистка полей сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) есть метод с именем [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
